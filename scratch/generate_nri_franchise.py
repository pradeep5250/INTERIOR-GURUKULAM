import os

root_dir = r'c:\Users\DELL\Downloads\INTERIOR GURUKULAM'
nri_dir = os.path.join(root_dir, 'nri')
franchise_dir = os.path.join(root_dir, 'franchise')

os.makedirs(nri_dir, exist_ok=True)
os.makedirs(franchise_dir, exist_ok=True)

# 1. NRI Online Course Page
nri_html = '''<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>30 Days NRI Online Practical Training - Interior Gurukulam</title>
  <meta name="description" content="30 Days Fast-Track Live Online Interior Design Practical Training for NRIs worldwide.">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@600;700;800&family=Arima:wght@500;600;700&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="../style.css">
  <link rel="stylesheet" href="../subpages.css">
  <style>
    .course-detail-hero {
      background: linear-gradient(135deg, rgba(81, 92, 46, 0.08), rgba(200, 90, 30, 0.05));
      padding: 36px 0 20px;
      border-bottom: 1px solid rgba(81, 92, 46, 0.12);
    }
    .detail-layout {
      display: grid;
      grid-template-columns: 1fr 380px;
      gap: 36px;
      margin-top: 24px;
    }
    @media (max-width: 900px) {
      .detail-layout { grid-template-columns: 1fr; }
    }
    .detail-card {
      background: #ffffff;
      border-radius: 20px;
      padding: 32px;
      box-shadow: 0 10px 30px rgba(42, 36, 24, 0.06);
      border: 1px solid rgba(81, 92, 46, 0.12);
    }
    .detail-media {
      width: 100%;
      height: 300px;
      border-radius: 16px;
      overflow: hidden;
      margin-bottom: 24px;
      background: #f0f0f8;
      display: flex;
      align-items: center;
      justify-content: center;
    }
    .detail-media img {
      max-width: 100%;
      max-height: 100%;
      object-fit: contain;
    }
    .detail-title {
      font-size: 1.8rem;
      font-weight: 800;
      color: var(--olive-deep);
      margin-bottom: 12px;
    }
    .overview-points-list {
      display: flex;
      flex-direction: column;
      gap: 12px;
      margin-top: 16px;
    }
    .overview-point-item {
      display: flex;
      align-items: flex-start;
      gap: 12px;
      background: #faf8f5;
      padding: 14px 18px;
      border-radius: 14px;
      border-left: 4px solid var(--terracotta);
      font-size: 0.98rem;
      color: var(--ink);
      line-height: 1.5;
    }
    .overview-point-bullet {
      color: var(--terracotta);
      font-size: 1.1rem;
      font-weight: bold;
      line-height: 1;
      margin-top: 2px;
    }
    .training-list {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(240px, 1fr));
      gap: 12px;
      margin-top: 16px;
    }
    .training-item {
      display: flex;
      align-items: center;
      gap: 12px;
      background: var(--cream);
      padding: 12px 16px;
      border-radius: 12px;
      font-weight: 600;
      color: var(--ink);
      border: 1px solid rgba(81, 92, 46, 0.1);
    }
    .training-item-icon {
      width: 24px;
      height: 24px;
      border-radius: 50%;
      background: var(--olive);
      color: #fff;
      display: flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
      font-size: 0.75rem;
    }
    .pricing-card {
      background: #ffffff;
      border-radius: 20px;
      padding: 24px;
      box-shadow: 0 10px 35px rgba(42, 36, 24, 0.08);
      border: 2px solid var(--olive);
      position: relative;
    }
    @media (min-height: 800px) and (min-width: 901px) {
      .pricing-card {
        position: sticky;
        top: 24px;
      }
    }
    .price-main {
      font-size: 2.2rem;
      font-weight: 800;
      color: var(--terracotta);
      margin-top: 4px;
    }
    .emi-box-detail {
      background: #fdfaf5;
      border: 1.5px dashed var(--olive);
      border-radius: 14px;
      padding: 14px 16px;
      margin: 16px 0;
    }
    .emi-row {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 8px 0;
      border-bottom: 1px solid rgba(0, 0, 0, 0.06);
      font-size: 0.92rem;
    }
    .emi-row:last-child { border-bottom: none; }

    .btn-enroll-primary {
      display: block;
      width: 100%;
      background: var(--terracotta);
      color: #ffffff !important;
      text-align: center;
      padding: 16px 24px;
      border-radius: 14px;
      font-weight: 800;
      font-size: 1.05rem;
      letter-spacing: 0.04em;
      text-decoration: none;
      box-shadow: 0 6px 20px rgba(200, 90, 30, 0.35);
      transition: all 0.3s ease;
      margin-top: 16px;
      border: none;
    }
    .btn-enroll-primary:hover {
      background: var(--terracotta-deep);
      transform: translateY(-2px);
      box-shadow: 0 8px 25px rgba(200, 90, 30, 0.45);
    }
  </style>
</head>

<body>
  <div class="subpage">
    <header class="subnav">
      <a class="brand" href="../index.html" aria-label="Interior Gurukulam Home">
        <div class="brand-logo-wrap">
          <img src="../assets/logo.png" alt="Interior Gurukulam Logo" class="brand-logo">
        </div>
        <div class="brand-text-group">
          <span class="brand-text-en">INTERIOR GURUKULAM</span>
          <span class="brand-text-ta"><span class="c-terracotta">இன்டீரியர்</span> <span class="c-olive">குருகுலம்</span></span>
        </div>
      </a>
      <button class="nav-toggle" aria-label="Toggle navigation">
        <span></span><span></span><span></span>
      </button>
      <nav class="navlinks">
        <a href="../index.html">HOME</a>
        <a href="../courses-new.html">ALL COURSES</a>
        <a href="../nri-training.html" class="active">NRI ONLINE TRAINING</a>
        <a href="../franchise-new.html">BUSINESS FRANCHISE</a>
        <a href="../joint-venture.html">INTERIOR OWNER JOINT VENTURE</a>
        <a href="../contact.html">CONTACT</a>
      </nav>
    </header>

    <main>
      <section class="course-detail-hero">
        <div class="container">
          <div style="font-size: 0.9rem; font-weight: 600; color: var(--terracotta); text-transform: uppercase;">
            <a href="../nri-training.html" style="color: inherit; text-decoration: none;">← Back to NRI Online Training</a>
          </div>
          <div style="font-size: 0.85rem; font-weight: 700; color: var(--olive-deep); margin-top: 8px;">GLOBAL NRI SPECIAL PROGRAM</div>
          <h1 class="detail-title" style="margin-top: 4px;">30 DAYS ONLINE PRACTICAL TRAINING</h1>
          <p style="color: #666; font-weight: 600;">Duration: 30 Days • Live Interactive Classes • Global Access</p>
        </div>
      </section>

      <section class="section">
        <div class="container">
          <div class="detail-layout">

            <!-- Left: Overview & Key Features -->
            <div class="detail-card">
              <div class="detail-media">
                <img src="../assets/nri-course-card.jpg" alt="NRI Online Interior Design Practical Training">
              </div>

              <h2 style="font-size: 1.4rem; color: var(--olive-deep); margin-bottom: 4px;">Course Highlights (Point by Point)</h2>
              <div class="overview-points-list">
                <div class="overview-point-item"><span class="overview-point-bullet">✦</span><span>30 Days intensive fast-track live practical interior design training program.</span></div>
                <div class="overview-point-item"><span class="overview-point-bullet">✦</span><span>Study from any country with interactive online sessions & recorded class access.</span></div>
                <div class="overview-point-item"><span class="overview-point-bullet">✦</span><span>Complete 2D/3D floor planning, elevation design, and material estimation guidance.</span></div>
                <div class="overview-point-item"><span class="overview-point-bullet">✦</span><span>ISO Certified Global Certificate of Completion upon course completion.</span></div>
              </div>

              <h2 style="font-size: 1.4rem; color: var(--olive-deep); margin-top: 32px; margin-bottom: 4px;">
                📚 Training Includes:
              </h2>
              <div class="training-list">
                <div class="training-item"><span class="training-item-icon">✓</span><span>Complete 2D/3D Interior Design Curriculum</span></div>
                <div class="training-item"><span class="training-item-icon">✓</span><span>Live project training & case studies</span></div>
                <div class="training-item"><span class="training-item-icon">✓</span><span>Business mentoring & material estimation</span></div>
                <div class="training-item"><span class="training-item-icon">✓</span><span>ISO Certified Global Certificate of completion</span></div>
              </div>
            </div>

            <!-- Right: Pricing Box -->
            <div>
              <div class="pricing-card">
                <div style="font-weight: 700; color: #777; font-size: 0.85rem; text-transform: uppercase;">Special Fee</div>
                <div class="price-main">₹2,39,000</div>
                <div style="font-size: 0.9rem; color: #888; text-decoration: line-through;">Original Fee: ₹4,00,000</div>
                <div style="font-size: 0.85rem; font-weight: 700; color: #3d4a28; background: #eef4e6; padding: 4px 10px; border-radius: 6px; display: inline-block; margin-top: 6px;">SAVE 40%</div>

                <div class="emi-box-detail">
                  <div style="font-weight: 700; color: var(--olive-deep); font-size: 0.95rem; margin-bottom: 10px;">
                    💳 EMI Payment Breakdown
                  </div>
                  <div class="emi-row">
                    <span style="color: #666;">Initial Payment:</span>
                    <strong style="color: var(--terracotta);">₹49,000</strong>
                  </div>
                  <div class="emi-row">
                    <span style="color: #666;">Monthly EMI:</span>
                    <strong>₹25,000 × 10 Months</strong>
                  </div>
                  <div class="emi-row">
                    <span style="color: #666;">Access Level:</span>
                    <strong>Global Online Access</strong>
                  </div>
                </div>

                <a href="../contact.html?course=nri-training" class="btn-enroll-primary">
                  ENROLL NOW
                </a>
              </div>
            </div>

          </div>
        </div>
      </section>
    </main>

    <footer class="footer2">
      <div class="footer-bottom">
        <span class="footer-text">INTERIOR GURUKULAM • இன்டீரியர் குருகுலம்</span>
      </div>
    </footer>
  </div>

  <script>
    document.addEventListener('DOMContentLoaded', () => {
      const toggleBtn = document.querySelector('.nav-toggle');
      const navLinks = document.querySelector('.navlinks');
      if (toggleBtn && navLinks) {
        toggleBtn.addEventListener('click', () => {
          toggleBtn.classList.toggle('open');
          navLinks.classList.toggle('show');
        });
      }
    });
  </script>
</body>

</html>'''

