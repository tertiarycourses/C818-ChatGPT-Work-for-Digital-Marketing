const STORE = 'cb_signups';
const dialog = document.querySelector('#signup-dialog');
const entry = document.querySelector('#signup-entry');
const success = document.querySelector('#signup-success');
const form = document.querySelector('#signup-form');
const courseDetails = document.querySelector('#signup-course');
const storageError = document.querySelector('#signup-storage-error');
const allergyWarning = document.querySelector('#allergy-warning');
const feeFormat = new Intl.NumberFormat('en-SG', { maximumFractionDigits: 0 });
const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/;
const mobilePattern = /^(?:\+65\s?)?[689]\d{3}\s?\d{4}$/;
let selectedCourse = null;

function field(name) {
  return form.elements.namedItem(name);
}

function dateStamp(date) {
  return `${date.getFullYear()}${String(date.getMonth() + 1).padStart(2, '0')}${String(date.getDate()).padStart(2, '0')}`;
}

function submissionDate(date) {
  const stamp = dateStamp(date);
  return `${stamp.slice(0, 4)}-${stamp.slice(4, 6)}-${stamp.slice(6)}`;
}

function readSignups() {
  const records = JSON.parse(localStorage.getItem(STORE) || '[]');
  if (!Array.isArray(records)) throw new Error('Invalid saved sign-ups');
  return records;
}

function newReference(date, records) {
  const prefix = `CB-${dateStamp(date)}-`;
  const used = new Set(records.map(record => record.ref));
  for (let number = 1000; number <= 9999; number += 1) {
    const candidate = `${prefix}${String(number).padStart(4, '0')}`;
    if (!used.has(candidate)) return candidate;
  }
  throw new Error('No reference numbers available today');
}

function clearValidation() {
  form.querySelectorAll('[aria-invalid]').forEach(input => input.removeAttribute('aria-invalid'));
  form.querySelectorAll('.field-error').forEach(error => { error.textContent = ''; });
  storageError.hidden = true;
  storageError.textContent = '';
}

function setCourseDetails(course) {
  courseDetails.replaceChildren();
  const details = [
    ['Code', course.code],
    ['Course', course.title],
    ['Fee', `S$${feeFormat.format(course.fee)}`],
    ['Length', `${course.weeks} ${course.weeks === 1 ? 'week' : 'weeks'}`],
    ['Schedule', course.when],
    ['Campus', course.campus],
  ];
  for (const [label, value] of details) {
    const row = document.createElement('div');
    const term = document.createElement('dt');
    const description = document.createElement('dd');
    term.textContent = label;
    description.textContent = value;
    row.append(term, description);
    courseDetails.append(row);
  }
}

export function openSignup(course) {
  selectedCourse = course;
  dialog.setAttribute('aria-labelledby', 'signup-title');
  form.reset();
  clearValidation();
  entry.hidden = false;
  success.hidden = true;
  document.querySelector('#signup-title').textContent = `Sign up — ${course.title}`;
  setCourseDetails(course);
  const intake = field('intake');
  intake.replaceChildren(...course.intakes.map(date => {
    const option = document.createElement('option');
    option.value = date;
    option.textContent = `Starts ${date}`;
    return option;
  }));
  allergyWarning.hidden = true;
  allergyWarning.textContent = '';
  dialog.showModal();
  field('full_name').focus();
}

function updateAllergyWarning() {
  const mentionsNuts = /nut/i.test(field('allergies').value);
  const courseUsesNuts = /nut/i.test(selectedCourse?.allergens || '');
  const warn = mentionsNuts && courseUsesNuts;
  allergyWarning.hidden = !warn;
  allergyWarning.textContent = warn
    ? `Please check with the academy before attending. This course lists: ${selectedCourse.allergens}.`
    : '';
}

function validate() {
  clearValidation();
  const problems = [];
  const intake = field('intake');
  if (!selectedCourse.intakes.includes(intake.value)) problems.push([intake, 'Choose a valid intake.']);
  const name = field('full_name');
  if (name.value.trim().length < 2) problems.push([name, 'Enter your full name (at least 2 characters).']);
  const email = field('email');
  if (!emailPattern.test(email.value.trim())) problems.push([email, 'Enter a valid email address.']);
  const mobile = field('mobile');
  if (!mobilePattern.test(mobile.value.trim())) problems.push([mobile, 'Enter a Singapore mobile number, such as +65 9123 4567.']);
  const consent = field('consent');
  if (!consent.checked) problems.push([consent, 'Agree to be contacted about this sign-up.']);

  for (const [input] of problems) input.setAttribute('aria-invalid', 'true');
  if (problems.length) {
    const [firstInput, firstMessage] = problems[0];
    const errorId = firstInput.getAttribute('aria-describedby');
    document.getElementById(errorId).textContent = firstMessage;
    firstInput.focus();
  }
  return problems.length === 0;
}

function mailtoLink(record) {
  const details = [
    `Reference: ${record.ref}`,
    `Course: ${record.course_code} — ${record.course_title}`,
    `Intake: ${record.intake}`,
    `Name: ${record.full_name}`,
    `Email: ${record.email}`,
    `Mobile: ${record.mobile}`,
    `Experience: ${record.experience}`,
    `Allergies: ${record.allergies || 'None stated'}`,
    `Newsletter opt-in: ${record.marketing_opt_in}`,
  ];
  const subject = encodeURIComponent(`Course sign-up ${record.ref} — ${record.course_code}`);
  const body = encodeURIComponent(details.join('\n'));
  return `mailto:enrol@cookbakeacademy.sg?subject=${subject}&body=${body}`;
}

form.addEventListener('submit', event => {
  event.preventDefault();
  if (!selectedCourse || !validate()) return;

  try {
    const records = readSignups();
    const now = new Date();
    const record = {
      ref: newReference(now, records),
      submitted: submissionDate(now),
      course_code: selectedCourse.code,
      course_title: selectedCourse.title,
      intake: field('intake').value,
      full_name: field('full_name').value.trim(),
      email: field('email').value.trim(),
      mobile: field('mobile').value.trim(),
      experience: field('experience').value,
      allergies: field('allergies').value.trim(),
      marketing_opt_in: field('marketing_opt_in').checked ? 'yes' : 'no',
      paid: 'no',
    };
    records.push(record);
    localStorage.setItem(STORE, JSON.stringify(records));
    document.querySelector('#signup-reference').textContent = record.ref;
    document.querySelector('#signup-mailto').href = mailtoLink(record);
    entry.hidden = true;
    success.hidden = false;
    dialog.setAttribute('aria-labelledby', 'signup-success-title');
    document.querySelector('#signup-mailto').focus();
  } catch (error) {
    storageError.textContent = 'This browser could not save your sign-up. Please check browser storage and try again.';
    storageError.hidden = false;
    storageError.focus();
    console.error('Sign-up storage error:', error);
  }
});

field('allergies').addEventListener('input', updateAllergyWarning);
document.querySelector('#signup-close').addEventListener('click', () => dialog.close());
document.querySelector('#signup-cancel').addEventListener('click', () => dialog.close());
document.querySelector('#signup-done').addEventListener('click', () => dialog.close());
dialog.addEventListener('click', event => {
  if (event.target === dialog) dialog.close();
});
