# -*- coding: utf-8 -*-
import os
import json
from build_html_helpers import get_header, get_footer

BASE_DIR = 'E:/Sites/bambino-kids-fashion'

# ==========================================
# 1. INDEX.HTML
# ==========================================
def build_index():
    header = get_header(active_nav='home')
    footer = get_footer()
    
    html = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>بامبينو كيدز | BAMBINO - متجر أرقى أزياء ومستلزمات الأطفال</title>
  <meta name="description" content="تسوقي أفخم ملابس وأزياء الأطفال، فساتين بناتي فاخرة، بدل وأطقم أولادي، ملابس بيبي ومواليد بأجود الخامات القطنية وتوصيل سريع لكافة مدن المملكة.">
  <link rel="stylesheet" href="css/style.css">
  <link rel="icon" href="images/kids_cat_girls.jpg">
</head>
<body>
__HEADER__

  <!-- HERO SLIDER SECTION -->
  <section class="hero-section">
    <div class="container">
      <div class="hero-slider-wrap">
        <!-- Slide 1 -->
        <div class="hero-slide active" style="background: linear-gradient(90deg, rgba(255,241,242,0.95) 0%, rgba(255,255,255,0.7) 100%);">
          <img src="images/kids_hero_banner.jpg" alt="تشكيلة بامبينو كيدز الحصرية" style="position: absolute; left: 0; top: 0; width: 55%; height: 100%; object-fit: cover; z-index: 1;">
          <div class="hero-content" style="position: relative; z-index: 2; max-width: 540px; padding: 40px;">
            <span class="hero-tag" style="background: var(--primary); color: #fff; padding: 5px 14px; border-radius: var(--radius-full); font-size: 0.85rem; font-weight: 800; display: inline-block; margin-bottom: 12px;">🌟 تشكيلة الموسم الجديد 2026</span>
            <h1 class="hero-title" style="font-size: 2.7rem; font-weight: 900; line-height: 1.25; color: var(--dark); margin-bottom: 16px;">
              أناقة استثنائية <br><span style="color: var(--primary);">تليق بابتسامة طفلك</span>
            </h1>
            <p class="hero-desc" style="font-size: 1.05rem; color: var(--text); margin-bottom: 26px;">
              اكتشفي تشكيلة الأزياء الفاخرة المصنوعة من القطن العضوي 100% بنعومة فائقة تناسب بشرة أطفالك الرقيقة، من عمر الولادة وحتى 14 سنة.
            </p>
            <div style="display: flex; gap: 14px; flex-wrap: wrap;">
              <a href="shop.html" class="btn-checkout" style="width: auto; padding: 13px 30px;">تسوقي التشكيلة الآن ✨</a>
              <a href="shop.html?cat=girls" class="btn-add-cart" style="padding: 13px 24px; font-weight: 800;">فساتين بناتي 👗</a>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- FEATURES / VALUE PROPOSITION BAR -->
  <section class="features-bar" style="background: var(--white); padding: 30px 0; border-bottom: 1px solid var(--border-light);">
    <div class="container">
      <div class="features-grid" style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 20px;">
        <div class="feature-item">
          <div class="feature-icon">🚚</div>
          <div class="feature-text">
            <h4>شحن سريع ومجاني</h4>
            <p>لكافة مدن المملكة للطلبات فوق 250 ر.س</p>
          </div>
        </div>
        <div class="feature-item">
          <div class="feature-icon">🌱</div>
          <div class="feature-text">
            <h4>قطن طبيعي 100%</h4>
            <p>أقمشة ناعمة وآمنة لبشرة طفلك الحساسة</p>
          </div>
        </div>
        <div class="feature-item">
          <div class="feature-icon">💬</div>
          <div class="feature-text">
            <h4>طلب سهل عبر واتساب</h4>
            <p>إتمام فوري للطلب مع خدمة عملاء متفانية</p>
          </div>
        </div>
        <div class="feature-item">
          <div class="feature-icon">🔄</div>
          <div class="feature-text">
            <h4>استبدال ميسر وسريع</h4>
            <p>سياسة مرنة للاستبدال واسترجاع المقاسات</p>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- CATEGORIES GRID SECTION -->
  <section class="section-padding">
    <div class="container">
      <div class="section-header">
        <span class="section-tag">أقسام المتجر</span>
        <h2 class="section-title">تسوق حسب الفئة</h2>
        <p class="section-desc">اختاري ما يناسب طفلك من أرقى التشكيلات المصممة خصيصاً لأناقة يومية ومناسبات مميزة</p>
      </div>

      <div class="categories-grid">
        <!-- Girls -->
        <a href="shop.html?cat=girls" class="category-card">
          <img src="images/kids_cat_girls.jpg" alt="ملابس بناتي">
          <div class="category-card-overlay">
            <h3 class="category-card-title">ملابس بناتي</h3>
            <span class="category-card-link">استكشف التشكيلة ←</span>
          </div>
        </a>

        <!-- Boys -->
        <a href="shop.html?cat=boys" class="category-card">
          <img src="images/kids_cat_boys.jpg" alt="ملابس أولادي">
          <div class="category-card-overlay">
            <h3 class="category-card-title">ملابس أولادي</h3>
            <span class="category-card-link">استكشف التشكيلة ←</span>
          </div>
        </a>

        <!-- Baby -->
        <a href="shop.html?cat=baby" class="category-card">
          <img src="images/kids_cat_baby.jpg" alt="بيبي ومواليد">
          <div class="category-card-overlay">
            <h3 class="category-card-title">بيبي ومواليد</h3>
            <span class="category-card-link">استكشف التشكيلة ←</span>
          </div>
        </a>

        <!-- Shoes & Accessories -->
        <a href="shop.html?cat=shoes" class="category-card">
          <img src="images/kids_cat_shoes.jpg" alt="أحذية وإكسسوارات">
          <div class="category-card-overlay">
            <h3 class="category-card-title">أحذية وإكسسوارات</h3>
            <span class="category-card-link">استكشف التشكيلة ←</span>
          </div>
        </a>
      </div>
    </div>
  </section>

  <!-- FLASH DEALS BANNER -->
  <section class="container">
    <div class="flash-banner">
      <div class="flash-content">
        <span class="flash-tag">⚡ عروض حصرية لفترة محدودة</span>
        <h2 class="flash-title">خصومات حتى 40% على تشكيلة الصيف</h2>
        <p class="flash-desc">اغتنمي الفرصة ووفري الكثير على أجمل الفساتين والأطقم الفاخرة لأطفالك. ينتهي العرض قريباً!</p>
        
        <div class="countdown-box">
          <div class="countdown-unit">
            <div class="countdown-num" id="timerHours">14</div>
            <div class="countdown-label">ساعة</div>
          </div>
          <div class="countdown-unit">
            <div class="countdown-num" id="timerMinutes">45</div>
            <div class="countdown-label">دقيقة</div>
          </div>
          <div class="countdown-unit">
            <div class="countdown-num" id="timerSeconds">20</div>
            <div class="countdown-label">ثانية</div>
          </div>
        </div>

        <a href="shop.html" class="btn-checkout" style="width: fit-content; background: #fff; color: var(--primary);">تسوق العروض الحصرية الآن 🛍️</a>
      </div>
      <div style="z-index: 2; max-width: 380px;" class="hide-mobile">
        <img src="images/flash_deal_kids_banner.jpg" alt="عروض بامبينو كيدز" style="border-radius: var(--radius-md); box-shadow: var(--shadow-md);">
      </div>
    </div>
  </section>

  <!-- FEATURED PRODUCTS GRID -->
  <section class="section-padding" style="background: var(--bg-soft);">
    <div class="container">
      <div class="section-header">
        <span class="section-tag">أحدث القطع</span>
        <h2 class="section-title">المختارات الأكثر طلباً</h2>
        <p class="section-desc">قطع مختارة بعناية تجمع بين الأناقة الراقية والراحة الفائقة لطفلك</p>
      </div>

      <!-- Filter Tabs -->
      <div class="filter-tabs">
        <button class="tab-btn active" onclick="filterHomeProducts('all', this)">جميع القطع</button>
        <button class="tab-btn" onclick="filterHomeProducts('girls', this)">ملابس بناتي 👗</button>
        <button class="tab-btn" onclick="filterHomeProducts('boys', this)">ملابس أولادي 👕</button>
        <button class="tab-btn" onclick="filterHomeProducts('baby', this)">بيبي ومواليد 🍼</button>
        <button class="tab-btn" onclick="filterHomeProducts('shoes', this)">أحذية وإكسسوارات 👟</button>
      </div>

      <!-- Grid Container -->
      <div class="products-grid" id="homeProductsGrid">
        <!-- Rendered dynamically by store.js -->
      </div>

      <div style="text-align: center; margin-top: 40px;">
        <a href="shop.html" class="btn-checkout" style="display: inline-flex; width: auto; padding: 14px 40px; margin: 0 auto;">
          <span>عرض جميع المنتجات في المتجر</span>
          <span>←</span>
        </a>
      </div>
    </div>
  </section>

  <!-- VIP NEWSLETTER SECTION -->
  <section class="container">
    <div class="vip-club-section">
      <span style="color: var(--secondary); font-weight: 800; font-size: 0.9rem; letter-spacing: 1px;">نادي أمهات بامبينو 👑</span>
      <h2 class="vip-title">انضمي لنادي الأمهات واحصلي على خصم 15%</h2>
      <p class="vip-desc">سجلي بريدك الإلكتروني ليصلك كل جديد في عالم أزياء الأطفال، ودعوات حصرية لخصومات المواسم قبل الجميع.</p>
      <form class="newsletter-form" onsubmit="event.preventDefault(); BambinoStore.showToast('🎉 شكراً لانضمامك لنادي أمهات بامبينو! كود خصمك: VIP15'); this.reset();">
        <input type="email" placeholder="أدخلي بريدك الإلكتروني..." required>
        <button type="submit" class="btn-checkout" style="width: auto; padding: 12px 28px;">انضمام 💌</button>
      </form>
    </div>
  </section>

