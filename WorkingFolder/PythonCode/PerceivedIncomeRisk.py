# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     cell_metadata_json: true
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.6.0
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# # Introduction
#
#
# Income risks matter for both individual behaviors and aggregate outcomes. With identical expected income and homogeneous risk preferences, different degrees of risks lead to different saving/consumption and portfolio choices. This is well understood in models in which agents are inter-temporally risk-averse, or prudent (<cite data-cite="kimball1990precautionary">(Kimball, 1990)</cite>, <cite data-cite="carroll2001liquidity">(Carroll and Kimball, 2001)</cite>), and the risks associated with future marginal utility motivate precautionary motives. Since it is widely known from the empirical research that idiosyncratic income risks are at most partially insured (<cite data-cite="blundell_consumption_2008">(Blundell, et al., 2008)</cite>) or because of borrowing constraints, such behavioral regularities equipped with market incompleteness leads to ex-post unequal wealth distribution and different degrees of marginal propensity to consume (MPC) (<cite data-cite="huggett1993risk">(Huggett,1993)</cite>, <cite data-cite="aiyagari1994uninsured">(Aiyagari, 1994)</cite>). This has important implications for the transmission of macroeconomic policies\footnote{<cite data-cite="krueger2016macroeconomics">(Krueger, et al., 2016)</cite>, <cite data-cite="kaplan2018monetary">(Kaplan, et al., 2018)</cite>, <cite data-cite="auclert2019monetary">(Auclert, 2019)</cite>, <cite data-cite="bayer2019precautionary">(Bayer, et al., 2019)</cite>.}   
#
# One important assumption prevailing in macroeconomic models with uninsured risks is that agents have a perfect understanding of the income risks. Under the assumption, economists typically estimate the income process based on micro income data and then treat the estimates as the true model parameters known by the agents making decisions in the model\footnote{For example, <cite data-cite="krueger2016macroeconomics">(Krueger, et al.,2016)</cite>, <cite data-cite="bayer2019precautionary">(Bayer, et al., 2019)</cite>.}. But given the mounting evidence that people form expectations in ways deviating from full-information rationality, leading to perennial heterogeneity in economic expectations held by micro agents, this assumption seems to be too stringent. To the extent that agents make decisions based on their *respective* perceptions, understanding the *perceived* income risk profile and its correlation structure with other macro variables are the keys to explaining their behavior patterns.
#
# The contributions of this paper are both theoretical and empirical. In the theory, it constructs a subjective model of learning that features agents' imperfect understanding of the size as well as the nature of income risks. In terms of the size, the imperfect understanding is modeled as a lack of knowledge of the true parameter of an assumed income process. Agents form their best guess about the parameters by learning from the past experienced income of their own as well as others. Such experience-based learning mechanisms engenders the perceived risks to be dependent on age, generation, and macroeconomic history. At the same time, the imperfect understanding of the nature of risks is captured by assuming that individuals do not understand if the income risks are commonly shared aggregate shock or idiosyncratic ones. They learn about the model based on a subjective determination of the nature of the past shocks, which is called *attribution* in this paper. The role of attribution in perception formation and prediction has been long developed in social pyschology literature\footnote{See <cite data-cite="heider1958psychology">(Heider, 1958)</cite>, <cite data-cite="kelley1967attribution">(Kelley, 1967)</cite>, <cite data-cite="kelley1980attribution">(Kelley and Michela, 1980)</cite>, <cite data-cite="fiske1991social">(Fiske and Taylor, 1991)</cite>, and <cite data-cite="weiner2010attribution">(Weiner, 2010)</cite>.}. This paper adapts the idea into a learning framework used by economists. With different subjective attributions, agents arrive at different degrees of model parameter uncertainty, thus different perceptions about income risks. 
#
# This general framework allows me to explore the implications of different attributions. For instance, I show that a higher degree of external attribution, i.e. perceiving the shocks to be common ones instead of idiosyncratic ones, leads to higher risk perceptions. This introduces a well-specified channel through which some imperfect understanding of the nature of shocks leads to differences in risk perceptions. The intuition for this is straightforward. As an econometrician would perfectly understand, learning comes from variations in the sample either cross-sectionally or over time. As agents subjectively perceive the correlation of her own income shocks and others' to be higher, the cross-sectional variation from the sample useful to the learning is reduced, which leads to higehr uncertainty associated with the parameter estimate. I show such a mechanism is generalizable to different assumed income processes such as AR(1) or one with permanent/transitory components of time-varying risks. 
#
# Incorporating attribution in learning allows it possible to explore the implications of possible mischaracterization of experienced shocks. Among various possible deviations, I explore a particular kind of attribution error which is reminiscent of the "self-serving bias" in the social psychology. In particular, it assumes that people have a tendency to external (internal) attribution in the face of negative (positive) experiences. By allowing the subjective correlation to be a function of the recent experience such as income change, the model neatly captures this psychological tendency. What is interesting is that such a state-dependence of attribution in learning may help explain why the average perceived risk is lower for the high-income groups than the low-income ones. In the presence of aggregate risks, it also generates counter-cyclical patterns of the average perceived risks, i.e. bad times are associated with high subjective risks. In addition, such a mechanism of asymmetric attribution may also help explain perception patterns by people at different income distributions about their relative position in the society. For instance, based on matched administrative records of income and perception surveys in Danmark, <cite data-cite="hvidberg2020social">(Hvidberg et al, 2021)</cite> found that the high-income group tends to underestimate its rank in the distribution while the low-income group is prone to overestimation. In my model, this can be explained by the fact that high-income(low-income) groups on average are prone to internal-attribution(external attribution), thus perceiving higher (lower) ex-post income inequality, leading to underperceived(overperceived) ranks. Drawing on another line of findings in their paper, it suggests that income perceptions not only affect micro/macro decisions, but also affect people' views about fairness and redistribution policies. In that regard, my model could be potentially useful in explaining differences in fairness attitudes. 
#
# Empirically, the paper sheds light on the perceptions of income risks by utilizing the recently available density forecasts of labor income surveyed by New York Fed's Survey of Consumer Expectation (SCE). What is special about this survey is that agents are asked to provide histogram-type forecasts of their earning growth over the next 12 months together with a set of expectational questions about the macroeconomy. When the individual density forecast is available, a parametric density estimation can be made to obtain the individual-specific subjective distribution. And higher moments reflecting the perceived income risks such as variance, as well as the asymmetry of the distribution such as skewness allow me to directly characterize the perceived risk profile without relying on external estimates from cross-sectional microdata. This provides the first-hand measured perceptions on income risks that are truly relevant to individual decisions.
# Perceived income risks exhibits a number of important patterns that are consistent with the predictions of my model of experience-based learning with subjective attribution. 
#
# - Higher experienced volatility is associated with higher perceived income risks. This helps explain why perceived risks differ systematically across different generations, who have experienced different histories of the income shocks. Besides, perceived risks declines with one's age.
#
# - Perceived income risks have a non-monotonic correlation with the current income, which can be best described as a skewed U shape. Perceived risk decreases with current income over the most range of income values follwed by an uppick in perceived risks for high-income group. 
#  
# - Perceived income risks are counter-cyclical with the labor market conditions or broadly business cycles. I found that average perceived income risks by U.S. earners are negatively correlated with the current labor market tightness measured by wage growth and unemployment rate. Besides, earners in states with higher unemployment rates and low wage growth also perceive income risks to be higher. This bears similarities to but important difference with a few previous studies that document the counter-cyclicality of income risks estimated by cross-sectional microdata (<cite data-cite="guvenen2014nature">(Guvenen, et al., 2014)</cite>, <cite data-cite="catherine_countercyclical_2019">(Catherine, 2019)</cite>). 
#
# - Perceived income risks translate into economic decisions in a way consistent with precautionary saving motives. In particular, households with higher income risk perceptions expect a higher growth in expenditure, i.e. lower consumption today versus tomorrow.  
#
#
# These patterns suggest that individuals have a roughly good yet imperfect understanding of their income risks. Good, in the sense that subjective perceptions are broadly consistent with the realization of cross-sectional income patterns. This is attained in my model because agents learn from past experiences, roughly as econometricians do. In contrast, subjective perceptions are imperfect in that bounded rationality prevents people from knowing about the true income process perfectly, which even hardworking economists equipped with different advanced econometrical techniques and a larger sample of income data cannot easily claim to have.
#
# As illustrated by much empirical work of testing the rationality in expectation formation, it is admittedly challenging to separately account for the differences in perceptions driven by the "truth" and the part driven by the pure subjective heterogeneity. The most straightforward way seems to be to treat econometrician's external estimates of the income process as the proxy to the truth, for which the subjective surveys are compared. But this approach implicitly assumes that econometricians correctly specify the model of the income process and ignores the possible superior information that is available only to the people in the sample but not to econometricians. The model built in this paper reconciles both possibilities by modeling agents as boundedly rational econometricians subject to model misspecification. 
#  
# Finally, the subjective learning model will be incorporated into an otherwise standard life-cycle consumption/saving model with uninsured idiosyncratic and aggregate risks. Experience-based learning makes income expectations and risks state-dependent when agents make dynamically optimal decisions at each point of the time. In particular, higher perceived risks will induce more precautionary saving behaviors. If this perceived risk is state-dependent on recent income changes, it will potentially shift the distribution of MPCs along income deciles, therefore, amplify the channels aggregate demand responses to shocks. 
#
#      
# ##  Related literature
#
# From both theoretical and empirical points of view, this paper is an extension of experience-based learning that is developed to account for how experiences shape people's economic expectations and subsequent behaviors. This paper extends the framework in three directions. First, building on the work that shows that experiences affect expectations\footnote{A very close line of literature focuses on the impacts of experience on preferences, such as risk-taking <cite data-cite="malmendier2011depression">Malmendier and Nagel, 2011</cite>.}, such as inflation (<cite data-cite="malmendier2015learning">(Malmendier and Nagel, 2015)</cite>) risky asset return (<cite data-cite="malmendier2019investor">(Malmendier, et al., 2019)</cite>), and housing prices (<cite data-cite="kuchler2019personal">(Kuchler and Zafar, 2019)</cite>). I show in the same framework that perceptions of second moments such as income risks can be influenced by the experienced outcome as well as its volatility. This is confirmed by the empirical evidence using the recently available density survey. This contributes to the understanding of how experiences of first and second moments shape perceptions in higher moments\footnote{For similar evidence for the house price, see <cite data-cite="kuchler2019personal">(Kuchler and Zafar, 2019)</cite>.}.Second, I introduce the subjective attribution into the framework to allow for the possibility of an imperfect understanding of the nature of the shocks. Finally, this paper tries to build such a belief-formation mechanism into workhorse models of consumption/saving to explore its macroeconomic implications. 
#
# Besides, this paper is relevant to four lines of literature. First, it is related to an old but recently reviving interest in studying consumption/saving behaviors in models incorporating imperfect expectations and perceptions. For instance, the closest to the current paper, <cite data-cite="pischke1995individual">(Pischke, 1995)</cite> explores the implications of the incomplete information about aggregate/individual income innovations by modeling agent's learning about inome component as a signal extraction problem. <cite data-cite="wang2004precautionary">(Wang, 2004)</cite> extends the framework to incorporate precautionary saving motives. In a similar spirit, <cite data-cite="carroll_sticky_2018">(Carroll et al. 2018)</cite> reconciles the low micro-MPC and high macro-MPCs by introducing to the model an information rigidity of households in learning about macro news while being updated about micro news. <cite data-cite="rozsypal_overpersistence_2017">(Rozsypal and Schlafmann, 2017)</cite> found that households' expectation of income exhibits an over-persistent bias using both expected and realized household income from Michigan household survey. The paper also shows that incorporating such bias affects the aggregate consumption function by distorting the cross-sectional distributions of marginal propensity to consume(MPCs) across the population.  <cite data-cite="lian2019imperfect">(Lian, 2019)</cite> shows that an imperfect perception of wealth accounts for such phenomenon as excess sensitivity to current income and higher MPCs out of wealth than current income and so forth. My paper has a similar flavor to all of these works in that I also explore the behavioral implications of households' perceptual imperfection. But it has important two distinctions. First, this paper focuses on higher moments such as income risks. Second, most of these existing work either considers inattention of shocks or bias introduced by the model parameter, none of these explores the possible misperception of the nature of income shocks. \footnote{For instance, <cite data-cite="pischke1995individual">(Pischke, 1995)</cite> assumes that agents know perfectly about the variance of permanent and transitory income so that they could filter the two components from observable income changes. This paper instead assumes that that the agents do not observe the two perfectly.} 
#
#
# Second, empirically, this paper also contributes to the literature studying expectation formation using subjective surveys. There has been a long list of "irrational expectation" theories developed in recent decades on how agents deviate from full-information rationality benchmark, such as sticky expectation, noisy signal extraction, least-square learning, etc. Also, empirical work has been devoted to testing these theories in a comparable manner (<cite data-cite="coibion2012can">(Coibion and Gorodnichenko, 2012)</cite>, <cite data-cite="fuhrer2018intrinsic">(Fuhrer, 2018)</cite>). But it is fair to say that thus far, relatively little work has been done on individual variables such as labor income, which may well be more relevant to individual economic decisions. Therefore, understanding expectation formation of the individual variables, in particular, concerning both mean and higher moments, will provide fruitful insights for macroeconomic modeling assumptions. 
#
# Third, the paper is indirectly related to the research that advocated for eliciting probabilistic questions measuring subjective uncertainty in economic surveys (<cite data-cite="manski_measuring_2004">(Manski, 2004)</cite>, <cite data-cite="delavande2011measuring">(Delavande et al. 2011)</cite>, <cite data-cite="manski_survey_2018">(Manski, 2018)</cite>). Although the initial suspicion concerning to people’s ability in understanding, using and answering probabilistic questions is understandable, <cite data-cite="bertrand_people_2001">(Bertrand and Mullainathan,2001)</cite> and other works have shown respondents have the consistent ability and willingness to assign a probability (or “percent chance”) to future events. <cite data-cite="armantier_overview_2017">(Armantier et al. 2017)</cite>  have a thorough discussion on designing, experimenting and implementing the consumer expectation surveys to ensure the quality of the responses. Broadly speaking, the advocates have argued that going beyond the revealed preference approach, availability to survey data provides economists with direct information on agents’ expectations and helps avoids imposing arbitrary assumptions. This insight holds for not only point forecast but also and even more importantly, for uncertainty, because for any economic decision made by a risk-averse agent, not only the expectation but also the perceived risks matter a great deal.
#
# Lastly, the idea of this paper echoes with an old problem in the consumption insurance literature: 'insurance or information' (<cite data-cite="pistaferri_superior_2001">Pistaferri, 2001</cite>, <cite data-cite="kaufmann_disentangling_2009">Kaufmann and Pistaferri, 2009</cite>,<cite data-cite="meghir2011earnings">Meghir et al. 2011</cite>). In any empirical tests of consumption insurance or consumption response to income, there is always a worry that what is interpreted as the shock has actually already entered the agents' information set or exactly the opposite. For instance, the notion of excessive sensitivity, namely households consumption highly responsive to anticipated income shock, maybe simply because agents have not incorporated the recently realized shocks that econometricians assume so (<cite data-cite="flavin_excess_1988">Flavin,1988</cite>). Also, recently, in the New York Fed [blog](https://libertystreeteconomics.newyorkfed.org/2017/11/understanding-permanent-and-temporary-income-shocks.html), the authors followed a similar approach to decompose the permanent and transitory shocks. My paper shares a similar spirit with these studies in the sense that I try to tackle the identification problem in the same approach: directly using the expectation data and explicitly controlling what are truly conditional expectations of the agents making the decision. This helps economists avoid making assumptions on what is exactly in the agents' information set. What differentiates my work from other authors is that I focus on higher moments, i.e. income risks and skewness by utilizing the recently available density forecasts of labor income. Previous work only focuses on the sizes of the realized shocks and estimates the variance of the shocks using cross-sectional distribution, while my paper directly studies the individual specific variance of these shocks perceived by different individuals.  
#

