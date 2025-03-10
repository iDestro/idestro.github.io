---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}

<span class='anchor' id='about-me'></span>

I am the 5-th-year Ph.D. student in the college of [Computer Science and Technology](http://www.cs.zju.edu.cn/) at 
[Zhejiang University](http://www.zju.edu.cn/), fortunately advised by Prof. [Yang Yang](http://yangy.org/) and [Yin Zhang](https://mypage.zju.edu.cn/yinzhang).

My research focuses are refined to include large-scale time series analysis, the development of foundation model for time series, and an exploration of engaging topics and the latest advancements in technology within this domain.
I have published several papers <a href='https://scholar.google.com/citations?user=uDVGV84AAAAJ'><img src="https://img.shields.io/endpoint?url={{ url | url_encode }}&logo=Google%20Scholar&labelColor=f6f6f6&color=9cf&style=flat&label=citations"></a> 
at the top international AI conferences such NeurIPS.

Currently, I am exploring the application of LLM in time series analysis to tackle complex industrial problems.
If you are seeking any form of academic cooperation, please feel free to touch me. Meanwhile, **I am actively seeking job opportunities in the industry. If there are any relevant openings, I would greatly appreciate you reaching out. Thank you!**


# 🔥 News
- *2024.09*: &nbsp;🎉🎉 Our papers “PowerPM” and “DMNet” have been accepted by NeurIPS 2024.

# 📝 Publications 

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">NeurIPS 2024</div><img src='images/PowerPM.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">
PowerPM: Foundation Model for Power Systems \\
**Shihao Tu\***, Yupeng Zhang\*, [Jing Zhang](https://xiaojingzi.github.io/), Zhendong Fu, [Yin Zhang](https://mypage.zju.edu.cn/yinzhang), [Yang Yang](http://yangy.org/) (*: equal contribution)\\
PowerPM is an advanced model for electricity time series (ETS) analysis, designed to address the complexities of hierarchical and temporal data for power systems applications, focusing on electricity usage forecasting, grid stability and consumer behaviour analysis.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">NeurIPS 2024</div><img src='images/DMNet.jpg' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">
DMNet: Self-comparison Driven Model for Subject-independent Seizure Detection \\
**Shihao Tu**, [Linfeng Cao](https://caolinfeng.github.io/homepage/), [Daoze Zhang](https://daozezhang.github.io/), 
[Junru Chen](https://mrnobodycali.github.io/), Lvbin Ma, [Yin Zhang](https://mypage.zju.edu.cn/yinzhang), [Yang Yang](http://yangy.org/) \\
Difference Matrix-based Neural Network (DMNet) addresses the domain shift in iEEG signals across different subjects by 
leveraging a self-comparison mechanism for subject-independent automatic seizure detection.
</div>
</div>

# 💻 Internships
- *2024.10 - Now*, [SUPCON](https://global.supcon.com/), Hangzhou, China.
- *2025.2 - Now*, [Zhipu AI](https://zhipu.ai/), Beijing, China.