import os

courses_dir = r'c:\Users\DELL\Downloads\INTERIOR GURUKULAM\courses'
os.makedirs(courses_dir, exist_ok=True)

courses = [
    {
        'file': 'course-instant-income.html',
        'id': 'mosquito-net',
        'title': 'INSTANT INCOME – MOSQUITO NET',
        'kicker': '01 • BEGINNER COURSE',
        'fee': '₹250',
        'fee_regular': '₹250',
        'fee_emi': 'N/A (One Time)',
        'fee_initial': '₹250',
        'fee_monthly': 'Instant Start',
        'duration': '1 Hour',
        'image': '../assets/mosquito-net-course.jpg',
        'overview_points': [
            '100% Practical hands-on installation training',
            'Instant income generation skill learned in just 1 hour',
            'Complete door and window mesh fixing techniques',
            'Step-by-step guidance on material measurement & fitting'
        ],
        'includes': [
            'Mosquito Net Door Type',
            'Mosquito Net Window Type'
        ]
    },
    {
        'file': 'course-pvc-upvc-frame.html',
        'id': 'pvc-upvc-frame',
        'title': 'PVC / UPVC INTERIOR FRAME TYPE COURSE',
        'kicker': '02 • INTERMEDIATE COURSE',
        'fee': '₹10,000',
        'fee_regular': '₹10,000',
        'fee_emi': '₹15,000',
        'fee_initial': '₹2,000',
        'fee_monthly': '₹500 × 26 Months',
        'duration': 'Flexible',
        'image': '../assets/pvc-upvc-frame.jpg',
        'overview_points': [
            'Hands-on PVC & UPVC frame installation mastery',
            'Bathroom door, glass work, and cupboard execution',
            'Practical project training with real interior materials',
            'Complete hardware alignment & mirror fixing techniques'
        ],
        'includes': [
            'Bathroom Door Fixing',
            'Cupboard Work',
            'Box Type Cupboard',
            'Pooja Door',
            'Sliding Glass Work',
            'Open Glass Work',
            'Mirror Fixing',
            'Pooja Bell Fixing',
            'SS Drawer Fixing'
        ]
    },
    {
        'file': 'course-upvc-panel.html',
        'id': 'upvc-panel',
        'title': 'UPVC PANEL WORK COURSE',
        'kicker': '03 • INTERMEDIATE COURSE',
        'fee': '₹20,000',
        'fee_regular': '₹20,000',
        'fee_emi': '₹25,000',
        'fee_initial': '₹5,000',
        'fee_monthly': '₹500 × 40 Months',
        'duration': 'Flexible',
        'image': '../assets/upvc-panel.jpg',
        'overview_points': [
            'Modern UPVC wall paneling & ceiling lighting design',
            'Cupboard, pooja door, and sliding glass fitting',
            'Real-world project mentorship & hands-on execution',
            'Durable moisture-proof interior paneling solutions'
        ],
        'includes': [
            'Cupboard Work',
            'Box Type Cupboard',
            'Pooja Door',
            'Sliding Glass Work',
            'Open Glass Work',
            'Mirror Fixing',
            'Pooja Bell Fixing',
            'SS Drawer Fixing'
        ]
    },
    {
        'file': 'course-mdf-panel.html',
        'id': 'mdf-panel',
        'title': 'MDF INTERIOR PANEL WORK',
        'kicker': '04 • INTERMEDIATE COURSE',
        'fee': '₹20,000',
        'fee_regular': '₹20,000',
        'fee_emi': '₹25,000',
        'fee_initial': '₹5,000',
        'fee_monthly': '₹500 × 40 Months',
        'duration': 'Flexible',
        'image': '../assets/mdf-interior.jpg',
        'overview_points': [
            'Complete MDF paneling & CNC divider installation',
            'Modern residential & commercial interior design',
            'Cupboard assembly, glass work, and finishing',
            'Geometric wall panel joinery & surface treatment'
        ],
        'includes': [
            'Cupboard Work',
            'Box Type Cupboard',
            'Pooja Door',
            'Sliding Glass Work',
            'Open Glass Work',
            'Mirror Fixing',
            'Pooja Bell Fixing',
            'SS Drawer Fixing',
            'Divider'
        ]
    },
    {
        'file': 'course-plywood.html',
        'id': 'plywood-course',
        'title': 'PLYWOOD INTERIOR COURSE',
        'kicker': '05 • ADVANCED COURSE',
        'fee': '₹25,000',
        'fee_regular': '₹25,000',
        'fee_emi': '₹30,000',
        'fee_initial': '₹5,000',
        'fee_monthly': '₹500 × 50 Months',
        'duration': 'Flexible',
        'image': '../assets/plywood-interior.jpg',
        'overview_points': [
            'Expert plywood joinery & custom furniture design',
            'Heavy-duty cupboard execution & hardware fitting',
            'Structural joinery & surface lamination techniques',
            'Complete pooja door, glass, & drawer assembly'
        ],
        'includes': [
            'Cupboard Work',
            'Box Type Cupboard',
            'Pooja Door',
            'Sliding Glass Work',
            'Open Glass Work',
            'Mirror Fixing',
            'Pooja Bell Fixing',
            'SS Drawer Fixing'
        ]
    },
    {
        'file': 'course-acrylic.html',
        'id': 'acrylic-course',
        'title': 'ACRYLIC INTERIOR COURSE',
        'kicker': '06 • ADVANCED COURSE',
        'fee': '₹30,000',
        'fee_regular': '₹30,000',
        'fee_emi': '₹35,000',
        'fee_initial': '₹5,000',
        'fee_monthly': '₹500 × 60 Months',
        'duration': 'Flexible',
        'image': '../assets/acrylic-interior.jpg',
        'overview_points': [
            'High-gloss luxury acrylic panel sheet application',
            'Seamless edge banding & modular kitchen design',
            'Surface care, maintenance & premium finishing',
            'Custom high-end residential interior execution'
        ],
        'includes': [
            'High-Gloss Acrylic Sheet Application',
            'Modular Kitchen Cupboard Work',
            'Seamless Edge Banding & Finishing',
            'Acrylic Surface Maintenance & Care'
        ]
    },
    {
        'file': 'course-basic-accessories.html',
        'id': 'basic-accessories',
        'title': 'ACCESSORIES – BASIC COURSE',
        'kicker': '07 • BEGINNER COURSE',
        'fee': '₹10,000',
        'fee_regular': '₹10,000',
        'fee_emi': '₹15,000',
        'fee_initial': '₹2,000',
        'fee_monthly': '₹500 × 26 Months',
        'duration': 'Flexible',
        'image': '../assets/basic-accessories.jpg',
        'overview_points': [
            'Essential interior hardware & fixture mounting',
            'Hinge adjustment, alignment & soft-close fittings',
            'Handle, knob, and basic accessory installation',
            'Precision alignment tools & hardware maintenance'
        ],
        'includes': [
            'Basic Hardware & Fixture Mounting',
            'Hinge Adjustment & Alignment',
            'Handle & Knob Installation',
            'Soft-Close Fitting Techniques'
        ]
    },
    {
        'file': 'course-advanced-accessories.html',
        'id': 'advanced-accessories',
        'title': 'ADVANCED ACCESSORIES FIXING COURSE',
        'kicker': '08 • ADVANCED COURSE',
        'fee': '₹20,000',
        'fee_regular': '₹20,000',
        'fee_emi': '₹25,000',
        'fee_initial': '₹5,000',
        'fee_monthly': '₹500 × 40 Months',
        'duration': 'Flexible',
        'image': '../assets/advanced-accessories.jpg',
        'overview_points': [
            'Modular kitchen baskets & pull-out drawer systems',
            'Tall unit, pantry, & wardrobe lift mechanisms',
            'Hydraulic lift-up fittings & heavy hardware',
            'Soft-close damper & architectural hardware mastery'
        ],
        'includes': [
            'Modular Kitchen Baskets & Pull-outs',
            'Tall Unit & Pantry Systems',
            'Wardrobe Lift & Sliding Mechanisms',
            'Hydraulic Lift-up Fittings'
        ]
    },
    {
        'file': 'course-estimation-measurement.html',
        'id': 'estimation-measurement',
        'title': 'ESTIMATION & MEASUREMENT COURSE',
        'kicker': '09 • PROFESSIONAL COURSE',
        'fee': '₹30,000',
        'fee_regular': '₹30,000',
        'fee_emi': '₹35,000',
        'fee_initial': '₹5,000',
        'fee_monthly': '₹500 × 60 Months',
        'duration': 'Flexible',
        'image': '../assets/estimation-measurement.jpg',
        'overview_points': [
            'On-site measurement & architectural floor plan drafting',
            'Bill of Materials (BOM) & Bill of Quantities (BOQ)',
            'Professional cost estimation & material calculation',
            'Project budgeting & client quotation preparation'
        ],
        'includes': [
            'Estimate',
            'Estimate Measurement',
            'Working Measurement',
            'BOM – Bill of Materials',
            'BOQ – Bill of Quantities'
        ]
    },
    {
        'file': 'course-interior-repair.html',
        'id': 'interior-repair',
        'title': 'INTERIOR REPAIR WORK COURSE',
        'kicker': '10 • PROFESSIONAL COURSE',
        'fee': '₹40,000',
        'fee_regular': '₹40,000',
        'fee_emi': '₹45,000',
        'fee_initial': '₹5,000',
        'fee_monthly': '₹500 × 80 Months',
        'duration': 'Flexible',
        'image': '../assets/interior-repair.jpg',
        'overview_points': [
            'Modular furniture restoration & structural repair',
            'Hinge, slide, and hardware replacement expertise',
            'Water damage sealing, re-lamination & refinishing',
            'On-site troubleshooting & maintenance mastery'
        ],
        'includes': [
            'Modular Furniture Restoration',
            'Hinge & Slide Replacement',
            'Water Damage Repair & Sealing',
            'Surface Re-lamination & Refinishing'
        ]
    }
]

