# **Human Liver Cytosolic Stability**

## **Model identifiers**
- Slug: ncats-hlcs
- Ersilia ID: 
- Tags: stability
#
## **Model description**
<p align="justify">
The human liver cytosol stability model is used for predicting the stability of a drug in the cytosol of human liver cells, which is beneficial for identifying potential drug candidates early during the drug discovery process. If a drug is quickly absorbed, it may become toxic or fail to reach the intended target in the body.
</p>
<p align="justify">
This data was provided by the National Center for Advancing Translational Sciences (NCATS). A probability of below 0.5 is considered high stability. Probability of 0.5 or greater is considered low stability. 
</p>

- Input: SMILES
- Output: SMILES
#
## **Source code**

Cite the source publication
[Predicting liver cytosol stability of small molecules](https://jcheminf.biomedcentral.com/articles/10.1186/s13321-020-00426-7)

- Code: [NCATS-ADME](https://github.com/ncats/ncats-adme.git)
- Checkpoints: include the link to the checkpoints used if model is a pretrained model
#
## **License**
GNU General Public License v3.0.

## **History**
- The model was incorporated into Ersilia on the 22th of January, 2023.
- Modifications to the original code.
    1. Removal of Flask functionalities and dependencies.
    2. Striping unused functions from the original code.

- To run the model, follow these [steps](model/README.md).

The [Ersilia Open Source Initiative](https://ersilia.io) is a Non Profit Organization ([1192266](https://register-of-charities.charitycommission.gov.uk/charity-search/-/charity-details/5170657/full-print)) with the mission is to equip labs, universities and clinics in LMIC with AI/ML tools for infectious disease research.

[Help us](https://www.ersilia.io/donate) achieve our mission or [volunteer](https://www.ersilia.io/volunteer) with us!
