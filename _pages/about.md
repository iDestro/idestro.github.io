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

<div class="lang-en" lang="en" markdown="1">
I am an Algorithm Development Expert at [SUPCON](https://global.supcon.com/). I received my Ph.D. from the College of [Computer Science and Technology](http://www.cs.zju.edu.cn/) at [Zhejiang University](http://www.zju.edu.cn/) in December 2025, advised by Prof. [Yang Yang](http://yangy.org/) and [Yin Zhang](https://mypage.zju.edu.cn/yinzhang).

My research focuses on **time series modeling and intelligent decision-making for the process industries**. I aim to build models that learn transferable dynamics from multivariate time series and support forecasting, simulation, and industrial decisions. My current interests include:

- **Time series foundation models:** learning temporal patterns and cross-variable dependencies at scale, with a focus on multivariate forecasting, conditioning on future-known covariates, and generalization across operating conditions and industrial processes.
- **Dynamics and causal modeling:** studying how models learn process responses to control inputs, how causal structure and process knowledge can inform modeling, and how to evaluate models for simulation and control beyond forecasting accuracy.
- **Industrial AI agents:** combining time series models, LLMs, and engineering tools to support predictive maintenance, anomaly diagnosis, and operational decision-making.

My earlier work spans spatiotemporal forecasting in chemical sensor networks and traffic networks, foundation models for power systems, and cross-subject seizure detection. My work has appeared at NeurIPS and KDD <a href='https://scholar.google.com/citations?user=uDVGV84AAAAJ'><img src="https://img.shields.io/endpoint?url={{ url | url_encode }}&logo=Google%20Scholar&labelColor=f6f6f6&color=9cf&style=flat&label=citations" alt="Google Scholar citations"></a>.

I welcome collaborations on time series foundation models, dynamical systems, and industrial AI. Please feel free to contact me at [shihao.tu@zju.edu.cn](mailto:shihao.tu@zju.edu.cn).
</div>

<div class="lang-zh" lang="zh" markdown="1">
我是涂世豪，现任[中控](https://global.supcon.com/)算法开发专家。2025年12月，我在[浙江大学](http://www.zju.edu.cn/)[计算机科学与技术学院](http://www.cs.zju.edu.cn/)获得博士学位，师从[杨洋](http://yangy.org/)教授、[张引](https://mypage.zju.edu.cn/yinzhang)教授。

我的研究聚焦于**面向流程工业的时间序列建模与智能决策**，希望从多变量时序数据中学习可迁移的动力学规律，支撑预测、仿真与工业决策。目前主要关注：

- **时间序列基础模型**：通过大规模预训练学习时间模式与变量间依赖，重点研究多变量预测、未来已知协变量条件下的建模，以及跨工况、跨装置的泛化能力。
- **动力学与因果建模**：研究模型如何学习工业过程对控制输入的响应，如何利用因果结构与工艺知识辅助建模，以及如何超越预测误差，从仿真与控制效果评价模型能力。
- **工业智能体（Agent）**：结合时序模型、大语言模型与工程工具，探索预测性维护、异常诊断与运行决策辅助。

此前，我的研究涉及化学传感器网络与交通网络的时空预测、电力系统基础模型，以及跨受试者癫痫检测，相关工作发表于 NeurIPS、KDD 等国际会议 <a href='https://scholar.google.com/citations?user=uDVGV84AAAAJ'><img src="https://img.shields.io/endpoint?url={{ url | url_encode }}&logo=Google%20Scholar&labelColor=f6f6f6&color=9cf&style=flat&label=citations" alt="Google Scholar 引用数"></a>。

欢迎就时序基础模型、动力系统建模与工业 AI 开展交流合作：[shihao.tu@zju.edu.cn](mailto:shihao.tu@zju.edu.cn)。
</div>

<h1 id="-news"><span class="lang-en">🔥 News</span><span class="lang-zh">🔥 新闻</span></h1>
- *2026.09*: <span class="lang-en">&nbsp;🎉🎉 Our paper “Can Time-Series Foundation Models Serve as Simulators for Process Control?” has been accepted by the FMTS Workshop at NeurIPS 2026.</span><span class="lang-zh">&nbsp;🎉🎉 论文《Can Time-Series Foundation Models Serve as Simulators for Process Control?》被 NeurIPS 2026 FMTS Workshop 录用。</span>
- *2026.05*: <span class="lang-en">&nbsp;🎉🎉 Our paper ``STUNet`` has been accepted by KDD 2026.</span><span class="lang-zh">&nbsp;🎉🎉 论文 ``STUNet`` 被 KDD 2026 录用。</span>
- *2026.01*: <span class="lang-en">&nbsp;Joined [SUPCON](https://global.supcon.com/) as an Algorithm Development Expert.</span><span class="lang-zh">&nbsp;入职[中控](https://global.supcon.com/)，担任算法开发专家。</span>
- *2025.12*: <span class="lang-en">&nbsp;Received my Ph.D. from Zhejiang University.</span><span class="lang-zh">&nbsp;于浙江大学获得博士学位。</span>
- *2025.05*: <span class="lang-en">&nbsp;🎉🎉 Our paper ``ASTNet`` has been accepted by KDD 2025.</span><span class="lang-zh">&nbsp;🎉🎉 论文 ``ASTNet`` 被 KDD 2025 录用。</span>
- *2024.09*: <span class="lang-en">&nbsp;🎉🎉 Our papers ``PowerPM`` and ``DMNet`` have been accepted by NeurIPS 2024.</span><span class="lang-zh">&nbsp;🎉🎉 论文 ``PowerPM`` 与 ``DMNet`` 被 NeurIPS 2024 录用。</span>

<h1 id="-publications"><span class="lang-en">📝 Publications</span><span class="lang-zh">📝 论文</span></h1>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">NeurIPS 2026 · FMTS Workshop</div><img src='images/CTSFM.png' alt="Evaluation of response prediction, candidate control selection, and executed control" width="100%"></div></div>
<div class='paper-box-text' markdown="1">
Can Time-Series Foundation Models Serve as Simulators for Process Control? \\
**Shihao Tu**, Wenyue Ding, Peixuan Ding, Zhaoxiang Wu, Huiyang Wang, Xu Zhang, Yuxin Chen, Yicheng Lu, Xiang Shao, Yangjie Zheng \\
<span class="lang-en">This study evaluates whether time-series foundation models can serve as simulators for process control, examining physical response fidelity, candidate evaluation, and closed-loop performance. On the tested noiseless linear processes, lower forecasting error does not always translate into better control, highlighting the need to jointly evaluate prediction, decision-making, and execution.</span><span class="lang-zh">本研究评估时序基础模型能否作为过程控制的仿真器，从物理响应保真度、候选控制方案评估和闭环控制效果三个层面进行检验。在所测试的无噪声线性过程中，较低的预测误差并不总能带来更好的控制效果，表明面向控制的模型评估需要同时考察预测、决策与执行。</span>
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">KDD 2026</div><img src='images/STUNet.png' alt="Architecture diagram of STUNet for traffic forecasting" width="100%"></div></div>
<div class='paper-box-text' markdown="1">
[Unified Spatio-Temporal Tokens are Bases for Generalizable Traffic Forecasting](https://yangy.org/works/timeseries/KDD26_STUNet.pdf) \\
**Yujun Chen\***, **Shihao Tu\***, Wenyue Ding, Yicheng Lu, Qingkai Ren, Yangjie Zheng, [Yang Yang](http://yangy.org/) (*: equal contribution)\\
<span class="lang-en">STUNet (Spatio-Temporal Unified Network) explicitly encodes spatial structure into unified tokens and integrates them with temporal representations for generalizable traffic forecasting. It tokenizes the adjacency matrix into spatial patches and uses query-aggregate attention to capture upstream–downstream dependencies across traffic networks.</span><span class="lang-zh">STUNet 面向交通流预测中的跨路网泛化问题，把空间结构显式编码为统一表征，再与时间信息结合。模型将邻接矩阵划分成空间 token，并用查询–聚合注意力刻画上下游依赖，从而在不同交通网络上保持较好的预测能力。</span>
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">KDD 2025</div><img src='images/ASTNet.png' alt="Architecture diagram of ASTNet for chemical sensor forecasting" width="100%"></div></div>
<div class='paper-box-text' markdown="1">
ASTNet: Asynchronous Spatio-Temporal Network for Large-Scale Chemical Sensor Forecasting \\
**Shihao Tu**, [Yang Yang](http://yangy.org/), Wenyue Ding, Yicheng Lu, Qingkai Ren, Yupeng Zhang, [Yin Zhang](https://mypage.zju.edu.cn/yinzhang) \\
<span class="lang-en">ASTNet proposes a novel approach for real-time spatiotemporal forecasting in chemical sensor networks, addressing computational latency and complex spatial dependencies. It features asynchronous modeling to reduce latency and dynamic graph fusion to enhance robustness.</span><span class="lang-zh">ASTNet 面向大规模化学传感器网络的实时时空预测：用异步建模降低计算时延，并用动态图融合更好地刻画复杂的空间依赖。</span>
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">NeurIPS 2024</div><img src='images/PowerPM.png' alt="Architecture diagram of PowerPM for power systems" width="100%"></div></div>
<div class='paper-box-text' markdown="1">
PowerPM: Foundation Model for Power Systems \\
**Shihao Tu\***, Yupeng Zhang\*, [Jing Zhang](https://xiaojingzi.github.io/), Zhendong Fu, [Yin Zhang](https://mypage.zju.edu.cn/yinzhang), [Yang Yang](http://yangy.org/) (*: equal contribution)\\
<span class="lang-en">PowerPM is an advanced model for electricity time series (ETS) analysis, designed to address the complexities of hierarchical and temporal data for power systems applications, focusing on electricity usage forecasting, grid stability and consumer behaviour analysis.</span><span class="lang-zh">PowerPM 是面向电力系统电量时间序列的基础模型，同时建模层次结构与时间依赖，可用于负荷预测、电网稳定评估和用户行为分析。</span>
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">NeurIPS 2024</div><img src='images/DMNet.jpg' alt="Architecture diagram of DMNet for seizure detection" width="100%"></div></div>
<div class='paper-box-text' markdown="1">
DMNet: Self-comparison Driven Model for Subject-independent Seizure Detection \\
**Shihao Tu**, [Linfeng Cao](https://caolinfeng.github.io/homepage/), [Daoze Zhang](https://daozezhang.github.io/),
[Junru Chen](https://mrnobodycali.github.io/), Lvbin Ma, [Yin Zhang](https://mypage.zju.edu.cn/yinzhang), [Yang Yang](http://yangy.org/) \\
<span class="lang-en">Difference Matrix-based Neural Network (DMNet) addresses the domain shift in iEEG signals across different subjects by leveraging a self-comparison mechanism for subject-independent automatic seizure detection.</span><span class="lang-zh">DMNet 针对不同患者颅内脑电信号的分布差异，借助自比较机制缓解域偏移，从而实现跨受试者的癫痫发作自动检测。</span>
</div>
</div>

<h1 id="-work"><span class="lang-en">💼 Work</span><span class="lang-zh">💼 工作</span></h1>
- <span class="lang-en">*2026.01.06 - Present*, Algorithm Development Expert, [SUPCON](https://global.supcon.com/), Hangzhou, China.</span><span class="lang-zh">*2026.01.06 – 至今*，算法开发专家，[中控](https://global.supcon.com/)，杭州。</span>

<h1 id="-internships"><span class="lang-en">💻 Internships</span><span class="lang-zh">💻 实习</span></h1>
- <span class="lang-en">*2024.11.13 - 2026.01.05*, [SUPCON](https://global.supcon.com/), Hangzhou, China.</span><span class="lang-zh">*2024.11.13 – 2026.01.05*，[中控](https://global.supcon.com/)，杭州。</span>
- <span class="lang-en">*2025.02.18 - 2025.06.15*, [Zhipu AI](https://zhipu.ai/), Beijing, China.</span><span class="lang-zh">*2025.02.18 – 2025.06.15*，[智谱 AI](https://zhipu.ai/)，北京。</span>