# + {"code_folding": [0], "hide_output": true}
## import libraries for inserting figures 

import matplotlib.pyplot as plt
import numpy as np
# %matplotlib inline 
from IPython.display import display, Image
import matplotlib.image as mpimg
import os
import pandas as pd

path = os.getcwd()

"""
def in_ipynb():
    try:
        if str(type(get_ipython())) == "<class 'ipykernel.zmqshell.ZMQInteractiveShell'>":
            return True
        else:
            return False
    except NameError:
        return False

# Determine whether to make the figures inline (for spyder or jupyter)
# vs whatever is the automatic setting that will apply if run from the terminal
if in_ipynb():
    # %matplotlib inline generates a syntax error when run from the shell
    # so do this instead
    get_ipython().run_line_magic('matplotlib', 'inline') 
else:
    get_ipython().run_line_magic('matplotlib', 'auto') 
    
"""
# -

# # Theoretical framework 
#
# ## Income process and risk perceptions
#
# Log income of individual $i$ from cohort $c$ at time $t$ follows the following process (<cite data-cite="meghir2004income">(Meghir and Pistaferri(2004))</cite>). Cohort $c$ represents the year of entering the job market. It contains a predictable component $z$, and a stochastical component $e$. The latter consists of aggregate component $g$, idiosyncratic permanent $p$, MA(1) component $\eta$ and a transitory component $\psi$. Here I do not consider unemployment risk since the perceived risk measured in the survey conditions on staying employed.
#
# \begin{equation}
# \begin{split}
# & y_{i,c,t} = z_{i,c,t}+e_{i,c,t} \\
# & e_{i,c,t}=g_t+p_{i,c,t}+\eta_{i,c,t}+\psi_{i,c,t}  \\
# & g_t = g_{t-1} + \xi_{t} \\
# & p_{i,c,t} = p_{i,c,t-1}+\theta_{i,c,t} \\
# & \eta_{i,c,t} = \phi\epsilon_{i,c,t-1}+\epsilon_{i,c,t}
# \end{split}
# \end{equation}
#
# All shocks including the aggregate $\xi_t$, and idiosyncratic ones follow normal distributions, with zero means and time-invariant variances denoted as $\sigma^2_{\xi}$, $\sigma^2_{\theta}$,$\sigma^2_{\epsilon}$,$\sigma^2_{\psi}$. Hypothetically, these variances could differ both across cohorts and time. I focus on the most simple case here and results with cohort-specific income risks are reported in the appendix. 
#
# Income growth from $t$ to $t+1$ consists predictable changes in $z_{i,c,t+1}$, and those from realized income shocks. 
#
# \begin{equation}
# \begin{split}
# \Delta y_{i,c,t+1} & =  \Delta z_{i,c,t+1}+\Delta e_{i,c,t} \\
# &= \Delta z_{i,c,t+1}+\xi_{t+1}+\theta_{i,c,t+1}+\epsilon_{i,c,t+1}+(\phi-1)\epsilon_{i,c,t}+\psi_{i,c,t+1}
# \end{split}
# \end{equation}
#
#
# All shocks that have realized till $t$ are observed by the agent at time $t$. Therefore, under full-information rational expectation(FIRE), namely when the agent perfectly knows the income process and parameters, the perceived income risks or the perceived variance of income growth from $t$ to $t+1$ is equal to the following.
#
# \begin{equation}
# Var_{t}^*(\Delta y_{i,c,t+1}) =Var_{t}^*(\Delta e_{i,c,t+1}) =   \sigma^2_\xi+\sigma^2_\theta + \sigma^2_\epsilon+\sigma^2_\psi 
# \end{equation}
#
# FIRE has a number of testable predictions about the behaviors of perceived risks. 
#
# - First, agents who share the same income process have no disagreements on perceived risks. This can be checked by comparing within-cohort/group dispersion in perceived risks. 
#
# - Second, the perceived risks under such an assumed income process are not dependent on past/recent income realizations. This can be tested by estimating the correlation between perceived risks and past income realizations or their proxies if the latter is not directly observed. 
#
# - Third, under the assumed progress, the variances of different-natured shocks sum up to exactly the perceived income risks and the loadings of all components are all positive. I report detailed derivations and proofs in the Appendix that these predictions are robust to the alternative income process and the time-aggregation problem discussed in the literature. The latter arises when the underlying income process is set at a higher frequency than the observed frequency of reported income or income expectations. This will cause different sizes of loadings of all future shocks to perceived annual risk but does not change the positivity of the loadings from different components onto perceived risk. 
#
# The challenge of testing the third prediction is that the risk parameters are not directly observable. Econometricians and modelers usually estimate them relying upon cross-sectional moment information from some panel data and take them as the model parameters understood perfectly by the agents. I can therefore use econometricians' best estimates using past income data as the FIRE benchmark (I will discuss the concerns of this approach later).
# Assuming the unexplained income residuals from this estimation regression is $\hat e_{i,t}= y_{i,c,t}-\hat z_{i,c,t}$($\hat z_{i,c,t}$ is the observable counterpart of $z_{i,c,t}$ from data). The unconditional cross-sectional variance of the change in residuals(equivalent to the ``income volatility'' or ``instability'' in the literature) is the following. Let's call this growth volatility. It can be further decomposed into different components in order to get the component-specific risk. 
#
# \begin{equation}
# Var(\Delta \hat e_{i,c,t}) = \hat\sigma^2_\xi+\hat\sigma^2_\theta + ((1-\phi)^2+1)\hat\sigma^2_\epsilon+\hat\sigma^2_\psi 
# \end{equation}
#
# Notice the unconditional growth volatility overlaps with the FIRE perceived risk in every component of the risks. But it is unambiguously greater than the perceived risk under FIRE because econometricians' do not directly observe the MA(1) shock from $t-1$. But this suffices to suggest that growth volatility is positively correlated with perceived risk. 
#
# Corresponding to the growth volatility, let's also define the level volatility as the cross-sectional variance of the levels of the residuals, which is denoted by $Var(\hat e_{i,t})$. Different from growth volatility, it includes the cumulative volatility from all the past permanent shocks as well as the MA shock from $t-1$, all of which are not correlated with the perceived risk under FIRE. Therefore, it any it will have only a weak correlation with perceived risks under FIRE. 
#
# This suggests the fourth testable prediction stated as below. Since we can obtain $Var(\Delta \hat e_{i,c,t})$ and $Var(\hat e_{i,c,t})$ using past income data, we can test this prediction.   
#
# - Growth volatility and risk perceptions are positively correlated. In contrast, level volatility is only weakly correlated with perceived risks. 
#
# It is worth asking how sensitive this prediction is to possible model misspecification of the income process in the first place. We consider three most common issues in the literature regarding the income risks. 
#
# - __Permanent versus persistent shock__. Replacing the permanent shock to $p$ with a persistent one in the above process essentially adds another component from the previous period to the growth in residuals, hence increases overall unconditional volatility. In the meantime, it does not change the perceived risk under FIRE. Therefore, the effect of making the permanent shock persistent will lead to a smaller correlation between FIRE risk perception and growth volatility. But the correlation will remain positive. 
#
# - __Moving average shock or purely transitory shock__. Our model actually nests both cases. Setting $\phi=0$ corresponds to purely transitory shocks. Any positive $\phi$ allows the coexistence of MA shock and transitory shocks. Our test is also robust to this alternative specification. 
#
# - __Time-invariant versus time-varying volatility__. Under the former assumption, the income volaility estimated from past income data can be directly comparable with the perceived risks reported for a different period. But doing so under the later assumption is inconsistent with the model. It requires the perceived risks and the realized income data are for the same time horizon. This is hard to satisfy based on the current data avaiability. But what's assuring is that if the stochastical volatilities are persistent over the time, we should still expect to see positive correlation between past volatility and FIRE risk perception even if the former is estimated from an earlier period.  
#
# There is another complication regarding the FIRE test: the superior information problem. It states that what econometrician's treat as income shocks are actually in the information set of the FIRE agents. Think this as when the known characteristics $\hat z$ used in the regression only partially captures the true predictable components $z$. Hence the sample residuals $\hat e$ are bigger than its true counterparts and this results in higher estimated growth and level volatility from data than the level relevant to FIRE agents in the model. It is true that this leads to a lower correlation between volatility and perceived risks, but it does not alter the prediction about the positive correlation between the two.