__FOOTER__

  <script src="js/store.js"></script>
  <script>
    function renderHomeProducts(category = 'all') {
      const container = document.getElementById('homeProductsGrid');
      if (!container) return;
      const products = BambinoStore.getProducts();
      
      const filtered = category === 'all' 
        ? products 
        : products.filter(p => p.cat === category);

      container.innerHTML = filtered.map(p => BambinoStore.renderProductCardHTML(p)).join('');
    }

    function filterHomeProducts(cat, btn) {
      document.querySelectorAll('.filter-tabs .tab-btn').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      renderHomeProducts(cat);
    }

    document.addEventListener('DOMContentLoaded', () => {
      renderHomeProducts('all');
    });
  </script>
</body>
</html>
"""
    with open(os.path.join(BASE_DIR, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(html.replace('__HEADER__', header).replace('__FOOTER__', footer))
    print("index.html written successfully!")


# ==========================================
# 2. SHOP.HTML (Catalog & Filters)
# ==========================================
def build_shop():
    header = get_header(active_nav='shop')
    footer = get_footer()

    html = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>المتجر والتشكيلات الكاملة | بامبينو كيدز</title>
  <meta name="description" content="تصفح جميع تشكيلات بامبينو كيدز، فساتين البنات، ملابس الأولاد، أطقم المواليد، والأحذية بأسعار مميزة وجودة لا تضاهى.">
  <link rel="stylesheet" href="css/style.css">
  <link rel="icon" href="images/kids_cat_girls.jpg">
</head>
<body>
__HEADER__

  <!-- PAGE HERO -->
  <div class="page-hero">
    <div class="container">
      <h1 class="page-hero-title">المتجر والتشكيلات الفاخرة</h1>
      <div class="breadcrumb">
        <a href="index.html">الرئيسية</a>
        <span>/</span>
        <span style="color: var(--primary); font-weight: 700;">المتجر</span>
      </div>
    </div>
  </div>

  <!-- SHOP CONTENT LAYOUT -->
  <div class="container">
    <div class="shop-layout">
      <!-- SIDEBAR FILTERS -->
      <aside class="shop-sidebar">
        <!-- Categories Widget -->
        <div class="filter-widget">
          <h3 class="filter-widget-title">أقسام المتجر</h3>
          <ul class="category-filter-list">
            <li class="category-filter-item active" onclick="setCategoryFilter('all', this)">
              <span>جميع الأقسام</span>
              <span class="filter-count" id="countAll">0</span>
            </li>
            <li class="category-filter-item" onclick="setCategoryFilter('girls', this)">
              <span>ملابس بناتي 👗</span>
              <span class="filter-count" id="countGirls">0</span>
            </li>
            <li class="category-filter-item" onclick="setCategoryFilter('boys', this)">
              <span>ملابس أولادي 👕</span>
              <span class="filter-count" id="countBoys">0</span>
            </li>
            <li class="category-filter-item" onclick="setCategoryFilter('baby', this)">
              <span>بيبي ومواليد 🍼</span>
              <span class="filter-count" id="countBaby">0</span>
            </li>
            <li class="category-filter-item" onclick="setCategoryFilter('shoes', this)">
              <span>أحذية وإكسسوارات 👟</span>
              <span class="filter-count" id="countShoes">0</span>
            </li>
          </ul>
        </div>

        <!-- Search Box inside sidebar -->
        <div class="filter-widget">
          <h3 class="filter-widget-title">بحث بالاسم</h3>
          <div class="search-box" style="max-width: 100%;">
            <input type="text" id="shopSearchInput" placeholder="اكتب اسم القطعة..." oninput="handleShopSearch(this.value)">
            <span class="search-icon">🔍</span>
          </div>
        </div>

        <!-- Price Range Filter -->
        <div class="filter-widget">
          <h3 class="filter-widget-title">نطاق السعر</h3>
          <div style="display: flex; gap: 8px; flex-direction: column;">
            <button class="btn-admin-pill btn-admin-outline" onclick="setPriceFilter(0, 9999, this)" style="justify-content: flex-start;">جميع الأسعار</button>
            <button class="btn-admin-pill btn-admin-outline" onclick="setPriceFilter(0, 150, this)" style="justify-content: flex-start;">أقل من 150 ر.س</button>
            <button class="btn-admin-pill btn-admin-outline" onclick="setPriceFilter(150, 250, this)" style="justify-content: flex-start;">من 150 إلى 250 ر.س</button>
            <button class="btn-admin-pill btn-admin-outline" onclick="setPriceFilter(250, 9999, this)" style="justify-content: flex-start;">أكثر من 250 ر.س</button>
          </div>
        </div>

        <!-- WhatsApp Assistance Banner -->
        <div style="background: var(--bg-soft); padding: 18px; border-radius: var(--radius-sm); border: 1px dashed var(--border); text-align: center;">
          <div style="font-size: 1.5rem; margin-bottom: 6px;">💬</div>
          <h4 style="font-size: 0.95rem; font-weight: 800; margin-bottom: 4px;">تحتاجين مساعدة في اختيار المقاس؟</h4>
          <p style="font-size: 0.8rem; color: var(--text-light); margin-bottom: 12px;">فريق خدمة العملاء جاهز لمساعدتك فوراً عبر واتساب</p>
          <a href="https://wa.me/966500000000" target="_blank" class="btn-add-cart store-whatsapp-link" style="padding: 6px 14px; font-size: 0.82rem;">محادثة واتساب</a>
        </div>
      </aside>

      <!-- PRODUCTS MAIN VIEW -->
      <main class="shop-main">
        <!-- Top bar: Count & Sort -->
        <div class="sort-search-bar">
          <div>
            <span id="shopProductCount" style="font-weight: 800; color: var(--dark); font-size: 1.05rem;">عرض المنتجات</span>
          </div>
          <div class="sort-box" style="display: flex; align-items: center; gap: 10px;">
            <label for="shopSortSelect" style="font-weight: 700; font-size: 0.88rem; color: var(--text-light);">ترتيب حسب:</label>
            <select id="shopSortSelect" onchange="handleSortChange(this.value)">
              <option value="default">الافتراضي (المقترح)</option>
              <option value="price-low">السعر: من الأقل للأعلى</option>
              <option value="price-high">السعر: من الأعلى للأقل</option>
              <option value="bestseller">الأكثر مبيعاً</option>
              <option value="rating">الأعلى تقييماً</option>
            </select>
          </div>
        </div>

        <!-- Products Grid -->
        <div class="products-grid" id="shopProductsGrid">
          <!-- Rendered dynamically -->
        </div>
      </main>
    </div>
  </div>

__FOOTER__

  <script src="js/store.js"></script>
  <script>
    let currentCategory = 'all';
    let currentSearchTerm = '';
    let currentMinPrice = 0;
    let currentMaxPrice = 9999;
    let currentSort = 'default';

    function initShop() {
      // Check URL parameters (e.g. ?cat=girls or ?search=dress)
      const params = new URLSearchParams(window.location.search);
      const catParam = params.get('cat');
      const searchParam = params.get('search');

      if (catParam) {
        currentCategory = catParam;
        document.querySelectorAll('.category-filter-item').forEach(el => {
          el.classList.toggle('active', el.textContent.includes(getCatNameAr(catParam)));
        });
      }

      if (searchParam) {
        currentSearchTerm = searchParam;
        const searchInput = document.getElementById('shopSearchInput');
        if (searchInput) searchInput.value = searchParam;
      }

      updateCategoryCounters();
      renderShopProducts();
    }

    function getCatNameAr(cat) {
      switch(cat) {
        case 'girls': return 'بناتي';
        case 'boys': return 'أولادي';
        case 'baby': return 'بيبي';
        case 'shoes': return 'أحذية';
        default: return 'جميع';
      }
    }

    function updateCategoryCounters() {
      const products = BambinoStore.getProducts();
      document.getElementById('countAll').textContent = products.length;
      document.getElementById('countGirls').textContent = products.filter(p => p.cat === 'girls').length;
      document.getElementById('countBoys').textContent = products.filter(p => p.cat === 'boys').length;
      document.getElementById('countBaby').textContent = products.filter(p => p.cat === 'baby').length;
      document.getElementById('countShoes').textContent = products.filter(p => p.cat === 'shoes').length;
    }

    function setCategoryFilter(cat, elem) {
      currentCategory = cat;
      document.querySelectorAll('.category-filter-item').forEach(el => el.classList.remove('active'));
      if (elem) elem.classList.add('active');
      renderShopProducts();
    }

    function setPriceFilter(min, max, elem) {
      currentMinPrice = min;
      currentMaxPrice = max;
      renderShopProducts();
    }

    function handleShopSearch(term) {
      currentSearchTerm = term.trim().toLowerCase();
      renderShopProducts();
    }

    function handleSortChange(sortVal) {
      currentSort = sortVal;
      renderShopProducts();
    }

    function renderShopProducts() {
      const container = document.getElementById('shopProductsGrid');
      const countEl = document.getElementById('shopProductCount');
      if (!container) return;

      let products = BambinoStore.getProducts();

      // Category filter
      if (currentCategory !== 'all') {
        products = products.filter(p => p.cat === currentCategory);
      }

      // Search filter
      if (currentSearchTerm) {
        products = products.filter(p => 
          p.name.toLowerCase().includes(currentSearchTerm) ||
          (p.desc && p.desc.toLowerCase().includes(currentSearchTerm)) ||
          p.catName.toLowerCase().includes(currentSearchTerm)
        );
      }

      // Price filter
      products = products.filter(p => p.price >= currentMinPrice && p.price <= currentMaxPrice);

      // Sorting
      if (currentSort === 'price-low') {
        products.sort((a, b) => a.price - b.price);
      } else if (currentSort === 'price-high') {
        products.sort((a, b) => b.price - a.price);
      } else if (currentSort === 'bestseller') {
        products.sort((a, b) => (b.sales || 0) - (a.sales || 0));
      } else if (currentSort === 'rating') {
        products.sort((a, b) => (b.rating || 0) - (a.rating || 0));
      }

      countEl.textContent = `تم العثور على (${products.length}) منتج`;

      if (products.length === 0) {
        container.innerHTML = `
          <div style="grid-column: 1 / -1; text-align: center; padding: 60px 20px; background: #fff; border-radius: var(--radius-md); border: 1px dashed var(--border);">
            <div style="font-size: 3rem; margin-bottom: 12px;">🔍</div>
            <h3 style="font-size: 1.3rem; font-weight: 800; color: var(--dark); margin-bottom: 6px;">لا توجد منتجات مطابقة لخيارات البحث</h3>
            <p style="color: var(--text-light); margin-bottom: 18px;">جربي إزالة بعض الفلاتر أو البحث بكلمات أخرى</p>
            <button onclick="setCategoryFilter('all'); document.getElementById('shopSearchInput').value=''; currentSearchTerm='';" class="btn-checkout" style="width: auto; margin: 0 auto; padding: 10px 24px;">عرض جميع المنتجات</button>
          </div>
        `;
        return;
      }

      container.innerHTML = products.map(p => BambinoStore.renderProductCardHTML(p)).join('');
    }

    document.addEventListener('DOMContentLoaded', () => {
      initShop();
    });
  </script>
</body>
</html>
"""
    with open(os.path.join(BASE_DIR, 'shop.html'), 'w', encoding='utf-8') as f:
        f.write(html.replace('__HEADER__', header).replace('__FOOTER__', footer))
    print("shop.html written successfully!")


