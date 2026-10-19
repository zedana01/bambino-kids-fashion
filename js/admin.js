/**
 * BAMBINO KIDS FASHION - Admin Dashboard Controller
 * Client-friendly, intuitive management for products, pages content, images, and settings
 */

const AdminApp = {
  activeTab: 'products',
  activePageKey: 'home',
  editingProductId: null,

  init() {
    this.checkAuth();
    this.bindEvents();
    this.loadStats();
    this.renderProductsTable();
    this.loadSettingsForm();
    this.loadPagesEditor();
  },

  checkAuth() {
    const isAuth = sessionStorage.getItem('bambino_admin_auth');
    const authBox = document.getElementById('adminAuthBox');
    const appBox = document.getElementById('adminAppBox');

    if (!isAuth) {
      if (authBox) authBox.style.display = 'flex';
      if (appBox) appBox.style.display = 'none';
    } else {
      if (authBox) authBox.style.display = 'none';
      if (appBox) appBox.style.display = 'block';
    }
  },

  login(pin) {
    const savedPin = localStorage.getItem('bambino_admin_pin') || '1234';
    if (pin === savedPin) {
      sessionStorage.setItem('bambino_admin_auth', 'true');
      this.checkAuth();
      this.loadStats();
      this.renderProductsTable();
      this.loadSettingsForm();
      this.loadPagesEditor();
    } else {
      alert('رمز الدخول غير صحيح! الرمز الافتراضي هو 1234');
    }
  },

  logout() {
    sessionStorage.removeItem('bambino_admin_auth');
    this.checkAuth();
  },

  bindEvents() {
    // Login form
    const loginForm = document.getElementById('adminLoginForm');
    if (loginForm) {
      loginForm.addEventListener('submit', (e) => {
        e.preventDefault();
        const pin = document.getElementById('adminPinInput')?.value.trim();
        this.login(pin);
      });
    }

    // Sidebar navigation
    document.querySelectorAll('.admin-nav-item').forEach(item => {
      item.addEventListener('click', () => {
        const targetTab = item.getAttribute('data-tab');
        this.switchTab(targetTab);
      });
    });

    // Product form submit
    const productForm = document.getElementById('adminProductForm');
    if (productForm) {
      productForm.addEventListener('submit', (e) => {
        e.preventDefault();
        this.saveProductForm();
      });
    }

    // Settings form submit
    const settingsForm = document.getElementById('adminSettingsForm');
    if (settingsForm) {
      settingsForm.addEventListener('submit', (e) => {
        e.preventDefault();
        this.saveSettingsForm();
      });
    }
  },

  switchTab(tabId) {
    this.activeTab = tabId;
    document.querySelectorAll('.admin-nav-item').forEach(el => {
      el.classList.toggle('active', el.getAttribute('data-tab') === tabId);
    });
    document.querySelectorAll('.admin-tab-content').forEach(el => {
      el.classList.toggle('active', el.id === `tab-${tabId}`);
    });
    if (tabId === 'pages') {
      this.loadPagesEditor();
    }
  },

  loadStats() {
    const products = BambinoStore.getProducts();
    const categories = new Set(products.map(p => p.cat));
    const avgPrice = products.length ? Math.round(products.reduce((acc, p) => acc + p.price, 0) / products.length) : 0;
    const settings = BambinoStore.getSettings();

    const statCount = document.getElementById('statTotalProducts');
    const statCats = document.getElementById('statTotalCats');
    const statAvg = document.getElementById('statAvgPrice');

    if (statCount) statCount.textContent = products.length;
    if (statCats) statCats.textContent = categories.size;
    if (statAvg) statAvg.textContent = `${avgPrice} ${settings.currency}`;
  },

  renderProductsTable(filterText = '') {
    const tbody = document.getElementById('adminProductsTbody');
    if (!tbody) return;

    let products = BambinoStore.getProducts();
    const settings = BambinoStore.getSettings();

    if (filterText) {
      const term = filterText.toLowerCase();
      products = products.filter(p => p.name.toLowerCase().includes(term) || p.catName.toLowerCase().includes(term));
    }

    if (products.length === 0) {
      tbody.innerHTML = `<tr><td colspan="7" style="text-align: center; padding: 30px; color: #94a3b8;">لا توجد منتجات مطابقة</td></tr>`;
      return;
    }

    let html = '';
    products.forEach(p => {
      const imgSrc = p.img.startsWith('data:') || p.img.startsWith('http') ? p.img : `../${p.img}`;
      html += `
        <tr>
          <td>
            <img src="${imgSrc}" alt="${p.name}" class="table-img" onerror="this.src='../images/prod_girls_party.jpg'">
          </td>
          <td>
            <strong style="color: var(--dark); font-size: 0.95rem;">${p.name}</strong>
            <div style="font-size: 0.8rem; color: #64748b;">معرّف المنتج: #${p.id}</div>
          </td>
          <td><span class="size-tag">${p.catName}</span></td>
          <td>
            <span style="color: var(--primary); font-weight: 800;">${p.price} ${settings.currency}</span>
            ${p.oldPrice ? `<span style="text-decoration: line-through; color: #94a3b8; font-size: 0.85rem; margin-right: 6px;">${p.oldPrice}</span>` : ''}
          </td>
          <td>
            ${p.badge ? `<span class="product-badge ${p.badgeClass || 'badge-featured'}" style="position: static; font-size: 0.72rem;">${p.badge}</span>` : '-'}
          </td>
          <td>
            <div style="font-size: 0.8rem; color: #475569;">${(p.sizes || []).join('، ')}</div>
          </td>
          <td>
            <div style="display: flex; gap: 8px;">
              <button class="btn-admin-pill btn-admin-outline" style="padding: 5px 12px; font-size: 0.8rem;" onclick="AdminApp.openEditModal(${p.id})">تعديل ✏️</button>
              <button class="btn-admin-pill btn-admin-danger" style="padding: 5px 12px; font-size: 0.8rem;" onclick="AdminApp.deleteProduct(${p.id})">حذف 🗑️</button>
            </div>
          </td>
        </tr>
      `;
    });

    tbody.innerHTML = html;
  },

  openAddModal() {
    this.editingProductId = null;
    document.getElementById('modalProductTitle').textContent = 'إضافة منتج جديد للمتجر';
    document.getElementById('adminProductForm').reset();
    document.getElementById('productImagePreview').src = '../images/prod_girls_party.jpg';
    document.getElementById('adminProductModalOverlay').classList.add('active');
  },

  openEditModal(id) {
    const product = BambinoStore.getProductById(id);
    if (!product) return;

    this.editingProductId = id;
    document.getElementById('modalProductTitle').textContent = `تعديل منتج: ${product.name}`;

    document.getElementById('prodNameInput').value = product.name;
    document.getElementById('prodCatInput').value = product.cat;
    document.getElementById('prodPriceInput').value = product.price;
    document.getElementById('prodOldPriceInput').value = product.oldPrice || '';
    document.getElementById('prodImgInput').value = product.img;
    document.getElementById('prodBadgeInput').value = product.badge || '';
    document.getElementById('prodSizesInput').value = (product.sizes || []).join(', ');
    document.getElementById('prodDescInput').value = product.desc || '';

    const preview = document.getElementById('productImagePreview');
    if (preview) {
      preview.src = product.img.startsWith('http') || product.img.startsWith('data:') ? product.img : `../${product.img}`;
    }

    document.getElementById('adminProductModalOverlay').classList.add('active');
  },

  closeModal() {
    document.getElementById('adminProductModalOverlay').classList.remove('active');
  },

  saveProductForm() {
    const name = document.getElementById('prodNameInput').value.trim();
    const cat = document.getElementById('prodCatInput').value;
    const price = parseFloat(document.getElementById('prodPriceInput').value);
    const oldPrice = parseFloat(document.getElementById('prodOldPriceInput').value) || (price + 50);
    let img = document.getElementById('prodImgInput').value.trim() || 'images/prod_girls_party.jpg';
    const badge = document.getElementById('prodBadgeInput').value.trim();
    const sizesStr = document.getElementById('prodSizesInput').value.trim();
    const desc = document.getElementById('prodDescInput').value.trim();

    if (!name || isNaN(price)) {
      alert('يرجى كتابة اسم المنتج وسعره بشكل صحيح');
      return;
    }

    const sizes = sizesStr ? sizesStr.split(',').map(s => s.trim()).filter(Boolean) : ['1-2y', '3-5y'];

    const catNamesMap = {
      girls: 'ملابس بناتي',
      boys: 'ملابس أولادي',
      baby: 'بيبي ومواليد',
      shoes: 'أحذية وإكسسوارات'
    };

    let products = BambinoStore.getProducts();

    if (this.editingProductId) {
      const idx = products.findIndex(p => p.id === this.editingProductId);
      if (idx > -1) {
        products[idx] = {
          ...products[idx],
          name,
          cat,
          catName: catNamesMap[cat] || 'تشكيلة الأطفال',
          price,
          oldPrice,
          img,
          badge,
          sizes,
          desc
        };
      }
    } else {
      const nextId = products.length > 0 ? Math.max(...products.map(p => p.id)) + 1 : 1;
      products.push({
        id: nextId,
        name,
        cat,
        catName: catNamesMap[cat] || 'تشكيلة الأطفال',
        price,
        oldPrice,
        rating: 5.0,
        reviews: 1,
        sales: 0,
        isBestSeller: false,
        isFeatured: true,
        isNew: true,
        badge: badge || 'جديد ✨',
        badgeClass: 'badge-new',
        sizes,
        img,
        desc: desc || 'منتج عالي الجودة مصنوع من أقمشة ناعمة ومريحة لبشرة أطفالك.'
      });
    }

    BambinoStore.saveProducts(products);
    this.closeModal();
    this.loadStats();
    this.renderProductsTable();
    alert('✅ تم حفظ المنتج بنجاح وتحديثه في المتجر فوراً!');
  },

  deleteProduct(id) {
    if (!confirm('هل أنت متأكد من رغبتك في حذف هذا المنتج من المتجر؟')) return;

    let products = BambinoStore.getProducts();
    products = products.filter(p => p.id !== id);
    BambinoStore.saveProducts(products);
    this.loadStats();
    this.renderProductsTable();
    alert('🗑️ تم حذف المنتج من المتجر');
  },

  loadSettingsForm() {
    const s = BambinoStore.getSettings();
    document.getElementById('settStoreName').value = s.storeName || '';
    document.getElementById('settAnnouncement').value = s.announcement || '';
    document.getElementById('settWhatsapp').value = s.whatsapp || '';
    document.getElementById('settPhone').value = s.phone || '';
    document.getElementById('settEmail').value = s.email || '';
    document.getElementById('settAddress').value = s.address || '';
    document.getElementById('settCurrency').value = s.currency || 'ر.س';
  },

  saveSettingsForm() {
    const s = {
      storeName: document.getElementById('settStoreName').value.trim(),
      announcement: document.getElementById('settAnnouncement').value.trim(),
      whatsapp: document.getElementById('settWhatsapp').value.trim(),
      phone: document.getElementById('settPhone').value.trim(),
      email: document.getElementById('settEmail').value.trim(),
      address: document.getElementById('settAddress').value.trim(),
      currency: document.getElementById('settCurrency').value.trim() || 'ر.س',
      freeShippingLimit: 250
    };

    BambinoStore.saveSettings(s);
    this.loadStats();
    this.renderProductsTable();
    alert('✅ تم حفظ جميع إعدادات المتجر وتطبيقها بنجاح!');
  },

  // ==========================================
  // PAGES CONTENT & MEDIA CMS EDITOR
  // ==========================================
  loadPagesEditor() {
    this.selectPage(this.activePageKey || 'home');
  },

  selectPage(pageKey) {
    this.activePageKey = pageKey;
    document.querySelectorAll('.cms-page-card').forEach(card => {
      card.classList.toggle('active', card.getAttribute('data-page') === pageKey);
    });

    document.querySelectorAll('.cms-page-form-wrapper').forEach(form => {
      form.style.display = form.id === `cmsForm-${pageKey}` ? 'block' : 'none';
    });

    // Populate current values
    const data = BambinoStore.getPagesContent();
    if (!data || !data[pageKey]) return;

    const pageData = data[pageKey];
    for (const [key, val] of Object.entries(pageData)) {
      const input = document.getElementById(`cms_${pageKey}_${key}`);
      if (input) {
        input.value = val;
      }
      const preview = document.getElementById(`prev_${pageKey}_${key}`);
      if (preview && val) {
        preview.src = val.startsWith('http') || val.startsWith('data:') ? val : `../${val}`;
      }
    }
  },

  saveCurrentPage(pageKey) {
    let content = BambinoStore.getPagesContent();
    if (!content[pageKey]) content[pageKey] = {};

    const form = document.getElementById(`cmsForm-${pageKey}`);
    if (!form) return;

    form.querySelectorAll('[data-cms-field]').forEach(input => {
      const field = input.getAttribute('data-cms-field');
      content[pageKey][field] = input.value.trim();
    });

    BambinoStore.savePagesContent(content);
    alert(`✅ تم حفظ محتوى وصور صفحة (${this.getPageNameAr(pageKey)}) وتحديثها بنجاح في المتجر!`);
  },

  resetCurrentPage(pageKey) {
    if (!confirm(`هل أنت متأكد من استعادة النصوص والصور الأصلية لصفحة (${this.getPageNameAr(pageKey)})؟`)) return;
    BambinoStore.resetPageContent(pageKey);
    this.selectPage(pageKey);
    alert(`🔄 تم استرجاع النصوص والصور الأصلية لصفحة (${this.getPageNameAr(pageKey)}) بنجاح!`);
  },

  getPageNameAr(key) {
    const map = {
      home: 'الصفحة الرئيسية',
      about: 'من نحن',
      contact: 'اتصل بنا',
      privacy: 'سياسة الخصوصية',
      terms: 'الشروط والأحكام',
      footer: 'الفوتر العام'
    };
    return map[key] || key;
  },

  previewPage(key) {
    const map = {
      home: '../index.html',
      about: '../about.html',
      contact: '../contact.html',
      privacy: '../privacy.html',
      terms: '../terms.html',
      footer: '../index.html'
    };
    window.open(map[key] || '../index.html', '_blank');
  },

  // File Upload Helper (converts image file to Base64)
  handleImageUpload(event, targetInputId, previewId) {
    const file = event.target.files[0];
    if (!file) return;

    const reader = new FileReader();
    reader.onload = (e) => {
      const base64 = e.target.result;
      const targetInput = document.getElementById(targetInputId);
      if (targetInput) targetInput.value = base64;

      const preview = document.getElementById(previewId);
      if (preview) preview.src = base64;
    };
    reader.readAsDataURL(file);
  },

  updateImagePreview(urlVal, previewId) {
    const preview = document.getElementById(previewId);
    if (!preview) return;
    preview.src = urlVal.startsWith('http') || urlVal.startsWith('data:') ? urlVal : `../${urlVal}`;
  },

  // ==========================================
  // BACKUP & RESTORE (PRODUCTS + PAGES + SETTINGS)
  // ==========================================
  exportFullBackupJSON() {
    const fullBackup = {
      products: BambinoStore.getProducts(),
      settings: BambinoStore.getSettings(),
      pagesContent: BambinoStore.getPagesContent(),
      exportDate: new Date().toISOString()
    };

    const dataStr = "data:text/json;charset=utf-8," + encodeURIComponent(JSON.stringify(fullBackup, null, 2));
    const downloadAnchor = document.createElement('a');
    downloadAnchor.setAttribute("href", dataStr);
    downloadAnchor.setAttribute("download", `bambino_full_backup_${new Date().toISOString().slice(0,10)}.json`);
    document.body.appendChild(downloadAnchor);
    downloadAnchor.click();
    downloadAnchor.remove();
  },

  importFullBackupJSON(event) {
    const file = event.target.files[0];
    if (!file) return;

    const reader = new FileReader();
    reader.onload = (e) => {
      try {
        const imported = JSON.parse(e.target.result);
        if (imported.products && Array.isArray(imported.products)) {
          BambinoStore.saveProducts(imported.products);
          if (imported.settings) BambinoStore.saveSettings(imported.settings);
          if (imported.pagesContent) BambinoStore.savePagesContent(imported.pagesContent);
          this.loadStats();
          this.renderProductsTable();
          this.loadSettingsForm();
          this.loadPagesEditor();
          alert(`✅ تم استيراد النسخة الاحتياطية بنجاح! (المنتجات: ${imported.products.length} منتج، إعدادات المتجر ومحتوى الصفحات)`);
        } else if (Array.isArray(imported)) {
          BambinoStore.saveProducts(imported);
          this.loadStats();
          this.renderProductsTable();
          alert(`✅ تم استيراد ${imported.length} منتج بنجاح!`);
        } else {
          alert('الملف المرفوع لا يحتوي على صيغة نسخ احتياطي صالحة');
        }
      } catch (err) {
        alert('حدث خطأ أثناء قراءة ملف JSON');
      }
    };
    reader.readAsText(file);
  },

  resetDefaultProducts() {
    if (!confirm('تحذير: سيتم حذف جميع التعديلات والمنتجات المضافة واسترجاع المنتجات الاصلية، هل توافق؟')) return;
    localStorage.removeItem('bambino_products');
    localStorage.removeItem('bambino_pages_content');
    localStorage.removeItem('bambino_settings');
    BambinoStore.initStorage();
    this.loadStats();
    this.renderProductsTable();
    this.loadSettingsForm();
    this.loadPagesEditor();
    alert('🔄 تم استرجاع كافة الإعدادات والمنتجات الأصلية للمتجر بنجاح!');
  }
};

document.addEventListener('DOMContentLoaded', () => {
  AdminApp.init();
});
