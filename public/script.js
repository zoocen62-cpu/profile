'use strict';
const menuToggle = document.getElementById('menuToggle');
const mobileMenu = document.getElementById('mobileMenu');
function closeMenu() {
  mobileMenu.hidden = true;
  menuToggle.setAttribute('aria-expanded', 'false');
  menuToggle.setAttribute('aria-label', '메뉴 열기');
}
menuToggle.addEventListener('click', () => {
  const opening = mobileMenu.hidden;
  mobileMenu.hidden = !opening;
  menuToggle.setAttribute('aria-expanded', String(opening));
  menuToggle.setAttribute('aria-label', opening ? '메뉴 닫기' : '메뉴 열기');
});
mobileMenu.addEventListener('click', (event) => {
  if (event.target.closest('a')) closeMenu();
});
document.addEventListener('keydown', (event) => {
  if (event.key === 'Escape' && !mobileMenu.hidden) {
    closeMenu();
    menuToggle.focus();
  }
});
window.matchMedia('(min-width: 768px)').addEventListener('change', closeMenu);
const navigationLinks = document.querySelectorAll('nav a[href^="#"]');
const sections = [...document.querySelectorAll('main section[id]')];
function updateNavigation() {
  const current = [...sections].reverse().find(section => section.getBoundingClientRect().top <= 150) || sections[0];
  navigationLinks.forEach(link => {
    if (link.hash === `#${current.id}`) link.setAttribute('aria-current', 'page');
    else link.removeAttribute('aria-current');
  });
}
window.addEventListener('scroll', updateNavigation, { passive: true });
updateNavigation();
const emailAddress = document.getElementById('emailText').textContent.trim();
const copyButton = document.getElementById('copyEmailBtn');
copyButton.addEventListener('click', async () => {
  const label = document.getElementById('copyLabel');
  try {
    await navigator.clipboard.writeText(emailAddress);
    label.textContent = '복사됨';
    document.getElementById('copyIcon').textContent = 'check';
    copyButton.setAttribute('aria-label', '이메일 주소가 복사되었습니다');
  } catch {
    label.textContent = '직접 복사';
    copyButton.setAttribute('aria-label', '이메일 주소를 선택했습니다. 직접 복사해 주세요');
    const range = document.createRange();
    range.selectNodeContents(document.getElementById('emailText'));
    const selection = window.getSelection();
    selection.removeAllRanges();
    selection.addRange(range);
  }
  setTimeout(() => {
    label.textContent = '복사';
    document.getElementById('copyIcon').textContent = 'content_copy';
    copyButton.setAttribute('aria-label', '이메일 주소 복사');
  }, 2500);
});
document.getElementById('contactForm').addEventListener('submit', event => {
  event.preventDefault();
  const name = document.getElementById('name').value.trim();
  const email = document.getElementById('email').value.trim();
  const subject = document.getElementById('subject').selectedOptions[0].textContent;
  const message = document.getElementById('message').value.trim();
  const body = `이름: ${name}\n회신 이메일: ${email}\n\n${message}`;
  window.location.href = `mailto:${emailAddress}?subject=${encodeURIComponent(`[포트폴리오 문의] ${subject}`)}&body=${encodeURIComponent(body)}`;
  document.getElementById('formSuccess').classList.remove('hidden');
});