# ==========================================
# 3. PRODUCT.HTML (Single Product Details)
# ==========================================
def build_product():
    header = get_header(active_nav='shop')
    footer = get_footer()

    html = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>تفاصيل المنتج | بامبينو كيدز</title>
  <meta name="description" content="تعرفي على تفاصيل ومواصفات المنتج الفاخر من بامبينو كيدز، خامات عضوية 100% ومقاسات متنوعة مع توصيل سريع وإمكانية الطلب المباشر عبر واتساب.">
  <link rel="stylesheet" href="css/style.css">
  <link rel="icon" href="images/kids_cat_girls.jpg">
</head>
<body>
__HEADER__

  <!-- BREADCRUMB -->
  <div class="page-hero" style="padding: 24px 0;">
    <div class="container">
      <div class="breadcrumb" style="justify-content: flex-start;">
        <a href="index.html">الرئيسية</a>
        <span>/</span>
        <a href="shop.html">المتجر</a>
        <span>/</span>
        <span id="productBreadcrumbCat" style="color: var(--text-light);">القسم</span>
        <span>/</span>
        <span id="productBreadcrumbTitle" style="color: var(--primary); font-weight: 700;">اسم المنتج</span>
      </div>
    </div>
  </div>

  <!-- PRODUCT DETAILS SECTION -->
  <div class="container">
    <div class="product-detail-grid">
      <!-- Gallery Column -->
      <div class="product-gallery">
        <img id="detailMainImg" src="images/prod_girls_party.jpg" alt="صورة المنتج" class="main-gallery-img">
        <div class="gallery-thumbs" id="detailThumbs">
          <!-- Thumbnail buttons -->
        </div>
      </div>

      <!-- Info Column -->
      <div class="product-detail-info">
        <div style="display: flex; gap: 8px; margin-bottom: 10px;">
          <span id="detailBadge" class="product-badge badge-featured" style="position: static; display: inline-block;">الأكثر مبيعاً ⭐</span>
          <span id="detailCatBadge" class="size-tag" style="padding: 4px 10px;">ملابس أطفال</span>
        </div>

        <h1 id="detailTitle">فستان روبي المخملي الفاخر بياقة دانتيل وأزرار ذهبية</h1>

        <div class="product-detail-meta">
          <div class="product-rating">
            <span id="detailStars">★★★★★</span>
            <span class="reviews-count" id="detailReviews">(42 تقييم عملاء موثق)</span>
          </div>
          <div style="color: #10b981; font-weight: 700; font-size: 0.88rem;">
            ✓ متوفر في المخزون وجاهز للشحن الفوري
          </div>
        </div>

        <div class="product-detail-price">
          <span class="current" id="detailPriceCurrent">295 ر.س</span>
          <span class="old" id="detailPriceOld">380 ر.س</span>
          <span class="discount-badge" id="detailDiscountBadge">خصم 22%</span>
        </div>

        <div class="product-detail-desc" id="detailDesc">
          قطعة فاخرة مصنوعة بعناية فائقة من أجود أنواع القطن العضوي 100% المريح والآمن على بشرة طفلك الحساسة. تصميم أنيق وعصري يجمع بين راحة الارتداء وفخامة الإطلالة لجميع المناسبات.
        </div>

        <!-- Size Selection -->
        <div class="size-select-group">
          <label>اختاري المقاس المناسب:</label>
          <div class="size-options" id="detailSizeOptions">
            <!-- Rendered sizes -->
          </div>
        </div>

        <!-- Quantity and Buttons -->
        <div class="qty-action-row">
          <div class="qty-stepper">
            <button onclick="changeDetailQty(-1)">-</button>
            <input type="text" id="detailQtyInput" value="1" readonly>
            <button onclick="changeDetailQty(1)">+</button>
          </div>

          <button class="btn-large-cart" onclick="addCurrentProductToCart()">
            <svg width="20" height="20" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 11V7a4 4 0 00-8 0v4M5 9h14l1 12H4L5 9z"></path></svg>
            <span>أضف إلى السلة</span>
          </button>
        </div>

        <!-- Direct WhatsApp Button -->
        <button class="btn-large-whatsapp" onclick="buyCurrentProductWhatsApp()">
          <svg width="22" height="22" fill="currentColor" viewBox="0 0 24 24"><path d="M12.031 6.172c-3.181 0-5.767 2.586-5.768 5.766-.001 1.298.38 2.27 1.019 3.287l-.711 2.598 2.668-.699c.97.53 1.77.818 2.792.818 3.182 0 5.768-2.587 5.768-5.768 0-3.181-2.586-5.764-5.768-5.764zm3.393 8.163c-.144.405-.837.774-1.17.824-.312.045-.634.07-1.782-.407-1.468-.609-2.42-2.094-2.493-2.193-.073-.098-.598-.795-.598-1.517 0-.721.378-1.077.513-1.223.135-.145.295-.181.393-.181.098 0 .197.001.283.006.09.005.21.034.322.302.118.283.407.994.442 1.066.035.073.059.158.012.253-.047.095-.071.154-.141.236-.07.082-.148.184-.211.247-.07.07-.143.146-.062.285.082.139.362.598.777.968.533.475.982.622 1.121.692.139.07.221.059.303-.035.082-.095.35-407.443-.547.093-.14.186-.116.312-.07.127.047.808.381.947.451.139.07.232.105.267.163.035.058.035.342-.109.747z"></path></svg>
          <span>اشتري الآن مباشرة عبر واتساب</span>
        </button>

        <!-- Perks List -->
        <div class="product-perks-box">
          <div class="perk-item">
            <span class="perk-icon">🚚</span>
            <span>توصيل سريع لباب منزلك خلال 2-4 أيام عمل في جميع مدن المملكة</span>
          </div>
          <div class="perk-item">
            <span class="perk-icon">🔄</span>
            <span>إمكانية الاستبدال والاسترجاع السهل خلال 7 أيام من الاستلام</span>
          </div>
          <div class="perk-item">
            <span class="perk-icon">💳</span>
            <span>دفع آمن عند الاستلام أو تحويل بنكي سريع</span>
          </div>
          <div class="perk-item">
            <span class="perk-icon">🌿</span>
            <span>أقمشة قطنية نقية 100% معتمدة لا تسبب أي تحسس لبشرة الأطفال</span>
          </div>
        </div>
      </div>
    </div>

    <!-- RELATED PRODUCTS -->
    <section class="section-padding" style="border-top: 1px solid var(--border-light);">
      <div class="section-header">
        <span class="section-tag">تشكيلات مقترحة</span>
        <h2 class="section-title">قطع مشابهة قد تعجبك</h2>
      </div>
      <div class="products-grid" id="relatedProductsGrid">
        <!-- Rendered dynamically -->
      </div>
    </section>
  </div>

