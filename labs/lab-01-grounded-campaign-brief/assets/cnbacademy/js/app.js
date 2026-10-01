import { openSignup } from './signup.js';

const grid = document.querySelector('#course-grid');
const status = document.querySelector('#course-status');
const search = document.querySelector('#course-search');
const chips = [...document.querySelectorAll('[data-filter]')];
const currency = new Intl.NumberFormat('en-SG', {
  maximumFractionDigits: 0,
});

let courses = [];
let category = 'All';

function photoUrl(id) {
  return `https://images.unsplash.com/photo-${encodeURIComponent(id)}?auto=format&fit=crop&w=800&q=70`;
}

function addText(parent, tag, className, value) {
  const element = document.createElement(tag);
  element.className = className;
  element.textContent = value;
  parent.append(element);
  return element;
}

function courseCard(course) {
  const card = document.createElement('article');
  card.className = 'course-card';
  card.id = `course-${course.code}`;

  const imageWrap = document.createElement('div');
  imageWrap.className = 'course-image-wrap';
  const image = document.createElement('img');
  image.className = 'course-image';
  image.src = photoUrl(course.img);
  image.alt = `Food photo for ${course.title}`;
  image.loading = 'lazy';
  image.width = 800;
  image.height = 520;
  imageWrap.append(image);
  addText(imageWrap, 'span', 'image-category', course.cat);
  card.append(imageWrap);

  const body = document.createElement('div');
  body.className = 'course-body';
  const top = document.createElement('div');
  top.className = 'course-topline';
  addText(top, 'span', 'course-code', course.code);
  addText(top, 'span', 'course-level', course.level);
  body.append(top);
  addText(body, 'h3', 'course-title', course.title);
  addText(body, 'p', 'course-summary', course.summary);

  const details = document.createElement('dl');
  details.className = 'course-details';
  for (const [label, value] of [
    ['Campus', course.campus],
    ['Length', `${course.weeks} ${course.weeks === 1 ? 'week' : 'weeks'}`],
    ['Schedule', course.when],
  ]) {
    const row = document.createElement('div');
    addText(row, 'dt', '', label);
    addText(row, 'dd', '', value);
    details.append(row);
  }
  body.append(details);

  const foot = document.createElement('div');
  foot.className = 'course-foot';
  addText(foot, 'span', 'fee-label', 'Course fee');
  addText(foot, 'strong', 'course-fee', `S$${currency.format(course.fee)}`);
  body.append(foot);
  const button = addText(body, 'button', 'button button-primary course-signup', 'Sign up');
  button.type = 'button';
  button.dataset.signup = course.code;
  card.append(body);
  return card;
}

function renderCourses() {
  const query = search.value.trim().toLocaleLowerCase();
  const visible = courses.filter(course => {
    const matchesCategory = category === 'All' || course.cat === category;
    const searchable = [course.code, course.title, course.summary, course.level, course.cat, course.campus, course.when]
      .join(' ').toLocaleLowerCase();
    return matchesCategory && searchable.includes(query);
  });
  grid.replaceChildren(...visible.map(courseCard));
  status.textContent = visible.length === 0
    ? 'No courses match your search. Try a different word or category.'
    : `Showing ${visible.length} of ${courses.length} courses`;
}

function setCategory(nextCategory) {
  category = nextCategory;
  for (const chip of chips) {
    const selected = chip.dataset.filter === category;
    chip.classList.toggle('is-active', selected);
    chip.setAttribute('aria-pressed', String(selected));
  }
  if (courses.length) renderCourses();
}

for (const chip of chips) {
  chip.addEventListener('click', () => setCategory(chip.dataset.filter));
}
search.addEventListener('input', () => {
  if (courses.length) renderCourses();
});
grid.addEventListener('click', event => {
  const button = event.target.closest('[data-signup]');
  if (!button) return;
  const course = courses.find(item => item.code === button.dataset.signup);
  if (course) openSignup(course);
});
for (const link of document.querySelectorAll('[data-campus-filter]')) {
  link.addEventListener('click', () => {
    search.value = '';
    setCategory(link.dataset.campusFilter);
  });
}
document.addEventListener('course-source-open', () => {
  search.value = '';
  setCategory('All');
});

async function loadCourses() {
  try {
    const response = await fetch('data/courses.json');
    if (!response.ok) throw new Error(`HTTP ${response.status}`);
    const data = await response.json();
    if (!Array.isArray(data)) throw new Error('Invalid course catalogue');
    courses = data;
    renderCourses();
  } catch (error) {
    status.textContent = 'Courses could not be loaded. Please refresh the page or try again later.';
    console.error('Course catalogue error:', error);
  }
}

loadCourses();
