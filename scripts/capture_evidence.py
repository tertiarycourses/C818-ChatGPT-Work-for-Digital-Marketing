from pathlib import Path
import functools,http.server,threading
from playwright.sync_api import sync_playwright
R=Path(__file__).resolve().parents[1];out=R/'courseware/assets';out.mkdir(exist_ok=True)
server=http.server.ThreadingHTTPServer(('127.0.0.1',8765),functools.partial(http.server.SimpleHTTPRequestHandler,directory=str(R)))
threading.Thread(target=server.serve_forever,daemon=True).start()
with sync_playwright() as p:
 b=p.chromium.launch();page=b.new_page(viewport={'width':1440,'height':1000},device_scale_factor=1)
 errors=[];page.on('pageerror',lambda e:errors.append(str(e)))
 url='http://127.0.0.1:8765/labs/lab-01-grounded-campaign-brief/assets/cnbacademy/'
 page.goto(url,wait_until='networkidle');page.screenshot(path=str(out/'academy-desktop.png'))
 cards=page.locator('.course-card').count();print('course card selector count',cards)
 page.set_viewport_size({'width':375,'height':812});page.goto(url,wait_until='networkidle');page.screenshot(path=str(out/'academy-mobile.png'))
 print('mobile widths',page.evaluate('[document.documentElement.scrollWidth,document.documentElement.clientWidth]'))
 page.get_by_role('button',name='Ask our course assistant',exact=True).click();page.locator('#chat-input').fill('BAK-101');page.locator('#chat-form button[type=submit]').click();print('assistant',page.locator('#chat-log').inner_text()[-400:]);print('site errors',errors)
 page.set_viewport_size({'width':900,'height':900});page.goto('http://127.0.0.1:8765/labs/lab-07-email-sequence-and-segmentation/checkpoints/email-1.html',wait_until='networkidle');page.screenshot(path=str(out/'email-desktop.png'))
 page.set_viewport_size({'width':375,'height':812});page.reload(wait_until='networkidle');page.screenshot(path=str(out/'email-mobile.png'));print('email mobile widths',page.evaluate('[document.documentElement.scrollWidth,document.documentElement.clientWidth]'))
 b.close()
server.shutdown()