__FOOTER__

  <script src="js/store.js"></script>
  <script>
    let currentProduct = null;
    let selectedSize = '';
    let currentQty = 1;

    function initProductPage() {
      const params = new URLSearchParams(window.location.search);
      const id = params.get('id') || 1;
      const product = BambinoStore.getProductById(id);

      if (!product) {
        window.location.href = 'shop.html';
        return;
      }

      currentProduct = product;
      const settings = BambinoStore.getSettings();

      // Set Title and meta
      document.title = `${product.name} | بامبينو كيدز`;
      document.getElementById('productBreadcrumbCat').textContent = product.catName;
      document.getElementById('productBreadcrumbTitle').textContent = product.name;

      document.getElementById('detailTitle').textContent = product.name;
      document.getElementById('detailCatBadge').textContent = product.catName;
      document.getElementById('detailDesc').textContent = product.desc || 'منتج أنيق وفاخر مصمم خصيصاً لأطفالك.';
      
      const badgeEl = document.getElementById('detailBadge');
      if (product.badge) {
        badgeEl.textContent = product.badge;
        badgeEl.className = `product-badge ${product.badgeClass || 'badge-featured'}`;
        badgeEl.style.display = 'inline-block';
      } else {
        badgeEl.style.display = 'none';
      }

      // Prices
      document.getElementById('detailPriceCurrent').textContent = `${product.price} ${settings.currency}`;
      if (product.oldPrice) {
        document.getElementById('detailPriceOld').textContent = `${product.oldPrice} ${settings.currency}`;
        const discount = Math.round(((product.oldPrice - product.price) / product.oldPrice) * 100);
        document.getElementById('detailDiscountBadge').textContent = `خصم ${discount}%`;
      } else {
        document.getElementById('detailPriceOld').style.display = 'none';
        document.getElementById('detailDiscountBadge').style.display = 'none';
      }

      // Ratings
      const stars = '★'.repeat(Math.floor(product.rating || 5)) + ((product.rating || 5) % 1 !== 0 ? '½' : '');
      document.getElementById('detailStars').textContent = stars;
      document.getElementById('detailReviews').textContent = `(${product.reviews || 25} تقييم عملاء موثق)`;

      // Image & Gallery Thumbs
      const mainImg = document.getElementById('detailMainImg');
      mainImg.src = product.img;
      mainImg.alt = product.name;

      const thumbsContainer = document.getElementById('detailThumbs');
      // Create thumbs (primary + duplicate/variations for rich gallery experience)
      const imagesList = [product.img, product.img];
      thumbsContainer.innerHTML = imagesList.map((imgSrc, idx) => `
        <img src="${imgSrc}" class="gallery-thumb ${idx === 0 ? 'active' : ''}" onclick="selectThumb(this, '${imgSrc}')" alt="صورة مصغرة">
      `).join('');

      // Sizes
      const sizesContainer = document.getElementById('detailSizeOptions');
      const sizes = product.sizes && product.sizes.length ? product.sizes : ['1-2y', '3-5y', '6-8y'];
      selectedSize = sizes[0];

      sizesContainer.innerHTML = sizes.map((sz, idx) => `
        <button class="size-btn ${idx === 0 ? 'active' : ''}" onclick="selectSize(this, '${sz}')">${sz}</button>
      `).join('');

      // Related Products
      const related = BambinoStore.getProducts().filter(p => p.cat === product.cat && p.id !== product.id).slice(0, 3);
      const relatedContainer = document.getElementById('relatedProductsGrid');
      if (relatedContainer) {
        relatedContainer.innerHTML = (related.length ? related : BambinoStore.getProducts().slice(0, 3))
          .map(p => BambinoStore.renderProductCardHTML(p)).join('');
      }
    }

    function selectThumb(thumbEl, src) {
      document.querySelectorAll('.gallery-thumb').forEach(t => t.classList.remove('active'));
      thumbEl.classList.add('active');
      document.getElementById('detailMainImg').src = src;
    }

    function selectSize(btn, sz) {
      document.querySelectorAll('.size-btn').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      selectedSize = sz;
    }

    function changeDetailQty(delta) {
      currentQty = Math.max(1, currentQty + delta);
      document.getElementById('detailQtyInput').value = currentQty;
    }

    function addCurrentProductToCart() {
      if (!currentProduct) return;
      BambinoStore.addToCart(currentProduct.id, selectedSize, currentQty);
    }

    function buyCurrentProductWhatsApp() {
      if (!currentProduct) return;
      BambinoStore.directWhatsAppProduct(currentProduct.id, selectedSize, currentQty);
    }

    document.addEventListener('DOMContentLoaded', () => {
      initProductPage();
    });
  </script>