# # Data, variables and density estimation
#
# ## Data
#
# The data used for this paper is from the core module of Survey of Consumer Expectation(SCE) conducted by the New York Fed, a monthly online survey for a rotating panel of around 1,300 household heads over the period from June 2013 to January 2020, over a total of 80 months. This makes about 95113 household-year observations, among which around 68361 observations provide non-empty answers to the density question on earning growth. 
#
# Particularly relevant for my purpose, the questionnaire asks each respondent to fill perceived probabilities of their same-job-hour earning growth to pre-defined non-overlapping bins. The question is framed as "suppose that 12 months from now, you are working in the exact same [“main” if Q11>1] job at the same place you currently work and working the exact same number of hours. In your view, what would you say is the percentage chance that 12 months from now: increased by x% or more?".
#
# As a special feature of the online questionnaire, the survey only moves on to the next question if the probabilities filled in all bins add up to one. This ensures the basic probabilistic consistency of the answers crucial for any further analysis. Besides, the earning growth expectation is formed for exactly the same position, same hours, and the same location. This has two important implications for my analysis. First, these conditions help make sure the comparability of the answers across time and also excludes the potential changes in earnings driven by endogenous labor supply decisions, i.e. working for longer hours. Empirical work estimating income risks are often based on data from received income in which voluntary labor supply changes are inevitably included. Our subjective measure is not subject to this problem and this is a great advantage. Second, the earning expectations and risks measured here are only conditional on non-separation from the current job. It excludes either unemployment, i.e. likely a zero earning, or an upward movement in the job ladder, i.e. a different earning growth rate. Therefore, this does not fully reflect the entire income risk profile relevant to each individual. 
#
# Unemployment and other involuntary job separations are undoubtedly important sources of income risks, but I choose to focus on the same-job/hour earning with the recognition that individuals' income expectations, if any, may be easier to be formed for the current job/hour than when taking into account unemployment risks. Given the focus of this paper being subjective perceptions, this serves as a  useful benchmark.  What is more assuring is that the bias due to omission of unemployment risk is unambiguous. We could interpret the moments of same-job-hour earning growth as an upper bound for the level of growth rate and a lower bound for the income risk. To put it in another way, the expected earning growth conditional on current employment is higher than the unconditional one, and the conditional earning risk is lower than the unconditional one. At the same time, since SCE separately elicits the perceived probability of losing the current job for each respondent, I could adjust the measured labor income moments taking into account the unemployment risk. 
#
# ## Density estimation and variables 
#
# With the histogram answers for each individual in hand, I follow <cite data-cite="engelberg_comparing_2009">(Engelberg, Manskiw and Williams, 2009)</cite> to fit each of them with a parametric distribution accordingly for three following cases. In the first case when there are three or more intervals filled with positive probabilities, it was fitted with a generalized beta distribution. In particular, if there is no open-ended bin on the left or right, then two-parameter beta distribution is sufficient. If there is either open-ended bin with positive probability, since the lower bound or upper bound of the support needs to be determined, a four-parameter beta distribution is estimated. In the second case, in which there are exactly two adjacent intervals with positive probabilities, it is fitted with an isosceles triangular distribution. In the third case, if there is only one positive-probability of interval only, i.e. equal to one, it is fitted with a uniform distribution. 
#
# Since subjective moments such as variance is calculated based on the estimated distribution, it is important to make sure the estimation assumptions of the density distribution do not mechanically distort my cross-sectional patterns of the estimated moments. This is the most obviously seen in the tail risk measure, skewness. The assumption of log normality of income process, common in the literature (See again <cite data-cite="blundell_consumption_2008">(Blundell et al. 2008)</cite>), implicitly assume zero skewness, i.e. that the income increase and decrease from its mean are equally likely. This may not be the case in our surveyed density for many individuals. In order to account for this possibility, the assumed density distribution should be flexible enough to allow for different shapes of subjective distribution. Beta distribution fits this purpose well. Of course, in the case of uniform and isosceles triangular distribution, the skewness is zero by default. 
#
# Since the microdata provided in the SCE website already includes the estimated mean, variance and IQR by the staff economists following the exact same approach, I directly use their estimates for these moments. At the same time, for the measure of tail-risk, i.e. skewness, as not provided, I use my own estimates. I also confirm that my estimates and theirs for the first two moments are correlated with a coefficient of 0.9. 
#
# For all the moment's estimates, there are inevitably extreme values. This could be due to the idiosyncratic answers provided by the original respondent, or some non-convergence of the numerical estimation program. Therefore, for each moment of the analysis, I exclude top and bottom $3\%$ observations, leading to a sample size of around 48,000. 
#
# I also recognize what is really relevant to many economic decisions such as consumption is real income instead of nominal income. I, therefore, use the inflation expectation and inflation uncertainty (also estimated from density question) to convert nominal earning growth moments to real terms for some robustness checks in this paper. In particular, the real earning growth rate is expected nominal growth minus inflation expectation. 
#
#
# \begin{eqnarray}
# \overline {\Delta y^{r}}_{i,t} = \overline\Delta y_{i,t} - \overline \pi_{i,t}
# \end{eqnarray}
#
# The variance associated with real earning growth, if we treat inflation and nominal earning growth as two independent stochastic variables, is equal to the summed variance of the two. The independence assumption is admittedly an imperfect assumption because of the correlation of wage growth and inflation at the macro level. So it is should be interpreted with caution. 
#
# \begin{eqnarray}
# \overline{var}_{i,t}(\Delta y^r_{i,t+1}) = \overline{var}_{i,t}(\Delta y_{i,t+1}) + \overline{var}_{i,t}(\pi_{t+1})
# \end{eqnarray}
#
# Not enough information is available for the same kind of transformation of IQR and skewness from nominal to real, so I only use nominal variables. Besides, as there are extreme values on inflation expectations and uncertainty, I also exclude top and bottom $5\%$ of the observations. This further shrinks the sample, when using real moments, to around 40,000. 
#

# #  Perceived income risks: basic facts 
#
#
# ##  Cross-sectional heterogeneity
#
# This section inspects some basic cross-sectional patterns of the subject moments of labor income. In the Figure \ref{fig:histmoms}, I plot the distribution of perceived income risks in nominal and real terms, $\overline{var}_{i,t}$ and $\overline{var^{r}}_{i,t}$, respectively. 
#
# There is a sizable dispersion in perceived income risks. In both nominal and real terms, the distribution is right-skewed with a long tail. Specifically, most of the workers have perceived a variance of nominal earning growth ranging from zero to $20$ (a standard-deviation equivalence of $4-4.5\%$ income growth a year). But in the tail, some of the workers perceive risks to be as high as $7-8\%$ standard deviation a year. To have a better sense of how large the risk is, consider a median individual in our sample, who has an expected earnings growth of $2.4\%$, and a perceived risk of $1\%$ standard deviation. This implies by no means negligible earning risk. \footnote{In the appendix, I also include histograms of expected income growth and subjective skewness, which show intuitive patterns such as nominal rigidity. Besides, about half of the sample exhibits non-zero skewness in their subjective distribution, indicating asymmetric upper/lower tail risks.}  
#
# \begin{center}
# [FIGURE \ref{fig:histmoms} HERE]
# \end{center}
# How are perceived income risks different across a variety of demographic factors? Empirical estimates of income risks of different demographic groups from microdata have been rare\footnote{For instance, <cite data-cite="meghir2004income">(Meghir and Pistaferri (2004))</cite> estimated that high-education group is faced with higher income risks than the low-education group.  <cite data-cite="bloom2018great">(Bloom et al.(2018))</cite> documented that income risks decreases with age and varies with current income level in a U-shaped.}, not mentioning in subjective risk perceptions. Figure \ref{fig:ts_incvar_age} plots the average perceived risks of young, middle-aged, and old workers over the sample period. It is clear that for most of the months, perceived risks decrease with age. Hypothetically, this may be either because of more stable earning dynamics as one is older in the market in reality, or a better grasp of the true income process and higher subjective certainty. The model I will build allows both to play a role.  
#
# \begin{center}
#  [FIGURE \ref{fig:ts_incvar_age} HERE]
#  \end{center}
#
# Another important question is how income risk perceptions depend on the realized income. This is unclear ex-ante because it depends on the true income process as well as the perception formation. SCE does not directly report the current earning by the individual who reports earning forecasts. Instead, I use what's available in the survey, the total pretax household income in the past year as a proxy to the past realizations of labor income. As Figure \ref{fig:barplot_byinc} shows, perceived risks gradually declines as one's household income increases for most range of income. But the pattern reverses for the top income group. Such a non-monotonic relationship between risk perceptions and past realizations, as I will show later in the theoretical section, will be reconciled by people's state-dependent attribution and learning. 
#
# \begin{center}
#  [FIGURE \ref{fig:barplot_byinc} HERE]
# \end{center}
#

# + {"caption": "Distribution of Individual Moments", "code_folding": [], "label": "fig:histmoms", "note": "this figure plots histograms of the individual income moments. inc for nominal and rinc for real.", "hide_input": true, "hide_output": true}
## insert figures

graph_path = os.path.join(path,'../Graphs/ind/')

fig_list = ['hist_incexp.jpg',
            'hist_rincexp.jpg',
            'hist_incvar.jpg',
            'hist_rincvar.jpg']
            
nb_fig = len(fig_list)
    
file_list = [graph_path+ fig for fig in fig_list]

## show figures 
plt.figure(figsize=(18,10))
for i in range(nb_fig):
    plt.subplot(int(nb_fig/2),2,i+1)
    plt.imshow(mpimg.imread(file_list[i]))
    plt.axis("off")

# + {"caption": "Perceived Income by Income", "code_folding": [], "label": "fig:barplot_byinc", "note": "this figure plots average perceived income risks by the range of household income.", "widefigure": true, "hide_input": true, "hide_output": true}
## insert figures 
graph_path = os.path.join(path,'../Graphs/ind/')

fig_list = ['boxplot_var_stata.png']
            
nb_fig = len(fig_list)
file_list = [graph_path+fig for fig in fig_list]

## show figures 
plt.figure(figsize=(8,8))
for i in range(nb_fig):
    plt.subplot(nb_fig,1,i+1)
    plt.imshow(mpimg.imread(file_list[i]))
    plt.axis("off")

# + {"caption": "Perceived Income by Age", "code_folding": [], "label": "fig:ts_incvar_age", "note": "this figure plots average perceived income risks of different age groups over time.", "widefigure": true, "hide_input": true, "hide_output": true}
## insert figures 
graph_path = os.path.join(path,'../Graphs/ind/ts/')

fig_list = ['ts_incvar_age_g_mean.png']
            
nb_fig = len(fig_list)
file_list = [graph_path+fig for fig in fig_list]

## show figures 
plt.figure(figsize=(8,8))
for i in range(nb_fig):
    plt.subplot(nb_fig,1,i+1)
    plt.imshow(mpimg.imread(file_list[i]))
    plt.axis("off")
# -

