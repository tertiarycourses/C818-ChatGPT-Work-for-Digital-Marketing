from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[4]
DATA=json.loads((ROOT/'data/course.json').read_text())
LABS=json.loads((ROOT/'data/labs.json').read_text())
TITLE=SHORT_TITLE=DATA['title'];COURSE_CODE=DATA['code'];VERSION=DATA['version'];VERSION_DATE=DATA['date']
ORG='Tertiary Infotech Academy Pte Ltd';UEN='UEN: 201200696W';TRAINER='Assigned by Tertiary Infotech';DAYS=2;COMPANY=DATA['company'];MODE='Instructor-led, hands-on marketing production labs';DARK_THEME=False
LEARNING_OUTCOMES=DATA['outcomes'];LO_TITLES=['Grounded delegation','Flyer production','Social content','Email and measurement']
TOPICS=[dict(num=t['num'],code=f"{t['num']:02d}",title=t['title'],subtitle=t['subtitle'],concepts=[c['title'] for c in t['concepts']]) for t in DATA['topics']]
LAB_SLUGS={a['num']:a['slug'] for a in LABS}
DAY_THEMES={1:'Ground the campaign and design the flyer',2:'Develop social content and the email campaign'}
VERSION_HISTORY=[('1.0',VERSION_DATE,'Initial C818 release with eight connected marketing labs and the reference PPT theme.',ORG)]
def SCHEDULE(lab_titles):
 return {
 1:(DAY_THEMES[1],[('9:30','9:50',20,'admin','Welcome, outcomes, source boundaries and setup'),('9:50','10:35',45,'topic','Topic 1 concepts: Work, sources and campaign brief'),('10:35','11:20',45,'lab',lab_titles([1])),('11:20','11:35',15,'break','Tea break'),('11:35','12:10',35,'topic','Topic 1 demonstration: reusable production workflow'),('12:10','13:00',50,'lab',lab_titles([2])),('13:00','14:00',60,'lunch','Lunch'),('14:00','14:45',45,'topic','Topic 2 concepts: hierarchy, brand and source-checked copy'),('14:45','16:00',75,'lab',lab_titles([3])),('16:00','16:15',15,'break','Tea break'),('16:15','17:10',55,'lab',lab_titles([4])),('17:10','18:10',60,'topic','Topic 2 design critique, correction demonstration and peer comparison'),('18:10','18:30',20,'recap','Day 1 recap: LO1 and LO2; checkpoint handoff')]),
 2:(DAY_THEMES[2],[('9:30','9:45',15,'recap','Day 1 checkpoint recovery and brief review'),('9:45','10:25',40,'topic','Topic 3 concepts: article structure, adaptation and brand voice'),('10:25','11:35',70,'lab',lab_titles([5])),('11:35','11:50',15,'break','Tea break'),('11:50','12:00',10,'topic','Topic 3 demonstration: calendar dependencies and editorial gate'),('12:00','13:00',60,'lab',lab_titles([6])),('13:00','14:00',60,'lunch','Lunch'),('14:00','14:45',45,'topic','Topic 4 concepts: recipient rules, sequence and draft preview'),('14:45','16:10',85,'lab',lab_titles([7])),('16:10','16:25',15,'break','Tea break'),('16:25','17:00',35,'topic','Topic 4 concepts: metrics, denominators and controlled comparisons'),('17:00','17:50',50,'lab',lab_titles([8])),('17:50','18:15',25,'topic','Campaign review: explain decisions using sources and evidence'),('18:15','18:30',15,'recap','LO3 and LO4 recap; keep practising and next steps')])}
