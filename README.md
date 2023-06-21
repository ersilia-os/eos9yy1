# Human Liver Cytosolic Stability

The human liver cytosol stability model is used for predicting the stability of a drug in the cytosol of human liver cells, which is beneficial for identifying potential drug candidates early during the drug discovery process. If a drug compound is quickly absorbed, it may not reach the intended target in the body or become toxic. On the other hand, if a drug compound is too stable, it could accumulate and cause detrimental effects. The authors use an NCATS dataset of 1450 compounds screened in vitro in mouse and human cytosol fractions. Compounds were classified as stable (half-life > 30min) or unstable (half-life ≤ 30 min). Note that authors report the dataset was biased towards stable compounds. The validation set of 250 compounds is openly available.

## Identifiers

* EOS model ID: `eos9yy1`
* Slug: `ncats-hlcs`

## Characteristics

* Input: `Compound`
* Input Shape: `Single`
* Task: `Classification`
* Output: `Probability`
* Output Type: `Float`
* Output Shape: `Single`
* Interpretation: Probability of a compound being unstable (half-life ≤ 30min) due to liver cells metabolism

## References

* [Publication](https://jcheminf.biomedcentral.com/articles/10.1186/s13321-020-00426-7)
* [Source Code](https://github.com/ncats/ncats-adme)
* Ersilia contributor: [pauline-banye](https://github.com/pauline-banye)

## Ersilia model URLs
* [GitHub](https://github.com/ersilia-os/eos9yy1)
* [AWS S3](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos9yy1.zip)
* [DockerHub](https://hub.docker.com/r/ersiliaos/eos9yy1) (AMD64, ARM64)

## Citation

If you use this model, please cite the [original authors](https://jcheminf.biomedcentral.com/articles/10.1186/s13321-020-00426-7) of the model and the [Ersilia Model Hub](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff).

## License

This package is licensed under a GPL-3.0 license. The model contained within this package is licensed under a None license.

Notice: Ersilia grants access to these models 'as is' provided by the original authors, please refer to the original code repository and/or publication if you use the model in your research.

## About Us

The [Ersilia Open Source Initiative](https://ersilia.io) is a Non Profit Organization ([1192266](https://register-of-charities.charitycommission.gov.uk/charity-search/-/charity-details/5170657/full-print)) with the mission is to equip labs, universities and clinics in LMIC with AI/ML tools for infectious disease research.

[Help us](https://www.ersilia.io/donate) achieve our mission!