# ## Counter-cyclicality of perceived risk
#
# Some studies have documented that income risks are counter-cyclical based on cross-sectional income data. \footnote{But they differ in exactly which moments of the income are counter-cyclical. For instance, <cite data-cite="storesletten2004cyclical">Storesletten et al.(2004)</cite> found that variances of income shocks are counter-cyclical, while <cite data-cite="guvenen2014nature"> Guvenen et al.(2014)</cite> and <cite data-cite="catherine_countercyclical_2019">Catherine (2019)</cite>, in contrast, found it to be the left skewness.}  It is worth inspecting if the subjective income risk profile has a similar pattern. Figure \ref{fig:tshe} plots the average perceived income risks from SCE against the YoY growth of the average hourly wage across the United States, which shows a clear negative correlation. Table \ref{macro_corr_he} further confirms such a counter-cyclicality by reporting the regression coefficients of different measures of average risks on the wage rate of different lags. All coefficients are significantly negative. 
#
# \begin{center}
# [FIGURE \ref{fig:tshe} HERE]
# \end{center}
#
#
# \begin{center}
# [TABLE \ref{macro_corr_he} HERE]
# \end{center}
#
# The pattern can be also seen at the state level. Table \ref{macro_corr_he_state} reports the regression coefficients of the monthly average perceived risk within each state on the state labor market conditions, measured by either wage growth or the state-level unemployment rate, respectively. It shows that a tighter labor market (higher wage growth or a lower unemployment rate) is associated with lower perceived income risks. Note that our sample stops in June 2019 thus not covering the outbreak of the pandemic in early 2020. The counter-cyclicality will be very likely more salient if it includes the current period, which was marked by catastrophic labor market deterioration and increase market risks.   
#
# \begin{center}
# [TABLE \ref{macro_corr_he_state} HERE]
# \end{center}
#
# The counter-cyclicality in subjective risk perceptions seen in the survey may suggest the standard assumption of state-independent symmetry in income shocks is questionable. But it may well be, alternatively, because people's subjective reaction to the positive and negative shocks are asymmetric even if the underlying process being symmetric. The model to be constructed in the theoretical section explores the possible role of both. 

# + {"caption": "Recent Labor Market Outcome and Perceived Risks", "code_folding": [], "label": "fig:tshe", "note": "Recent labor market outcome is measured by hourly earning growth (YoY).", "hide_input": true, "hide_output": true}
## insert figures 
graph_path = os.path.join(path,'../Graphs/pop/')

fig_list = ['tsMeanexp_he.jpg',
            'tsMeanvar_he.jpg']
            
nb_fig = len(fig_list)

file_list = [graph_path+fig for fig in fig_list]


## show figures 

fig, ax = plt.subplots(figsize =(30,10),
                       nrows = nb_fig,
                       ncols = 1)
for i in range(nb_fig):
    ax[i].imshow(mpimg.imread(file_list[i]))
    ax[i].axis("off") 
plt.tight_layout(pad =0, w_pad=0, h_pad=0)

# + {"hide_input": true, "hide_output": true}
macro_corr  = pd.read_excel('../Tables/macro_corr_he.xlsx',index_col=0)
print('Correlation of perceived risks and past labor market conditions')
macro_corr

# + {"hide_input": true, "hide_output": true}
mom_group_state  = pd.read_excel('../Tables/mom_group_state.xls',index_col = 0)
print('Perceived income risk and state labor market condition')
mom_group_state = mom_group_state.replace(np.nan, '', regex=True)
mom_group_state
# -

# ## Experiences and perceived risk 
#
# Different generations also have different perceived income risks. Let us explore to what extent the cohort-specific risk perceptions are influenced by the income volatility experienced by that particular cohort. Different cohorts usually have experienced distinct macroeconomic and individual histories. On one hand, these non-identical experiences could lead to long-lasting differences in realized life-long outcomes. An example is that college graduates graduating during recessions have lower life-long income than others. (<cite data-cite="kahn2010long">Kahn 2010</cite>, <cite data-cite="oreopoulos2012short">Oreopoulos et al. 2012</cite>, <cite data-cite="schwandt2019unlucky">Schwandt and Von Wachter(2019)</cite>). On the other hand, experiences may have also shaped people's expectations directly, leading to behavioral heterogeneity across cohorts (<cite data-cite="malmendier2015learning">Malmendier and Nagel (2015)</cite>). Benefiting from having direct access to the subjective income risk perceptions, I could directly examine the relationship between experiences and perceptions. 
#
# Individuals from each cohort are borned in the same year and obtained the same level of their respective highest education. The experienced volatility specific to a certain cohort $c$ at a given time $t$ can be approximated as the average squared residuals from an income regression based on the historical sample only available to the cohort's life time. This is approximately the unexpected income changes of each person in the sample. I use the labor income panel data from PSID to estimate the income shocks. \footnote{I obtain the labor income records of all household heads between 1970-2017. Farm workers, youth and olds and observations with empty entries of major demographic variables are dropped. } In particular, I first undertake a Mincer-style regression using major demographic variables as regressors, including age, age polynomials, education, gender and time-fixed effect. Then, for each cohort-time sample, the regression mean-squared error (RMSE) is used as the approximate to the cohort/time-specific income volatility. 
#
# There are two issues associated with such an approximation of experienced volatility. First, I, as an economist with PSID data in my hand, am obviously equipped with a much larger sample than the sample size facing an individual that may have entered her experience. Since larger sample also results in a smaller RMSE, my approximation might be smaller than the real experienced volatility. Second, however, the counteracting effect comes from the superior information problem, i.e. the information set held by earners in the sample contains what is not available to econometricians. Therefore, not all known factors predictable by the individual are used as a regressor. This will bias upward the estimated experienced volatility. Despite these concerns, my method serves as a feasible approximation sufficient for my purpose here. 
#
# The right figure in Figure \ref{fig:var_experience_data} plots the (logged) average perceived risk from each cohort $c$ at year $t$ against the (logged) experienced volatility estimated from above. It shows a clear positive correlation between the two, which suggests that cohorts who have experienced higher income volatility also perceived future income to be riskier. The results are reconfirmed in Table \ref{micro_reg}, for which I run a regression of logged perceived risks of each individual in SCE on the logged experienced volatility specific to her cohort while controlling individuals age, income, educations, etc. What is interesting is that the coefficient of $expvol$ declines from 0.73 to 0.41 when controlling the age effect because that variations in experienced volatility are indeed partly from age differences. While controlling more individual factors, the effect of the experienced volatility becomes even stronger. This implies potential heterogeneity as to how experience was translated into perceived risks.     
#
# How does experienced income shock per se affect risk perceptions? We can also explore the question by approximating experienced income growth as the growth in unexplained residuals. As shown in the left figure of Figure \ref{fig:var_experience_data}, it turns out that that a better past labor market outcome experienced by the cohort is associated with lower risk perceptions. This indicates that it is not not just the volatility, but also the change in level of the income, that is assymmetrically extrapolated into their perceiptions of risk. 
#
# \begin{center}
# [FIGURE \ref{fig:var_experience_data} HERE]
# \end{center}
#
# In theory, individual income change is driven by both aggregate and indiosyncratic risks. It is thus worth examining how experienced outcome from the two respective source translate into risk perceptions differently. In order to do so, we need to approximate idiosyncratic and aggregate experiences, separately. The former is basically the unexplained income residual from a regression controlling time fixed effect and also time-education effect. Since the two effects pick up the samplewide or groupwide common factors of each calender year, it excludes aggregate income shocks. The difference between such a residual and one from a regression dropping the two effects can be used to approximate aggregate shocks. As an alternative measure of aggregate economy, I use the official unemployment rate. For all aggregate measures, the volatility is correspondingly computed as the variance across time periods specific to each cohort. 
#
# Figure \ref{fig:experience_id_ag_data} plot income risk perceptions against both aggregate and idiosyncratic  experiences measured by the level and the volatility of shocks. It suggests different patterns between the aggregate and idiosyncratic experiences. In particular, a positive aggregate shock (both indicated by a higher aggregate income growth, or a lower unexmployment rate) is associated with lower risk perceptions. Such a negative relationship seems to be non-existent at the individual level.  What's common between aggregate and idiosyncratic risks is that the volatility of both kinds of experiences are positively correlated with risk perceptions. Such correlations are confirmed in a regression of controlling other individual characteristics, as shown in Table \ref{micro_reg}. Individual volatility, aggregate volatility and experience in unemployment rates are all significantly positively correlated with income risk perceptions. 
#
# \begin{center}
# [FIGURE \ref{fig:experience_id_ag_data} HERE]
# \end{center} 
#
# As another dimension of the inquiry, one may wonder the effects from experiences of income changes of different degree of persistance. In particular, do experiences of volatility from permanent and transitory shocks affect risk perceptions differently? In order to examine this question, what we can do is to decompose the experienced income volatility of different cohorts into components of different degree of persistences and see how the they are loaded into the future perceptions, separately. In particular, I follow the tradition of a long list of labor/macro literature by assuming the unexplained earning to consist of a permanent and a transitory component which have time-varying volatilities \footnote{<cite data-cite="gottschalk1994growth">Gottschalk et al. 1994</cite>, <cite data-cite="carroll1997nature">Carroll and Samwick, 1997</cite>, <cite data-cite="meghir2004income">Meghir and Pistaferri, 2004</cite>, etc.}. Then relying upon the cross-sectional moment restrictions of income changes, one could estimate the size of the permanent and transitory income risks based on realized income data. Experienced permanent and transitory volatility is approximated as the the average of estimated risks of respective component from the year of birth of the cohort till the year for which the income risk perceptions is formed.
#
# In theory, both permanent and transitory risks increase the volatility in income changes in the same way. But the results here suggest the pattern only holds for transitory income risks, as shown in the Figure \ref{fig:experience_var_per_tran_var_data}. In contrast, higher experienced permanent volatility is associated with lower perceived risk. I also confirm that the pattern is not sensitive to the particular definition of the cohort here by alterantively letting people's income risks be specific to education level. To understand which compoennt overweights the other in determining overal risk perception given their opposite signs, I also examine how the relative size of permanent and transitory volatility affect income risk perceptions. The ratio essentially reflect the degree of persistency of income changes, i.e. higher permanent/transitory risk ratio leads to a higher serial correlation of unexpected income changes. The right graph in Figure \ref{fig:experience_var_per_tran_var_data} suggest that higher permanent/transitory ratio is actually associated with lower perceived income risks. The fact that income risk perceptions differ depending upon the nature of experienced volatility suggests that income risk perceptions are formed in a way that is not consistent with the underlying income process. This will be a crutial input to the modeling of perception formation in the next section.
#
# \begin{center}
# [FIGURE \ref{fig:experience_var_per_tran_var_data} HERE]
# \end{center} 
#
#

# + {"caption": "Experienced Volatility and Perceived Income Risk", "code_folding": [], "label": "fig:var_experience_var_data", "note": "Experienced volatility is the mean squred error(MSE) of income regression based on a particular year-cohort sample. The perceived income risk is the average across all individuals from the cohort in that year.", "hide_input": true, "hide_output": true}
## insert figures 
graph_path = os.path.join(path,'../Graphs/ind/')

fig_list = ['experience_var_var_data.png']
            
nb_fig = len(fig_list)

file_list = [graph_path+fig for fig in fig_list]


## show figures 
plt.figure(figsize =(5,5))
for i in range(nb_fig):
    plt.imshow(mpimg.imread(file_list[i]))
    plt.axis("off") 
plt.tight_layout(pad =0, w_pad=0, h_pad=0)

# + {"caption": "Experienced Permanent Volatility and Perceived Income Risk", "code_folding": [], "label": "fig:experience_var_permanent_var_data", "note": "Experienced permanent volatility is average of the estimated risks of the permanent income component of a particular year-cohort sample. The perceived income risk is the average across all individuals from the cohort in that year.", "hide_input": true, "hide_output": true}
## insert figures 
graph_path = os.path.join(path,'../Graphs/ind/')

