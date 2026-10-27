from pathlib import Path
import re
s=Path('stitch-export/code.html').read_text(encoding='utf-8')
s=s.replace('lang="en"','lang="ko"')
s=s.replace('<meta charset="utf-8">','<meta charset="utf-8"><title>김민서 | 개인 포트폴리오 · 예시</title><meta name="description" content="디자인과 기술을 연결하는 김민서의 예시 개인 포트폴리오"><link rel="stylesheet" href="styles.css"><script src="script.js" defer></script>')
s=s.replace('<header class=', '<a class="skip-link" href="#home">본문으로 바로 이동</a><header class=',1)
s=s.replace('<nav class="hidden md:flex','<nav aria-label="주 메뉴" class="hidden md:flex',1)
s=s.replace('<div class="flex items-center gap-space-md"><a','<div class="flex items-center gap-space-md"><button id="menuToggle" class="menu-toggle" type="button" aria-label="메뉴 열기" aria-expanded="false" aria-controls="mobileMenu"><span aria-hidden="true">☰</span></button><a',1)
s=s.replace('</header>','<nav id="mobileMenu" class="mobile-menu" aria-label="모바일 메뉴" hidden><a href="#home">Home</a><a href="#about">About</a><a href="#projects">Projects</a><a href="#contact">Contact</a></nav></header>',1)
s=s.replace('Product Designer &amp; Frontend Engineer','Product Designer &amp; Frontend Engineer · 예시')
s=s.replace('실무 임팩트와 기술적 완성도를 담은 대표 프로젝트 3선','예시 프로젝트 3선 · 카드 클릭 시 관련 기술의 공식 사이트로 이동합니다.')
s=s.replace('서울대학교 컴퓨터공학','예시대학교 컴퓨터공학').replace('토스, 네이버 등','예시 테크 기업 등')
s=s.replace('저를 소개합니다','저를 소개합니다 <span class="example-label">예시 프로필</span>')
s=s.replace('© 2025 Minseo Kim. All rights reserved.','© 2026 Minseo Kim. 개인정보·경력·프로젝트·수치는 모두 예시입니다.')
s=s.replace('React','JavaScript').replace('Next.js','HTML / CSS').replace('Tailwind CSS','CSS').replace('>Tailwind<','>CSS<')
pattern=r'(<div class=")(group flex flex-col rounded-3xl[^\"]*)(">)(.*?)(?=<!-- PROJECT [23]:|</div>\s*</div>\s*</section>\s*<!-- CONTACT SECTION -->)'
urls=['https://www.figma.com/','https://storybook.js.org/','https://developer.mozilla.org/en-US/docs/Web/API/Canvas_API']
count=[0]
def card(m):
 i=count[0]; count[0]+=1
 block=re.sub(r'<a class="([^"]*)" href="#contact">',r'<span class="\1">',m.group(4)).replace('</a>','</span>')
 end=block.rfind('</div>'); block=block[:end]+'</a>'+block[end+6:]
 return '<a class="project-card '+m.group(2)+'" href="'+urls[i]+'" target="_blank" rel="noopener noreferrer" aria-label="'+['FinFlow','Aura Design System','CollabSpace'][i]+' 예시 프로젝트 관련 기술 사이트 (새 탭)">'+block
s=re.sub(pattern,card,s,flags=re.S)
assert count[0]==3
s=s.replace('<span class="font-mono text-sm font-semibold text-on-surface truncate" id="emailText">minseo.kim.design@example.com</span>','<a class="email-address font-mono text-sm font-semibold text-on-surface" id="emailText" href="mailto:minseo.kim.design@example.com">minseo.kim.design@example.com</a>')
s=re.sub(r' onsubmit="[^"]*"','',s)
s=s.replace('보내주신 문의는 24시간 이내에 확인 후 회신드립니다.','입력한 내용으로 메일 앱을 엽니다. 실제 발송은 메일 앱에서 완료해 주세요.')
s=s.replace('메시지가 성공적으로 전송되었습니다! 빠르게 검토 후 답변드리겠습니다.','메일 작성창을 요청했습니다. 열리지 않으면 이메일 주소를 직접 클릭해 주세요.')
s=s.replace('id="formSuccess"','id="formSuccess" role="status" aria-live="polite"')
s=s.replace('메시지 보내기 (Send Message)','메일 작성창 열기 (Compose Email)')
s=re.sub(r'<!-- Interactive JavaScript for Copy Email -->\s*<script>.*?</script>','',s,flags=re.S)
Path('public').mkdir(exist_ok=True)
Path('public/index.html').write_text(s,encoding='utf-8')