</body>
</html>
"""
    with open(os.path.join(BASE_DIR, 'product.html'), 'w', encoding='utf-8') as f:
        f.write(html.replace('__HEADER__', header).replace('__FOOTER__', footer))
    print("product.html written successfully!")


# ==========================================
# 4. ABOUT.HTML (About Us)
# ==========================================
def build_about():
    header = get_header(active_nav='about')
    footer = get_footer()

    html = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>من نحن | بامبينو كيدز للأزياء الراقية</title>
  <meta name="description" content="تعرف على قصة بامبينو كيدز، شغفنا بتوفير أرقى أزياء الأطفال المصنوعة من القطن الطبيعي لراحة وأناقة تدوم طويلاً.">
  <link rel="stylesheet" href="css/style.css">
  <link rel="icon" href="images/kids_cat_girls.jpg">
</head>
<body>
__HEADER__

  <div class="page-hero">
    <div class="container">
      <h1 class="page-hero-title">من نحن - قصة بامبينو كيدز</h1>
      <div class="breadcrumb">
        <a href="index.html">الرئيسية</a>
        <span>/</span>
        <span style="color: var(--primary); font-weight: 700;">من نحن</span>
      </div>
    </div>
  </div>

  <div class="container">
    <div class="static-page-content">
      <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 40px; align-items: center; margin-bottom: 40px;">
        <div>
          <span class="section-tag">شغف بالأناقة والراحة</span>
          <h2>أزياء راقية تُصنع بحب لأجمل لحظات الطفولة</h2>
          <p>
            تأسست علامة <strong>بامبينو كيدز (BAMBINO KIDS)</strong> انطلاقاً من إيماننا العميق بأن أطفالنا يستحقون الأفضل دائماً. نحن ندرك أن ملابس الأطفال ليست مجرد مظهر أنيق، بل هي راحة يومية وحرية حركة وأمان تام على بشرتهم الغضة.
          </p>
          <p>
            منذ اليوم الأول، وضعنا معايير صارمة في انتقاء خامات القطن العضوي النقي 100% والتصاميم الراقية المستوحاة من أحدث صيحات الموضة الأوروبية والعالمية، لنقدم للأمهات تشكيلات تلبي طموحاتهن في إطلالات استثنائية لأطفالهن في جميع المناسبات.
          </p>
        </div>
        <div>
          <img src="images/hero_kids_slide_2.jpg" alt="أطفال بامبينو كيدز" style="border-radius: var(--radius-lg); box-shadow: var(--shadow-md);">
        </div>
      </div>

      <div class="features-grid" style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 24px; margin: 40px 0;">
        <div style="background: var(--bg-soft); padding: 26px; border-radius: var(--radius-md); border-right: 4px solid var(--primary);">
          <div style="font-size: 2.2rem; margin-bottom: 10px;">🌟</div>
          <h3 style="font-size: 1.2rem; font-weight: 800; color: var(--dark); margin-bottom: 8px;">جودة لا تقبل المساومة</h3>
          <p style="font-size: 0.95rem; color: var(--text-light);">نختار بعناية فائقة أنعم أنواع الخيوط القطنية وأدق تفاصيل الحياكة لضمان متانة القطعة بعد كل غسيل.</p>
        </div>

        <div style="background: var(--bg-soft); padding: 26px; border-radius: var(--radius-md); border-right: 4px solid var(--primary);">
          <div style="font-size: 2.2rem; margin-bottom: 10px;">👶</div>
          <h3 style="font-size: 1.2rem; font-weight: 800; color: var(--dark); margin-bottom: 8px;">أمان وراحة تامة</h3>
          <p style="font-size: 0.95rem; color: var(--text-light);">جميع أصباغنا وأزرارنا وإكسسواراتنا معتمدة وخالية من المواد الكيميائية الضارة لسلامة طفلك التامة.</p>
        </div>

        <div style="background: var(--bg-soft); padding: 26px; border-radius: var(--radius-md); border-right: 4px solid var(--primary);">
          <div style="font-size: 2.2rem; margin-bottom: 10px;">❤️</div>
          <h3 style="font-size: 1.2rem; font-weight: 800; color: var(--dark); margin-bottom: 8px;">خدمة أمهات استثنائية</h3>
          <p style="font-size: 0.95rem; color: var(--text-light);">فريقنا يتفهم متطلبات المقاسات ويسعد دائماً بتقديم المشورة وتيسير الشحن والاستبدال بكل رحابة صدر.</p>
        </div>
      </div>

      <h2>رسالتنا</h2>
      <p>
        أن نكون الوجهة الأولى والمفضلة لكل أسرة تبحث عن الفخامة والعملية في ملابس الأطفال في المملكة والخليج، مقدمين تجربة تسوق راقية تبدأ من سهولة الطلب وتتوج بابتسامة طفلك عند ارتداء قطعته المفضلة.
      </p>
    </div>
  </div>

__FOOTER__

  <script src="js/store.js"></script>
</body>
</html>
"""
    with open(os.path.join(BASE_DIR, 'about.html'), 'w', encoding='utf-8') as f:
        f.write(html.replace('__HEADER__', header).replace('__FOOTER__', footer))
    print("about.html written successfully!")


# ==========================================
# 5. CONTACT.HTML (Contact Us)
# ==========================================
def build_contact():
    header = get_header(active_nav='contact')
    footer = get_footer()

    html = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>اتصل بنا | خدمة عملاء بامبينو كيدز</title>
  <meta name="description" content="تواصل مع فريق خدمة عملاء بامبينو كيدز عبر واتساب، الهاتف أو البريد الإلكتروني. يسعدنا الرد على استفساراتكم ومساعدتكم على مدار الساعة.">
  <link rel="stylesheet" href="css/style.css">
  <link rel="icon" href="images/kids_cat_girls.jpg">
</head>
<body>
__HEADER__

  <div class="page-hero">
    <div class="container">
      <h1 class="page-hero-title">يسعدنا تواصلكم دائماً</h1>
      <div class="breadcrumb">
        <a href="index.html">الرئيسية</a>
        <span>/</span>
        <span style="color: var(--primary); font-weight: 700;">اتصل بنا</span>
      </div>
    </div>
  </div>

  <div class="container">
    <div class="contact-grid">
      <!-- Info Cards -->
      <div class="contact-info-card">
        <div>
          <span class="section-tag">نحن هنا للمساعدة</span>
          <h2 style="font-size: 1.6rem; font-weight: 900; color: var(--dark); margin-bottom: 8px;">قنوات التواصل المباشر</h2>
          <p style="color: var(--text-light); font-size: 0.95rem;">فريق خدمة العملاء جاهز للإجابة عن أسئلتكم ومساعدتكم في اختيار المقاسات أو متابعة الشحنات.</p>
        </div>

        <div class="contact-card-item">
          <div class="contact-card-icon">💬</div>
          <div>
            <h4 style="font-weight: 800; color: var(--dark); margin-bottom: 2px;">محادثة واتساب الفورية</h4>
            <p style="font-size: 0.88rem; color: var(--text-light); margin-bottom: 4px;">الرد السريع خلال دقائق</p>
            <a href="https://wa.me/966500000000" target="_blank" class="store-whatsapp-link" style="color: #25d366; font-weight: 800;">بدء المحادثة الآن ←</a>
          </div>
        </div>

        <div class="contact-card-item">
          <div class="contact-card-icon">📞</div>
          <div>
            <h4 style="font-weight: 800; color: var(--dark); margin-bottom: 2px;">الهاتف المباشر</h4>
            <p style="font-size: 0.88rem; color: var(--text-light); margin-bottom: 4px;">يومياً من 9:00 ص إلى 11:00 م</p>
            <span class="store-phone-text" style="color: var(--primary); font-weight: 800;">+966 50 000 0000</span>
          </div>
        </div>

        <div class="contact-card-item">
          <div class="contact-card-icon">✉️</div>
          <div>
            <h4 style="font-weight: 800; color: var(--dark); margin-bottom: 2px;">البريد الإلكتروني</h4>
            <p style="font-size: 0.88rem; color: var(--text-light); margin-bottom: 4px;">للاستفسارات والشكاوى الرسمية</p>
            <span class="store-email-text" style="color: var(--primary); font-weight: 800;">care@bambinokids.com</span>
          </div>
        </div>

        <div class="contact-card-item">
          <div class="contact-card-icon">📍</div>
          <div>
            <h4 style="font-weight: 800; color: var(--dark); margin-bottom: 2px;">موقع المتجر والمقر</h4>
            <p class="store-address-text" style="font-size: 0.9rem; color: var(--text);">المملكة العربية السعودية - الرياض - طريق الملك فهد</p>
          </div>
        </div>
      </div>

      <!-- Form Card -->
      <div class="contact-form-card">
        <h3 style="font-size: 1.4rem; font-weight: 900; color: var(--dark); margin-bottom: 16px;">أرسل لنا رسالة سريعة</h3>
        <form onsubmit="handleContactSubmit(event)">
          <div class="form-group">
            <label>الاسم الكامل *</label>
            <input type="text" id="contactName" placeholder="اكتب اسمك الكريم" required>
          </div>
          <div class="form-group">
            <label>رقم الجوال أو واتساب *</label>
            <input type="tel" id="contactPhone" placeholder="05xxxxxxxx" required>
          </div>
          <div class="form-group">
            <label>موضوع الاستفسار *</label>
            <select id="contactSubject">
              <option value="استفسار عن مقاسات">استفسار عن مقاسات ومنتجات</option>
              <option value="متابعة حالة طلب">متابعة حالة شحنة أو طلب</option>
              <option value="طلب استبدال واسترجاع">طلب استبدال واسترجاع</option>
              <option value="اقتراح أو ملاحظة">اقتراح أو ملاحظة عامة</option>
            </select>
          </div>
          <div class="form-group">
            <label>تفاصيل الرسالة *</label>
            <textarea id="contactMessage" rows="4" placeholder="كيف يمكننا مساعدتك اليوم؟" required></textarea>
          </div>
          <button type="submit" class="btn-checkout" style="width: 100%; margin-top: 10px;">
            <span>إرسال الرسالة عبر واتساب 💬</span>
          </button>
        </form>
      </div>
    </div>
  </div>