with open(os.path.join(nri_dir, 'nri-online-course.html'), 'w', encoding='utf-8') as f:
    f.write(nri_html)
print("Generated NRI course page: nri/nri-online-course.html")

# 2. Franchise Investment Packages Pages (Starter, Growth, Premium)
franchise_packages = [
    {
        'file': 'franchise-starter.html',
        'badge': 'STARTER PACKAGE',
        'title': 'FRANCHISE STARTER INVESTMENT PACKAGE',
        'investment': '₹5 Lakhs',
        'subtitle': 'Full Office Setup Included',
        'profit_user': '10%',
        'profit_company': '90%',
        'overview_points': [
            'Complete office setup with essential furniture & branding fixtures.',
            'Initial trainer certification and student recruitment guidance.',
            'Comprehensive brand guidance & teaching materials included.',
            'First-year dedicated operational and administrative support.'
        ],
        'includes': [
            'Complete office setup',
            'Furniture and fixtures',
            'Brand materials & guidance',
            'Initial training program',
            'Teaching materials',
            'Student recruitment support',
            'First-year operational support'
        ]
    },
    {
        'file': 'franchise-growth.html',
        'badge': 'GROWTH PACKAGE',
        'title': 'FRANCHISE GROWTH INVESTMENT PACKAGE',
        'investment': '₹10 Lakhs',
        'subtitle': 'Enhanced Business Support',
        'profit_user': '20%',
        'profit_company': '80%',
        'overview_points': [
            'Full office setup with premium interior fixtures and furniture.',
            'Advanced teaching materials & comprehensive trainer certification.',
            'Marketing, promotional support & client acquisition strategies.',
            'Extended multi-year operational excellence & business guidance.'
        ],
        'includes': [
            'Full office setup + premium fixtures',
            'Advanced teaching materials',
            'Comprehensive training program',
            'Enhanced business guidance',
            'Marketing & promotional support',
            'Client acquisition strategies',
            'Extended operational support'
        ]
    },
    {
        'file': 'franchise-premium.html',
        'badge': 'PREMIUM PACKAGE',
        'title': 'FRANCHISE PREMIUM INVESTMENT PACKAGE',
        'investment': '₹20 Lakhs',
        'subtitle': 'Maximum Business Support',
        'profit_user': '50%',
        'profit_company': '50%',
        'overview_points': [
            '50% Equal Profit Share partnership with maximum corporate backing.',
            'Premium luxury office setup, furniture, & exclusive teaching suites.',
            'Dedicated business mentor, marketing consultation & support team.',
            'Multi-location expansion rights & priority brand representation.'
        ],
        'includes': [
            'Premium office setup & furniture',
            'Exclusive teaching materials',
            'Premium trainer certification',
            'Comprehensive business mentoring',
            'Marketing strategy consultation',
            'Dedicated business support team',
            'Multi-location expansion guidance'
        ]
    }
]

