/**
 * BAMBINO KIDS FASHION - Central Store Engine
 * Handles Data, Cart, Navigation, WhatsApp Order, and Dynamic Views
 */

const DEFAULT_PRODUCTS = [
  {
    "id": 1,
    "name": "فستان روبي المخملي الفاخر بياقة دانتيل وأزرار ذهبية",
    "cat": "girls",
    "catName": "ملابس بناتي",
    "price": 295,
    "oldPrice": 380,
    "rating": 5.0,
    "reviews": 42,
    "sales": 340,
    "isBestSeller": true,
    "isFeatured": true,
    "isNew": false,
    "badge": "الأكثر مبيعاً ⭐",
    "badgeClass": "badge-bestseller",
    "sizes": [
      "1-2y",
      "3-5y",
      "6-8y"
    ],
    "img": "images/prod_girls_party.jpg",
    "desc": "قطعة فاخرة مصنوعة بعناية فائقة من أجود أنواع القطن العضوي 100% المريح والآمن على بشرة طفلك الحساسة. تصميم أنيق وعصري يجمع بين راحة الارتداء وفخامة الإطلالة لجميع المناسبات."
  },
  {
    "id": 2,
    "name": "سلة هدايا المواليد الفاخرة (بطانية محبوكة ودبدوب ولعبة خشبية)",
    "cat": "baby",
    "catName": "بيبي ومواليد",
    "price": 360,
    "oldPrice": 450,
    "rating": 4.9,
    "reviews": 58,
    "sales": 290,
    "isBestSeller": true,
    "isFeatured": true,
    "isNew": false,
    "badge": "الأعلى سعراً وفخامة 💎",
    "badgeClass": "badge-featured",
    "sizes": [
      "0-6m"
    ],
    "img": "images/prod_baby_gift.jpg",
    "desc": "قطعة فاخرة مصنوعة بعناية فائقة من أجود أنواع القطن العضوي 100% المريح والآمن على بشرة طفلك الحساسة. تصميم أنيق وعصري يجمع بين راحة الارتداء وفخامة الإطلالة لجميع المناسبات."
  },
  {
    "id": 3,
    "name": "بليزر أولادي كحلي فاخر بأزرار مذهبة ومنديل قرمزي",
    "cat": "boys",
    "catName": "ملابس أولادي",
    "price": 260,
    "oldPrice": 320,
    "rating": 4.8,
    "reviews": 31,
    "sales": 210,
    "isBestSeller": false,
    "isFeatured": true,
    "isNew": true,
    "badge": "وصل حديثاً 🚀",
    "badgeClass": "badge-new",
    "sizes": [
      "3-5y",
      "6-8y",
      "9-12y"
    ],
    "img": "images/prod_boys_blazer.jpg",
    "desc": "قطعة فاخرة مصنوعة بعناية فائقة من أجود أنواع القطن العضوي 100% المريح والآمن على بشرة طفلك الحساسة. تصميم أنيق وعصري يجمع بين راحة الارتداء وفخامة الإطلالة لجميع المناسبات."
  },
  {
    "id": 4,
    "name": "طقم الأعياد أولادي قميص كتان بيج وحمالات وبنطال كحلي",
    "cat": "boys",
    "catName": "ملابس أولادي",
    "price": 235,
    "oldPrice": 290,
    "rating": 4.9,
    "reviews": 45,
    "sales": 310,
    "isBestSeller": true,
    "isFeatured": true,
    "isNew": false,
    "badge": "الأكثر طلباً 🔥",
    "badgeClass": "badge-bestseller",
    "sizes": [
      "1-2y",
      "3-5y",
      "6-8y"
    ],
    "img": "images/kids_cat_boys.jpg",
    "desc": "قطعة فاخرة مصنوعة بعناية فائقة من أجود أنواع القطن العضوي 100% المريح والآمن على بشرة طفلك الحساسة. تصميم أنيق وعصري يجمع بين راحة الارتداء وفخامة الإطلالة لجميع المناسبات."
  },
  {
    "id": 5,
    "name": "فستان أبيض مطرز مع كارديجان صوف أحمر وحذاء ناعم",
    "cat": "girls",
    "catName": "ملابس بناتي",
    "price": 245,
    "oldPrice": 310,
    "rating": 4.9,
    "reviews": 38,
    "sales": 260,
    "isBestSeller": false,
    "isFeatured": true,
    "isNew": true,
    "badge": "المجموعة الحصرية ✨",
    "badgeClass": "badge-featured",
    "sizes": [
      "1-2y",
      "3-5y",
      "6-8y"
    ],
    "img": "images/kids_cat_girls.jpg",
    "desc": "قطعة فاخرة مصنوعة بعناية فائقة من أجود أنواع القطن العضوي 100% المريح والآمن على بشرة طفلك الحساسة. تصميم أنيق وعصري يجمع بين راحة الارتداء وفخامة الإطلالة لجميع المناسبات."
  },
  {
    "id": 6,
    "name": "رومبر أطفال مخطط ناعم من الصوف الطبيعي مع طاقية وجوارب",
    "cat": "baby",
    "catName": "بيبي ومواليد",
    "price": 185,
    "oldPrice": 230,
    "rating": 4.8,
    "reviews": 29,
    "sales": 180,
    "isBestSeller": false,
    "isFeatured": false,
    "isNew": true,
    "badge": "صوف طبيعي 100%",
    "badgeClass": "badge-new",
    "sizes": [
      "0-6m",
      "1-2y"
    ],
    "img": "images/kids_cat_baby.jpg",
    "desc": "قطعة فاخرة مصنوعة بعناية فائقة من أجود أنواع القطن العضوي 100% المريح والآمن على بشرة طفلك الحساسة. تصميم أنيق وعصري يجمع بين راحة الارتداء وفخامة الإطلالة لجميع المناسبات."
  },
  {
    "id": 7,
    "name": "هودي أطفال قرمزي قطن عضوي بشعار الدبدوب المطرز",
    "cat": "accessories",
    "catName": "هوديز وكاجوال",
    "price": 160,
    "oldPrice": 210,
    "rating": 4.7,
    "reviews": 24,
    "sales": 195,
    "isBestSeller": false,
    "isFeatured": false,
    "isNew": true,
    "badge": "قطن عضوي مريح",
    "badgeClass": "badge-new",
    "sizes": [
      "3-5y",
      "6-8y",
      "9-12y"
    ],
    "img": "images/prod_kids_hoodie.jpg",
    "desc": "قطعة فاخرة مصنوعة بعناية فائقة من أجود أنواع القطن العضوي 100% المريح والآمن على بشرة طفلك الحساسة. تصميم أنيق وعصري يجمع بين راحة الارتداء وفخامة الإطلالة لجميع المناسبات."
  },
  {
    "id": 8,
    "name": "سنيكرز أطفال جلدي أبيض بنجمة حمراء مع حقيبة ونظارة",
    "cat": "accessories",
    "catName": "أحذية وإكسسوارات",
    "price": 130,
    "oldPrice": 175,
    "rating": 4.8,
    "reviews": 52,
    "sales": 280,
    "isBestSeller": true,
    "isFeatured": false,
    "isNew": false,
    "badge": "أفضل قيمة 🏷️",
    "badgeClass": "badge-discount",
    "sizes": [
      "1-2y",
      "3-5y",
      "6-8y"
    ],
    "img": "images/kids_cat_shoes.jpg",
    "desc": "قطعة فاخرة مصنوعة بعناية فائقة من أجود أنواع القطن العضوي 100% المريح والآمن على بشرة طفلك الحساسة. تصميم أنيق وعصري يجمع بين راحة الارتداء وفخامة الإطلالة لجميع المناسبات."
  },
  {
    "id": 9,
    "name": "فستان الأميرة الملكي ياقوتي مخملي بتطريز دانتيل إسباني وحذاء أحمر",
    "cat": "girls",
    "catName": "ملابس بناتي",
    "price": 385,
    "oldPrice": 480,
    "rating": 5.0,
    "reviews": 64,
    "sales": 320,
    "isBestSeller": true,
    "isFeatured": true,
    "isNew": true,
    "badge": "إصدار ملكي خاص 👑",
    "badgeClass": "badge-bestseller",
    "sizes": [
      "1-2y",
      "3-5y",
      "6-8y"
    ],
    "img": "images/prod_girl_floral_dress.jpg",
    "desc": "قطعة فاخرة مصنوعة بعناية فائقة من أجود أنواع القطن العضوي 100% المريح والآمن على بشرة طفلك الحساسة. تصميم أنيق وعصري يجمع بين راحة الارتداء وفخامة الإطلالة لجميع المناسبات."
  }
];