__FOOTER__

  <script src="js/store.js"></script>
  <script>
    function handleContactSubmit(e) {
      e.preventDefault();
      const name = document.getElementById('contactName').value.trim();
      const phone = document.getElementById('contactPhone').value.trim();
      const subject = document.getElementById('contactSubject').value;
      const message = document.getElementById('contactMessage').value.trim();
      const settings = BambinoStore.getSettings();

      const text = `*📩 رسالة جديدة من صفحة اتصل بنا - بامبينو كيدز*\\n` +
        `--------------------------------\\n` +
        `👤 *الاسم:* ${name}\\n` +
        `📱 *الجوال:* ${phone}\\n` +
        `📋 *الموضوع:* ${subject}\\n` +
        `📝 *الرسالة:* ${message}\\n` +
        `--------------------------------`;

      const waUrl = `https://wa.me/${settings.whatsapp}?text=${encodeURIComponent(text)}`;
      window.open(waUrl, '_blank');
      BambinoStore.showToast('✅ تم فتح محادثة واتساب لإرسال رسالتك مباشرة!');
    }
  </script>
</body>
</html>
"""
    with open(os.path.join(BASE_DIR, 'contact.html'), 'w', encoding='utf-8') as f:
        f.write(html.replace('__HEADER__', header).replace('__FOOTER__', footer))
    print("contact.html written successfully!")


# ==========================================
# 6. PRIVACY.HTML (Privacy Policy)
# ==========================================
def build_privacy():
    header = get_header(active_nav='')
    footer = get_footer()

    html = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>سياسة الخصوصية | بامبينو كيدز</title>
  <link rel="stylesheet" href="css/style.css">
  <link rel="icon" href="images/kids_cat_girls.jpg">
</head>
<body>
__HEADER__

  <div class="page-hero">
    <div class="container">
      <h1 class="page-hero-title">سياسة الخصوصية وسرية المعلومات</h1>
      <div class="breadcrumb">
        <a href="index.html">الرئيسية</a>
        <span>/</span>
        <span style="color: var(--primary); font-weight: 700;">سياسة الخصوصية</span>
      </div>
    </div>
  </div>

  <div class="container">
    <div class="static-page-content">
      <p>
        نقدر مخاوفكم واهتمامكم بشأن خصوصية بياناتكم على شبكة الإنترنت. تم إعداد هذه السياسة لمساعدتكم في فهم طبيعة البيانات التي نقوم بجمعها منكم عند زيارتكم لمتجر <strong>بامبينو كيدز (BAMBINO KIDS)</strong> وكيفية تعاملنا مع هذه البيانات الشخصية.
      </p>

      <h2>1. البيانات التي نقوم بجمعها</h2>
      <p>
        عند تقديمكم لطلب شراء أو التواصل معنا عبر واتساب أو نموذج الاتصال، قد نطلب منكم تزويدنا ببيانات تشمل: الاسم الكامل، رقم الجوال، عنوان التوصيل داخل المملكة العربية السعودية، والملاحظات المتعلقة بالطلب.
      </p>

      <h2>2. الغرض من جمع البيانات</h2>
      <ul>
        <li>تجهيز وشحن وتوصيل طلباتكم إلى العنوان المحدد بكل دقة وسرعة.</li>
        <li>التواصل معكم عبر واتساب أو الرسائل النصية لتأكيد الطلب وتزويدكم برقم التتبع.</li>
        <li>الرد على استفساراتكم واقتراحاتكم وتقديم الدعم الفني اللازم.</li>
        <li>إشعاركم بالعروض الحصرية والتخفيضات الموسمية (في حال رغبتكم في ذلك).</li>
      </ul>

      <h2>3. سرية وأمان المعلومات</h2>
      <p>
        نلتزم التزاماً تاماً بعدم بيع، تأجير، أو مشاركة أي من بياناتكم الشخصية مع أي طرف ثالث لأغراض تسويقية أو تجارية. تُستخدم بياناتكم حصرياً لإتمام طلباتكم وتقديم أرقى مستوى من الخدمة من خلال فريقنا المعتمد وشركات الشحن الشريكة.
      </p>

      <h2>4. التعديلات على سياسة الخصوصية</h2>
      <p>
        نحتفظ بالحق في تعديل بنود وشروط سياسة الخصوصية عند الضرورة وبما يتوافق مع الأنظمة المعمول بها في المملكة العربية السعودية. سيتم نشر أي تحديث على هذه الصفحة مع إشعار عملائنا الكرام.
      </p>

      <h2>5. الاتصال بنا</h2>
      <p>
        إذا كانت لديكم أي استفسارات أو ملاحظات بشأن سياسة الخصوصية، يرجى التواصل معنا عبر البريد الإلكتروني <span class="store-email-text" style="font-weight: 700; color: var(--primary);">care@bambinokids.com</span> أو عبر واتساب خدمة العملاء.
      </p>
    </div>
  </div>

__FOOTER__

  <script src="js/store.js"></script>
</body>
</html>
"""
    with open(os.path.join(BASE_DIR, 'privacy.html'), 'w', encoding='utf-8') as f:
        f.write(html.replace('__HEADER__', header).replace('__FOOTER__', footer))
    print("privacy.html written successfully!")


# ==========================================
# 7. TERMS.HTML (Terms of Service)
# ==========================================
def build_terms():
    header = get_header(active_nav='')
    footer = get_footer()

    html = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>الشروط والأحكام | بامبينو كيدز</title>
  <link rel="stylesheet" href="css/style.css">
  <link rel="icon" href="images/kids_cat_girls.jpg">