fig_list = ['experience_var_permanent_var_data.png']
            
nb_fig = len(fig_list)

file_list = [graph_path+fig for fig in fig_list]


## show figures 
plt.figure(figsize =(5,5))
for i in range(nb_fig):
    plt.imshow(mpimg.imread(file_list[i]))
    plt.axis("off") 
plt.tight_layout(pad =0, w_pad=0, h_pad=0)

# + {"caption": "Experienced Transitory Volatility and Perceived Income Risk", "code_folding": [], "label": "fig:experience_var_transitory_var_data", "note": "Experienced transitory volatility is average of the estimated risks of the transitory component of a particular year-cohort sample. The perceived income risk is the average across all individuals from the cohort in that year.", "hide_input": true, "hide_output": true}
## insert figures 
graph_path = os.path.join(path,'../Graphs/ind/')

fig_list = ['experience_var_transitory_var_data.png']
            
nb_fig = len(fig_list)

file_list = [graph_path+fig for fig in fig_list]


## show figures 
plt.figure(figsize =(5,5))
for i in range(nb_fig):
    plt.imshow(mpimg.imread(file_list[i]))
    plt.axis("off") 
plt.tight_layout(pad =0, w_pad=0, h_pad=0)

# + {"caption": "Experienced Permanent/Transitory Ratio and Perceived Income Risk", "code_folding": [], "label": "fig:experience_var_ratio_var_data", "note": "Experienced permanent/transitory ratio is ratio of the estimated risks of the permanent to transitory component of a particular year-cohort sample. The perceived income risk is the average across all individuals from the cohort in that year.", "hide_input": true, "hide_output": true}
## insert figures 
graph_path = os.path.join(path,'../Graphs/ind/')

fig_list = ['experience_var_ratio_var_data.png']
            
nb_fig = len(fig_list)

file_list = [graph_path+fig for fig in fig_list]


## show figures 
plt.figure(figsize =(5,5))
for i in range(nb_fig):
    plt.imshow(mpimg.imread(file_list[i]))
    plt.axis("off") 
plt.tight_layout(pad =0, w_pad=0, h_pad=0)

# + {"hide_input": true, "hide_output": true}
micro_reg_history_vol  = pd.read_excel('../Tables/micro_reg_history_vol.xlsx',index_col = 0)
print('Experienced volatility and perceived income risk')
micro_reg_history_vol = micro_reg_history_vol.replace(np.nan, '', regex=True)
micro_reg_history_vol
# -

#
# ##  Other individual characteristics
#   What other factors are associated with risk perceptions? This section inspects the question by regressing the perceived income risks at the individual level on four major blocks of variables: experiences, demographics, unemployment expectations by the respondent, as well as job-specific characteristics.  The regression is specified as followed. 
#
# \begin{eqnarray}
# \overline{risk}_{i,c,t} = \alpha + \beta_0 \textrm{HH}_{i,c,t} + \beta_1 \textrm{Exp}_{c,t} + \beta_2 \textrm{Prob}_{i,c,t} + \beta_3 \textrm{JobType}_{i,c,t} + \epsilon_{i,t}
# \end{eqnarray}
#
# The dependent variable is the individual $i$ from cohort $c$'s perceived risk. The experience block $\textit{Exp}_{c,t}$ includes individual experienced volatility $\textit{IdExpVol}_{c,t}$, the aggregate experience of volatility $\textit{AgExpVol}_{c,t}$ and experience of unemployment rate $\textit{AgExpUE}_{c,t}$. They are all cohort/time-specific since different birth cohort at different points of time have had difference experience of both micro and macro histories. The second type of factors denoted $\textit{HH}_{i,t}$ represents household-specific demographics such as the age, household income level, education, gender as well as the numeracy of the respondent. In particular, the numeracy score is generated based on the individual's answers to seven questions that are designed to measure the individual's basic knowlege of probability, intrest rate compounding, the difference between nominal and real return and risk diversification. Third, $\textit{Prob}_{i,t}$ represents other subjective probabilities regarding unemployment held by the same individual. As far as this paper is concerned, I include the perceived probability of unemployment herself and the probability of a higher nationwide unemployment rate. The fourth block of factors, as called $\textit{Jobtype}_{i,t}$ includes dummy variables indicating if the job is part-time or if the work is for others or self-employed. 
#
# Besides, since many of the regressors are time-invariant household characteristics, I choose not to control household fixed effects in these regressions ($\omega_i$). Throughout all specifications, I cluster standard errors at the household level because of the concern of unobservable household heterogeneity. 
#
# The regression results reported in Table \ref{micro_reg}  are rather intuitive. From the first to the sixth column, I gradually control more factors. All specifications confirm that higher experienced volatility at both idiosyncratic level and aggregate level, as well as high unemployment rate experience in the past all lead to higher risk perceptions. Besides, workers from low-income households, females, and lower education and self-employed jobs have higher perceived income risks.
#
# In our sample, there are around $15\%$ (6000) of the individuals who report themselves to be self-employed instead of working for others. The effects are statistically and economically significant. Whether a part-time job is associated with higher perceived risk is ambiguous depending on if we control household demographics. At first sight, part-time jobs may be thought of as more unstable. But the exact nature of part-time job varies across different types and populations. It is possible, for instance, that the part-time jobs available to high-income and educated workers bear lower risks than those by the low-income and low-education groups. 
#
# Another interesting finding is that individual risk perception decreases as the individual's numeracy test scores higher. This is not particularly driven by the difference in education as the pattern remains even if we jointly control for the education. This coroborates the findings that individual's perception and decisions are affected by the financial literacy (<cite data-cite="van2011financial">Van Rooij et al. 2011</cite>, <cite data-cite="lusardi2014economic">Lusardi and Mitchell,2014</cite>).
#
# In addition, higher perceived the probability of losing the current job, which I call individual unemployment risk, $\textit{UEprobInd}$ is associated with higher earning risks of the current job. The perceived chance that the nationwide unemployment rate going up next year, which I call aggregate unemployment risk, $\textit{UEprobAgg}$ has a similar correlation with perceived earning risks. Such a positive correlation is important because this implies that a more comprehensively measured income risk facing the individual that incorporates not only the current job's earning risks but also the risk of unemployment is actually higher. Moreover, the perceived risk is higher for those whose perceptions of the earning risk and unemployment risk are more correlated than those less correlated. 
#
#
#  \begin{center}
#  [TABLE \ref{micro_reg} HERE]
#  \end{center}

reg_tb = pd.read_excel('../Tables/micro_reg.xlsx').replace(np.nan,'')

# + {"hide_input": true, "hide_output": true}
reg_tb
# -

# ##  Perceived income risk and decisions
#
# Finally, how individual-specific perceived risks affect household economic decisions such as consumption? The testable prediction is higher perceived risks shall increase precautionary saving motive therefore lower current consumption (higher consumption growth.) Although we cannot directly observe the respondent's spending decisions, we can alternatively rely on the self-reported spending plan in the SCE to shed some light on this \footnote{Other work that directly examines the impacts of expectations on readiness to spend includes <cite data-cite="bachmann2015inflation">Bachmann et al. 2015</cite>,<cite data-cite="coibion2020forward">Coibon et al. 2020</cite>.}.
#
# Table \ref{spending_reg} reports the regression results of planned spending growth over the next year on the expected earning's growth (the first column) as well as a number of perceived income risk measures. \footnote{There is one important econometric concern when I run regressions of the decision variable on perceived risks due to the measurement error in the regressor used here. In a typical OLS regression in which the regressor has i.i.d. measurement errors, the coefficient estimate for the imperfectly measured regressor will have a bias toward zero. For this reason, if I find that willingness to consume is indeed negatively correlated with perceived risks, taking into account the bias, it implies that the correlation of the two is greater in the magnitude.}  Each percentage point increase in expected income growth is associated with a 0.39 percentage point increase in spending growth. At the same time, one percentage point higher in the perceived risk increases the planned spending growth by 0.58 percentage. This effect is even stronger for real income risks. As a double-check, the individual's perceived probability of a higher unemployment rate next year also has a similar effect. These results suggest that individuals do exhibit precautionary saving motives according to their own perceived risks.  
#
#
# \begin{center}
# [TABLE \ref{spending_reg} HERE]
# \end{center}

spending_reg_tb = pd.read_excel('../Tables/spending_reg.xlsx').replace(np.nan,'')

# + {"hide_input": true, "hide_output": true}
spending_reg_tb
# -

# #  A model of risk perception formation 
#
# This section will show that the empirical patterns discussed above can be reconciled by a model of learning featuring an imperfect understanding of the income process. In particular, the model will specify how experienced volatility is translated into future risk perceptions and how the process also depends on people's perceived nature of the income risks. 
#
#
# ## Under a simple income process 
#
# We start by defining an AR(1) process of the individual income. In the next section for a life-cycle consumption problem, we will extend the model for a more realistic income process with risks of different persistence, i.e. permanent and transitory components. In particular, the income of individual $i$ from the cohort $c$ at time $t$ depends on her previous-period income with a persistence parameter of $\rho$ and an individual and time-specific shock $\epsilon_{i,c,t}$\footnote{There are usually predictable components of income by known individual characteristics. It is more accurate to think $y$ here as the unexplained income component.}. I define cohort $c$ to be measured by the year of entry in the job market. 
#
# \begin{eqnarray}
# y_{i,c,t} = \rho y_{i,c,t-1} + \epsilon_{i,c,t}
# \end{eqnarray}
#
# It is assumed that the $\rho$ is the same across all inviduals. Also, I assume the income shock $\epsilon_{i,c,t}$ to be i.i.d., namely independent across individuals and the time and with an identical variance, as defined in the equation below. Later sections will relax this assumption by allowing for cross-sectional correlation, namely some aggregate risks. Further extensions are also allowed for cohort or time-specific volatility. The i.i.d. assumption implies at any time $t$, the variance-covariance matrix of income shocks across individuals is a diagonal matrix defined as below. 
#
# \begin{eqnarray}
# E(\epsilon_{t}'\epsilon_{t}|Y_{t-1}) = \sigma^2 I_n \quad \forall t 
# \end{eqnarray}
#
# where $\sigma^2$ is the volatility of income shock and $I_n$ is an identity matrix whose length is the number of agents in the economy, $n$. Although income volatility is not cohort-specific, any past shock still leaves different impacts on the young and old generations because of different experiences of histories. This is reminiscent of <cite data-cite="bansal2004risks">Storesletten et al. (2004)</cite>. Since both $\rho$ and $\sigma^2$ are not cohort-specific, I drop the subscript $c$ from now on to avoid clustering. 
#
# Both $\rho$ and $\sigma$ are the "true" parameters only known by the modeler, but unknown by agents in the economy. Individual $i$ learns about the income process by "running a regression" of the form laid out above using a small sample of her past experience starting from the year of entering the job market $c$ till $t$. Critically, for this paper's purpose,  I allow the experience used for learning to include both her own and others' past income over the same period. It is admittedly bizarre to assume individual agents have full access to the entire population's income. A more realistic assumption could be that only a small cross-sectional sample is available to the agent. Any scope of cross-sectional learning suffices for the point to be made in this paper.  

