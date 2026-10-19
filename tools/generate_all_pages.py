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
          <img src="images/kids_hero_banner.jpg" data-cms-src="home.heroImg" alt="تشكيلة بامبينو كيدز الحصرية" style="position: absolute; left: 0; top: 0; width: 55%; height: 100%; object-fit: cover; z-index: 1;">
          <div class="hero-content" style="position: relative; z-index: 2; max-width: 540px; padding: 40px;">
            <span class="hero-tag" data-cms="home.heroBadge" style="background: var(--primary); color: #fff; padding: 5px 14px; border-radius: var(--radius-full); font-size: 0.85rem; font-weight: 800; display: inline-block; margin-bottom: 12px;">🌟 تشكيلة الموسم الجديد 2026</span>
            <h1 class="hero-title" data-cms="home.heroTitle" style="font-size: 2.7rem; font-weight: 900; line-height: 1.25; color: var(--dark); margin-bottom: 16px;">
              أناقة استثنائية تليق بابتسامة طفلك
            </h1>
            <p class="hero-desc" data-cms="home.heroDesc" style="font-size: 1.05rem; color: var(--text); margin-bottom: 26px;">
              اكتشفي تشكيلة الأزياء الفاخرة المصنوعة من القطن العضوي 100% بنعومة فائقة تناسب بشرة أطفالك الرقيقة، من عمر الولادة وحتى 14 سنة.
            </p>
            <div style="display: flex; gap: 14px; flex-wrap: wrap;">
              <a href="shop.html" class="btn-checkout" style="width: auto; padding: 13px 30px;"><span data-cms="home.heroBtnText">تسوقي التشكيلة الآن ✨</span></a>
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
          <div class="feature-icon" data-cms-icon="home.feat1Icon">🚚</div>
          <div class="feature-text">
            <h4 data-cms="home.feat1Title">شحن سريع ومجاني</h4>
            <p data-cms="home.feat1Desc">لكافة مدن المملكة للطلبات فوق 250 ر.س</p>
          </div>
        </div>
        <div class="feature-item">
          <div class="feature-icon" data-cms-icon="home.feat2Icon">🌱</div>
          <div class="feature-text">
            <h4 data-cms="home.feat2Title">قطن طبيعي 100%</h4>
            <p data-cms="home.feat2Desc">أقمشة ناعمة وآمنة لبشرة طفلك الحساسة</p>
          </div>
        </div>
        <div class="feature-item">
          <div class="feature-icon" data-cms-icon="home.feat3Icon">💬</div>
          <div class="feature-text">
            <h4 data-cms="home.feat3Title">طلب سهل عبر واتساب</h4>
            <p data-cms="home.feat3Desc">إتمام فوري للطلب مع خدمة عملاء متفانية</p>
          </div>
        </div>
        <div class="feature-item">
          <div class="feature-icon" data-cms-icon="home.feat4Icon">🔄</div>
          <div class="feature-text">
            <h4 data-cms="home.feat4Title">استبدال ميسر وسريع</h4>
            <p data-cms="home.feat4Desc">سياسة مرنة للاستبدال واسترجاع المقاسات</p>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- CATEGORIES GRID SECTION -->
  <section class="section-padding">
    <div class="container">
      <div class="section-header">
        <span class="section-tag" data-cms="home.catSecTag">أقسام المتجر</span>
        <h2 class="section-title" data-cms="home.catSecTitle">تسوق حسب الفئة</h2>
        <p class="section-desc" data-cms="home.catSecDesc">اختاري ما يناسب طفلك من أرقى التشكيلات المصممة خصيصاً لأناقة يومية ومناسبات مميزة</p>
      </div>

      <div class="categories-grid">
        <!-- Girls -->
        <a href="shop.html?cat=girls" class="category-card">
          <img src="images/kids_cat_girls.jpg" data-cms-src="home.catGirlsImg" alt="ملابس بناتي">
          <div class="category-card-overlay">
            <h3 class="category-card-title">ملابس بناتي</h3>
            <span class="category-card-link">استكشف التشكيلة ←</span>
          </div>
        </a>

        <!-- Boys -->
        <a href="shop.html?cat=boys" class="category-card">
          <img src="images/kids_cat_boys.jpg" data-cms-src="home.catBoysImg" alt="ملابس أولادي">
          <div class="category-card-overlay">
            <h3 class="category-card-title">ملابس أولادي</h3>
            <span class="category-card-link">استكشف التشكيلة ←</span>
          </div>
        </a>

        <!-- Baby -->
        <a href="shop.html?cat=baby" class="category-card">
          <img src="images/kids_cat_baby.jpg" data-cms-src="home.catBabyImg" alt="بيبي ومواليد">
          <div class="category-card-overlay">
            <h3 class="category-card-title">بيبي ومواليد</h3>
            <span class="category-card-link">استكشف التشكيلة ←</span>
          </div>
        </a>

        <!-- Shoes & Accessories -->
        <a href="shop.html?cat=shoes" class="category-card">
          <img src="images/kids_cat_shoes.jpg" data-cms-src="home.catShoesImg" alt="أحذية وإكسسوارات">
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
        <span class="flash-tag" data-cms="home.flashTag">⚡ عروض حصرية لفترة محدودة</span>
        <h2 class="flash-title" data-cms="home.flashTitle">خصومات حتى 40% على تشكيلة الصيف</h2>
        <p class="flash-desc" data-cms="home.flashDesc">اغتنمي الفرصة ووفري الكثير على أجمل الفساتين والأطقم الفاخرة لأطفالك. ينتهي العرض قريباً!</p>
        
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
        <img src="images/flash_deal_kids_banner.jpg" data-cms-src="home.flashImg" alt="عروض بامبينو كيدز" style="border-radius: var(--radius-md); box-shadow: var(--shadow-md);">
      </div>
    </div>
  </section>

  <!-- FEATURED PRODUCTS GRID -->
  <section class="section-padding" style="background: var(--bg-soft);">
    <div class="container">
      <div class="section-header">
        <span class="section-tag" data-cms="home.prodSecTag">أحدث القطع</span>
        <h2 class="section-title" data-cms="home.prodSecTitle">المختارات الأكثر طلباً</h2>
        <p class="section-desc" data-cms="home.prodSecDesc">قطع مختارة بعناية تجمع بين الأناقة الراقية والراحة الفائقة لطفلك</p>
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
      <span style="color: var(--secondary); font-weight: 800; font-size: 0.9rem; letter-spacing: 1px;" data-cms="home.vipTag">نادي أمهات بامبينو 👑</span>
      <h2 class="vip-title" data-cms="home.vipTitle">انضمي لنادي الأمهات واحصلي على خصم 15%</h2>
      <p class="vip-desc" data-cms="home.vipDesc">سجلي بريدك الإلكتروني ليصلك كل جديد في عالم أزياء الأطفال، ودعوات حصرية لخصومات المواسم قبل الجميع.</p>
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
# 2. ABOUT.HTML
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
      <h1 class="page-hero-title" data-cms="about.heroTitle">من نحن - قصة بامبينو كيدز</h1>
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
          <span class="section-tag" data-cms="about.storyTag">شغف بالأناقة والراحة</span>
          <h2 data-cms="about.storyTitle">أزياء راقية تُصنع بحب لأجمل لحظات الطفولة</h2>
          <p data-cms="about.storyP1">
            تأسست علامة بامبينو كيدز (BAMBINO KIDS) انطلاقاً من إيماننا العميق بأن أطفالنا يستحقون الأفضل دائماً. نحن ندرك أن ملابس الأطفال ليست مجرد مظهر أنيق، بل هي راحة يومية وحرية حركة وأمان تام على بشرتهم الغضة.
          </p>
          <p data-cms="about.storyP2">
            منذ اليوم الأول، وضعنا معايير صارمة في انتقاء خامات القطن العضوي النقي 100% والتصاميم الراقية المستوحاة من أحدث صيحات الموضة الأوروبية والعالمية، لنقدم للأمهات تشكيلات تلبي طموحاتهن في إطلالات استثنائية لأطفالهن في جميع المناسبات.
          </p>
        </div>
        <div>
          <img src="images/hero_kids_slide_2.jpg" data-cms-src="about.storyImg" alt="أطفال بامبينو كيدز" style="border-radius: var(--radius-lg); box-shadow: var(--shadow-md);">
        </div>
      </div>

      <div class="features-grid" style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 24px; margin: 40px 0;">
        <div style="background: var(--bg-soft); padding: 26px; border-radius: var(--radius-md); border-right: 4px solid var(--primary);">
          <div style="font-size: 2.2rem; margin-bottom: 10px;" data-cms-icon="about.card1Icon">🌟</div>
          <h3 style="font-size: 1.2rem; font-weight: 800; color: var(--dark); margin-bottom: 8px;" data-cms="about.card1Title">جودة لا تقبل المساومة</h3>
          <p style="font-size: 0.95rem; color: var(--text-light);" data-cms="about.card1Desc">نختار بعناية فائقة أنعم أنواع الخيوط القطنية وأدق تفاصيل الحياكة لضمان متانة القطعة بعد كل غسيل.</p>
        </div>

        <div style="background: var(--bg-soft); padding: 26px; border-radius: var(--radius-md); border-right: 4px solid var(--primary);">
          <div style="font-size: 2.2rem; margin-bottom: 10px;" data-cms-icon="about.card2Icon">👶</div>
          <h3 style="font-size: 1.2rem; font-weight: 800; color: var(--dark); margin-bottom: 8px;" data-cms="about.card2Title">أمان وراحة تامة</h3>
          <p style="font-size: 0.95rem; color: var(--text-light);" data-cms="about.card2Desc">جميع أصباغنا وأزرارنا وإكسسواراتنا معتمدة وخالية من المواد الكيميائية الضارة لسلامة طفلك التامة.</p>
        </div>

        <div style="background: var(--bg-soft); padding: 26px; border-radius: var(--radius-md); border-right: 4px solid var(--primary);">
          <div style="font-size: 2.2rem; margin-bottom: 10px;" data-cms-icon="about.card3Icon">❤️</div>
          <h3 style="font-size: 1.2rem; font-weight: 800; color: var(--dark); margin-bottom: 8px;" data-cms="about.card3Title">خدمة أمهات استثنائية</h3>
          <p style="font-size: 0.95rem; color: var(--text-light);" data-cms="about.card3Desc">فريقنا يتفهم متطلبات المقاسات ويسعد دائماً بتقديم المشورة وتيسير الشحن والاستبدال بكل رحابة صدر.</p>
        </div>
      </div>

      <h2 data-cms="about.missionTitle">رسالتنا</h2>
      <p data-cms="about.missionText">
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
# 3. ADMIN/INDEX.HTML (WITH COMPLETE MEDIA & IMAGES CMS)
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
      <p style="color: var(--text-light); font-size: 0.9rem; margin-bottom: 24px;">يرجى إدخال رمز الأمان (PIN) لتعديل المتجر وإدارة المنتجات والصفحات والصور</p>

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
        <div class="admin-nav-item" data-tab="pages">
          <span>📄</span>
          <span>محتوى وتعديل الصفحات</span>
        </div>
        <div class="admin-nav-item" data-tab="settings">
          <span>⚙️</span>
          <span>إعدادات المتجر</span>
        </div>
        <div class="admin-nav-item" data-tab="backup">
          <span>💾</span>
          <span>النسخ الاحتياطي الشامل</span>
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

        <!-- TAB 2: PAGES & MEDIA CMS -->
        <div class="admin-tab-content" id="tab-pages">
          <div class="admin-card">
            <div class="admin-card-header">
              <div>
                <h3>محرر محتوى وصور صفحات المتجر (Visual Page CMS)</h3>
                <p style="color: var(--text-light); font-size: 0.88rem; margin-top: 4px;">
                  يمكنك تعديل أي نص، تبديل أي بانر أو صورة، وتغيير الأيقونات في أي صفحة مع إمكانية رفع الصور مباشرة من جهازك!
                </p>
              </div>
            </div>

            <!-- Page Switcher Cards -->
            <div class="cms-pages-grid">
              <div class="cms-page-card active" data-page="home" onclick="AdminApp.selectPage('home')">
                <div class="cms-page-card-icon">🏠</div>
                <div>
                  <div class="cms-page-card-title">الصفحة الرئيسية</div>
                  <div class="cms-page-card-sub">السلايدر، البانرات، الصور، الميزات</div>
                </div>
              </div>

              <div class="cms-page-card" data-page="about" onclick="AdminApp.selectPage('about')">
                <div class="cms-page-card-icon">✨</div>
                <div>
                  <div class="cms-page-card-title">صفحة من نحن</div>
                  <div class="cms-page-card-sub">القصة، صورة البراند، الجودة</div>
                </div>
              </div>

              <div class="cms-page-card" data-page="contact" onclick="AdminApp.selectPage('contact')">
                <div class="cms-page-card-icon">📞</div>
                <div>
                  <div class="cms-page-card-title">صفحة اتصل بنا</div>
                  <div class="cms-page-card-sub">عناوين ونصوص التواصل</div>
                </div>
              </div>

              <div class="cms-page-card" data-page="terms" onclick="AdminApp.selectPage('terms')">
                <div class="cms-page-card-icon">📋</div>
                <div>
                  <div class="cms-page-card-title">الشروط والأحكام</div>
                  <div class="cms-page-card-sub">شروط الطلب وسياسة الاسترجاع</div>
                </div>
              </div>

              <div class="cms-page-card" data-page="privacy" onclick="AdminApp.selectPage('privacy')">
                <div class="cms-page-card-icon">🔒</div>
                <div>
                  <div class="cms-page-card-title">سياسة الخصوصية</div>
                  <div class="cms-page-card-sub">بنود حماية بيانات العملاء</div>
                </div>
              </div>

              <div class="cms-page-card" data-page="footer" onclick="AdminApp.selectPage('footer')">
                <div class="cms-page-card-icon">🔻</div>
                <div>
                  <div class="cms-page-card-title">الفوتر العام</div>
                  <div class="cms-page-card-sub">نبذة الفوتر وحقوق النشر</div>
                </div>
              </div>
            </div>

            <!-- EDIT FORMS FOR EACH PAGE -->
            <div id="cmsFormsContainer">

              <!-- HOME PAGE FORM -->
              <div class="cms-page-form-wrapper" id="cmsForm-home">
                
                <!-- 1. BANNERS & IMAGES FOR HOMEPAGE -->
                <div class="cms-section-group" style="border: 2px solid #fecdd3; background: #fffdfd;">
                  <h4 style="color: var(--primary);">🖼️ بانرات وصور الصفحة الرئيسية (Banners & Media)</h4>
                  
                  <!-- Hero Banner Image -->
                  <div class="form-group" style="background: #fff; padding: 14px; border-radius: var(--radius-sm); border: 1px solid var(--border-light); margin-bottom: 16px;">
                    <label style="font-weight: 800; color: var(--dark);">صورة البانر الرئيسي الكبير (Hero Slider Banner)</label>
                    <div style="display: flex; gap: 14px; align-items: center; margin-top: 8px;">
                      <img id="prev_home_heroImg" src="../images/kids_hero_banner.jpg" style="width: 100px; height: 70px; object-fit: cover; border-radius: 8px; border: 1px solid #cbd5e1;">
                      <div style="flex: 1;">
                        <input type="text" id="cms_home_heroImg" data-cms-field="heroImg" placeholder="images/kids_hero_banner.jpg أو رابط مباشر" oninput="AdminApp.updateImagePreview(this.value, 'prev_home_heroImg')" style="width: 100%; margin-bottom: 6px;">
                        <input type="file" accept="image/*" onchange="AdminApp.handleImageUpload(event, 'cms_home_heroImg', 'prev_home_heroImg')" style="display: none;" id="upload_home_heroImg">
                        <button type="button" class="btn-admin-pill btn-admin-outline" onclick="document.getElementById('upload_home_heroImg').click()">📁 رفع صورة من جهازك</button>
                      </div>
                    </div>
                  </div>

                  <!-- Flash Deal Banner Image -->
                  <div class="form-group" style="background: #fff; padding: 14px; border-radius: var(--radius-sm); border: 1px solid var(--border-light); margin-bottom: 16px;">
                    <label style="font-weight: 800; color: var(--dark);">صورة بانر العروض الخاطفة (Flash Deals Banner)</label>
                    <div style="display: flex; gap: 14px; align-items: center; margin-top: 8px;">
                      <img id="prev_home_flashImg" src="../images/flash_deal_kids_banner.jpg" style="width: 100px; height: 70px; object-fit: cover; border-radius: 8px; border: 1px solid #cbd5e1;">
                      <div style="flex: 1;">
                        <input type="text" id="cms_home_flashImg" data-cms-field="flashImg" placeholder="images/flash_deal_kids_banner.jpg أو رابط مباشر" oninput="AdminApp.updateImagePreview(this.value, 'prev_home_flashImg')" style="width: 100%; margin-bottom: 6px;">
                        <input type="file" accept="image/*" onchange="AdminApp.handleImageUpload(event, 'cms_home_flashImg', 'prev_home_flashImg')" style="display: none;" id="upload_home_flashImg">
                        <button type="button" class="btn-admin-pill btn-admin-outline" onclick="document.getElementById('upload_home_flashImg').click()">📁 رفع صورة من جهازك</button>
                      </div>
                    </div>
                  </div>

                  <!-- 4 Category Cards Images -->
                  <label style="font-weight: 800; display: block; margin-bottom: 10px; color: var(--dark);">صور بطاقات أقسام المتجر (Categories Cards):</label>
                  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 14px;">
                    
                    <!-- Cat Girls -->
                    <div style="background: #fff; padding: 12px; border-radius: var(--radius-sm); border: 1px solid var(--border-light);">
                      <label style="font-size: 0.85rem; font-weight: 700;">صورة قسم (ملابس بناتي)</label>
                      <div style="display: flex; gap: 10px; align-items: center; margin-top: 6px;">
                        <img id="prev_home_catGirlsImg" src="../images/kids_cat_girls.jpg" style="width: 55px; height: 55px; object-fit: cover; border-radius: 6px; border: 1px solid #cbd5e1;">
                        <div style="flex: 1;">
                          <input type="text" id="cms_home_catGirlsImg" data-cms-field="catGirlsImg" oninput="AdminApp.updateImagePreview(this.value, 'prev_home_catGirlsImg')" style="width: 100%; font-size: 0.8rem; margin-bottom: 4px;">
                          <input type="file" accept="image/*" onchange="AdminApp.handleImageUpload(event, 'cms_home_catGirlsImg', 'prev_home_catGirlsImg')" style="display: none;" id="upload_home_catGirlsImg">
                          <button type="button" class="btn-admin-pill btn-admin-outline" style="padding: 4px 10px; font-size: 0.75rem;" onclick="document.getElementById('upload_home_catGirlsImg').click()">📁 رفع صورة</button>
                        </div>
                      </div>
                    </div>

                    <!-- Cat Boys -->
                    <div style="background: #fff; padding: 12px; border-radius: var(--radius-sm); border: 1px solid var(--border-light);">
                      <label style="font-size: 0.85rem; font-weight: 700;">صورة قسم (ملابس أولادي)</label>
                      <div style="display: flex; gap: 10px; align-items: center; margin-top: 6px;">
                        <img id="prev_home_catBoysImg" src="../images/kids_cat_boys.jpg" style="width: 55px; height: 55px; object-fit: cover; border-radius: 6px; border: 1px solid #cbd5e1;">
                        <div style="flex: 1;">
                          <input type="text" id="cms_home_catBoysImg" data-cms-field="catBoysImg" oninput="AdminApp.updateImagePreview(this.value, 'prev_home_catBoysImg')" style="width: 100%; font-size: 0.8rem; margin-bottom: 4px;">
                          <input type="file" accept="image/*" onchange="AdminApp.handleImageUpload(event, 'cms_home_catBoysImg', 'prev_home_catBoysImg')" style="display: none;" id="upload_home_catBoysImg">
                          <button type="button" class="btn-admin-pill btn-admin-outline" style="padding: 4px 10px; font-size: 0.75rem;" onclick="document.getElementById('upload_home_catBoysImg').click()">📁 رفع صورة</button>
                        </div>
                      </div>
                    </div>

                    <!-- Cat Baby -->
                    <div style="background: #fff; padding: 12px; border-radius: var(--radius-sm); border: 1px solid var(--border-light);">
                      <label style="font-size: 0.85rem; font-weight: 700;">صورة قسم (بيبي ومواليد)</label>
                      <div style="display: flex; gap: 10px; align-items: center; margin-top: 6px;">
                        <img id="prev_home_catBabyImg" src="../images/kids_cat_baby.jpg" style="width: 55px; height: 55px; object-fit: cover; border-radius: 6px; border: 1px solid #cbd5e1;">
                        <div style="flex: 1;">
                          <input type="text" id="cms_home_catBabyImg" data-cms-field="catBabyImg" oninput="AdminApp.updateImagePreview(this.value, 'prev_home_catBabyImg')" style="width: 100%; font-size: 0.8rem; margin-bottom: 4px;">
                          <input type="file" accept="image/*" onchange="AdminApp.handleImageUpload(event, 'cms_home_catBabyImg', 'prev_home_catBabyImg')" style="display: none;" id="upload_home_catBabyImg">
                          <button type="button" class="btn-admin-pill btn-admin-outline" style="padding: 4px 10px; font-size: 0.75rem;" onclick="document.getElementById('upload_home_catBabyImg').click()">📁 رفع صورة</button>
                        </div>
                      </div>
                    </div>

                    <!-- Cat Shoes -->
                    <div style="background: #fff; padding: 12px; border-radius: var(--radius-sm); border: 1px solid var(--border-light);">
                      <label style="font-size: 0.85rem; font-weight: 700;">صورة قسم (أحذية وإكسسوارات)</label>
                      <div style="display: flex; gap: 10px; align-items: center; margin-top: 6px;">
                        <img id="prev_home_catShoesImg" src="../images/kids_cat_shoes.jpg" style="width: 55px; height: 55px; object-fit: cover; border-radius: 6px; border: 1px solid #cbd5e1;">
                        <div style="flex: 1;">
                          <input type="text" id="cms_home_catShoesImg" data-cms-field="catShoesImg" oninput="AdminApp.updateImagePreview(this.value, 'prev_home_catShoesImg')" style="width: 100%; font-size: 0.8rem; margin-bottom: 4px;">
                          <input type="file" accept="image/*" onchange="AdminApp.handleImageUpload(event, 'cms_home_catShoesImg', 'prev_home_catShoesImg')" style="display: none;" id="upload_home_catShoesImg">
                          <button type="button" class="btn-admin-pill btn-admin-outline" style="padding: 4px 10px; font-size: 0.75rem;" onclick="document.getElementById('upload_home_catShoesImg').click()">📁 رفع صورة</button>
                        </div>
                      </div>
                    </div>

                  </div>
                </div>

                <!-- 2. TEXTS & SECTIONS FOR HOMEPAGE -->
                <div class="cms-section-group">
                  <h4>🎨 نصوص البانر الرئيسي (Hero Texts)</h4>
                  <div class="form-group">
                    <label>الشارة العلوية للبانر</label>
                    <input type="text" id="cms_home_heroBadge" data-cms-field="heroBadge">
                  </div>
                  <div class="form-group">
                    <label>العنوان الرئيسي الكبير</label>
                    <input type="text" id="cms_home_heroTitle" data-cms-field="heroTitle">
                  </div>
                  <div class="form-group">
                    <label>النص الوصفي للبانر</label>
                    <textarea id="cms_home_heroDesc" data-cms-field="heroDesc" rows="2"></textarea>
                  </div>
                  <div class="form-group">
                    <label>نص زر التسوق الرئيسي</label>
                    <input type="text" id="cms_home_heroBtnText" data-cms-field="heroBtnText">
                  </div>
                </div>

                <!-- 3. FEATURES BAR -->
                <div class="cms-section-group">
                  <h4>🚚 ميزات وأيقونات المتجر الأربعة (Features & Icons)</h4>
                  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 14px;">
                    <div class="form-group">
                      <div style="display: flex; gap: 8px;">
                        <div style="width: 60px;">
                          <label>أيقونة 1</label>
                          <input type="text" id="cms_home_feat1Icon" data-cms-field="feat1Icon" style="text-align: center; font-size: 1.2rem;">
                        </div>
                        <div style="flex: 1;">
                          <label>عنوان الميزة 1</label>
                          <input type="text" id="cms_home_feat1Title" data-cms-field="feat1Title">
                        </div>
                      </div>
                      <label style="font-size:0.8rem; color:#64748b; margin-top:4px;">وصف الميزة 1</label>
                      <input type="text" id="cms_home_feat1Desc" data-cms-field="feat1Desc">
                    </div>

                    <div class="form-group">
                      <div style="display: flex; gap: 8px;">
                        <div style="width: 60px;">
                          <label>أيقونة 2</label>
                          <input type="text" id="cms_home_feat2Icon" data-cms-field="feat2Icon" style="text-align: center; font-size: 1.2rem;">
                        </div>
                        <div style="flex: 1;">
                          <label>عنوان الميزة 2</label>
                          <input type="text" id="cms_home_feat2Title" data-cms-field="feat2Title">
                        </div>
                      </div>
                      <label style="font-size:0.8rem; color:#64748b; margin-top:4px;">وصف الميزة 2</label>
                      <input type="text" id="cms_home_feat2Desc" data-cms-field="feat2Desc">
                    </div>

                    <div class="form-group">
                      <div style="display: flex; gap: 8px;">
                        <div style="width: 60px;">
                          <label>أيقونة 3</label>
                          <input type="text" id="cms_home_feat3Icon" data-cms-field="feat3Icon" style="text-align: center; font-size: 1.2rem;">
                        </div>
                        <div style="flex: 1;">
                          <label>عنوان الميزة 3</label>
                          <input type="text" id="cms_home_feat3Title" data-cms-field="feat3Title">
                        </div>
                      </div>
                      <label style="font-size:0.8rem; color:#64748b; margin-top:4px;">وصف الميزة 3</label>
                      <input type="text" id="cms_home_feat3Desc" data-cms-field="feat3Desc">
                    </div>

                    <div class="form-group">
                      <div style="display: flex; gap: 8px;">
                        <div style="width: 60px;">
                          <label>أيقونة 4</label>
                          <input type="text" id="cms_home_feat4Icon" data-cms-field="feat4Icon" style="text-align: center; font-size: 1.2rem;">
                        </div>
                        <div style="flex: 1;">
                          <label>عنوان الميزة 4</label>
                          <input type="text" id="cms_home_feat4Title" data-cms-field="feat4Title">
                        </div>
                      </div>
                      <label style="font-size:0.8rem; color:#64748b; margin-top:4px;">وصف الميزة 4</label>
                      <input type="text" id="cms_home_feat4Desc" data-cms-field="feat4Desc">
                    </div>
                  </div>
                </div>

                <!-- 4. FLASH DEALS TEXTS -->
                <div class="cms-section-group">
                  <h4>⚡ نصوص الخصومات الخاطفة (Flash Deals)</h4>
                  <div class="form-group">
                    <label>شارة العرض</label>
                    <input type="text" id="cms_home_flashTag" data-cms-field="flashTag">
                  </div>
                  <div class="form-group">
                    <label>عنوان العرض الكبير</label>
                    <input type="text" id="cms_home_flashTitle" data-cms-field="flashTitle">
                  </div>
                  <div class="form-group">
                    <label>وصف العرض</label>
                    <textarea id="cms_home_flashDesc" data-cms-field="flashDesc" rows="2"></textarea>
                  </div>
                </div>

                <!-- 5. VIP CLUB -->
                <div class="cms-section-group">
                  <h4>👑 قسم نادي أمهات بامبينو (VIP Club)</h4>
                  <div class="form-group">
                    <label>شارة نادي الأمهات</label>
                    <input type="text" id="cms_home_vipTag" data-cms-field="vipTag">
                  </div>
                  <div class="form-group">
                    <label>عنوان النادي</label>
                    <input type="text" id="cms_home_vipTitle" data-cms-field="vipTitle">
                  </div>
                  <div class="form-group">
                    <label>النص التشجيعي للاشتراك</label>
                    <textarea id="cms_home_vipDesc" data-cms-field="vipDesc" rows="2"></textarea>
                  </div>
                </div>

                <div style="display: flex; gap: 12px; margin-top: 20px;">
                  <button type="button" class="btn-checkout" style="width: auto; padding: 12px 28px;" onclick="AdminApp.saveCurrentPage('home')">حفظ تعديلات وصور الصفحة الرئيسية ✅</button>
                  <button type="button" class="btn-admin-pill btn-admin-outline" onclick="AdminApp.previewPage('home')">معاينة مباشرة للصفحة 👁️</button>
                  <button type="button" class="btn-admin-pill btn-admin-danger" onclick="AdminApp.resetCurrentPage('home')">استعادة النصوص والصور الأصلية 🔄</button>
                </div>
              </div>

              <!-- ABOUT PAGE FORM -->
              <div class="cms-page-form-wrapper" id="cmsForm-about" style="display: none;">
                
                <!-- About Story Image -->
                <div class="cms-section-group" style="border: 2px solid #fecdd3; background: #fffdfd;">
                  <h4 style="color: var(--primary);">🖼️ صورة قصة المتجر (About Brand Image)</h4>
                  <div class="form-group" style="background: #fff; padding: 14px; border-radius: var(--radius-sm); border: 1px solid var(--border-light);">
                    <div style="display: flex; gap: 14px; align-items: center;">
                      <img id="prev_about_storyImg" src="../images/hero_kids_slide_2.jpg" style="width: 100px; height: 70px; object-fit: cover; border-radius: 8px; border: 1px solid #cbd5e1;">
                      <div style="flex: 1;">
                        <input type="text" id="cms_about_storyImg" data-cms-field="storyImg" placeholder="images/hero_kids_slide_2.jpg أو رابط مباشر" oninput="AdminApp.updateImagePreview(this.value, 'prev_about_storyImg')" style="width: 100%; margin-bottom: 6px;">
                        <input type="file" accept="image/*" onchange="AdminApp.handleImageUpload(event, 'cms_about_storyImg', 'prev_about_storyImg')" style="display: none;" id="upload_about_storyImg">
                        <button type="button" class="btn-admin-pill btn-admin-outline" onclick="document.getElementById('upload_about_storyImg').click()">📁 رفع صورة من جهازك</button>
                      </div>
                    </div>
                  </div>
                </div>

                <div class="cms-section-group">
                  <h4>📖 قصة العلامة التجارية (Brand Story)</h4>
                  <div class="form-group">
                    <label>عنوان هيدر الصفحة</label>
                    <input type="text" id="cms_about_heroTitle" data-cms-field="heroTitle">
                  </div>
                  <div class="form-group">
                    <label>شارة القصة</label>
                    <input type="text" id="cms_about_storyTag" data-cms-field="storyTag">
                  </div>
                  <div class="form-group">
                    <label>عنوان القصة الرئيسي</label>
                    <input type="text" id="cms_about_storyTitle" data-cms-field="storyTitle">
                  </div>
                  <div class="form-group">
                    <label>الفقرة الأولى من القصة</label>
                    <textarea id="cms_about_storyP1" data-cms-field="storyP1" rows="3"></textarea>
                  </div>
                  <div class="form-group">
                    <label>الفقرة الثانية من القصة</label>
                    <textarea id="cms_about_storyP2" data-cms-field="storyP2" rows="3"></textarea>
                  </div>
                </div>

                <div class="cms-section-group">
                  <h4>🌟 بطاقات وأيقونات مميزات الجودة الثلاثة</h4>
                  <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 14px;">
                    <div class="form-group">
                      <label>أيقونة 1</label>
                      <input type="text" id="cms_about_card1Icon" data-cms-field="card1Icon" style="text-align: center; font-size: 1.2rem; width: 60px; margin-bottom: 6px;">
                      <label>عنوان البطاقة 1</label>
                      <input type="text" id="cms_about_card1Title" data-cms-field="card1Title">
                      <label style="font-size:0.8rem; color:#64748b; margin-top:4px;">وصف البطاقة 1</label>
                      <textarea id="cms_about_card1Desc" data-cms-field="card1Desc" rows="2"></textarea>
                    </div>
                    <div class="form-group">
                      <label>أيقونة 2</label>
                      <input type="text" id="cms_about_card2Icon" data-cms-field="card2Icon" style="text-align: center; font-size: 1.2rem; width: 60px; margin-bottom: 6px;">
                      <label>عنوان البطاقة 2</label>
                      <input type="text" id="cms_about_card2Title" data-cms-field="card2Title">
                      <label style="font-size:0.8rem; color:#64748b; margin-top:4px;">وصف البطاقة 2</label>
                      <textarea id="cms_about_card2Desc" data-cms-field="card2Desc" rows="2"></textarea>
                    </div>
                    <div class="form-group">
                      <label>أيقونة 3</label>
                      <input type="text" id="cms_about_card3Icon" data-cms-field="card3Icon" style="text-align: center; font-size: 1.2rem; width: 60px; margin-bottom: 6px;">
                      <label>عنوان البطاقة 3</label>
                      <input type="text" id="cms_about_card3Title" data-cms-field="card3Title">
                      <label style="font-size:0.8rem; color:#64748b; margin-top:4px;">وصف البطاقة 3</label>
                      <textarea id="cms_about_card3Desc" data-cms-field="card3Desc" rows="2"></textarea>
                    </div>
                  </div>
                </div>

                <div class="cms-section-group">
                  <h4>🎯 رسالة المتجر</h4>
                  <div class="form-group">
                    <label>عنوان الرسالة</label>
                    <input type="text" id="cms_about_missionTitle" data-cms-field="missionTitle">
                  </div>
                  <div class="form-group">
                    <label>نص الرسالة</label>
                    <textarea id="cms_about_missionText" data-cms-field="missionText" rows="3"></textarea>
                  </div>
                </div>

                <div style="display: flex; gap: 12px; margin-top: 20px;">
                  <button type="button" class="btn-checkout" style="width: auto; padding: 12px 28px;" onclick="AdminApp.saveCurrentPage('about')">حفظ تعديلات صفحة من نحن ✅</button>
                  <button type="button" class="btn-admin-pill btn-admin-outline" onclick="AdminApp.previewPage('about')">معاينة صفحة من نحن 👁️</button>
                  <button type="button" class="btn-admin-pill btn-admin-danger" onclick="AdminApp.resetCurrentPage('about')">استعادة النصوص والصور الأصلية 🔄</button>
                </div>
              </div>

              <!-- CONTACT PAGE FORM -->
              <div class="cms-page-form-wrapper" id="cmsForm-contact" style="display: none;">
                <div class="cms-section-group">
                  <h4>📞 نصوص ومعلومات التواصل</h4>
                  <div class="form-group">
                    <label>عنوان هيدر الصفحة</label>
                    <input type="text" id="cms_contact_heroTitle" data-cms-field="heroTitle">
                  </div>
                  <div class="form-group">
                    <label>شارة قسم التواصل</label>
                    <input type="text" id="cms_contact_secTag" data-cms-field="secTag">
                  </div>
                  <div class="form-group">
                    <label>عنوان قنوات التواصل</label>
                    <input type="text" id="cms_contact_secTitle" data-cms-field="secTitle">
                  </div>
                  <div class="form-group">
                    <label>الوصف التمهيدي لخدمة العملاء</label>
                    <textarea id="cms_contact_secDesc" data-cms-field="secDesc" rows="2"></textarea>
                  </div>
                  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 14px;">
                    <div class="form-group">
                      <label>عنوان واتساب</label>
                      <input type="text" id="cms_contact_waTitle" data-cms-field="waTitle">
                      <label style="font-size:0.8rem; color:#64748b; margin-top:4px;">وصف رد واتساب</label>
                      <input type="text" id="cms_contact_waDesc" data-cms-field="waDesc">
                    </div>
                    <div class="form-group">
                      <label>عنوان الهاتف</label>
                      <input type="text" id="cms_contact_phoneTitle" data-cms-field="phoneTitle">
                      <label style="font-size:0.8rem; color:#64748b; margin-top:4px;">أوقات عمل الهاتف</label>
                      <input type="text" id="cms_contact_phoneDesc" data-cms-field="phoneDesc">
                    </div>
                  </div>
                </div>

                <div style="display: flex; gap: 12px; margin-top: 20px;">
                  <button type="button" class="btn-checkout" style="width: auto; padding: 12px 28px;" onclick="AdminApp.saveCurrentPage('contact')">حفظ تعديلات صفحة اتصل بنا ✅</button>
                  <button type="button" class="btn-admin-pill btn-admin-outline" onclick="AdminApp.previewPage('contact')">معاينة صفحة اتصل بنا 👁️</button>
                  <button type="button" class="btn-admin-pill btn-admin-danger" onclick="AdminApp.resetCurrentPage('contact')">استعادة النصوص الأصلية 🔄</button>
                </div>
              </div>

              <!-- TERMS PAGE FORM -->
              <div class="cms-page-form-wrapper" id="cmsForm-terms" style="display: none;">
                <div class="cms-section-group">
                  <h4>📋 بنود الشروط والأحكام</h4>
                  <div class="form-group">
                    <label>عنوان الصفحة الرئيسي</label>
                    <input type="text" id="cms_terms_heroTitle" data-cms-field="heroTitle">
                  </div>
                  <div class="form-group">
                    <label>المقدمة التمهيدية</label>
                    <textarea id="cms_terms_intro" data-cms-field="intro" rows="2"></textarea>
                  </div>
                  <div class="form-group">
                    <label>عنوان البند 1 (الطلب والأسعار)</label>
                    <input type="text" id="cms_terms_sec1Title" data-cms-field="sec1Title">
                    <label style="font-size:0.8rem; color:#64748b; margin-top:4px;">تفاصيل البند 1</label>
                    <textarea id="cms_terms_sec1Desc" data-cms-field="sec1Desc" rows="2"></textarea>
                  </div>
                  <div class="form-group">
                    <label>عنوان البند 2 (الشحن والتوصيل)</label>
                    <input type="text" id="cms_terms_sec2Title" data-cms-field="sec2Title">
                    <label style="font-size:0.8rem; color:#64748b; margin-top:4px;">تفاصيل البند 2</label>
                    <textarea id="cms_terms_sec2Desc" data-cms-field="sec2Desc" rows="2"></textarea>
                  </div>
                  <div class="form-group">
                    <label>عنوان البند 3 (الاستبدال والاسترجاع)</label>
                    <input type="text" id="cms_terms_sec3Title" data-cms-field="sec3Title">
                    <label style="font-size:0.8rem; color:#64748b; margin-top:4px;">تفاصيل البند 3</label>
                    <textarea id="cms_terms_sec3Desc" data-cms-field="sec3Desc" rows="2"></textarea>
                  </div>
                </div>

                <div style="display: flex; gap: 12px; margin-top: 20px;">
                  <button type="button" class="btn-checkout" style="width: auto; padding: 12px 28px;" onclick="AdminApp.saveCurrentPage('terms')">حفظ تعديلات الشروط والأحكام ✅</button>
                  <button type="button" class="btn-admin-pill btn-admin-outline" onclick="AdminApp.previewPage('terms')">معاينة صفحة الشروط 👁️</button>
                  <button type="button" class="btn-admin-pill btn-admin-danger" onclick="AdminApp.resetCurrentPage('terms')">استعادة النصوص الأصلية 🔄</button>
                </div>
              </div>

              <!-- PRIVACY PAGE FORM -->
              <div class="cms-page-form-wrapper" id="cmsForm-privacy" style="display: none;">
                <div class="cms-section-group">
                  <h4>🔒 بنود سياسة الخصوصية</h4>
                  <div class="form-group">
                    <label>عنوان الصفحة الرئيسي</label>
                    <input type="text" id="cms_privacy_heroTitle" data-cms-field="heroTitle">
                  </div>
                  <div class="form-group">
                    <label>المقدمة التمهيدية</label>
                    <textarea id="cms_privacy_intro" data-cms-field="intro" rows="2"></textarea>
                  </div>
                  <div class="form-group">
                    <label>عنوان البند 1</label>
                    <input type="text" id="cms_privacy_sec1Title" data-cms-field="sec1Title">
                    <label style="font-size:0.8rem; color:#64748b; margin-top:4px;">تفاصيل البند 1</label>
                    <textarea id="cms_privacy_sec1Desc" data-cms-field="sec1Desc" rows="2"></textarea>
                  </div>
                  <div class="form-group">
                    <label>عنوان البند 2</label>
                    <input type="text" id="cms_privacy_sec2Title" data-cms-field="sec2Title">
                    <label style="font-size:0.8rem; color:#64748b; margin-top:4px;">تفاصيل البند 2</label>
                    <textarea id="cms_privacy_sec2Desc" data-cms-field="sec2Desc" rows="2"></textarea>
                  </div>
                  <div class="form-group">
                    <label>عنوان البند 3</label>
                    <input type="text" id="cms_privacy_sec3Title" data-cms-field="sec3Title">
                    <label style="font-size:0.8rem; color:#64748b; margin-top:4px;">تفاصيل البند 3</label>
                    <textarea id="cms_privacy_sec3Desc" data-cms-field="sec3Desc" rows="2"></textarea>
                  </div>
                </div>

                <div style="display: flex; gap: 12px; margin-top: 20px;">
                  <button type="button" class="btn-checkout" style="width: auto; padding: 12px 28px;" onclick="AdminApp.saveCurrentPage('privacy')">حفظ تعديلات سياسة الخصوصية ✅</button>
                  <button type="button" class="btn-admin-pill btn-admin-outline" onclick="AdminApp.previewPage('privacy')">معاينة صفحة الخصوصية 👁️</button>
                  <button type="button" class="btn-admin-pill btn-admin-danger" onclick="AdminApp.resetCurrentPage('privacy')">استعادة النصوص الأصلية 🔄</button>
                </div>
              </div>

              <!-- FOOTER FORM -->
              <div class="cms-page-form-wrapper" id="cmsForm-footer" style="display: none;">
                <div class="cms-section-group">
                  <h4>🔻 نبذة الفوتر وحقوق النشر</h4>
                  <div class="form-group">
                    <label>النبذة التعريفية في الفوتر</label>
                    <textarea id="cms_footer_aboutText" data-cms-field="aboutText" rows="3"></textarea>
                  </div>
                  <div class="form-group">
                    <label>نص حقوق النشر والملكية (Copyright)</label>
                    <input type="text" id="cms_footer_copyright" data-cms-field="copyright">
                  </div>
                </div>

                <div style="display: flex; gap: 12px; margin-top: 20px;">
                  <button type="button" class="btn-checkout" style="width: auto; padding: 12px 28px;" onclick="AdminApp.saveCurrentPage('footer')">حفظ تعديلات الفوتر ✅</button>
                  <button type="button" class="btn-admin-pill btn-admin-outline" onclick="AdminApp.previewPage('footer')">معاينة الفوتر في الرئيسية 👁️</button>
                  <button type="button" class="btn-admin-pill btn-admin-danger" onclick="AdminApp.resetCurrentPage('footer')">استعادة النصوص الأصلية 🔄</button>
                </div>
              </div>

            </div>
          </div>
        </div>

        <!-- TAB 3: STORE SETTINGS -->
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

        <!-- TAB 4: BACKUP & DATA (FULL BACKUP: Products + Settings + Pages + Images) -->
        <div class="admin-tab-content" id="tab-backup">
          <div class="admin-card" style="max-width: 750px;">
            <div class="admin-card-header">
              <h3>النسخ الاحتياطي الشامل وإدارة البيانات</h3>
            </div>

            <div style="display: flex; flex-direction: column; gap: 20px;">
              <div style="background: var(--bg-soft); padding: 20px; border-radius: var(--radius-sm); border: 1px solid var(--border-light);">
                <h4 style="font-size: 1.05rem; font-weight: 800; color: var(--dark); margin-bottom: 6px;">📥 تصدير نسخة احتياطية شاملة (المنتجات + الصور والبانرات + محتوى الصفحات + الإعدادات)</h4>
                <p style="font-size: 0.9rem; color: var(--text-light); margin-bottom: 14px;">يمكنك تحميل ملف JSON متكامل يحتوي على كامل منتجات المتجر، نصوص كل الصفحات، الصور والبانرات المرفوعة، والإعدادات لحفظها كأمان على جهازك.</p>
                <button class="btn-admin-pill btn-admin-primary" onclick="AdminApp.exportFullBackupJSON()">
                  <span>تحميل ملف النسخة الاحتياطية الشاملة (JSON) 📥</span>
                </button>
              </div>

              <div style="background: var(--bg-soft); padding: 20px; border-radius: var(--radius-sm); border: 1px solid var(--border-light);">
                <h4 style="font-size: 1.05rem; font-weight: 800; color: var(--dark); margin-bottom: 6px;">📤 استيراد واستعادة المتجر من ملف نسخ احتياطي</h4>
                <p style="font-size: 0.9rem; color: var(--text-light); margin-bottom: 14px;">ارفع ملف JSON الذي قمت بتصديره سابقاً لاستعادة جميع المنتجات والصفحات والصور في لحظات معدودة.</p>
                <input type="file" id="importProductsInput" accept=".json" onchange="AdminApp.importFullBackupJSON(event)" style="display: none;">
                <button class="btn-admin-pill btn-admin-outline" onclick="document.getElementById('importProductsInput').click()">
                  <span>اختيار ملف JSON ورفعه 📤</span>
                </button>
              </div>

              <div style="background: #fff1f2; padding: 20px; border-radius: var(--radius-sm); border: 1px solid #fecdd3;">
                <h4 style="font-size: 1.05rem; font-weight: 800; color: #dc2626; margin-bottom: 6px;">⚠️ استعادة ضبط المصنع لجميع محتويات المتجر</h4>
                <p style="font-size: 0.9rem; color: #b91c1c; margin-bottom: 14px;">سيؤدي هذا إلى إعادة المتجر ونصوص الصفحات والصور والمنتجات إلى الحالة الأصلية الافتراضية.</p>
                <button class="btn-admin-pill btn-admin-danger" onclick="AdminApp.resetDefaultProducts()">
                  <span>استرجاع الإعدادات والمنتجات الأصلية 🔄</span>
                </button>
              </div>
            </div>
          </div>
        </div>
      </main>
    </div>
  </div>

  <!-- ADD / EDIT PRODUCT MODAL (WITH FILE UPLOAD BUTTON) -->
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
          <label>صورة المنتج (مسار أو رابط، أو رفع صورة من جهازك) *</label>
          <div style="display: flex; gap: 10px; align-items: center;">
            <img id="productImagePreview" src="../images/prod_girls_party.jpg" style="width: 55px; height: 55px; border-radius: 6px; object-fit: cover; border: 1px solid #cbd5e1;">
            <div style="flex: 1;">
              <input type="text" id="prodImgInput" placeholder="images/prod_girls_party.jpg أو رابط مباشر" oninput="AdminApp.updateImagePreview(this.value, 'productImagePreview')" required style="width: 100%; margin-bottom: 6px;">
              <input type="file" accept="image/*" onchange="AdminApp.handleImageUpload(event, 'prodImgInput', 'productImagePreview')" style="display: none;" id="upload_prod_img">
              <button type="button" class="btn-admin-pill btn-admin-outline" onclick="document.getElementById('upload_prod_img').click()">📁 رفع صورة من جهازك</button>
            </div>
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
    build_about()
    build_admin()
    print("ALL PAGES AND ADMIN MEDIA CMS UPDATED 100% SUCCESSFULLY!")