const DEFAULT_SETTINGS = {
  storeName: "بامبينو كيدز | BAMBINO KIDS",
  announcement: "🚚 توصيل سريع لجميع مدن المملكة | خصم 20% على تشكيلة الصيف الفاخرة | كود: KIDS20",
  whatsapp: "966500000000",
  phone: "+966 50 000 0000",
  email: "care@bambinokids.com",
  address: "المملكة العربية السعودية - الرياض - طريق الملك فهد",
  currency: "ر.س",
  freeShippingLimit: 250
};

const BambinoStore = {
  // Initialization
  init() {
    this.initStorage();
    this.updateCartBadge();
    this.bindGlobalEvents();
    this.applySettingsToDOM();
  },

  initStorage() {
    if (!localStorage.getItem('bambino_products')) {
      localStorage.setItem('bambino_products', JSON.stringify(DEFAULT_PRODUCTS));
    }
    if (!localStorage.getItem('bambino_settings')) {
      localStorage.setItem('bambino_settings', JSON.stringify(DEFAULT_SETTINGS));
    }
    if (!localStorage.getItem('bambino_cart')) {
      localStorage.setItem('bambino_cart', JSON.stringify([]));
    }
  },

  getProducts() {
    try {
      const p = localStorage.getItem('bambino_products');
      return p ? JSON.parse(p) : DEFAULT_PRODUCTS;
    } catch (e) {
      return DEFAULT_PRODUCTS;
    }
  },

  saveProducts(products) {
    localStorage.setItem('bambino_products', JSON.stringify(products));
  },

  getProductById(id) {
    const products = this.getProducts();
    return products.find(p => p.id === parseInt(id));
  },

  getSettings() {
    try {
      const s = localStorage.getItem('bambino_settings');
      return s ? JSON.parse(s) : DEFAULT_SETTINGS;
    } catch (e) {
      return DEFAULT_SETTINGS;
    }
  },

  saveSettings(settings) {
    localStorage.setItem('bambino_settings', JSON.stringify(settings));
    this.applySettingsToDOM();
  },

  applySettingsToDOM() {
    const s = this.getSettings();
    document.querySelectorAll('.store-announcement-text').forEach(el => el.textContent = s.announcement);
    document.querySelectorAll('.store-phone-text').forEach(el => el.textContent = s.phone);
    document.querySelectorAll('.store-email-text').forEach(el => el.textContent = s.email);
    document.querySelectorAll('.store-address-text').forEach(el => el.textContent = s.address);
    document.querySelectorAll('.store-whatsapp-link').forEach(el => {
      el.href = `https://wa.me/${s.whatsapp}`;
    });
  },

  // Cart Management
  getCart() {
    try {
      return JSON.parse(localStorage.getItem('bambino_cart')) || [];
    } catch (e) {
      return [];
    }
  },

  saveCart(cart) {
    localStorage.setItem('bambino_cart', JSON.stringify(cart));
    this.updateCartBadge();
    this.renderCartDrawer();
  },

  addToCart(productId, size = '1-2y', qty = 1) {
    const product = this.getProductById(productId);
    if (!product) return;

    let cart = this.getCart();
    const existingIndex = cart.findIndex(item => item.id === product.id && item.size === size);

    if (existingIndex > -1) {
      cart[existingIndex].qty += parseInt(qty);
    } else {
      cart.push({
        id: product.id,
        name: product.name,
        price: product.price,
        img: product.img,
        size: size,
        qty: parseInt(qty)
      });
    }

    this.saveCart(cart);
    this.showToast(`✨ تم إضافة "${product.name}" إلى سلة مشترياتك!`);
    this.openCart();
  },

  removeFromCart(index) {
    let cart = this.getCart();
    cart.splice(index, 1);
    this.saveCart(cart);
    this.showToast('🗑️ تم حذف المنتج من السلة');
  },

  updateCartQty(index, delta) {
    let cart = this.getCart();
    if (!cart[index]) return;
    cart[index].qty += delta;
    if (cart[index].qty <= 0) {
      cart.splice(index, 1);
    }
    this.saveCart(cart);
  },

  clearCart() {
    this.saveCart([]);
  },

  getCartCount() {
    const cart = this.getCart();
    return cart.reduce((sum, item) => sum + item.qty, 0);
  },

  getCartSubtotal() {
    const cart = this.getCart();
    return cart.reduce((sum, item) => sum + (item.price * item.qty), 0);
  },

  updateCartBadge() {
    const count = this.getCartCount();
    document.querySelectorAll('.cart-badge-count').forEach(el => {
      el.textContent = count;
      el.style.display = count > 0 ? 'flex' : 'none';
    });
  },

  openCart() {
    const overlay = document.getElementById('cartOverlay');
    if (overlay) {
      this.renderCartDrawer();
      overlay.classList.add('active');
      document.body.style.overflow = 'hidden';
    }
  },

  closeCart() {
    const overlay = document.getElementById('cartOverlay');
    if (overlay) {
      overlay.classList.remove('active');
      document.body.style.overflow = '';
    }
  },

  renderCartDrawer() {
    const container = document.getElementById('cartItemsList');
    const subtotalEl = document.getElementById('cartSubtotalValue');
    if (!container || !subtotalEl) return;

    const cart = this.getCart();
    const settings = this.getSettings();

    if (cart.length === 0) {
      container.innerHTML = `
        <div style="text-align: center; padding: 40px 10px; color: #94a3b8;">
          <svg style="width: 64px; height: 64px; margin-bottom: 16px; opacity: 0.5;" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M16 11V7a4 4 0 00-8 0v4M5 9h14l1 12H4L5 9z"></path></svg>
          <h4 style="color: var(--dark); margin-bottom: 8px; font-weight: 800;">سلة المشتريات فارغة</h4>
          <p style="font-size: 0.9rem; margin-bottom: 20px;">استكشف تشكيلاتنا الأنيقة وأضف قطع أطفالك المفضلة</p>
          <a href="shop.html" class="btn-add-cart" style="display: inline-block; padding: 10px 24px;">تسوق الآن</a>
        </div>
      `;
      subtotalEl.textContent = `0 ${settings.currency}`;
      return;
    }

    let html = '';
    cart.forEach((item, idx) => {
      html += `
        <div class="cart-item">
          <img src="${item.img}" alt="${item.name}" class="cart-item-img">
          <div class="cart-item-details">
            <div class="cart-item-title">${item.name}</div>
            <div class="cart-item-meta">المقاس: <strong>${item.size}</strong></div>
            <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 6px;">
              <div class="cart-item-price">${item.price * item.qty} ${settings.currency}</div>
              <div class="qty-stepper" style="height: 32px;">
                <button onclick="BambinoStore.updateCartQty(${idx}, -1)" style="width: 28px;">-</button>
                <input type="text" value="${item.qty}" readonly style="width: 32px; font-size: 0.85rem;">
                <button onclick="BambinoStore.updateCartQty(${idx}, 1)" style="width: 28px;">+</button>
              </div>
            </div>
            <button class="cart-item-remove" onclick="BambinoStore.removeFromCart(${idx})" style="margin-top: 6px;">حذف من السلة ✕</button>
          </div>
        </div>
      `;
    });

    container.innerHTML = html;
    subtotalEl.textContent = `${this.getCartSubtotal()} ${settings.currency}`;
  },

  // Checkout Modal
  openCheckoutModal() {
    const cart = this.getCart();
    if (cart.length === 0) {
      this.showToast('⚠️ سلتك فارغة! يرجى اختيار منتجات أولاً');
      return;
    }
    this.closeCart();
    const modal = document.getElementById('checkoutModalOverlay');
    if (modal) {
      modal.classList.add('active');
      document.body.style.overflow = 'hidden';
      this.renderCheckoutSummary();
    }
  },

  closeCheckoutModal() {
    const modal = document.getElementById('checkoutModalOverlay');
    if (modal) {
      modal.classList.remove('active');
      document.body.style.overflow = '';
    }
  },

  renderCheckoutSummary() {
    const summaryEl = document.getElementById('checkoutItemsSummary');
    if (!summaryEl) return;
    const cart = this.getCart();
    const settings = this.getSettings();

    let html = '';
    cart.forEach(item => {
      html += `
        <div style="display: flex; justify-content: space-between; font-size: 0.88rem; margin-bottom: 6px;">
          <span>${item.name} (مقاس: ${item.size} × ${item.qty})</span>
          <strong>${item.price * item.qty} ${settings.currency}</strong>
        </div>
      `;
    });
    summaryEl.innerHTML = html;
    const totalEl = document.getElementById('checkoutTotalText');
    if (totalEl) totalEl.textContent = `${this.getCartSubtotal()} ${settings.currency}`;
  },

  submitOrderToWhatsApp(event) {
    if (event) event.preventDefault();

    const name = document.getElementById('orderName')?.value.trim();
    const phone = document.getElementById('orderPhone')?.value.trim();
    const city = document.getElementById('orderCity')?.value.trim();
    const address = document.getElementById('orderAddress')?.value.trim();
    const notes = document.getElementById('orderNotes')?.value.trim() || 'لا توجد ملاحظات إضافية';

    if (!name || !phone || !city || !address) {
      alert('يرجى ملء جميع الحقول المطلوبة (الاسم، الجوال، المدينة، والعنوان التفصيلي)');
      return;
    }

    const cart = this.getCart();
    const settings = this.getSettings();
    const total = this.getCartSubtotal();

    let itemsText = '';
    cart.forEach((item, index) => {
      itemsText += `${index + 1}. ${item.name}%0a   - المقاس: ${item.size}%0a   - الكمية: ${item.qty}%0a   - السعر: ${item.price * item.qty} ${settings.currency}%0a`;
    });

    const msg = 
`*🛍️ طلب جديد من متجر بامبينو كيدز*
--------------------------------
*بيانات العميل:*
👤 *الاسم:* ${name}
📱 *الجوال:* ${phone}
📍 *المدينة:* ${city}
🏠 *العنوان:* ${address}
--------------------------------
*المنتجات المطلوبة:*
${itemsText}
--------------------------------
💰 *إجمالي الطلب:* ${total} ${settings.currency}
🚚 *الشحن:* مجاني
📝 *الملاحظات:* ${notes}
--------------------------------
شكراً لكم، في انتظار تأكيد الطلب وسرعة الشحن! ✨`;

    const waUrl = `https://wa.me/${settings.whatsapp}?text=${msg}`;
    window.open(waUrl, '_blank');

    this.clearCart();
    this.closeCheckoutModal();
    this.showToast('🎉 تم إرسال طلبك عبر واتساب بنجاح! سنتواصل معك للتأكيد');
  },

  directWhatsAppProduct(productId, size, qty = 1) {
    const product = this.getProductById(productId);
    if (!product) return;
    const settings = this.getSettings();

    const msg = 
`*🌸 استفسار وطلب فوري من بامبينو كيدز*
--------------------------------
أود شراء المنتج التالي:
👗 *اسم المنتج:* ${product.name}
📏 *المقاس المطلوب:* ${size}
🔢 *الكمية:* ${qty}
💰 *السعر:* ${product.price * qty} ${settings.currency}
--------------------------------
يرجى تأكيد التوفر وترتيب الشحن إلى عنواني.`;

    const waUrl = `https://wa.me/${settings.whatsapp}?text=${encodeURIComponent(msg)}`;
    window.open(waUrl, '_blank');
  },

  // Toast Notification
  showToast(message) {
    let container = document.querySelector('.toast-container');
    if (!container) {
      container = document.createElement('div');
      container.className = 'toast-container';
      document.body.appendChild(container);
    }

    const toast = document.createElement('div');
    toast.className = 'toast';
    toast.innerHTML = `<span>${message}</span>`;
    container.appendChild(toast);

    setTimeout(() => toast.classList.add('show'), 50);

    setTimeout(() => {
      toast.classList.remove('show');
      setTimeout(() => toast.remove(), 400);
    }, 3500);
  },

  // Global UI Events
  bindGlobalEvents() {
    // Mobile Drawer
    const mobileToggle = document.querySelector('.mobile-toggle');
    const mobileOverlay = document.getElementById('mobileNavOverlay');
    const mobileClose = document.getElementById('closeMobileNav');

    if (mobileToggle && mobileOverlay) {
      mobileToggle.addEventListener('click', () => {
        mobileOverlay.classList.add('active');
      });
    }
    if (mobileClose && mobileOverlay) {
      mobileClose.addEventListener('click', () => {
        mobileOverlay.classList.remove('active');
      });
    }

    // Cart Drawer Toggle
    const cartBtn = document.getElementById('btnOpenCart');
    const closeCartBtn = document.getElementById('btnCloseCart');
    const cartOverlay = document.getElementById('cartOverlay');

    if (cartBtn) cartBtn.addEventListener('click', () => this.openCart());
    if (closeCartBtn) closeCartBtn.addEventListener('click', () => this.closeCart());
    if (cartOverlay) {
      cartOverlay.addEventListener('click', (e) => {
        if (e.target === cartOverlay) this.closeCart();
      });
    }

    // Checkout Modal
    const btnProceedCheckout = document.getElementById('btnProceedCheckout');
    const btnProceedCheckoutWa = document.getElementById('btnProceedCheckoutWa');
    const btnCloseCheckout = document.getElementById('btnCloseCheckout');
    const checkoutOverlay = document.getElementById('checkoutModalOverlay');

    if (btnProceedCheckout) btnProceedCheckout.addEventListener('click', () => this.openCheckoutModal());
    if (btnProceedCheckoutWa) btnProceedCheckoutWa.addEventListener('click', () => this.openCheckoutModal());
    if (btnCloseCheckout) btnCloseCheckout.addEventListener('click', () => this.closeCheckoutModal());
    if (checkoutOverlay) {
      checkoutOverlay.addEventListener('click', (e) => {
        if (e.target === checkoutOverlay) this.closeCheckoutModal();
      });
    }

    // Checkout Form Submit
    const checkoutForm = document.getElementById('checkoutOrderForm');
    if (checkoutForm) {
      checkoutForm.addEventListener('submit', (e) => this.submitOrderToWhatsApp(e));
    }

    // Search Box Submit
    document.querySelectorAll('.global-search-form').forEach(form => {
      form.addEventListener('submit', (e) => {
        e.preventDefault();
        const input = form.querySelector('input[name="search"]');
        if (input && input.value.trim()) {
          window.location.href = `shop.html?search=${encodeURIComponent(input.value.trim())}`;
        }
      });
    });

    // Countdown Timer (if present on page)
    this.initCountdown();
  },

  initCountdown() {
    const hoursEl = document.getElementById('timerHours');
    const minsEl = document.getElementById('timerMinutes');
    const secsEl = document.getElementById('timerSeconds');

    if (!hoursEl || !minsEl || !secsEl) return;

    let totalSeconds = 14 * 3600 + 45 * 60 + 20;

    setInterval(() => {
      if (totalSeconds <= 0) {
        totalSeconds = 24 * 3600;
      }
      totalSeconds--;

      const h = Math.floor(totalSeconds / 3600);
      const m = Math.floor((totalSeconds % 3600) / 60);
      const s = totalSeconds % 60;

      hoursEl.textContent = String(h).padStart(2, '0');
      minsEl.textContent = String(m).padStart(2, '0');
      secsEl.textContent = String(s).padStart(2, '0');
    }, 1000);
  },

  // Helper: Render Single Product Card HTML
  renderProductCardHTML(product) {
    const settings = this.getSettings();
    const discount = Math.round(((product.oldPrice - product.price) / product.oldPrice) * 100);
    const sizeTags = (product.sizes || []).map(s => `<span class="size-tag">${s}</span>`).join('');
    const stars = '★'.repeat(Math.floor(product.rating || 5)) + ((product.rating || 5) % 1 !== 0 ? '½' : '');

    return `
      <div class="product-card" data-id="${product.id}" data-category="${product.cat}">
        <div class="product-img-wrap">
          <a href="product.html?id=${product.id}">
            <img src="${product.img}" alt="${product.name}" loading="lazy">
          </a>
          ${product.badge ? `<span class="product-badge ${product.badgeClass || 'badge-featured'}">${product.badge}</span>` : ''}
          <div class="product-quick-actions">
            <button class="btn-action-round" onclick="BambinoStore.addToCart(${product.id}, '${(product.sizes && product.sizes[0]) || 'قياسي'}')" title="إضافة سريعة للسلة">
              <svg width="18" height="18" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 11V7a4 4 0 00-8 0v4M5 9h14l1 12H4L5 9z"></path></svg>
            </button>
            <a href="product.html?id=${product.id}" class="btn-action-round" title="تفاصيل المنتج">
              <svg width="18" height="18" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"></path><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"></path></svg>
            </a>
          </div>
        </div>

        <div class="product-info">
          <div class="product-cat">${product.catName || ''}</div>
          <h3 class="product-title"><a href="product.html?id=${product.id}">${product.name}</a></h3>
          <div class="product-rating">
            <span>${stars}</span>
            <span class="reviews-count">(${product.reviews || 20} تقييم)</span>
          </div>
          <div class="product-sizes-tags">
            ${sizeTags}
          </div>
          <div class="product-price-row">
            <span class="price-current">${product.price} ${settings.currency}</span>
            <span class="price-old">${product.oldPrice} ${settings.currency}</span>
            <span class="discount-badge">خصم ${discount}%</span>
          </div>
          <div class="product-card-btns">
            <button class="btn-add-cart" onclick="BambinoStore.addToCart(${product.id}, '${(product.sizes && product.sizes[0]) || 'قياسي'}')">
              <svg width="18" height="18" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 11V7a4 4 0 00-8 0v4M5 9h14l1 12H4L5 9z"></path></svg>
              <span>أضف للسلة</span>
            </button>
            <button class="btn-whatsapp-order" onclick="BambinoStore.directWhatsAppProduct(${product.id}, '${(product.sizes && product.sizes[0]) || 'قياسي'}')" title="طلب مباشر عبر واتساب">
              <svg width="20" height="20" fill="currentColor" viewBox="0 0 24 24"><path d="M12.031 6.172c-3.181 0-5.767 2.586-5.768 5.766-.001 1.298.38 2.27 1.019 3.287l-.711 2.598 2.668-.699c.97.53 1.77.818 2.792.818 3.182 0 5.768-2.587 5.768-5.768 0-3.181-2.586-5.764-5.768-5.764zm3.393 8.163c-.144.405-.837.774-1.17.824-.312.045-.634.07-1.782-.407-1.468-.609-2.42-2.094-2.493-2.193-.073-.098-.598-.795-.598-1.517 0-.721.378-1.077.513-1.223.135-.145.295-.181.393-.181.098 0 .197.001.283.006.09.005.21.034.322.302.118.283.407.994.442 1.066.035.073.059.158.012.253-.047.095-.071.154-.141.236-.07.082-.148.184-.211.247-.07.07-.143.146-.062.285.082.139.362.598.777.968.533.475.982.622 1.121.692.139.07.221.059.303-.035.082-.095.35-407.443-.547.093-.14.186-.116.312-.07.127.047.808.381.947.451.139.07.232.105.267.163.035.058.035.342-.109.747z"></path></svg>
            </button>
          </div>
        </div>
      </div>
    `;
  }
};

document.addEventListener('DOMContentLoaded', () => {
  BambinoStore.init();
});