# If each agent knows _perfectly_ the model parameters $\rho$ and $\sigma$, the uncertainty about future income growth is 
#
# \begin{eqnarray}
# \begin{split}
# Var^*_{i,t}(\Delta y_{i,t+1}) & =  Var^*_{i,t}(y_{i,t+1}- y_{i,t}) \\ 
# & =  Var^*_{i,t}((\rho-1)y_{i,t} + \epsilon_{i,t+1}) \\
# & = Var^*_{i,t}(\epsilon_{i,t+1}) \\
# & = \sigma^2
# \end{split}
# \end{eqnarray}
#
# The superscript $*$ is the notation for perfect understanding. The first equality follows because both $y_{i,t}$ and the persistent parameter $\rho$ is known by the agent. The second follows because $\sigma^2$ is also known. 
#
# Under _imperfect_ understanding and learning, both $\rho$ and $\sigma^2$ are unknown to agents. Therefore, the agent needs to learn about the parameters from the small panel sample experienced up to that point of the time. We represent the sample estimates of $\rho$ and $\sigma^2$ using $\widehat \rho$ and $\hat{\sigma}^2$. 
#
# \begin{eqnarray}
# \begin{split}
# \widehat Var_{i,t}(\Delta y_{i,t+1}) & = y_{i,t}^2 \underbrace{\widehat{Var}^{\rho}_{i,t}}_{\text{Persistence uncertainty}} + \underbrace{\hat{\sigma}^2_{i,t}}_{\text{Shock uncertainty}}
# \end{split}
# \end{eqnarray}
#
# The perceived risks of future income growth have two components. The first one comes from the uncertainty about the persistence parameter. It reflects how uncertain the agent feels about the degree to which realized income shocks will affect her future income, which is non-existent under perfect understanding. I will refer to this as the parameter uncertainty or persistence uncertainty hereafter. Notice the persistence uncertainty is scaled by the squared size of the contemporary income. It implies that the income risks are size-dependent under imperfect understanding. It introduces one of the possible channels via which current income affects perceived income risk. 
#
# The second component of perceived risk has to do with the unrealized shock itself. Hence, it can be called shock uncertainty. Because the agent does not know perfectly the underlying volatility of the income shock, she can only infer that from the past volatility. 
#
# We assume agents learn about the parameters using a least-square rule widely used in the learning literature (For instance, <cite data-cite="marcet1989convergence">Marcet and Sargent (1989)</cite>, <cite data-cite="evans2012learning">Evans and Honkapohja (2012)</cite>, <cite data-cite="malmendier2015learning">Malmendier and Negal (2015)</cite>) The bounded rationality prevents her from adopting any more sophisticated rule that econometricians may consider to be superior to the OLS in this context. (For instance, OLS applied in autocorrelated models induce bias in estimate.) Under OLS learning, the parameter estimate is the following.
#
#
# \begin{eqnarray}
# \hat \rho_{i,t} = (\sum^{t-c}_{k=0}\sum^{n}_{j=1}y^2_{j,t-k-1})^{-1}(\sum^{t-c}_{k=0}\sum^{n}_{j=1}y_{j,t-k-1}y_{j,t-k})
# \end{eqnarray}
#
# The sample variance of regression residuals $\widehat e$, or the mean squared errors (MSE),  in econometrician's word,  are the agents' best guess of the income volatility $\sigma^2$. It can be seen as the experienced volatility over the past history. 
#
# \begin{eqnarray}
# \widehat{\sigma}^2_{i,t} = s^2_{i,t} = \frac{1}{N_{i,t}-1} \sum^{n}_{j=1}\sum^{t-c}_{k=0} \hat e_{j,t-k}^2
# \end{eqnarray}
#
# where $N_{i,t}$ is the size of the panel sample available to the agent $i$ at time t. It is equal to $n_{i}(t-c_{i})$, the number of people in the sample times the duration of agent $i$'s career. 
#
# We first consider the case when the agent understands that the income shocks are i.i.d. To put it differently, this is when the agent correctly specify the income model when learning. Under i.i.d. assumption, the estimated uncertainty about the estimate is 
#
# \begin{eqnarray}
# \widehat {Var}^{\rho}_{i,t} = (\sum^{t-c}_{k=0}\sum^{n}_{j=1}y^2_{j,t-k-1})^{-1}\widehat{\sigma}^2_{i,t}
# \end{eqnarray}
#
# Experience-based learning naturally introduces a mechanism for the perceived income risks to be cohort-specific and age-specific. Different generations who have experienced different realizations of the income shocks have different estimates of $Var^{\rho}$ and $\sigma^2$, thus differ in their uncertainty about future income. In the meantime, people at an older age are faced with a larger sample size than younger ones, this will drive the age profile of perceived risks in line with the observation that the perceived risk is lower as one grows older. Also, note that the learning literature has explored a wide variety of assumptions on the gains from learning to decline over time or age. These features can be easily incorporated into my framework. For now, equal weighting of the past experience suffices for the exposition here. 
#
# We can rewrite the perceived risk under correct model specification as the following. 
#
#
# \begin{eqnarray}
# \widehat{Var}_{i,t}(\Delta y_{i,t+1}) = [(\sum^{t-c}_{k=0}\sum^{n}_{j=1}y^2_{j,t-k-1})^{-1}y^2_{i,t} + 1] \hat{\sigma}^2_{i,t}
# \end{eqnarray}
#
#

#
# ## Attribution  
#
# Attribution means that agents subjectively determine the nature of the income shocks, or equivalently, form perceptions about the correlation between their own outcome and others. This opens a room for possible model-misspecification about the nature of income shock due to bounded rationality. Although people specify the form of the regression model correctly, they do not necessarily perceive the nature of the income shocks correctly. 
#
# Without taking stances on how exactly people might mis-attribute, it is worth discussing the general implications of subjective attribution for risk perceptions. For instance, would it imply a higher perceived income risk if the subjective perception of the cross-sectional correlation is higher? 
#
# Under the least-square estimation, the estimated parameter uncertainty takes a general sandwich form as below. It is similar to accounting for within-time clustering in computing standard errors by econometricians. The main distinction is that the following is subjective. 
#
# \begin{eqnarray}
# \begin{split}
# \tilde {Var}^{\rho}_{i,t} & =   (\sum^{t-c}_{k=0}\sum^{n}_{j=1}y^2_{j,t-k-1})^{-1}(\sum^{t-c}_{k=0}\tilde \Omega_{i,t-k})(\sum^{t-c}_{k=0}\sum^{n}_{j=1}y^2_{j,t-k-1})^{-1}
# \end{split}
# \end{eqnarray}
#
# where $\tilde \Omega_{t-k}$ is the perceived variance-covariance of income and income shocks within each point of time. It reflects how individual $i$ thinks about the correlation between her own income and others'. 
#
# \begin{eqnarray}
# \begin{split}
# \tilde \Omega_{i,t} = \tilde E_{i,t}(Y_{t-1}e_{t}'e_{t}Y_{t-1})
# \end{split}
# \end{eqnarray}
#
# In order to get more intuition, we can simplify the matrix in the following way. If we assume constant group size $n$ over time and the homoscedasticity, i.e. income risks $\sigma$ do not change over time, given the individual ascribes a subjective correlation coefficient of $\tilde \delta_{\epsilon, i,t}$ across income shocks and a correlation $\tilde \delta_{y, i,t}$ across the levels of income, $\tilde \Omega_{i,t}$ can be approximated as the following. (See the appendix for derivation) \footnote{This is analogous to the cluster-robust standard error by <cite data-cite="cameron2011robust">Cameron et al. (2011)</cite>. But again, they are different because here it is subjective.} 
#
#
# \begin{eqnarray}
# \begin{split}
# \tilde \Omega_{i,t} & \approx \sum^{n}_{j=1}y^2_{j,t} (1+\tilde \delta_{y,i,t}\tilde \delta_{\epsilon,i,t}(n-1))\tilde \sigma^2_{t}
# \end{split}
# \end{eqnarray}
#
# It follows that the parameter uncertainty under the subjective attribution writes as below.
#
# \begin{eqnarray}
# \begin{split}
# \tilde {Var}^{\rho}_{i,t} & = (\sum^{t-c}_{k=0}\sum^{n}_{j=1}y^2_{j,t-k-1})^{-1}(1+ \tilde\delta_{i,t}(n-1))\tilde{\sigma}^2_{t}
# \end{split}
# \end{eqnarray}
#
# Notice we bundle the two correlation coefficients parameters together as a single parameter of the attribution $\tilde\delta_{i,t}$. 
#
# \begin{eqnarray}
# \tilde \delta_{y,i,t}\tilde \delta_{\epsilon,i,t}\equiv \tilde \delta_{i,t}  
# \end{eqnarray}
#
# The subjective attribution is jointly determined by two perceived correlation parameters, $\tilde \delta_{\epsilon}$ and $\tilde \delta_y$. They can be more intuively thought as long-run attribution and short-run attribution, respectively, because the former is the perceived correlation in the level of the income and later in shocks. The multiplication of two jointly governs the degree to which the agents inflate experienced volatility in forming perceptions about future income risks. 
#
# We can define internal and external attribution as the following. 
#
# \begin{eqnarray}
# \begin{split}
# \textrm{Internal attribution: }\quad \tilde\delta_{i,t} = 0 \\
# \textrm{External attribution: }\quad \tilde\delta_{i,t} \in (0,1]
# \end{split}
# \end{eqnarray}
#
# The internal attribution represents the scenario when the agent $i$ thinks that her income shock or the long-run income is uncorrelated with others' ($\tilde \delta_{\epsilon} = 0$ or $\tilde \delta_y = 0$). In contrast, the external attribution stands for the case when the agent perceive her own income to be positively correlated with others'. The external attribution attains its maximum value of $1$ if the agent thinks both her income shock and income are perfectly correlated with others. In general, $\tilde \delta_{\epsilon,i,t}$ and $\tilde \delta_{y,i,t}$ are not necessarily consistent with the true income process. Since long-run correlation increases with the short-run correlation, bundling them together as a single parameter is feasible. 
#
# Now, it is clear that the subjective attribution affects perceived risks through its effect on parameter uncertainty. One can show that a higher degree of external attribution (a higher $\tilde \delta_{i,t}$)  is associated with higher parameter uncertainty as well as higher perceived risks.  
#
# \begin{eqnarray}
# \begin{split}
# \tilde {Var}_{i,t}(\Delta y_{i,t+1}|\tilde \delta_{i,t}) >  \tilde {Var}_{i,t}(\Delta y_{i,t+1}|\tilde \delta'_{i,t}) \quad \forall \tilde \delta_{i,t} > \tilde \delta'_{i,t}
# \end{split}
# \end{eqnarray}
#
# Taking stock, we have the following predictions about how the perceived income risks depend on experienced volatility and subjective attribution. 
#
# - Higher experienced volatility, measured by $s^2 \equiv \tilde{\sigma}^2_{i,t}$ leads to higher perceived income risks. 
#
# - In the same time, future perceptions of the risks inflate the past volatility proportionally depending on their subjective attribution. A higher degree of external attribution reflected by a higher $\tilde \delta_{i,t}$ implies a higher parameter uncertainty (Figure \ref{fig:corr_var}) and higher inflation of past volatility into the future. (Figure \ref{fig:var_experience_var})
#

# + {"caption": "Attribution and Parameter Uncertainty", "code_folding": [], "label": "fig:corr_var", "widefigure": true, "hide_input": true, "hide_output": true}
## insert figures 
graph_path = os.path.join(path,'../Graphs/theory/')

fig_list = ['corr_var.jpg']
            
nb_fig = len(fig_list)
file_list = [graph_path+fig for fig in fig_list]

## show figures 
plt.figure(figsize=(10,10))
for i in range(nb_fig):
    plt.subplot(nb_fig,1,i+1)
    plt.imshow(mpimg.imread(file_list[i]))
    plt.axis("off")

# + {"caption": "Experienced Volatility and Perceived Risk", "code_folding": [], "label": "fig:var_experience_var", "widefigure": true, "hide_input": true, "hide_output": true}
## insert figures 
graph_path = os.path.join(path,'../Graphs/theory/')

fig_list = ['var_experience_var.jpg']
            
