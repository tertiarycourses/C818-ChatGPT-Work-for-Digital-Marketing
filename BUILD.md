# C818 build instructions

The published content source is data/course.json and data/labs.json. The course-local build engine is .claude/skills/non-wsq-courseware-build/build/. All artifacts share title, version, topic order and lab inventory.

```bash
bash .claude/skills/non-wsq-courseware-build/build/build_courseware.sh
python3 scripts/build_lab_documents.py
python3 /Users/alfredang/.agents/skills/non-wsq-courseware-qa/scan_prohibited.py .
```

Python dependencies: python-pptx, python-docx, Pillow, PyMuPDF and pypdf. PDF export requires LibreOffice (soffice). Browser evidence uses Playwright Chromium. The static document TOC is corrected against final PDF pagination by scripts/finalize_toc.py before the last export.

scripts/author_course.py and author_labs.py preserve the original authored sources. author_course.py references the local academy source checkout used for the initial copy; normal courseware rebuilding does not need that source checkout. Review current files before running an authoring script, as it replaces generated content. scripts/prepare_samples.py regenerates classroom recovery samples; preserve later edits before using it.

Detailed learner procedures belong in lab READMEs and the Learner Guide. The deck contains concepts and lab overviews only. Run independent rendered QA after content changes. Publish only the verified current version; exclude reference/, assessment/, credentials and superseded archive/ content.