</head>
<body>
__HEADER__

  <div class="page-hero">
    <div class="container">
      <h1 class="page-hero-title">شروط وأحكام الاستخدام والطلب</h1>
      <div class="breadcrumb">
        <a href="index.html">الرئيسية</a>
        <span>/</span>
        <span style="color: var(--primary); font-weight: 700;">الشروط والأحكام</span>
      </div>
    </div>
  </div>

  <div class="container">
    <div class="static-page-content">
      <p>
        أهلاً بكم في متجر <strong>بامبينو كيدز (BAMBINO KIDS)</strong>. يرجى قراءة هذه الشروط والأحكام بعناية قبل استخدام الموقع أو تقديم أي طلب شراء. يُعد استخدامكم للمتجر أو إتمام الطلب موافقة صريحة على الالتزام بكافة الشروط الموضحة أدناه.
      </p>

      <h2>1. الطلب وتأكيد المشتريات</h2>
      <ul>
        <li>يتم استقبال وتأكيد الطلبات عبر النظام الإلكتروني للمتجر أو مباشرة عبر تطبيق واتساب المعتمد.</li>
        <li>يتحمل العميل مسؤولية التأكد من صحة بيانات التواصل والعنوان التفصيلي والمقاسات المطلوبة.</li>
        <li>جميع الأسعار المعروضة في المتجر تشمل ضريبة القيمة المضافة ومسعرة بالريال السعودي (ر.س).</li>
      </ul>

      <h2>2. الشحن والتوصيل</h2>
      <ul>
        <li>نقوم بالشحن إلى جميع مدن ومناطق المملكة العربية السعودية عبر أسرع شركات الشحن المعتمدة.</li>
        <li>مدة التوصيل المعتادة تتراوح بين 2 إلى 4 أيام عمل من تاريخ تأكيد الطلب.</li>
        <li>الشحن مجاني لجميع الطلبات التي تتجاوز قيمتها 250 ريال سعودي.</li>
      </ul>

      <h2>3. سياسة الاستبدال والاسترجاع</h2>
      <ul>
        <li>حرصاً على سلامتكم ورضاكم، يحق للعميل طلب استبدال المقاس أو استرجاع المنتج خلال 7 أيام من تاريخ الاستلام.</li>
        <li>يشترط أن تكون القطعة في حالتها الأصلية غير ملبوسة، مع بطاقات السعر والتغليف الأصلي.</li>
        <li>في حال وجود أي عيب مصنعي في المنتج، يتحمل المتجر كافة تكاليف الشحن والاستبدال بالكامل دون أي رسوم على العميل.</li>
      </ul>

      <h2>4. المقاسات والألوان</h2>
      <p>
        نبذل قصارى جهدنا لعرض ألوان وتفاصيل المنتجات بأعلى دقة ممكنة، إلا أنه قد يطرأ اختلاف طفيف جداً في درجات الألوان نتيجة لاختلاف إعدادات شاشات العرض وإضاءة التصوير. فريقنا متاح دائماً عبر واتساب لإرسال صور وفيديوهات حية للقطعة قبل شحنها.
      </p>
    </div>
  </div>

__FOOTER__

  <script src="js/store.js"></script>