nb_fig = len(fig_list)
file_list = [graph_path+fig for fig in fig_list]

## show figures 
plt.figure(figsize=(10,10))
for i in range(nb_fig):
    plt.subplot(nb_fig,1,i+1)
    plt.imshow(mpimg.imread(file_list[i]))
    plt.axis("off")
# -

#
# ## Attribution errors
#
# Now, let us explore some possible attribution errors. Being subjective attribution, one can possibly think of many forms in which agents' attribution is not in line with the true nature of income shocks. This section explores one plausible possibility. In particular, we incorporate the psychological tendency of ascribing bad experiences to external causes and good experiences to internal ones, which is known as self-serving bias. \footnote{See <cite data-cite="zuckerman1979attribution">(Zuckerman, 1979)</cite>, <cite data-cite="al1993attributional">(Al-Zahrani et al.,1993)</cite>, <cite data-cite="campbell1999self">(Campbell and Sedikides, 1999)</cite>, <cite data-cite="seidel2010blame">(Seidel et al., 2010)</cite>.} The manifestation of the attribution error is that people asymmetrically assign the subjective correlation $\tilde \delta_{i,t}$ depending on the recent income change (or the realized shocks) being positive or negative. 
#
# More formally, define an attribution function that maps the recent income change $\Delta y_{i,t}$ into the subjective attribution $\tilde \delta_{i,t}$, according to the following form. 
# \begin{eqnarray}
# \begin{split}
# \tilde \delta(\Delta y_{i,t}) = 1- \frac{1}{(1+e^{\alpha-\theta \Delta y_{i,t}})}
# \end{split}
# \end{eqnarray}
#
# Figure \ref{fig:theta_corr} plots the attribution function under different parameter value. Basically, the attribution function is a variant of a logistic function with its function value bounded between $[0,1]$. It takes an s-shape and the parameter $\theta$ governs the steepness of the s-shape around its input value.  The higher the value of $\theta$ is,  the more prone to such an error. It takes any non-negative value. $\alpha$ is an adjustable parameter chosen such that the attribution free of attribution errors happens to be equal to the true correlation dictated by the underlying income process, $\delta$. Or it can be used to capture the degree of bias in attribution, which is a separate mechanism from the attribution error examined here. 
#
# Such a state-dependence of the attribution leads to systematically higher perceived risks by the "unlucky group", i.e. agents who have experienced negative income shocks than the "lucky group" even if the underlying income process does not have such a feature. It is important to note that this difference still exists even if the underlying shocks are indeed non-independent. Although different types of income shocks have different implications as to which group correctly or mis-specifies the model, it does not alter the distinction between the lucky and unlucky group. To put it differently,  the underlying process only determines who is over-confident or under-confident. But the group with a positive experience (thus internal distribution) is always more certain about their future income than the negative-experienced group. 
#
# So far, we have maintained the assumption of i.i.d. shock. What if there is indeed some aggregate risk? It turns out the presence of aggregate risk will induce the counter-cyclical pattern of the average perceived risk under such attribution errors. To see this clearly, I define at each point of the time $t$, there is $\lambda_t$ fraction of the agents that have experienced a positive income change, the "lucky group". Then the average perceived risk across all agents is a weighted average of the perceived risks between two groups. 
#
# \begin{eqnarray}
# \begin{split}
# \tilde {Var}_{t}(\Delta y_{i,t+1}) & = \underbrace{\lambda_t}_{\text{lucky fraction}} \tilde{Var_t}^{internal} + (1-\lambda_t) \tilde{Var_t}^{external} 
# \end{split}
# \end{eqnarray}
#
# The counter-cyclicality of perceived risk is very straightforward in such an environment. Imagine a positive aggregate shock at a given time, it leads to a larger fraction of the people who have experienced positive shocks, thus internal attribution and lowers perceived risks, while a negative aggregate shock induces more people to externally attribute and higher perceive risks. 
#
# Both the presence of attribution errors and aggregate risks are necessary conditions for generating the counter-cyclicality. Under aggregate risk, the fraction of lucky group $\lambda_t$ is procyclical, while under idiosyncratic risks, it is a constant $0.5$. With attribution error, the perceived risk under external attribution is always higher than that of internal attribution, i.e. $\tilde{Var_t}^{external} >\tilde{Var_t}^{internal}$, while the two are equal without attribution errors. 
#
# To summarize, introducing a particular form of attribution errors leads to testable predictions. 
#
# - Perceived income risks are state-dependent, i.e. the recent past income,  even if the underlying income process assumes income risks are independent of the past. Because of the attribution errors, we will also see the perceived income risks will be systematically lower for the high-income group than the low-income group.
#
# - In the presence of aggregate risks and attribution error, the average perceived risks are counter-cyclical. 

# + {"caption": "Attribution Function", "code_folding": [], "label": "fig:theta_corr", "widefigure": true, "hide_input": true, "hide_output": true}
## insert figures 
graph_path = os.path.join(path,'../Graphs/theory/')

fig_list = ['theta_corr.jpg']
            
nb_fig = len(fig_list)
file_list = [graph_path+fig for fig in fig_list]

## show figures 
plt.figure(figsize=(10,10))
for i in range(nb_fig):
    plt.subplot(nb_fig,1,i+1)
    plt.imshow(mpimg.imread(file_list[i]))
    plt.axis("off")

# + {"caption": "Current Income and Perceived Risk", "code_folding": [], "label": "fig:var_recent", "widefigure": true, "hide_input": true, "hide_output": true}
## insert figures 
graph_path = os.path.join(path,'../Graphs/theory/')

fig_list = ['var_recent.jpg']
            
nb_fig = len(fig_list)
file_list = [graph_path+fig for fig in fig_list]

## show figures 
plt.figure(figsize=(10,10))
for i in range(nb_fig):
    plt.subplot(nb_fig,1,i+1)
    plt.imshow(mpimg.imread(file_list[i]))
    plt.axis("off")
# -

# ## Simulation 
#
# ### Current income and perceived risks
#
# How do perceived risks depend on the current income level of $y_{i,t}$? Since the recent income changes $\Delta y_{i,t}$ triggers asymmetric attribution, the perceived risks depend on the current level of income beyond the past-dependence of future income on current income that is embodied in the AR(1) process. In particular, $\widehat{Var}^\rho_{i,t}$ does not depend on $\Delta y_{i,t}$ while $\tilde{Var}^\rho_{i,t}$ does and is always greater than the former as a positive, it will amplify the loading of the current level of income into perceived risks about future income. This generates a U-shaped perceived income profile depending on current level income.  
#
# Figure \ref{fig:var_recent} and \ref{fig:var_recent_sim} plots both the theory-predicted and simulated correlation between $y_{i,t}$ and perceived income risks with/without attribution errors. In the former scenario, perceived risks only mildly change with current income and the entire income profile of perceived risk is approximately flat. In the latter scenario, in contrast, perceived risks exhibit a clear U-shape across the income distribution. People sitting at both ends of the income distribution have high perceived risks than ones in the middle. The non-monotonic of the income profile arise due to the combined effects directly from $y_{i,t}$ and indirectly via its impact on $\tilde Var^{\rho}$. The former effect is symmetric around the long-run average of income (zero here). Deviations from the long-run mean on both sides lead to higher perceived risk. The latter monotonically decreases with current income because higher income level is associated with a more positive income change recently. The two effects combined create a U-shaped pattern.
#
# A subtle but interesting point is that the U-shape is skewed toward left, meaning perceived risks decrease with the income over the most part of the income distribution before the pattern reverses. More intuitively, it means that although low and high income perceived risks to be higher because of its deviation from the its long-run mean. This force is muted for the high income group because they have a lower peceived risks due to the attribution errors. 

# + {"caption": "Simulated Income Profile of Perceived Risk", "code_folding": [], "label": "fig:var_recent_sim", "widefigure": true, "hide_input": true, "hide_output": true}
## insert figures 
graph_path = os.path.join(path,'../Graphs/theory/')

fig_list = ['var_recent_sim.jpg']
            
nb_fig = len(fig_list)
file_list = [graph_path+fig for fig in fig_list]

## show figures 
plt.figure(figsize=(10,10))
for i in range(nb_fig):
    plt.subplot(nb_fig,1,i+1)
    plt.imshow(mpimg.imread(file_list[i]))
    plt.axis("off")
# -

# ### Age and experience and perceived risks 
#
# Figure \ref{fig:var_age_sim} plots the simulated age profile of perceived income risks with and without attribution errors. Due to experience-based learning, older agents have a larger sample size when learning about the model parameter, which induces the parameter uncertainty to be lower. What is interesting is that with attribution errors, since the parameter uncertainty is inflated proportionally with the degree of attribution, it makes the negative correlation between the perceived income risks and age more salient. This is consistent with our empirical findings shown in Figure \ref{fig:ts_incvar_age}. 

# + {"caption": "Simulated Experience of Volatility and Perceived Risk", "code_folding": [], "label": "fig:var_experience_var_sim", "widefigure": true, "hide_input": true, "hide_output": true}
## insert figures 
graph_path = os.path.join(path,'../Graphs/theory/')

fig_list = ['var_experience_var_sim.jpg']
            
nb_fig = len(fig_list)
file_list = [graph_path+fig for fig in fig_list]

## show figures 
plt.figure(figsize=(10,10))
for i in range(nb_fig):
    plt.subplot(nb_fig,1,i+1)
    plt.imshow(mpimg.imread(file_list[i]))
    plt.axis("off")

# + {"caption": "Simulated Age Profile of Perceived Risk", "code_folding": [], "label": "fig:var_age_sim", "widefigure": true, "hide_input": true, "hide_output": true}
## insert figures 
graph_path = os.path.join(path,'../Graphs/theory/')

fig_list = ['var_age_sim.jpg']
            
nb_fig = len(fig_list)
file_list = [graph_path+fig for fig in fig_list]

## show figures 
plt.figure(figsize=(10,10))
for i in range(nb_fig):
    plt.subplot(nb_fig,1,i+1)
    plt.imshow(mpimg.imread(file_list[i]))
    plt.axis("off")
# -

#
# ### Aggregate risk and counter-cyclicality 
#
# Previously, I assume the underlying shock is i.i.d. This section considers the implication of the attribution errors in the presence of both aggregate and idiosyncratic risks. This can be modeled by assuming that the shocks to individuals' income are positively correlated with each other at each point of the time. Denoting $\delta>0$ as the true cross-sectional correlation of income shocks, the conditional variance-covariance of income shocks within each period is the following. 
#
#
# \begin{eqnarray}
# \begin{split}
# E(\epsilon_{t}'\epsilon_{t}|Y_{t-1}) = \Sigma^2 = \sigma^2\Omega \quad \forall t  
# \end{split}
# \end{eqnarray}
#
# where $\Omega$ takes one in its diagonal and $\delta$ in off-diagonal.  
#
# The learning process and the attribution errors all stay the same as before. Individuals specify their subjective structure of the shocks depending on the sign and size of their own experienced income changes. By the same mechanism elaborated above, a lucky person has lower perceived risks than her unlucky peer at any point of the time. This distinction between the two group stays the same even if the underlying income shocks are indeed correlated. 
#
# What's new in the presence of aggregate risks lies in the behaviors of average perceived risks, because there is an aggregate shock that drives the comovement of the income shocks affecting individuals. Compared to the environment with pure idiosyncratic risks, there is no longer an approximately equal fraction of lucky and unlucky agents at a given time. Instead, the relative fraction of each group depends on the recently realized aggregate shock. If the aggregate shock is positive, more people have experienced good luck and may, therefore, underestimate the correlation (a smaller $\tilde \delta$). This drives down the average perceived income risks among the population. If the aggregate shock is negative, more people have just experienced income decrease thus arriving at a higher perceived income uncertainty. 
#
# This naturally leads to a counter-cyclical pattern of the average perceived risks in the economy. The interplay of aggregate risks and attribution errors adds cyclical movements of the average perceived risks. The two conditions are both necessary to generate this pattern. Without the aggregate risk, both income shocks and perceived income shocks are purely idiosyncratic and they are averaged out in the aggregate level. Without attribution errors, agents symmetrically process experiences when forming future risk perceptions.
#
# The upper panel in Figure \ref{fig:recent_change_var_sim} illustrates the first point. The scatter plots showcase the correlation between average income changes across population and average perceive risks under purely idiosyncratic risks and aggregate risks. The negative correlation with aggregate risks illustrate the counter-cylical perceived risks. There is no such a correlation under purely idiosyncratic risks. The bottom panel in Figure \ref{fig:recent_change_var_sim} testifies the second point. It plots the same correlation with and without attribution errors when the aggregate risk exists. Attribution errors brings about the asymmetry not seen when the bias is absent. 