franchise_template = '''<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} - Interior Gurukulam</title>
  <meta name="description" content="{title} at Interior Gurukulam Franchise Program.">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@600;700;800&family=Arima:wght@500;600;700&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="../style.css">
  <link rel="stylesheet" href="../subpages.css">
  <style>
    .course-detail-hero {{
      background: linear-gradient(135deg, rgba(81, 92, 46, 0.08), rgba(200, 90, 30, 0.05));
      padding: 36px 0 20px;
      border-bottom: 1px solid rgba(81, 92, 46, 0.12);
    }}
    .detail-layout {{
      display: grid;
      grid-template-columns: 1fr 380px;
      gap: 36px;
      margin-top: 24px;
    }}
    @media (max-width: 900px) {{
      .detail-layout {{ grid-template-columns: 1fr; }}
    }}
    .detail-card {{
      background: #ffffff;
      border-radius: 20px;
      padding: 32px;
      box-shadow: 0 10px 30px rgba(42, 36, 24, 0.06);
      border: 1px solid rgba(81, 92, 46, 0.12);
    }}
    .detail-media {{
      width: 100%;
      height: 280px;
      border-radius: 16px;
      overflow: hidden;
      margin-bottom: 24px;
    }}
    .detail-media img {{
      width: 100%;
      height: 100%;
      object-fit: cover;
    }}
    .detail-title {{
      font-size: 1.8rem;
      font-weight: 800;
      color: var(--olive-deep);
      margin-bottom: 12px;
    }}
    .overview-points-list {{
      display: flex;
      flex-direction: column;
      gap: 12px;
      margin-top: 16px;
    }}
    .overview-point-item {{
      display: flex;
      align-items: flex-start;
      gap: 12px;
      background: #faf8f5;
      padding: 14px 18px;
      border-radius: 14px;
      border-left: 4px solid var(--terracotta);
      font-size: 0.98rem;
      color: var(--ink);
      line-height: 1.5;
    }}
    .overview-point-bullet {{
      color: var(--terracotta);
      font-size: 1.1rem;
      font-weight: bold;
      line-height: 1;
      margin-top: 2px;
    }}
    .training-list {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(240px, 1fr));
      gap: 12px;
      margin-top: 16px;
    }}
    .training-item {{
      display: flex;
      align-items: center;
      gap: 12px;
      background: var(--cream);
      padding: 12px 16px;
      border-radius: 12px;
      font-weight: 600;
      color: var(--ink);
      border: 1px solid rgba(81, 92, 46, 0.1);
    }}
    .training-item-icon {{
      width: 24px;
      height: 24px;
      border-radius: 50%;
      background: var(--olive);
      color: #fff;
      display: flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
      font-size: 0.75rem;
    }}
    .pricing-card {{
      background: #ffffff;
      border-radius: 20px;
      padding: 24px;
      box-shadow: 0 10px 35px rgba(42, 36, 24, 0.08);
      border: 2px solid var(--olive);
      position: relative;
    }}
    @media (min-height: 800px) and (min-width: 901px) {{
      .pricing-card {{
        position: sticky;
        top: 24px;
      }}
    }}
    .price-main {{
      font-size: 2.2rem;
      font-weight: 800;
      color: var(--terracotta);
      margin-top: 4px;
    }}
    .profit-box-detail {{
      background: #fdfaf5;
      border: 1.5px dashed var(--olive);
      border-radius: 14px;
      padding: 14px 16px;
      margin: 16px 0;
    }}
    .emi-row {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 8px 0;
      border-bottom: 1px solid rgba(0, 0, 0, 0.06);
      font-size: 0.92rem;
    }}
    .emi-row:last-child {{ border-bottom: none; }}

    .btn-enroll-primary {{
      display: block;
      width: 100%;
      background: var(--terracotta);
      color: #ffffff !important;
      text-align: center;
      padding: 16px 24px;
      border-radius: 14px;
      font-weight: 800;
      font-size: 1.05rem;
      letter-spacing: 0.04em;
      text-decoration: none;
      box-shadow: 0 6px 20px rgba(200, 90, 30, 0.35);
      transition: all 0.3s ease;
      margin-top: 16px;
      border: none;
    }}
    .btn-enroll-primary:hover {{
      background: var(--terracotta-deep);
      transform: translateY(-2px);
      box-shadow: 0 8px 25px rgba(200, 90, 30, 0.45);
    }}
  </style>
</head>

<body>
  <div class="subpage">
    <header class="subnav">
      <a class="brand" href="../index.html" aria-label="Interior Gurukulam Home">
        <div class="brand-logo-wrap">
          <img src="../assets/logo.png" alt="Interior Gurukulam Logo" class="brand-logo">
        </div>
        <div class="brand-text-group">
          <span class="brand-text-en">INTERIOR GURUKULAM</span>
          <span class="brand-text-ta"><span class="c-terracotta">இன்டீரியர்</span> <span class="c-olive">குருகுலம்</span></span>
        </div>
      </a>
      <button class="nav-toggle" aria-label="Toggle navigation">
        <span></span><span></span><span></span>
      </button>
      <nav class="navlinks">
        <a href="../index.html">HOME</a>
        <a href="../courses-new.html">ALL COURSES</a>
        <a href="../nri-training.html">NRI ONLINE TRAINING</a>
        <a href="../franchise-new.html" class="active">BUSINESS FRANCHISE</a>
        <a href="../joint-venture.html">INTERIOR OWNER JOINT VENTURE</a>
        <a href="../contact.html">CONTACT</a>
      </nav>
    </header>

    <main>
      <section class="course-detail-hero">
        <div class="container">
          <div style="font-size: 0.9rem; font-weight: 600; color: var(--terracotta); text-transform: uppercase;">
            <a href="../franchise-new.html" style="color: inherit; text-decoration: none;">← Back to Franchise Packages</a>
          </div>
          <div style="font-size: 0.85rem; font-weight: 700; color: var(--olive-deep); margin-top: 8px;">{badge}</div>
          <h1 class="detail-title" style="margin-top: 4px;">{title}</h1>
          <p style="color: #666; font-weight: 600;">{subtitle} • Interior Gurukulam Business Franchise</p>
        </div>
      </section>

      <section class="section">
        <div class="container">
          <div class="detail-layout">

            <!-- Left: Package Overview & Included Features -->
            <div class="detail-card">
              <div class="detail-media">
                <img src="../assets/franchise-banner.jpg" alt="{title}">
              </div>

              <h2 style="font-size: 1.4rem; color: var(--olive-deep); margin-bottom: 4px;">Package Highlights (Point by Point)</h2>
              <div class="overview-points-list">
                {overview_points_html}
              </div>

              <h2 style="font-size: 1.4rem; color: var(--olive-deep); margin-top: 32px; margin-bottom: 4px;">
                📦 What's Included:
              </h2>
              <div class="training-list">
                {includes_html}
              </div>
            </div>

            <!-- Right: Investment & Profit Share Box -->
            <div>
              <div class="pricing-card">
                <div style="font-weight: 700; color: #777; font-size: 0.85rem; text-transform: uppercase;">Investment Amount</div>
                <div class="price-main">{investment}</div>

                <div class="profit-box-detail">
                  <div style="font-weight: 700; color: var(--olive-deep); font-size: 0.95rem; margin-bottom: 10px;">
                    📈 Profit Share Breakdown
                  </div>
                  <div class="emi-row">
                    <span style="color: #666;">Your Profit Share:</span>
                    <strong style="color: var(--terracotta);">{profit_user}</strong>
                  </div>
                  <div class="emi-row">
                    <span style="color: #666;">Company Share:</span>
                    <strong>{profit_company}</strong>
                  </div>
                  <div class="emi-row">
                    <span style="color: #666;">Setup Status:</span>
                    <strong>Full Setup Included</strong>
                  </div>
                </div>

                <a href="../contact.html?course=franchise" class="btn-enroll-primary">
                  ENROLL NOW
                </a>
              </div>
            </div>

          </div>
        </div>
      </section>
    </main>

    <footer class="footer2">
      <div class="footer-bottom">
        <span class="footer-text">INTERIOR GURUKULAM • இன்டீரியர் குருகுலம்</span>
      </div>
    </footer>
  </div>

  <script>
    document.addEventListener('DOMContentLoaded', () => {{
      const toggleBtn = document.querySelector('.nav-toggle');
      const navLinks = document.querySelector('.navlinks');
      if (toggleBtn && navLinks) {{
        toggleBtn.addEventListener('click', () => {{
          toggleBtn.classList.toggle('open');
          navLinks.classList.toggle('show');
        }});
      }}
    }});
  </script>
</body>

</html>'''

for fp in franchise_packages:
    overview_points_html = '\n'.join([
        f'                <div class="overview-point-item"><span class="overview-point-bullet">✦</span><span>{pt}</span></div>'
        for pt in fp['overview_points']
    ])
    includes_html = '\n'.join([
        f'                  <div class="training-item"><span class="training-item-icon">✓</span><span>{item}</span></div>'
        for item in fp['includes']
    ])
    html_content = franchise_template.format(
        title=fp['title'],
        badge=fp['badge'],
        subtitle=fp['subtitle'],
        investment=fp['investment'],
        profit_user=fp['profit_user'],
        profit_company=fp['profit_company'],
        overview_points_html=overview_points_html,
        includes_html=includes_html
    )
    filepath = os.path.join(franchise_dir, fp['file'])
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html_content)
    print(f"Generated Franchise package page: franchise/{fp['file']}")