</body>
</html>
"""
    with open(os.path.join(BASE_DIR, 'terms.html'), 'w', encoding='utf-8') as f:
        f.write(html.replace('__HEADER__', header).replace('__FOOTER__', footer))
    print("terms.html written successfully!")


# ==========================================
# 8. ADMIN/INDEX.HTML (Admin Dashboard)
# ==========================================
def build_admin():
    html = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>لوحة التحكم | متجر بامبينو كيدز</title>
  <link rel="stylesheet" href="../css/style.css">
  <link rel="icon" href="../images/kids_cat_girls.jpg">
</head>
<body class="admin-body">

  <!-- ADMIN AUTH BOX (PIN Protection) -->
  <div id="adminAuthBox" style="min-height: 100vh; display: flex; align-items: center; justify-content: center; padding: 20px; background: linear-gradient(135deg, #fff5f6 0%, #fee2e2 100%);">
    <div style="background: #fff; padding: 40px; border-radius: var(--radius-lg); box-shadow: var(--shadow-lg); max-width: 420px; width: 100%; text-align: center; border: 1px solid var(--border-light);">
      <div style="font-size: 3rem; margin-bottom: 10px;">🔐</div>
      <h2 style="font-size: 1.6rem; font-weight: 900; color: var(--dark); margin-bottom: 6px;">لوحة تحكم بامبينو كيدز</h2>
      <p style="color: var(--text-light); font-size: 0.9rem; margin-bottom: 24px;">يرجى إدخال رمز الأمان (PIN) لتعديل المتجر وإدارة المنتجات</p>

      <form id="adminLoginForm">
        <div class="form-group">
          <input type="password" id="adminPinInput" placeholder="أدخل رمز الدخول (الافتراضي: 1234)" style="text-align: center; font-size: 1.2rem; letter-spacing: 4px; padding: 14px;" required autofocus>
        </div>
        <button type="submit" class="btn-checkout" style="width: 100%; margin-top: 10px;">
          <span>دخول إلى لوحة التحكم ←</span>
        </button>
      </form>

      <div style="margin-top: 20px; font-size: 0.85rem; color: #64748b;">
        الرمز الافتراضي للوحة هو: <strong style="color: var(--primary);">1234</strong>
      </div>
      <div style="margin-top: 14px;">
        <a href="../index.html" style="font-size: 0.88rem; color: var(--primary); font-weight: 700;">الرجوع إلى المتجر الرئيسي</a>
      </div>
    </div>
  </div>

  <!-- ADMIN APP BOX -->
  <div id="adminAppBox" style="display: none;">
    <!-- Admin Top Navbar -->
    <header class="admin-navbar">
      <div class="admin-brand">
        <h2>BAMBINO</h2>
        <span>لوحة تحكم المتجر</span>
      </div>

      <div class="admin-top-actions">
        <a href="../index.html" target="_blank" class="btn-admin-pill btn-admin-outline" title="معاينة المتجر في صفحة جديدة">
          <span>معاينة المتجر</span>
          <span>👁️</span>
        </a>
        <button onclick="AdminApp.logout()" class="btn-admin-pill btn-admin-danger">
          <span>خروج</span>
          <span>🚪</span>
        </button>
      </div>
    </header>

    <div class="admin-layout">
      <!-- Admin Sidebar -->
      <aside class="admin-sidebar">
        <div class="admin-nav-item active" data-tab="products">
          <span>🛍️</span>
          <span>إدارة المنتجات</span>
        </div>
        <div class="admin-nav-item" data-tab="settings">
          <span>⚙️</span>
          <span>إعدادات المتجر</span>
        </div>
        <div class="admin-nav-item" data-tab="backup">
          <span>💾</span>
          <span>النسخ الاحتياطي</span>
        </div>
      </aside>

      <!-- Admin Main Content -->
      <main class="admin-main">
        <!-- STATS OVERVIEW -->
        <div class="stats-grid">
          <div class="stat-card">
            <div class="stat-card-title">إجمالي المنتجات</div>
            <div class="stat-card-val" id="statTotalProducts">0</div>
          </div>
          <div class="stat-card">
            <div class="stat-card-title">الأقسام النشطة</div>
            <div class="stat-card-val" id="statTotalCats">0</div>
          </div>
          <div class="stat-card">
            <div class="stat-card-title">متوسط أسعار القطع</div>
            <div class="stat-card-val" id="statAvgPrice">0 ر.س</div>
          </div>
          <div class="stat-card">
            <div class="stat-card-title">حالة المتجر</div>
            <div class="stat-card-val" style="color: #10b981; font-size: 1.3rem;">● متصل ويعمل</div>
          </div>
        </div>

        <!-- TAB 1: PRODUCTS MANAGER -->
        <div class="admin-tab-content active" id="tab-products">
          <div class="admin-card">
            <div class="admin-card-header">
              <h3>قائمة المنتجات في المتجر</h3>
              <button class="btn-admin-pill btn-admin-primary" onclick="AdminApp.openAddModal()">
                <span>+ إضافة منتج جديد</span>
              </button>
            </div>

            <!-- Search and Filter input -->
            <div style="margin-bottom: 18px; max-width: 350px;">
              <input type="text" placeholder="بحث سريع في المنتجات بالاسم أو القسم..." oninput="AdminApp.renderProductsTable(this.value)" style="width: 100%; padding: 10px 14px; border: 1px solid #cbd5e1; border-radius: var(--radius-sm); font-size: 0.9rem;">
            </div>

            <div class="admin-table-wrap">
              <table class="admin-table">
                <thead>
                  <tr>
                    <th>الصورة</th>
                    <th>اسم المنتج</th>
                    <th>القسم</th>
                    <th>السعر الحالي</th>
                    <th>شارة التميز</th>
                    <th>المقاسات</th>
                    <th>الإجراءات</th>
                  </tr>
                </thead>
                <tbody id="adminProductsTbody">
                  <!-- Rendered dynamically -->
                </tbody>
              </table>
            </div>
          </div>
        </div>

        <!-- TAB 2: STORE SETTINGS -->
        <div class="admin-tab-content" id="tab-settings">
          <div class="admin-card" style="max-width: 750px;">
            <div class="admin-card-header">
              <h3>إعدادات وتفاصيل المتجر</h3>
            </div>

            <form id="adminSettingsForm">
              <div class="form-group">
                <label>اسم المتجر والبراند</label>
                <input type="text" id="settStoreName" required>
              </div>

              <div class="form-group">
                <label>نص شريط الإعلانات العلوي (Announcement Bar)</label>
                <input type="text" id="settAnnouncement" required>
              </div>

              <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px;">
                <div class="form-group">
                  <label>رقم واتساب لاستقبال الطلبات (بدون +)</label>
                  <input type="text" id="settWhatsapp" placeholder="966500000000" required>
                </div>
                <div class="form-group">
                  <label>رقم هاتف الاتصال المباشر</label>
                  <input type="text" id="settPhone" placeholder="+966 50 000 0000" required>
                </div>
              </div>

              <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px;">
                <div class="form-group">
                  <label>البريد الإلكتروني الرسمي</label>
                  <input type="email" id="settEmail" required>
                </div>
                <div class="form-group">
                  <label>العملة</label>
                  <input type="text" id="settCurrency" value="ر.س" required>
                </div>
              </div>

              <div class="form-group">
                <label>عنوان المتجر / المقر</label>
                <input type="text" id="settAddress" required>
              </div>

              <button type="submit" class="btn-checkout" style="width: auto; padding: 12px 30px;">
                <span>حفظ التعديلات في المتجر ✅</span>
              </button>
            </form>
          </div>
        </div>

        <!-- TAB 3: BACKUP & DATA -->
        <div class="admin-tab-content" id="tab-backup">
          <div class="admin-card" style="max-width: 750px;">
            <div class="admin-card-header">
              <h3>النسخ الاحتياطي وإدارة البيانات</h3>
            </div>

            <div style="display: flex; flex-direction: column; gap: 20px;">
              <div style="background: var(--bg-soft); padding: 20px; border-radius: var(--radius-sm); border: 1px solid var(--border-light);">
                <h4 style="font-size: 1.05rem; font-weight: 800; color: var(--dark); margin-bottom: 6px;">📥 تصدير نسخة احتياطية من جميع المنتجات</h4>
                <p style="font-size: 0.9rem; color: var(--text-light); margin-bottom: 14px;">يمكنك تحميل ملف JSON يحتوي على كامل منتجات المتجر وأسعارها وتفاصيلها لحفظها على جهازك.</p>
                <button class="btn-admin-pill btn-admin-primary" onclick="AdminApp.exportProductsJSON()">
                  <span>تحميل ملف المنتجات (JSON) 📥</span>
                </button>
              </div>

              <div style="background: var(--bg-soft); padding: 20px; border-radius: var(--radius-sm); border: 1px solid var(--border-light);">
                <h4 style="font-size: 1.05rem; font-weight: 800; color: var(--dark); margin-bottom: 6px;">📤 استيراد وتحديث المنتجات من ملف</h4>
                <p style="font-size: 0.9rem; color: var(--text-light); margin-bottom: 14px;">ارفع ملف JSON الذي قمت بتصديره سابقاً لاستعادة المنتجات في ثوانٍ معدودة.</p>
                <input type="file" id="importProductsInput" accept=".json" onchange="AdminApp.importProductsJSON(event)" style="display: none;">
                <button class="btn-admin-pill btn-admin-outline" onclick="document.getElementById('importProductsInput').click()">
                  <span>اختيار ملف JSON ورفعه 📤</span>
                </button>
              </div>

              <div style="background: #fff1f2; padding: 20px; border-radius: var(--radius-sm); border: 1px solid #fecdd3;">
                <h4 style="font-size: 1.05rem; font-weight: 800; color: #dc2626; margin-bottom: 6px;">⚠️ استعادة المنتجات الافتراضية (إعادة ضبط المصنع)</h4>
                <p style="font-size: 0.9rem; color: #b91c1c; margin-bottom: 14px;">سيؤدي هذا إلى إعادة المتجر إلى المنتجات الأصلية وحذف أي منتجات تجريبية تمت إضافتها.</p>
                <button class="btn-admin-pill btn-admin-danger" onclick="AdminApp.resetDefaultProducts()">
                  <span>استرجاع المنتجات الاصلية للمتجر 🔄</span>
                </button>
              </div>
            </div>
          </div>
        </div>
      </main>
    </div>
  </div>

  <!-- ADD / EDIT PRODUCT MODAL -->
  <div class="admin-modal-overlay" id="adminProductModalOverlay">
    <div class="admin-modal">
      <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px; border-bottom: 1px solid var(--border-light); padding-bottom: 14px;">
        <h3 id="modalProductTitle" style="font-size: 1.3rem; font-weight: 900; color: var(--dark);">إضافة منتج جديد</h3>
        <button onclick="AdminApp.closeModal()" style="background: none; border: none; font-size: 1.4rem; cursor: pointer; color: var(--text-light);">✕</button>
      </div>

      <form id="adminProductForm">
        <div class="form-group">
          <label>اسم المنتج *</label>
          <input type="text" id="prodNameInput" placeholder="مثال: فستان سهرة وردي للأميرات" required>
        </div>

        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px;">
          <div class="form-group">
            <label>القسم / التصنيف *</label>
            <select id="prodCatInput" required>
              <option value="girls">ملابس بناتي</option>
              <option value="boys">ملابس أولادي</option>
              <option value="baby">بيبي ومواليد</option>
              <option value="shoes">أحذية وإكسسوارات</option>
            </select>
          </div>
          <div class="form-group">
            <label>شارة التميز (Badge)</label>
            <input type="text" id="prodBadgeInput" placeholder="الأكثر مبيعاً ⭐، جديد 🚀، خصم خاص ⚡">
          </div>
        </div>

        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px;">
          <div class="form-group">
            <label>السعر بعد الخصم (ر.س) *</label>
            <input type="number" id="prodPriceInput" step="1" placeholder="مثال: 250" required>
          </div>
          <div class="form-group">
            <label>السعر الأصلي قبل الخصم (ر.س)</label>
            <input type="number" id="prodOldPriceInput" step="1" placeholder="مثال: 320">
          </div>
        </div>

        <div class="form-group">
          <label>مسار الصورة أو رابط الصورة (URL) *</label>
          <div style="display: flex; gap: 10px; align-items: center;">
            <input type="text" id="prodImgInput" placeholder="images/prod_girls_party.jpg أو رابط مباشر" oninput="document.getElementById('productImagePreview').src = this.value.startsWith('http') ? this.value : '../' + this.value" required style="flex: 1;">
            <img id="productImagePreview" src="../images/prod_girls_party.jpg" style="width: 50px; height: 50px; border-radius: 6px; object-fit: cover; border: 1px solid #cbd5e1;">
          </div>
        </div>

        <div class="form-group">
          <label>المقاسات المتوفرة (مفصولة بفواصل)</label>
          <input type="text" id="prodSizesInput" placeholder="1-2y, 3-5y, 6-8y">
        </div>

        <div class="form-group">
          <label>وصف المنتج وتفاصيل القماش</label>
          <textarea id="prodDescInput" rows="3" placeholder="اكتب وصفاً مميزاً للمنتج وخاماته وطريقة العناية به..."></textarea>
        </div>

        <div style="display: flex; justify-content: flex-end; gap: 10px; margin-top: 20px;">
          <button type="button" class="btn-admin-pill btn-admin-outline" onclick="AdminApp.closeModal()">إلغاء</button>
          <button type="submit" class="btn-admin-pill btn-admin-primary">حفظ وتحديث المتجر ✅</button>
        </div>
      </form>
    </div>
  </div>

  <script src="../js/store.js"></script>
  <script src="../js/admin.js"></script>
</body>
</html>
"""
    os.makedirs(os.path.join(BASE_DIR, 'admin'), exist_ok=True)
    with open(os.path.join(BASE_DIR, 'admin', 'index.html'), 'w', encoding='utf-8') as f:
        f.write(html)
    print("admin/index.html written successfully!")

if __name__ == '__main__':
    build_index()
    build_shop()
    build_product()
    build_about()
    build_contact()
    build_privacy()
    build_terms()
    build_admin()
    print("ALL 8 HTML PAGES GENERATED SUCCESSFULLY!")