# + {"caption": "Simulatd Average Labor Market and Perceived Risk", "code_folding": [], "label": "fig:recent_change_var_sim1", "widefigure": true, "hide_input": true, "hide_output": true}
## insert figures 
graph_path = os.path.join(path,'../Graphs/theory/')

fig_list = ['var_recent_change_sim.jpg']
            
nb_fig = len(fig_list)
file_list = [graph_path+fig for fig in fig_list]

## show figures 
plt.figure(figsize=(70,45))
for i in range(nb_fig):
    plt.subplot(nb_fig,1,i+1)
    plt.imshow(mpimg.imread(file_list[i]))
    plt.axis("off")

# + {"caption": "Simulated Average Labor Market Outcome and Perceived Risk", "code_folding": [], "label": "fig:recent_change_var_sim2", "widefigure": true, "hide_input": true, "hide_output": true}
## insert figures 
graph_path = os.path.join(path,'../Graphs/theory/')

fig_list = ['var_recent_change_sim2.jpg']
            
nb_fig = len(fig_list)
file_list = [graph_path+fig for fig in fig_list]

## show figures 
plt.figure(figsize=(70,45))
for i in range(nb_fig):
    plt.subplot(nb_fig,1,i+1)
    plt.imshow(mpimg.imread(file_list[i]))
    plt.axis("off")
# -

# # Experience-based life-cycle consumption/saving  
#
# Each consumer solves a life-cycle consumption/saving problem formulated by <cite data-cite="gourinchas2002consumption">Gourinchas and Parker, 2002</cite>. There is only one deviation from the original model: each agent imperfectly knows the parameters of income process over the life cycle and forms his/her best guess at each point of the time based on past experience. I first set up the model under the assumption of perfect understanding and then extend it to the imperfect understanding scenarior in the next section.   
#
#
#
# ## The standard life-cycle problem
#
# Each agent works for $T$ periods since entering the labor market, during which he/she earns stochastic labor income $y_\tau$ at the work-age of $\tau$. After retiring at age of $T+1$, the agent lives for for another $L-T$ periods of life. Since a cannonical life-cycle problem is the same in nature regardless of the cohort and calender time, we set up the problem generally along the age of work $\tau$. The consumer chooses the whole future consumption path to maximize expected life-long utility. 
#
# \begin{equation}
# \begin{split}
# E\left[\sum^{\tau=L}_{\tau=1}\beta^\tau u(c_{\tau})\right] \\
# u(c) = \frac{c^{1-\rho}}{1-\rho}
# \end{split}
# \end{equation}
#
# where $c_\tau$ represents consumption at the work-age of $\tau$. The felicity function $u$ takes the standard CRRA form with relative risk aversion of $\rho$. We assume away the bequest motive and preference-shifter along life cycle that are present in the original model without loss of the key insights regarding income risks. 
#
# Denote the financial wealth at age of $\tau$ as $b_{\tau}$. Given initial wealth $b_1$, the consumer's problem is subject to the borrowing constraint 
#
# \begin{equation}
# b_{\tau}\geq 0
# \end{equation}
#
# and inter-temporal budget constraint.
#
# \begin{equation}
# \begin{split}
# b_{\tau}+y_{\tau} = m_\tau   \\
# b_{\tau+1} = (m_\tau-c_{\tau})R
# \end{split}
# \end{equation}
#
# where $m_\tau$ is the total cash in hand at the begining of period $\tau$. $R$ is the risk-free interest rate. Note that after retirement labor income is zero through the end of life. 
#
# The stochastic labor income during the agent's career consists of a mulplicative predictable component by known factors $Z_\tau$ and a stochastic component $\epsilon_{\tau}$ which embodies shocks of different nature.  
#
# \begin{equation}
# \begin{split}
# y_{\tau} = \phi Z_{\tau}\epsilon_{\tau} 
# \end{split}
# \end{equation}
#
#
# Notice here I explicitly include the predictable component, deviating from the common practice in the literature. Although under perfect understanding, the predictable component does not enter consumption decision effectively since it is anticipated ex ante, this is no longer so once we introduce imperfect understanding regarding the parameters of the income process $\phi$. The prediction uncertainty enters the perception of income risks. We will return to this point in the next section. 
#
#
# The stochastic shock to income $\epsilon$ is composed of two components: a permanent one $p_t$  and a transitory one $u$. The former grows by a age-specific growth rate $G$ along the life cycle and is subject to a shock $n$ at each period. 
#
# \begin{equation}
# \begin{split}
# \epsilon_{\tau} = p_{\tau}u_{\tau} \\
# p_{\tau} = G_{\tau}p_{\tau-1} n_{\tau}
# \end{split}
# \end{equation}
#
# The permanent shock $n$ follows a log normal distribution, $ln(n_\tau) \sim N(0,\sigma^2_\tau)$. The transitory shock $u$ either takes value of zero with probability of $0\leq p<1$, i.e. unemployment, or otherwise follows a log normal with $ln(u_\tau) \sim N(0,\sigma^2_u)$. Following <cite data-cite="gourinchas2002consumption">Gourinchas and Parker, 2002</cite>, I assume the size of the volatility of the two shocks are time-invariant. The results of this paper are not sensitive to this assumption. 
#
# At this stage, we do not seek to differentiate the aggregate/idiosyncratic components of either one the two enter the individual consumption problem indifferently under perfect understanding. With imperfect understanding and subjective attribution, however, the differences of the two matters since it affects the prediction uncertainty and perceived income risks. 
#
# The following value function characterizes the problem. 
#
# \begin{equation}
# \begin{split}
# V_{\tau}(m_\tau, p_\tau) = \textrm{max} \quad u(c_\tau) + \beta E_{\tau}\left[V_{\tau+1}(m_{\tau+1}, p_{\tau+1})\right] 
# \end{split}
# \end{equation}
#
# where the agents treat total cash in hand and permanent income as the two state variables. On the backgroud, the income process parameters $\Gamma = [\phi,\sigma_n,\sigma_u]$ affect the consumption decisions. But to the extent that the agents have perfect knowledge of them, they are simply taken as given. 
#
#
# ## Under imperfect understanding/learning from experience
#
# The crucial deviation of this model from the standard framework reproduced above is that the agents do not know about the income parameters $\Gamma$, and the decisions are only based on their best guess obtained through learning from experience in a manner we formulate in the previous section. This changes the problem in at least two ways. First, given agents potentially differ in their experiences, perceived income processes differ. Second, even if under same experiences, different subjective determinations of the nature of income shocks result in different risk perceptions. To allow for the cross-sectional heterogeneity across individuals and cohorts in income risk perceptions, now explicitly define the problem using agent-time-cohort-specific value function. For agent $i$ from cohort $c=t-\tau$ at time $t$, the value function is the following.
#
# \begin{equation}
# \begin{split}
# V_{i,\tau,t}(m_{i,\tau,t}, p_{i,\tau,t}) = \textrm{max} \quad u(c_{i,\tau+1,t+1}) + \beta E_{i,\tau,t}\left[V_{i,\tau+1,t+1}(m_{i,\tau+1,t+1}, p_{i,\tau+1,t+1})\right] 
# \end{split}
# \end{equation}
#
# Notice that the key difference of the new value function from the one under a perfect understanding is that expectational operator of next-period value function becomes subjective and potentially agent-time-specific. Another way to put it is that $E_{i,\tau,t}$ is conditional on the most recent parameter estimate of the income process $\tilde \Gamma_{i,\tau,t} = \left[\tilde \phi_{i,\tau,t},\tilde \sigma_{n,i,\tau,t}, \tilde \sigma_{u,i,\tau,t}\right]$ and the uncertainty about the estimate $Var_{i,\tau,t}(\tilde \phi)$. 
#
# The perceived income risk affects the value of the expected value. It implicitly contains two components. The first is the shock uncertainty that can be predicted at best by the past income volatility estimation of different components. The second is the parameter uncertainty regarding the agents' estimation of a parameter associated with the deterministic components $\phi$. Since both components imply a further dispersion from the perfect understanding case, it will unambiguously induce a stronger precautionary saving motive than the latter case. 
#
#
# ## Consumption functions 
#
# I compare the life cycle consumption functions between
#
# - perfectly understanding vs imperfect understanding
# - same age different experiences 
# - under different digree of attribution 
#
# ## Implications for consumption inequality 
#
# - consumption inequality(thus wealth inequality) and heterogeneity in MPCs now is further amplified by belief differences in income risks. 

#
# #  Conclusion
#
# How do people form perceptions about their income risks? Theoretically, this paper builds an experience-based learning model that features an imperfect understanding of the size of the risks as well as its nature. By extending the learning-from-experience into a cross-sectional setting, I introduce a mechanism in which future risk perceptions are dependent upon past income volatility or cross-sectional distributions of the income shocks. I also introduce a novel channel - subjective attribution, into the learning to capture how income risk perceptions are also affected by the subjective determination of the nature of income risks. It is shown that the model generates a few testable predictions about the relationship between experience/age/income and perceived income risks.
#
# Empirically, I utilize a recently available panel of income density surveys of U.S. earners to shed light directly on subjective income risk profiles. I explore the cross-sectional heterogeneity in income risk perceptions across ages, generations, and income group as well as its cyclicality with the current labor market outcome. I found that risk perceptions are positively correlated with experienced income volatility, therefore differing across age and cohorts. I also found perceived income risks of earners counter-cyclically react to the recent labor market conditions.
#
# Finally, the paper builds the experience-based-learning and subjective attribution into an otherwise standard life cycle model of consumption. I show an imperfect understanding of the income process unambiguously motivates additional precautionary saving than in a model of perfect understanding. I also show that the consumption decisions of agents at the same age may still differ as long as they have experienced different histories at both individual and aggregate levels. Such belief heterogeneity further amplifies the inequality in consumption and wealth accumulation of different generations.
#
# Many interesting questions are worth exploring although they are beyond the scope of the paper. First, to what extent the model in this paper could help account for the well-documented differences between millennials and earlier generations in their saving behaviors, homeownership, and stock market investment? Within the very short span of their early career, millennials have had experienced two aggregate economic catastrophes, namely the global financial crisis and the pandemic. The evidence and model in this paper both suggest that this may have persistent impacts on the new generations' risk perceptions, thus economic decisions. 
#
# Second, what general equilibrium consequences would the life-cycle and intergenerational differences in risk perceptions generate? It is true that demographic compositions are slow-moving variables. But the gradual change in the demographic structure of the economy may interact with the different experienced macroeconomic histories, generating non-stationary belief distributions across time. This will undoubtedly lead to a different macroeconomic equilibrium. 
#
# Third, although this paper focuses on the size and nature of income risks, the imperfect understanding could also and may very likely take the form of misperceiving correlation between different random variables relevant to economic decisions. A perfect example of this is the correlation between income risks and stock market returns. The subjective correlation between the two may shed light on participation puzzles and equity premium in the macroeconomic finance literature. 
