[TOC]

# **Notes of Machine Learning**

## **What is Ml?**
it's said to learn from experience E with respect to some task T and performance measure P,if T measured by P improves with E.

most recently used:supervised learning and unsupervised learning

## **Supervised Learning**
house pricing prediction:Price ~ Size

Supervised learning--right answers given,Regression:predict continuous valued output(price)

Breast Cancer:malignant or benign? ~ Tumor size/age...(classification question:discrete valued output(0 or 1))

## **Unsupervised Learning**
do not have labels,e.g. clustering algorithm 

cocktail party problem:many speakers speak at the same time while many microphones recording--how to separate them?

Octave

## **Linear Regression**

size of house $\rightarrow$ hypothsis(h) $\rightarrow$ estimated price 

how to represent h?
$$ 
h_\theta(x)=\theta_0+\theta_1 x 
$$
(**univariate linear regression**)

$\theta_i:$ parameters

the idea is to choose $\theta_1,\theta_0$ so that $h_\theta (x)$ is close to $y$ for training examples,that is,to minimize
$$
\mathop{\text{minimize}}\limits_{\theta_0,\theta_1}\frac{1}{2m} \sum_{i=1}^m[h_\theta(x^{(i)})-y^{(i)}]^2 
$$

**cost function:**
$$
J(\theta_0,\theta_1)=\frac{1}{2m} \sum_{i=1}^m[h_\theta(x^{(i)})-y^{(i)}]^2
$$
**Squared error cost function**

### **Cost Function**

gradient descent algorithm:
outline:

* start with some $\theta_0,\theta_1$
* keep changing $\theta_0,\theta_1$ to reduce $J(\theta_0,\theta_1)$ until we hopefully end up at a minimum(or local minimum)
  