template = '''<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} - Interior Gurukulam</title>
  <meta name="description" content="{title} at Interior Gurukulam. Complete practical training.">
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
    .training-container {{
      margin-top: 16px;
    }}
    .training-list {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(240px, 1fr));
      gap: 12px;
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
    .emi-box-detail {{
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
        <a href="../courses-new.html" class="active">ALL COURSES</a>
        <a href="../nri-training.html">NRI ONLINE TRAINING</a>
        <a href="../franchise-new.html">BUSINESS FRANCHISE</a>
        <a href="../joint-venture.html">INTERIOR OWNER JOINT VENTURE</a>
        <a href="../contact.html">CONTACT</a>
      </nav>
    </header>

    <main>
      <section class="course-detail-hero">
        <div class="container">
          <div style="font-size: 0.9rem; font-weight: 600; color: var(--terracotta); text-transform: uppercase;">
            <a href="../courses-new.html" style="color: inherit; text-decoration: none;">← Back to All Courses</a>
          </div>
          <div style="font-size: 0.85rem; font-weight: 700; color: var(--olive-deep); margin-top: 8px;">{kicker}</div>
          <h1 class="detail-title" style="margin-top: 4px;">{title}</h1>
          <p style="color: #666; font-weight: 600;">Duration: {duration} • Practical Interior Design Training</p>
        </div>
      </section>

      <section class="section">
        <div class="container">
          <div class="detail-layout">

            <!-- Left: Course Overview & Training Includes -->
            <div class="detail-card">
              <div class="detail-media">
                <img src="{image}" alt="{title}">
              </div>

              <h2 style="font-size: 1.4rem; color: var(--olive-deep); margin-bottom: 4px;">Course Highlights (Point by Point)</h2>
              <div class="overview-points-list">
                {overview_points_html}
              </div>

              <h2 style="font-size: 1.4rem; color: var(--olive-deep); margin-top: 32px; margin-bottom: 4px;">
                📚 Training Includes:
              </h2>
              <div class="training-container">
                <div class="training-list">
                  {includes_html}
                </div>
              </div>
            </div>

            <!-- Right: Pricing & Enroll Box -->
            <div>
              <div class="pricing-card">
                <div style="font-weight: 700; color: #777; font-size: 0.85rem; text-transform: uppercase;">Course Fee</div>
                <div class="price-main">{fee}</div>

                <div class="emi-box-detail">
                  <div style="font-weight: 700; color: var(--olive-deep); font-size: 0.95rem; margin-bottom: 10px;">
                    💳 Payment Breakdown
                  </div>
                  <div class="emi-row">
                    <span style="color: #666;">Regular Course Fee:</span>
                    <strong>{fee_regular}</strong>
                  </div>
                  <div class="emi-row">
                    <span style="color: #666;">EMI Course Fee:</span>
                    <strong>{fee_emi}</strong>
                  </div>
                  <div class="emi-row">
                    <span style="color: #666;">Initial Payment:</span>
                    <strong style="color: var(--terracotta);">{fee_initial}</strong>
                  </div>
                  <div class="emi-row">
                    <span style="color: #666;">Balance Monthly EMI:</span>
                    <strong>{fee_monthly}</strong>
                  </div>
                </div>

                <a href="../contact.html?course={id}" class="btn-enroll-primary">
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

for c in courses:
    overview_points_html = '\n'.join([
        f'                <div class="overview-point-item"><span class="overview-point-bullet">✦</span><span>{pt}</span></div>'
        for pt in c['overview_points']
    ])
    includes_html = '\n'.join([
        f'                  <div class="training-item"><span class="training-item-icon">✓</span><span>{item}</span></div>'
        for item in c['includes']
    ])
    html_content = template.format(
        title=c['title'],
        kicker=c['kicker'],
        image=c['image'],
        fee=c['fee'],
        fee_regular=c['fee_regular'],
        fee_emi=c['fee_emi'],
        fee_initial=c['fee_initial'],
        fee_monthly=c['fee_monthly'],
        duration=c['duration'],
        id=c['id'],
        overview_points_html=overview_points_html,
        includes_html=includes_html
    )
    filepath = os.path.join(courses_dir, c['file'])
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html_content)
    print(f'Generated page inside courses/ folder: courses/{c["file"]}')
