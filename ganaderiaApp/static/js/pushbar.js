function Pushbar()
{
  this.config = { overlay: true, blur: true }
  this.activeId;
  this.activeElement;
  this.overlayElement;
  if (this.config.overlay) {
      this.overlayElement = document.createElement('div');
      this.overlayElement.classList.add('pushbar_overlay');
      document.querySelector('body').appendChild(this.overlayElement);
  }
  if (this.config.blur) {
      const mainContent = document.querySelector('.pushbar_main_content');
      if (mainContent) {
          mainContent.classList.add('pushbar_blur');
      }
  }
  this.bindEvents();
}
Pushbar.prototype.emitOpening = function () {
  const event = new CustomEvent('pushbar_opening', { bubbles: true, detail: { element: this.activeElement, id: this.activeId } });
  this.activeElement.dispatchEvent(event);
}

Pushbar.prototype.emitClosing = function () {
  const event = new CustomEvent('pushbar_closing', { bubbles: true, detail: { element: this.activeElement, id: this.activeId } });
  this.activeElement.dispatchEvent(event);
}

Pushbar.prototype.handleOpenEvent = function (e) {
  e.preventDefault();
  const pushbarId = e.currentTarget.getAttribute('data-pushbar-target');
  this.open(pushbarId);
}

Pushbar.prototype.handleCloseEvent = function (e) {
  e.preventDefault();
  this.close();
}
Pushbar.prototype.handleKeyEvent= function (e) {
  if (e.keyCode === 27) this.close();
}
Pushbar.prototype.bindEvents= function () {
  const triggers = document.querySelectorAll('[data-pushbar-target]');
  const closers = document.querySelectorAll('[data-pushbar-close]');
  triggers.forEach(trigger => trigger.addEventListener('click', e => this.handleOpenEvent(e), false));
  closers.forEach(closer => closer.addEventListener('click', e => this.handleCloseEvent(e), false));
  if (this.overlayElement) {
      this.overlayElement.addEventListener('click', e => this.handleCloseEvent(e), false);
  }
  document.addEventListener('keyup', e => this.handleKeyEvent(e));
}
Pushbar.prototype.open= function (pushbarId) {
  if (this.activeId === String(pushbarId) || !pushbarId) return;
  if (this.activeId && this.activeId !== String(pushbarId)) this.close();
  this.activeId = pushbarId
  this.activeElement = document.querySelector(`[data-pushbar-id="${this.activeId}"]`)
  if (!this.activeElement) return;
  this.emitOpening();
  this.activeElement.classList.add('opened');
  const pageRootElement = document.querySelector('html')
  pageRootElement.classList.add('pushbar_locked');
  pageRootElement.setAttribute('pushbar', pushbarId)
}
Pushbar.prototype.close= function () {
  if (!this.activeId) return;
  this.emitClosing();
  this.activeElement.classList.remove('opened');
  const pageRootElement = document.querySelector('html')
  pageRootElement.classList.remove('pushbar_locked');
  pageRootElement.removeAttribute('pushbar')
  this.activeId = null;
  this.activeElement = null;
}
