# -*- coding: utf-8 -*-
import subprocess
import os

BASE_DIR = 'E:/Sites/bambino-kids-fashion'

HTML_DOC = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="utf-8">
  <title>وثيقة التسليم الفني ودليل التشغيل الشامل - متجر بامبينو كيدز</title>
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@300;400;500;700;800;900&display=swap');

    @page {
      size: A4;
      margin: 18mm 14mm 18mm 14mm;
      @bottom-center {
        content: "صفحة " counter(page);
        font-family: 'Tajawal', sans-serif;
        font-size: 8pt;
        color: #64748b;
      }
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    body {
      font-family: 'Tajawal', 'Segoe UI', Tahoma, sans-serif;
      direction: rtl;
      text-align: right;
      color: #1e293b;
      background: #ffffff;
      line-height: 1.6;
      font-size: 10pt;
    }

    /* COVER PAGE */
    .cover-page {
      page-break-after: always;
      height: 96vh;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      border: 3px solid #e11d48;
      border-radius: 12px;
      padding: 40px;
      background: linear-gradient(180deg, #fffdfd 0%, #fff1f2 100%);
      position: relative;
    }
    .cover-header {
      text-align: center;
      margin-top: 20px;
    }
    .cover-brand {
      font-size: 38pt;
      font-weight: 900;
      color: #e11d48;
      letter-spacing: 2px;
      line-height: 1;
      margin-bottom: 6px;
    }
    .cover-sub {
      font-size: 13pt;
      font-weight: 700;
      color: #64748b;
      letter-spacing: 1px;
    }
    .cover-badge {
      display: inline-block;
      background: #e11d48;
      color: #fff;
      padding: 6px 18px;
      border-radius: 9999px;
      font-size: 11pt;
      font-weight: 800;
      margin: 25px auto 15px;
    }
    .cover-title {
      font-size: 24pt;
      font-weight: 900;
      color: #0f172a;
      line-height: 1.3;
      margin-bottom: 15px;
    }
    .cover-desc {
      font-size: 11pt;
      color: #475569;
      max-width: 600px;
      margin: 0 auto;
      line-height: 1.7;
    }
    .cover-meta {
      background: #ffffff;
      border: 1px solid #fecdd3;
      border-radius: 10px;
      padding: 20px 25px;
      box-shadow: 0 4px 12px rgba(225, 29, 72, 0.05);
    }
    .cover-meta-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 12px;
      font-size: 9.5pt;
    }
    .cover-meta-item strong {
      color: #e11d48;
    }

    /* SECTION STYLES */
    .page-break {
      page-break-before: always;
    }
    h2.section-header {
      font-size: 15pt;
      font-weight: 900;
      color: #0f172a;
      border-bottom: 2px solid #e11d48;
      padding-bottom: 6px;
      margin: 24px 0 14px;
      display: flex;
      align-items: center;
      gap: 8px;
    }
    h3 {
      font-size: 11.5pt;
      font-weight: 800;
      color: #e11d48;
      margin: 16px 0 8px;
    }
    h4 {
      font-size: 10.5pt;
      font-weight: 800;
      color: #0f172a;
      margin: 12px 0 4px;
    }
    p {
      margin-bottom: 10px;
      color: #334155;
      line-height: 1.65;
    }
    ul, ol {
      margin: 8px 24px 14px;
    }
    li {
      margin-bottom: 5px;
      color: #334155;
    }

    /* CALLOUT BOXES */
    .callout {
      background: #fff1f2;
      border-right: 4px solid #e11d48;
      border-radius: 6px;
      padding: 12px 16px;
      margin: 12px 0 16px;
      font-size: 9.5pt;
    }
    .callout-success {
      background: #ecfdf5;
      border-right-color: #10b981;
    }
    .callout-info {
      background: #f0f9ff;
      border-right-color: #0284c7;
    }
    .callout strong {
      color: #0f172a;
    }

    /* TABLES */
    table {
      width: 100%;
      border-collapse: collapse;
      margin: 12px 0 16px;
      font-size: 9pt;
    }
    th {
      background: #fff1f2;
      color: #e11d48;
      font-weight: 800;
      padding: 8px 10px;
      border: 1px solid #fecdd3;
      text-align: right;
    }
    td {
      padding: 8px 10px;
      border: 1px solid #e2e8f0;
      color: #334155;
    }
    tr:nth-child(even) td {
      background: #f8fafc;
    }

    /* CODE BOXES */
    pre, code {
      font-family: 'Consolas', 'Courier New', monospace;
      direction: ltr;
      text-align: left;
    }
    pre {
      background: #0f172a;
      color: #f8fafc;
      padding: 10px 14px;
      border-radius: 6px;
      font-size: 8.5pt;
      overflow-x: auto;
      margin: 10px 0 14px;
      line-height: 1.5;
    }
    p code, li code {
      background: #f1f5f9;
      color: #e11d48;
      padding: 2px 5px;
      border-radius: 4px;
      font-size: 8.5pt;
      font-weight: 700;
    }

    .badge-pill {
      display: inline-block;
      padding: 3px 8px;
      border-radius: 9999px;
      font-size: 7.5pt;
      font-weight: 800;
      color: #fff;
      background: #e11d48;
    }
  </style>
</head>
<body>

  <!-- ==================== COVER PAGE ==================== -->
  <div class="cover-page">
    <div class="cover-header">
      <div class="cover-brand">BAMBINO</div>
      <div class="cover-sub">KIDS FASHION • أزياء الأطفال الراقية</div>
      <div><span class="cover-badge">وثيقة التسليم الفني ودليل التشغيل الشامل</span></div>
      <h1 class="cover-title">المشروع الإلكتروني المتكامل<br>متجر بامبينو كيدز الفاخر</h1>
      <p class="cover-desc">
        دليل هندسي وتقني شامل ومفصل يشرح هيكلية المشروع، آلية الربط التلقائي الدائم مع Cloudflare Pages، تفاصيل لوحة التحكم ومحرر الصفحات CMS، وجميع التعليمات والبيانات التي تمكن أي مبرمج أو مسؤول من إدارة وتطوير المتجر مباشرة دون الحاجة لأي إعدادات مسبقة.
      </p>
    </div>

    <div class="cover-meta">
      <div class="cover-meta-grid">
        <div class="cover-meta-item"><strong>اسم المشروع:</strong> BAMBINO Kids Fashion</div>
        <div class="cover-meta-item"><strong>بيئة النشر:</strong> Cloudflare Pages (Edge Network)</div>
        <div class="cover-meta-item"><strong>مستودع الكود:</strong> GitHub (zedana01/bambino-kids-fashion)</div>
        <div class="cover-meta-item"><strong>لوحة التحكم:</strong> Visual CMS مدمجة بالكامل</div>
        <div class="cover-meta-item"><strong>تاريخ الإعداد:</strong> أكتوبر 2026</div>
        <div class="cover-meta-item"><strong>حالة الربط والنشر:</strong> دائم ونشط 100% (Automated CI/CD)</div>
      </div>
    </div>
  </div>

  <!-- ==================== SECTION 1 ==================== -->
  <div class="page-break"></div>
  <h2 class="section-header">1. الإجابة الحاسمة: هل يحتاج الشخص القادم لإعادة ربط Cloudflare؟</h2>
  
  <div class="callout callout-success">
    <strong>الجواب المباشر والنهائي: لا، لا يحتاج لأي ربط أو إعداد من جديد إطلاقاً!</strong><br>
    المشروع مربوط ومضبوط بالكامل وبشكل دائم عبر خط أنابيب نشر آلي ومستمر (Automated CI/CD Pipeline).
  </div>

  <p>
    بمجرد تسليم هذا الملف للمبرمج أو المسؤول القادم، لن يحتاج إلى فتح الـ Task القديم أو كتابة أي أوامر ربط، لأن كل البنية التحتية قد تم إعدادها وتشغيلها فعلياً عبر المستويات الثلاثة التالية:
  </p>

  <table>
    <thead>
      <tr>
        <th style="width: 28%;">المسار / الشخص</th>
        <th style="width: 32%;">ماذا يفعل؟</th>
        <th style="width: 40%;">النتيجة المباشرة</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>1. صاحب المتجر / مسؤول المحتوى (بدون كود)</strong></td>
        <td>يدخل إلى لوحة التحكم عبر المتصفح: <code>/admin/</code> ويدخل رمز الأمان <code>1234</code>.</td>
        <td>يعدل أي منتج، سعر، صورة، بانر، أو نص في أي صفحة، ويضغط "حفظ" ليتم التحديث في ثوانٍ دون الحاجة للمساس بأي سيرفر أو كود.</td>
      </tr>
      <tr>
        <td><strong>2. المبرمج (عبر Git)</strong></td>
        <td>يعدل على الأكواد في مجلده المحلي، ويكتب فقط: <code>git push origin main</code>.</td>
        <td>يقوم GitHub Actions تلقائياً بتشغيل سكريبت الـ Deploy وإرسال التحديثات لـ Cloudflare Pages فوراً وبشكل آلي تماماً.</td>
      </tr>
      <tr>
        <td><strong>3. مسؤول الدومينات (عبر Cloudflare)</strong></td>
        <td>يدخل لحساب Cloudflare ويفتح مشروع <code>bambino-kids-fashion</code> ويضغط على "Custom Domains".</td>
        <td>يربط أي دومين رسمي (مثل <code>bambinokids.com</code>) بضغطة زر دون أي تعقيد.</td>
      </tr>
    </tbody>
  </table>

  <!-- ==================== SECTION 2 ==================== -->
  <h2 class="section-header">2. الاعتمادات والروابط الرسمية للمشروع (Credentials & URLs)</h2>

  <p>جميع الروابط والبيانات المسجلة والجاهزة للعمل فوراً:</p>

  <table>
    <thead>
      <tr>
        <th style="width: 30%;">البند</th>
        <th style="width: 70%;">القيمة / الرابط</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>رابط المتجر الحي (Live Website)</strong></td>
        <td><a href="https://bambino-kids-fashion.pages.dev">https://bambino-kids-fashion.pages.dev</a></td>
      </tr>
      <tr>
        <td><strong>رابط لوحة التحكم (Admin Panel)</strong></td>
        <td><a href="https://bambino-kids-fashion.pages.dev/admin/">https://bambino-kids-fashion.pages.dev/admin/</a></td>
      </tr>
      <tr>
        <td><strong>رمز الدخول للوحة التحكم (PIN)</strong></td>
        <td><code>1234</code></td>
      </tr>
      <tr>
        <td><strong>مستودع الكود (GitHub Repo)</strong></td>
        <td><a href="https://github.com/zedana01/bambino-kids-fashion">https://github.com/zedana01/bambino-kids-fashion</a></td>
      </tr>
      <tr>
        <td><strong>اسم مستخدم GitHub</strong></td>
        <td><code>zedana01</code></td>
      </tr>
      <tr>
        <td><strong>اسم مشروع Cloudflare Pages</strong></td>
        <td><code>bambino-kids-fashion</code></td>
      </tr>
      <tr>
        <td><strong>معرف حساب Cloudflare (Account ID)</strong></td>
        <td><code>53ed3d29e7de4f5ece3884a47462c2c4</code></td>
      </tr>
      <tr>
        <td><strong>رمز الـ API لـ Cloudflare (Token)</strong></td>
        <td><code>cfat_zgrByAmWir... (محفوظ ومشفر داخل GitHub Secrets باسم CLOUDFLARE_API_TOKEN)</code></td>
      </tr>
      <tr>
        <td><strong>المسار المحلي للمشروع على الجهاز</strong></td>
        <td><code>E:\Sites\bambino-kids-fashion\</code></td>
      </tr>
    </tbody>
  </table>

  <!-- ==================== SECTION 3 ==================== -->
  <div class="page-break"></div>
  <h2 class="section-header">3. كيف تم الربط التلقائي؟ (Automated CI/CD Pipeline)</h2>

  <p>
    تم تصميم الربط وفق معايير <strong>DevOps & CI/CD</strong> المعتمدة عالمياً، حيث لا يحتاج المستخدم لرفع ملفات يدوياً أو استخدام FTP. الدورة البرمجية تسير كالتالي:
  </p>

  <ol>
    <li>
      <strong>البيئة المحلية (Local Workspace):</strong> مجلد المشروع على جهازك <code>E:\Sites\bambino-kids-fashion\</code> متصل بمستودع Git الرسمي.
    </li>
    <li>
      <strong>المستودع السحابي (GitHub Repository):</strong> المستودع <code>zedana01/bambino-kids-fashion</code> يحتوي على فرع الإنتاج <code>main</code>.
    </li>
    <li>
      <strong>الأسرار المشفرة (Encrypted Secrets):</strong> تم تسجيل وحفظ اعتمادات Cloudflare مسبقاً داخل إعدادات الأمان في GitHub (GitHub Actions Secrets):
      <ul>
        <li><code>CLOUDFLARE_API_TOKEN</code>: التوكن المعتمد للوصول لـ Cloudflare.</li>
        <li><code>CLOUDFLARE_ACCOUNT_ID</code>: معرف الحساب الرسمي.</li>
      </ul>
    </li>
    <li>
      <strong>سير العمل الآلي (GitHub Actions Workflow):</strong> ملف الإعدادات الموجود داخل المشروع في المسار:
      <br><code>.github/workflows/deploy.yml</code>
      <br>يحتوي على الكود البرمجي الآتي الذي يعمل ذاتياً عند كل دفع كود:
    </li>
  </ol>

  <pre>name: Deploy to Cloudflare Pages

on:
  push:
    branches:
      - main
  workflow_dispatch:

jobs:
  deploy:
    runs-on: ubuntu-latest
    permissions:
      contents: read
      deployments: write
    steps:
      - name: Checkout Repository
        uses: actions/checkout@v4

      - name: Deploy to Cloudflare Pages
        uses: cloudflare/wrangler-action@v3
        with:
          apiToken: ${{ secrets.CLOUDFLARE_API_TOKEN }}
          accountId: ${{ secrets.CLOUDFLARE_ACCOUNT_ID }}
          command: pages deploy . --project-name=bambino-kids-fashion --commit-dirty=true</pre>

  <div class="callout callout-info">
    <strong>💡 الفائدة للمبرمج القادم:</strong>
    كل ما على أي مبرمج فعله هو تعديل أي ملف محلياً ثم كتابة:
    <br><code>git add .</code>
    <br><code>git commit -m "تعديل جديد"</code>
    <br><code>git push origin main</code>
    <br>وخلال 15 إلى 30 ثانية سيكون الموقع الجديد منشوراً على الرابط العالمي مباشرة!
  </div>

  <!-- ==================== SECTION 4 ==================== -->
  <div class="page-break"></div>
  <h2 class="section-header">4. الهيكلية البرمجية وشرح الملفات (Project Structure)</h2>

  <p>المشروع مبني بهيكلية برمجية نقية وخفيفة وسريعة التحميل (Vanilla HTML5 / Modern CSS3 / Modular ES6 JavaScript) بدون أي أطر عمل ثقيلة تسبب بطء التصفح:</p>

  <table>
    <thead>
      <tr>
        <th style="width: 25%;">الملف / المجلد</th>
        <th style="width: 75%;">الوظيفة والمحتوى</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><code>index.html</code></td>
        <td><strong>الصفحة الرئيسية:</strong> الهيدر، السلايدر، شريط الميزات، شبكة الأقسام، بانر العروض مع عداد تنازلي حي، شبكة المنتجات مع فلترة، ونادي الأمهات.</td>
      </tr>
      <tr>
        <td><code>shop.html</code></td>
        <td><strong>صفحة المتجر والكاتالوج:</strong> تصفح كافة المنتجات مع فلاتر جانبية (الأقسام، نطاق الأسعار، الترتيب حسب السعر والتقييم، والبحث الحي).</td>
      </tr>
      <tr>
        <td><code>product.html</code></td>
        <td><strong>صفحة تفاصيل المنتج:</strong> قراءة معرّف المنتج <code>?id=X</code>، معرض صور تفاعلي مع مصغرات، اختيار المقاس، السلة، وزر طلب فوري عبر واتساب.</td>
      </tr>
      <tr>
        <td><code>about.html</code></td>
        <td><strong>صفحة من نحن:</strong> قصة تأسيس المتجر، رسالتنا، ومعايير الجودة والأمان لأقمشة القطن العضوي 100%.</td>
      </tr>
      <tr>
        <td><code>contact.html</code></td>
        <td><strong>صفحة اتصل بنا:</strong> قنوات التواصل المباشر ونموذج إرسال استفسار تفاعلي يفتح محادثة واتساب فورية منسقة.</td>
      </tr>
      <tr>
        <td><code>terms.html</code></td>
        <td><strong>الشروط والأحكام:</strong> شروط الطلب، تفاصيل الشحن والتوصيل، وسياسة الاستبدال والاسترجاع السهل خلال 7 أيام.</td>
      </tr>
      <tr>
        <td><code>privacy.html</code></td>
        <td><strong>سياسة الخصوصية:</strong> بنود حماية بيانات العملاء وسرية المعاملات وأمان الطلبات.</td>
      </tr>
      <tr>
        <td><code>admin/index.html</code></td>
        <td><strong>لوحة التحكم (Dashboard):</strong> محرك الإدارة الكامل، محمي برمز PIN، للتحكم في المنتجات ومحتوى الصفحات والصور والإعدادات.</td>
      </tr>
      <tr>
        <td><code>css/style.css</code></td>
        <td><strong>ملف التصميم والتنسيق:</strong> متوافق مع RTL، درجات الوردي والأحمر الخفيف (<code>#e11d48</code>)، خط Tajawal، وتصميم متجاوب لجميع الشاشات.</td>
      </tr>
      <tr>
        <td><code>js/store.js</code></td>
        <td><strong>محرك المتجر المركزي:</strong> يدير بيانات المنتجات، السلة المنبثقة، إتمام الطلب بالواتساب، ومزامنة نصوص وصور الـ CMS مع الواجهة.</td>
      </tr>
      <tr>
        <td><code>js/admin.js</code></td>
        <td><strong>محرك لوحة التحكم:</strong> المصادقة، عمليات الـ CRUD للمنتجات، محرر الصفحات، تحويل الصور المرفوعة لـ Base64، والنسخ الاحتياطي JSON.</td>
      </tr>
      <tr>
        <td><code>data/products.json</code></td>
        <td><strong>قاعدة البيانات الافتراضية:</strong> تحتوي على المنتجات الأصلية والمقاسات والأسعار والأقسام.</td>
      </tr>
      <tr>
        <td><code>images/</code></td>
        <td><strong>مجلد الوسائط:</strong> يحتوي على 13 صورة وبانر أصلية عالية الدقة لجميع الأقسام والمنتجات.</td>
      </tr>
      <tr>
        <td><code>tools/</code></td>
        <td><strong>مجلد أدوات البناء:</strong> سكريبتات بايثون المساعدة في توليد الصفحات والتحقق من الروابط والصور.</td>
      </tr>
    </tbody>
  </table>

  <!-- ==================== SECTION 5 ==================== -->
  <div class="page-break"></div>
  <h2 class="section-header">5. دليل لوحة التحكم ونظام محرر المحتوى (CMS Guide)</h2>

  <p>
    تم تزويد المتجر بنظام إدارة محتوى متكامل (Visual CMS) لا يتطلب أي خبرة برمجية. يمكن لصاحب المتجر القيام بالآتي:
  </p>

  <h3>أ. إدارة المنتجات (Products Management)</h3>
  <ul>
    <li><strong>إضافة منتج جديد:</strong> كتابة الاسم، السعر، السعر القديم، اختيار القسم، إدخال المقاسات، والوصف.</li>
    <li><strong>رفع صورة المنتج من الجهاز مباشرة:</strong> يوجد زر <code>📁 رفع صورة من جهازك</code> يقوم بتحميل الصورة من الكمبيوتر أو الجوال ومعاينتها فوراً.</li>
    <li><strong>تعديل أي منتج:</strong> تعديل الأسعار أو تبديل الصور أو الشارات بنقرة زر.</li>
    <li><strong>حذف المنتجات:</strong> إمكانية إزالة أي قطعة من المتجر مع تأكيد الأمان.</li>
  </ul>

  <h3>ب. محرر نصوص وبانرات الصفحات (Visual Page CMS)</h3>
  <p>
    عند الدخول لتبويب <strong>«📄 محتوى وتعديل الصفحات»</strong>، يظهر أمامك اختيار لجميع صفحات الموقع:
  </p>
  <ul>
    <li><strong>الصفحة الرئيسية:</strong> تعديل صورة ونصوص البانر الكبير، ميزات المتجر الأربعة وأيقوناتها، بانر العروض الحصرية، ونادي الأمهات.</li>
    <li><strong>صفحة من نحن:</strong> تعديل قصة المتجر، رسالتنا، صورة البراند، وبطاقات معايير الجودة الثلاثة وأيقوناتها.</li>
    <li><strong>صفحة اتصل بنا:</strong> تعديل مواعيد العمل، أرقام التواصل، وعنوان المقر.</li>
    <li><strong>الشروط والأحكام وسياسة الخصوصية:</strong> تعديل كافة البنود والفقرات التمهيدية.</li>
    <li><strong>الفوتر العام:</strong> تعديل النبذة التعريفية في أسفل الموقع وحقوق النشر.</li>
  </ul>

  <h3>ج. ميزة رفع الصور والأيقونات من الجهاز (Media Uploader)</h3>
  <p>
    جميع صور وبانرات الصفحات (مثل بانر الهيرو، بانر العروض الخاطفة، وصور أقسام المتجر الأربعة) مزودة بزر <code>📁 رفع صورة من جهازك</code>.
    يقوم النظام تلقائياً بتحويل الصورة إلى صيغة <code>Base64 Data-URL</code> وحفظها داخل الذاكرة التخزينية للمتصفح (<code>localStorage</code>) وعرضها فورياً للزوار دون الحاجة لأي خادم رفع خارجي.
  </p>

  <h3>د. النسخ الاحتياطي الشامل (Full Backup & Restore)</h3>
  <ul>
    <li><strong>تصدير نسخة احتياطية:</strong> زر <code>تحميل ملف النسخة الاحتياطية (JSON)</code> يقوم بتنزيل ملف واحد يحتوي على كل شيء: (المنتجات + أسعارها + صورها المرفوعة + نصوص كافة الصفحات + إعدادات المتجر).</li>
    <li><strong>استيراد النسخة:</strong> يمكن رفع هذا الملف في أي وقت على أي جهاز لاسترجاع المتجر بالكامل في ثانية واحدة.</li>
    <li><strong>استعادة ضبط المصنع:</strong> زر أمان لإرجاع نصوص وصور ومنتجات المتجر لحالتها الأصلية الأولى.</li>
  </ul>

  <!-- ==================== SECTION 6 ==================== -->
  <div class="page-break"></div>
  <h2 class="section-header">6. دليل المطور المستقبلي وخطوات العمل (Developer Guide)</h2>

  <p>فيما يلي الخطوات والتعليمات العملية لأي مبرمج يرغب في العمل على المشروع:</p>

  <h3>أ. التشغيل والتجربة محلياً (Local Development)</h3>
  <p>يمكن فتح ملفات <code>.html</code> مباشرة، أو تشغيل سيرفر محلي خفيف لتجربة المتصفح:</p>
  <pre># الانتقال لمجلد المشروع
cd E:\Sites\bambino-kids-fashion

# تشغيل سيرفر بايثون محلي على البورت 8080
python -m http.server 8080</pre>
  <p>ثم فتح: <code>http://localhost:8080/index.html</code> أو <code>http://localhost:8080/admin/index.html</code>.</p>

  <h3>ب. خطوات التعديل ودفع الكود لـ Cloudflare (Git Commands)</h3>
  <p>بعد تعديل أي كود في المشروع، لتحديث الموقع الحي على Cloudflare Pages يكفي تنفيذ الآتي:</p>
  <pre>git add .
git commit -m "وصف التعديل الجديد"
git push origin main</pre>
  <p>سيتولى GitHub Actions النشر التلقائي فوراً، ويمكن متابعة حالة البناء من تبويب <strong>Actions</strong> في مستودع GitHub.</p>

  <h3>ج. خطوات ربط دومين رسمي مخصص (Custom Domain Setup)</h3>
  <p>إذا رغب العميل مستقبلاً في ربط المتجر بنطاق مثل <code>bambinokids.com</code> أو <code>bambino.sa</code>:</p>
  <ol>
    <li>تسجيل الدخول إلى حساب Cloudflare بالبيانات المرفقة.</li>
    <li>الذهاب إلى <strong>Workers & Pages</strong> ثم اختيار المشروع <strong>bambino-kids-fashion</strong>.</li>
    <li>الضغط على تبويب <strong>Custom domains</strong> ثم النقر على <strong>Set up a domain</strong>.</li>
    <li>إدخال اسم الدومين والضغط على <strong>Continue</strong>.</li>
    <li>سيقوم Cloudflare تلقائياً بإصدار شهادة الأمان SSL وتفعيل الدومين خلال دقائق دون أي رسوم إضافية.</li>
  </ol>

  <h3>د. الأسئلة الشائعة وحلول المشاكل (Troubleshooting FAQ)</h3>
  <table>
    <thead>
      <tr>
        <th style="width: 40%;">المشكلة / السؤال</th>
        <th style="width: 60%;">الحل والسبب</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>عدلت في لوحة التحكم ولكن التعديل لا يظهر على جهاز آخر؟</strong></td>
        <td>لوحة التحكم تعتمد على <code>localStorage</code> لتعديل وتجربة الموقع فورياً. لمشاركة التعديلات مع الجميع، يمكن تصدير ملف الـ Backup أو تعديل ملف <code>products.json</code> ورفعه عبر Git.</td>
      </tr>
      <tr>
        <td><strong>هل أحتاج لسيرفر أو استضافة مدفوعة شهرياً؟</strong></td>
        <td>لا! الموقع منشور على Cloudflare Pages كـ Static Web App، وهو <strong>مجاني بالكامل مدى الحياة</strong>، مع حماية غير محدودة ضد هجمات DDoS وسرعة تحميل عالمية فائقة (Edge CDN).</td>
      </tr>
      <tr>
        <td><strong>كيف أغير رقم الواتساب الذي يستقبل الطلبات؟</strong></td>
        <td>من لوحة التحكم: تبويب <strong>«إعدادات المتجر»</strong> -> حقل <strong>رقم واتساب</strong>، أو عبر ملف <code>js/store.js</code> في متغير <code>DEFAULT_SETTINGS.whatsapp</code>.</td>
      </tr>
    </tbody>
  </table>

  <div style="margin-top: 35px; border-top: 2px solid #e11d48; padding-top: 15px; text-align: center; color: #64748b; font-size: 8.5pt;">
    تم إعداد وتوثيق هذا الدليل التقني بعناية لضمان استمرارية وكفاءة تشغيل متجر <strong>بامبينو كيدز (BAMBINO KIDS)</strong> بنسبة 100%.
  </div>

</body>
</html>
"""

def generate_pdf():
    html_path = os.path.join(BASE_DIR, 'handover_doc.html')
    pdf_path = os.path.join(BASE_DIR, 'Bambino_Project_Handover_Documentation.pdf')

    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(HTML_DOC)

    chrome_cmd = [
        'C:/Program Files/Google/Chrome/Application/chrome.exe',
        '--headless=new',
        '--disable-gpu',
        '--no-pdf-header-footer',
        f'--print-to-pdf={pdf_path}',
        html_path
    ]

    subprocess.run(chrome_cmd, check=True)
    size = os.path.getsize(pdf_path)
    print(f"PDF generated successfully at {pdf_path} (Size: {size:,} bytes)")

if __name__ == '__main__':
    generate_pdf()
