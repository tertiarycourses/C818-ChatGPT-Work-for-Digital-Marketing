import course_data as C
DOMAIN2=[dict(num=a['num'],topic=a['topic'],title=a['title'],objective=C.LEARNING_OUTCOMES[1],desc=a['goal']+' '+a['build'],build=a['build'],services='ChatGPT Work, browser and file editor',steps=[(h,t) for h,t in a['steps']],test=' '.join(a['checks'])) for a in C.LABS if a['topic']==2]
