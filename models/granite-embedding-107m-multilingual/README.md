---
language:
- en
- ar
- cs
- de
- es
- fr
- it
- ja
- ko
- nl
- pt
- zh
license: apache-2.0
library_name: sentence-transformers
tags:
- language
- granite
- embeddings
- multilingual
- mteb
- transformers
model-index:
- name: ibm-granite/granite-embedding-107m-multilingual
  results:
  - dataset:
      config: en-ext
      name: MTEB AmazonCounterfactualClassification (en-ext)
      revision: e8379541af4e31359cca9fbcf4b00f2671dba205
      split: test
      type: mteb/amazon_counterfactual
    metrics:
    - type: accuracy
      value: 72.7136
    - type: f1
      value: 60.44540000000001
    - type: f1_weighted
      value: 77.8541
    - type: ap
      value: 22.4958
    - type: ap_weighted
      value: 22.4958
    - type: main_score
      value: 72.7136
    task:
      type: Classification
  - dataset:
      config: en
      name: MTEB AmazonCounterfactualClassification (en)
      revision: e8379541af4e31359cca9fbcf4b00f2671dba205
      split: test
      type: mteb/amazon_counterfactual
    metrics:
    - type: accuracy
      value: 71.6716
    - type: f1
      value: 65.4221
    - type: f1_weighted
      value: 74.3533
    - type: ap
      value: 33.7567
    - type: ap_weighted
      value: 33.7567
    - type: main_score
      value: 71.6716
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB AmazonPolarityClassification (default)
      revision: e2d317d38cd51312af73b3d32a06d1a08b442046
      split: test
      type: mteb/amazon_polarity
    metrics:
    - type: accuracy
      value: 66.5804
    - type: f1
      value: 66.2191
    - type: f1_weighted
      value: 66.2191
    - type: ap
      value: 61.340799999999994
    - type: ap_weighted
      value: 61.340799999999994
    - type: main_score
      value: 66.5804
    task:
      type: Classification
  - dataset:
      config: en
      name: MTEB AmazonReviewsClassification (en)
      revision: 1399c76144fd37290681b995c656ef9b2e06e26d
      split: test
      type: mteb/amazon_reviews_multi
    metrics:
    - type: accuracy
      value: 36.412
    - type: f1
      value: 35.633199999999995
    - type: f1_weighted
      value: 35.633199999999995
    - type: main_score
      value: 36.412
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB AppsRetrieval (default)
      revision: f22508f96b7a36c2415181ed8bb76f76e04ae2d5
      split: test
      type: CoIR-Retrieval/apps
    metrics:
    - type: ndcg_at_1
      value: 2.39
    - type: ndcg_at_3
      value: 3.527
    - type: ndcg_at_5
      value: 3.9759999999999995
    - type: ndcg_at_10
      value: 4.537
    - type: ndcg_at_20
      value: 5.140000000000001
    - type: ndcg_at_100
      value: 6.526
    - type: ndcg_at_1000
      value: 9.797
    - type: map_at_1
      value: 2.39
    - type: map_at_3
      value: 3.2489999999999997
    - type: map_at_5
      value: 3.499
    - type: map_at_10
      value: 3.7220000000000004
    - type: map_at_20
      value: 3.887
    - type: map_at_100
      value: 4.058
    - type: map_at_1000
      value: 4.146
    - type: recall_at_1
      value: 2.39
    - type: recall_at_3
      value: 4.329000000000001
    - type: recall_at_5
      value: 5.418
    - type: recall_at_10
      value: 7.198
    - type: recall_at_20
      value: 9.588000000000001
    - type: recall_at_100
      value: 17.371
    - type: recall_at_1000
      value: 45.206
    - type: precision_at_1
      value: 2.39
    - type: precision_at_3
      value: 1.443
    - type: precision_at_5
      value: 1.084
    - type: precision_at_10
      value: 0.72
    - type: precision_at_20
      value: 0.479
    - type: precision_at_100
      value: 0.174
    - type: precision_at_1000
      value: 0.045
    - type: mrr_at_1
      value: 2.3904
    - type: mrr_at_3
      value: 3.2492
    - type: mrr_at_5
      value: 3.4989
    - type: mrr_at_10
      value: 3.7220000000000004
    - type: mrr_at_20
      value: 3.8869000000000002
    - type: mrr_at_100
      value: 4.0578
    - type: mrr_at_1000
      value: 4.1463
    - type: nauc_ndcg_at_1_max
      value: 37.599700000000006
    - type: nauc_ndcg_at_1_std
      value: 20.302899999999998
    - type: nauc_ndcg_at_1_diff1
      value: 40.4987
    - type: nauc_ndcg_at_3_max
      value: 31.119400000000002
    - type: nauc_ndcg_at_3_std
      value: 11.7335
    - type: nauc_ndcg_at_3_diff1
      value: 28.788000000000004
    - type: nauc_ndcg_at_5_max
      value: 28.505399999999998
    - type: nauc_ndcg_at_5_std
      value: 12.1402
    - type: nauc_ndcg_at_5_diff1
      value: 25.730900000000002
    - type: nauc_ndcg_at_10_max
      value: 27.0656
    - type: nauc_ndcg_at_10_std
      value: 12.648699999999998
    - type: nauc_ndcg_at_10_diff1
      value: 22.0832
    - type: nauc_ndcg_at_20_max
      value: 25.953599999999998
    - type: nauc_ndcg_at_20_std
      value: 12.550500000000001
    - type: nauc_ndcg_at_20_diff1
      value: 19.3722
    - type: nauc_ndcg_at_100_max
      value: 23.268
    - type: nauc_ndcg_at_100_std
      value: 12.8176
    - type: nauc_ndcg_at_100_diff1
      value: 15.9275
    - type: nauc_ndcg_at_1000_max
      value: 21.921499999999998
    - type: nauc_ndcg_at_1000_std
      value: 12.656300000000002
    - type: nauc_ndcg_at_1000_diff1
      value: 13.9004
    - type: nauc_map_at_1_max
      value: 37.599700000000006
    - type: nauc_map_at_1_std
      value: 20.302899999999998
    - type: nauc_map_at_1_diff1
      value: 40.4987
    - type: nauc_map_at_3_max
      value: 32.2818
    - type: nauc_map_at_3_std
      value: 13.276399999999999
    - type: nauc_map_at_3_diff1
      value: 30.9064
    - type: nauc_map_at_5_max
      value: 30.5166
    - type: nauc_map_at_5_std
      value: 13.406
    - type: nauc_map_at_5_diff1
      value: 28.8213
    - type: nauc_map_at_10_max
      value: 29.731999999999996
    - type: nauc_map_at_10_std
      value: 13.5688
    - type: nauc_map_at_10_diff1
      value: 26.888499999999997
    - type: nauc_map_at_20_max
      value: 29.211399999999998
    - type: nauc_map_at_20_std
      value: 13.4739
    - type: nauc_map_at_20_diff1
      value: 25.6814
    - type: nauc_map_at_100_max
      value: 28.578300000000002
    - type: nauc_map_at_100_std
      value: 13.5385
    - type: nauc_map_at_100_diff1
      value: 24.793100000000003
    - type: nauc_map_at_1000_max
      value: 28.3912
    - type: nauc_map_at_1000_std
      value: 13.5039
    - type: nauc_map_at_1000_diff1
      value: 24.570600000000002
    - type: nauc_recall_at_1_max
      value: 37.599700000000006
    - type: nauc_recall_at_1_std
      value: 20.302899999999998
    - type: nauc_recall_at_1_diff1
      value: 40.4987
    - type: nauc_recall_at_3_max
      value: 28.598000000000003
    - type: nauc_recall_at_3_std
      value: 8.3847
    - type: nauc_recall_at_3_diff1
      value: 24.1871
    - type: nauc_recall_at_5_max
      value: 24.5381
    - type: nauc_recall_at_5_std
      value: 9.8274
    - type: nauc_recall_at_5_diff1
      value: 19.6821
    - type: nauc_recall_at_10_max
      value: 22.5445
    - type: nauc_recall_at_10_std
      value: 11.4415
    - type: nauc_recall_at_10_diff1
      value: 13.8268
    - type: nauc_recall_at_20_max
      value: 21.3196
    - type: nauc_recall_at_20_std
      value: 11.5932
    - type: nauc_recall_at_20_diff1
      value: 10.1991
    - type: nauc_recall_at_100_max
      value: 16.9415
    - type: nauc_recall_at_100_std
      value: 12.353200000000001
    - type: nauc_recall_at_100_diff1
      value: 5.7534
    - type: nauc_recall_at_1000_max
      value: 15.9223
    - type: nauc_recall_at_1000_std
      value: 12.2848
    - type: nauc_recall_at_1000_diff1
      value: 3.5477000000000003
    - type: nauc_precision_at_1_max
      value: 37.599700000000006
    - type: nauc_precision_at_1_std
      value: 20.302899999999998
    - type: nauc_precision_at_1_diff1
      value: 40.4987
    - type: nauc_precision_at_3_max
      value: 28.598000000000003
    - type: nauc_precision_at_3_std
      value: 8.3847
    - type: nauc_precision_at_3_diff1
      value: 24.1871
    - type: nauc_precision_at_5_max
      value: 24.5381
    - type: nauc_precision_at_5_std
      value: 9.8274
    - type: nauc_precision_at_5_diff1
      value: 19.6821
    - type: nauc_precision_at_10_max
      value: 22.5445
    - type: nauc_precision_at_10_std
      value: 11.4415
    - type: nauc_precision_at_10_diff1
      value: 13.8268
    - type: nauc_precision_at_20_max
      value: 21.3196
    - type: nauc_precision_at_20_std
      value: 11.5932
    - type: nauc_precision_at_20_diff1
      value: 10.1991
    - type: nauc_precision_at_100_max
      value: 16.9415
    - type: nauc_precision_at_100_std
      value: 12.353200000000001
    - type: nauc_precision_at_100_diff1
      value: 5.7534
    - type: nauc_precision_at_1000_max
      value: 15.9223
    - type: nauc_precision_at_1000_std
      value: 12.2848
    - type: nauc_precision_at_1000_diff1
      value: 3.5477000000000003
    - type: nauc_mrr_at_1_max
      value: 37.599700000000006
    - type: nauc_mrr_at_1_std
      value: 20.302899999999998
    - type: nauc_mrr_at_1_diff1
      value: 40.4987
    - type: nauc_mrr_at_3_max
      value: 32.2818
    - type: nauc_mrr_at_3_std
      value: 13.276399999999999
    - type: nauc_mrr_at_3_diff1
      value: 30.9064
    - type: nauc_mrr_at_5_max
      value: 30.5166
    - type: nauc_mrr_at_5_std
      value: 13.406
    - type: nauc_mrr_at_5_diff1
      value: 28.8213
    - type: nauc_mrr_at_10_max
      value: 29.731999999999996
    - type: nauc_mrr_at_10_std
      value: 13.5688
    - type: nauc_mrr_at_10_diff1
      value: 26.888499999999997
    - type: nauc_mrr_at_20_max
      value: 29.211399999999998
    - type: nauc_mrr_at_20_std
      value: 13.4739
    - type: nauc_mrr_at_20_diff1
      value: 25.6814
    - type: nauc_mrr_at_100_max
      value: 28.578300000000002
    - type: nauc_mrr_at_100_std
      value: 13.5385
    - type: nauc_mrr_at_100_diff1
      value: 24.793100000000003
    - type: nauc_mrr_at_1000_max
      value: 28.3912
    - type: nauc_mrr_at_1000_std
      value: 13.5039
    - type: nauc_mrr_at_1000_diff1
      value: 24.570600000000002
    - type: main_score
      value: 4.537
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB ArguAna (default)
      revision: c22ab2a51041ffd869aaddef7af8d8215647e41a
      split: test
      type: mteb/arguana
    metrics:
    - type: ndcg_at_1
      value: 27.168999999999997
    - type: ndcg_at_3
      value: 41.08
    - type: ndcg_at_5
      value: 46.375
    - type: ndcg_at_10
      value: 51.663000000000004
    - type: ndcg_at_20
      value: 54.339999999999996
    - type: ndcg_at_100
      value: 55.656000000000006
    - type: ndcg_at_1000
      value: 55.875
    - type: map_at_1
      value: 27.168999999999997
    - type: map_at_3
      value: 37.482
    - type: map_at_5
      value: 40.416000000000004
    - type: map_at_10
      value: 42.624
    - type: map_at_20
      value: 43.376999999999995
    - type: map_at_100
      value: 43.578
    - type: map_at_1000
      value: 43.588
    - type: recall_at_1
      value: 27.168999999999997
    - type: recall_at_3
      value: 51.565000000000005
    - type: recall_at_5
      value: 64.43799999999999
    - type: recall_at_10
      value: 80.654
    - type: recall_at_20
      value: 91.11
    - type: recall_at_100
      value: 97.937
    - type: recall_at_1000
      value: 99.57300000000001
    - type: precision_at_1
      value: 27.168999999999997
    - type: precision_at_3
      value: 17.188
    - type: precision_at_5
      value: 12.888
    - type: precision_at_10
      value: 8.065
    - type: precision_at_20
      value: 4.555
    - type: precision_at_100
      value: 0.979
    - type: precision_at_1000
      value: 0.1
    - type: mrr_at_1
      value: 27.6671
    - type: mrr_at_3
      value: 37.6245
    - type: mrr_at_5
      value: 40.6188
    - type: mrr_at_10
      value: 42.8016
    - type: mrr_at_20
      value: 43.5582
    - type: mrr_at_100
      value: 43.7551
    - type: mrr_at_1000
      value: 43.765
    - type: nauc_ndcg_at_1_max
      value: -4.3233
    - type: nauc_ndcg_at_1_std
      value: -3.5458000000000003
    - type: nauc_ndcg_at_1_diff1
      value: 10.8118
    - type: nauc_ndcg_at_3_max
      value: -1.1566
    - type: nauc_ndcg_at_3_std
      value: -2.5897
    - type: nauc_ndcg_at_3_diff1
      value: 8.3298
    - type: nauc_ndcg_at_5_max
      value: -1.399
    - type: nauc_ndcg_at_5_std
      value: -1.9604
    - type: nauc_ndcg_at_5_diff1
      value: 7.6803
    - type: nauc_ndcg_at_10_max
      value: 0.7746000000000001
    - type: nauc_ndcg_at_10_std
      value: -0.9521
    - type: nauc_ndcg_at_10_diff1
      value: 9.1107
    - type: nauc_ndcg_at_20_max
      value: 1.0111999999999999
    - type: nauc_ndcg_at_20_std
      value: 0.1519
    - type: nauc_ndcg_at_20_diff1
      value: 9.5802
    - type: nauc_ndcg_at_100_max
      value: -0.3616
    - type: nauc_ndcg_at_100_std
      value: -0.6704
    - type: nauc_ndcg_at_100_diff1
      value: 9.2401
    - type: nauc_ndcg_at_1000_max
      value: -0.6766
    - type: nauc_ndcg_at_1000_std
      value: -1.0513
    - type: nauc_ndcg_at_1000_diff1
      value: 9.0561
    - type: nauc_map_at_1_max
      value: -4.3233
    - type: nauc_map_at_1_std
      value: -3.5458000000000003
    - type: nauc_map_at_1_diff1
      value: 10.8118
    - type: nauc_map_at_3_max
      value: -1.9845000000000002
    - type: nauc_map_at_3_std
      value: -2.6683
    - type: nauc_map_at_3_diff1
      value: 8.7329
    - type: nauc_map_at_5_max
      value: -2.1342
    - type: nauc_map_at_5_std
      value: -2.3612
    - type: nauc_map_at_5_diff1
      value: 8.4139
    - type: nauc_map_at_10_max
      value: -1.331
    - type: nauc_map_at_10_std
      value: -1.982
    - type: nauc_map_at_10_diff1
      value: 9.004199999999999
    - type: nauc_map_at_20_max
      value: -1.3376000000000001
    - type: nauc_map_at_20_std
      value: -1.7424
    - type: nauc_map_at_20_diff1
      value: 9.1012
    - type: nauc_map_at_100_max
      value: -1.5152
    - type: nauc_map_at_100_std
      value: -1.8418
    - type: nauc_map_at_100_diff1
      value: 9.0513
    - type: nauc_map_at_1000_max
      value: -1.5264
    - type: nauc_map_at_1000_std
      value: -1.8530000000000002
    - type: nauc_map_at_1000_diff1
      value: 9.043800000000001
    - type: nauc_recall_at_1_max
      value: -4.3233
    - type: nauc_recall_at_1_std
      value: -3.5458000000000003
    - type: nauc_recall_at_1_diff1
      value: 10.8118
    - type: nauc_recall_at_3_max
      value: 1.2361
    - type: nauc_recall_at_3_std
      value: -2.4248
    - type: nauc_recall_at_3_diff1
      value: 7.2543
    - type: nauc_recall_at_5_max
      value: 0.9835999999999999
    - type: nauc_recall_at_5_std
      value: -0.5726
    - type: nauc_recall_at_5_diff1
      value: 5.2376
    - type: nauc_recall_at_10_max
      value: 12.7099
    - type: nauc_recall_at_10_std
      value: 4.9688
    - type: nauc_recall_at_10_diff1
      value: 10.5016
    - type: nauc_recall_at_20_max
      value: 28.2615
    - type: nauc_recall_at_20_std
      value: 23.7662
    - type: nauc_recall_at_20_diff1
      value: 17.6392
    - type: nauc_recall_at_100_max
      value: 31.295099999999998
    - type: nauc_recall_at_100_std
      value: 47.1556
    - type: nauc_recall_at_100_diff1
      value: 24.055699999999998
    - type: nauc_recall_at_1000_max
      value: 14.418000000000001
    - type: nauc_recall_at_1000_std
      value: 56.899699999999996
    - type: nauc_recall_at_1000_diff1
      value: 3.7199999999999998
    - type: nauc_precision_at_1_max
      value: -4.3233
    - type: nauc_precision_at_1_std
      value: -3.5458000000000003
    - type: nauc_precision_at_1_diff1
      value: 10.8118
    - type: nauc_precision_at_3_max
      value: 1.2361
    - type: nauc_precision_at_3_std
      value: -2.4248
    - type: nauc_precision_at_3_diff1
      value: 7.2543
    - type: nauc_precision_at_5_max
      value: 0.9835999999999999
    - type: nauc_precision_at_5_std
      value: -0.5726
    - type: nauc_precision_at_5_diff1
      value: 5.2376
    - type: nauc_precision_at_10_max
      value: 12.7099
    - type: nauc_precision_at_10_std
      value: 4.9688
    - type: nauc_precision_at_10_diff1
      value: 10.5016
    - type: nauc_precision_at_20_max
      value: 28.2615
    - type: nauc_precision_at_20_std
      value: 23.7662
    - type: nauc_precision_at_20_diff1
      value: 17.6392
    - type: nauc_precision_at_100_max
      value: 31.295099999999998
    - type: nauc_precision_at_100_std
      value: 47.1556
    - type: nauc_precision_at_100_diff1
      value: 24.055699999999998
    - type: nauc_precision_at_1000_max
      value: 14.418000000000001
    - type: nauc_precision_at_1000_std
      value: 56.899699999999996
    - type: nauc_precision_at_1000_diff1
      value: 3.7199999999999998
    - type: nauc_mrr_at_1_max
      value: -4.2285
    - type: nauc_mrr_at_1_std
      value: -2.9951
    - type: nauc_mrr_at_1_diff1
      value: 9.2226
    - type: nauc_mrr_at_3_max
      value: -2.8361
    - type: nauc_mrr_at_3_std
      value: -2.5372
    - type: nauc_mrr_at_3_diff1
      value: 7.205
    - type: nauc_mrr_at_5_max
      value: -2.827
    - type: nauc_mrr_at_5_std
      value: -2.1469
    - type: nauc_mrr_at_5_diff1
      value: 6.9564
    - type: nauc_mrr_at_10_max
      value: -2.0531
    - type: nauc_mrr_at_10_std
      value: -1.8227
    - type: nauc_mrr_at_10_diff1
      value: 7.500500000000001
    - type: nauc_mrr_at_20_max
      value: -2.0823
    - type: nauc_mrr_at_20_std
      value: -1.585
    - type: nauc_mrr_at_20_diff1
      value: 7.5577000000000005
    - type: nauc_mrr_at_100_max
      value: -2.2609
    - type: nauc_mrr_at_100_std
      value: -1.6787
    - type: nauc_mrr_at_100_diff1
      value: 7.500500000000001
    - type: nauc_mrr_at_1000_max
      value: -2.2721999999999998
    - type: nauc_mrr_at_1000_std
      value: -1.6898
    - type: nauc_mrr_at_1000_diff1
      value: 7.492400000000001
    - type: main_score
      value: 51.663000000000004
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB ArxivClusteringP2P (default)
      revision: a122ad7f3f0291bf49cc6f4d32aa80929df69d5d
      split: test
      type: mteb/arxiv-clustering-p2p
    metrics:
    - type: v_measure
      value: 41.4944
    - type: v_measure_std
      value: 13.6458
    - type: main_score
      value: 41.4944
    task:
      type: Clustering
  - dataset:
      config: default
      name: MTEB ArxivClusteringS2S (default)
      revision: f910caf1a6075f7329cdf8c1a6135696f37dbd53
      split: test
      type: mteb/arxiv-clustering-s2s
    metrics:
    - type: v_measure
      value: 30.6155
    - type: v_measure_std
      value: 14.377999999999998
    - type: main_score
      value: 30.6155
    task:
      type: Clustering
  - dataset:
      config: default
      name: MTEB AskUbuntuDupQuestions (default)
      revision: 2000358ca161889fa9c082cb41daa8dcfb161a54
      split: test
      type: mteb/askubuntudupquestions-reranking
    metrics:
    - type: map
      value: 61.9001
    - type: mrr
      value: 77.0427
    - type: nAUC_map_max
      value: 27.7273
    - type: nAUC_map_std
      value: 14.369299999999999
    - type: nAUC_map_diff1
      value: 10.7899
    - type: nAUC_mrr_max
      value: 35.606100000000005
    - type: nAUC_mrr_std
      value: 20.2621
    - type: nAUC_mrr_diff1
      value: 17.814
    - type: main_score
      value: 61.9001
    task:
      type: Reranking
  - dataset:
      config: default
      name: MTEB BIOSSES (default)
      revision: d3fb88f8f02e40887cd149695127462bbcf29b4a
      split: test
      type: mteb/biosses-sts
    metrics:
    - type: pearson
      value: 81.5558
    - type: spearman
      value: 79.2952
    - type: cosine_pearson
      value: 81.5558
    - type: cosine_spearman
      value: 79.2952
    - type: manhattan_pearson
      value: 79.4434
    - type: manhattan_spearman
      value: 78.803
    - type: euclidean_pearson
      value: 80.0336
    - type: euclidean_spearman
      value: 79.2952
    - type: main_score
      value: 79.2952
    task:
      type: STS
  - dataset:
      config: default
      name: MTEB Banking77Classification (default)
      revision: 0fd18e25b25c072e09e0d92ab615fda904d66300
      split: test
      type: mteb/banking77
    metrics:
    - type: accuracy
      value: 75.9481
    - type: f1
      value: 74.9851
    - type: f1_weighted
      value: 74.9851
    - type: main_score
      value: 75.9481
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB BiorxivClusteringP2P (default)
      revision: 65b79d1d13f80053f67aca9498d9402c2d9f1f40
      split: test
      type: mteb/biorxiv-clustering-p2p
    metrics:
    - type: v_measure
      value: 35.6038
    - type: v_measure_std
      value: 0.5428999999999999
    - type: main_score
      value: 35.6038
    task:
      type: Clustering
  - dataset:
      config: default
      name: MTEB BiorxivClusteringS2S (default)
      revision: 258694dd0231531bc1fd9de6ceb52a0853c6d908
      split: test
      type: mteb/biorxiv-clustering-s2s
    metrics:
    - type: v_measure
      value: 28.3652
    - type: v_measure_std
      value: 1.0767
    - type: main_score
      value: 28.3652
    task:
      type: Clustering
  - dataset:
      config: python
      name: MTEB COIRCodeSearchNetRetrieval (python)
      revision: 4adc7bc41202b5c13543c9c886a25f340634dab3
      split: test
      type: CoIR-Retrieval/CodeSearchNet
    metrics:
    - type: ndcg_at_1
      value: 78.69699999999999
    - type: ndcg_at_3
      value: 82.666
    - type: ndcg_at_5
      value: 83.607
    - type: ndcg_at_10
      value: 84.407
    - type: ndcg_at_20
      value: 84.92699999999999
    - type: ndcg_at_100
      value: 85.641
    - type: ndcg_at_1000
      value: 85.978
    - type: map_at_1
      value: 78.69699999999999
    - type: map_at_3
      value: 81.723
    - type: map_at_5
      value: 82.245
    - type: map_at_10
      value: 82.577
    - type: map_at_20
      value: 82.722
    - type: map_at_100
      value: 82.821
    - type: map_at_1000
      value: 82.834
    - type: recall_at_1
      value: 78.69699999999999
    - type: recall_at_3
      value: 85.38
    - type: recall_at_5
      value: 87.666
    - type: recall_at_10
      value: 90.133
    - type: recall_at_20
      value: 92.171
    - type: recall_at_100
      value: 96.012
    - type: recall_at_1000
      value: 98.68599999999999
    - type: precision_at_1
      value: 78.69699999999999
    - type: precision_at_3
      value: 28.46
    - type: precision_at_5
      value: 17.533
    - type: precision_at_10
      value: 9.013
    - type: precision_at_20
      value: 4.609
    - type: precision_at_100
      value: 0.96
    - type: precision_at_1000
      value: 0.099
    - type: mrr_at_1
      value: 78.7036
    - type: mrr_at_3
      value: 81.7223
    - type: mrr_at_5
      value: 82.24719999999999
    - type: mrr_at_10
      value: 82.5792
    - type: mrr_at_20
      value: 82.72460000000001
    - type: mrr_at_100
      value: 82.82350000000001
    - type: mrr_at_1000
      value: 82.8357
    - type: nauc_ndcg_at_1_max
      value: 84.22319999999999
    - type: nauc_ndcg_at_1_std
      value: 23.538999999999998
    - type: nauc_ndcg_at_1_diff1
      value: 90.73750000000001
    - type: nauc_ndcg_at_3_max
      value: 85.0914
    - type: nauc_ndcg_at_3_std
      value: 25.0172
    - type: nauc_ndcg_at_3_diff1
      value: 89.3858
    - type: nauc_ndcg_at_5_max
      value: 84.9112
    - type: nauc_ndcg_at_5_std
      value: 25.732899999999997
    - type: nauc_ndcg_at_5_diff1
      value: 89.1327
    - type: nauc_ndcg_at_10_max
      value: 84.6806
    - type: nauc_ndcg_at_10_std
      value: 26.488
    - type: nauc_ndcg_at_10_diff1
      value: 88.83879999999999
    - type: nauc_ndcg_at_20_max
      value: 84.8315
    - type: nauc_ndcg_at_20_std
      value: 26.9453
    - type: nauc_ndcg_at_20_diff1
      value: 88.9755
    - type: nauc_ndcg_at_100_max
      value: 84.924
    - type: nauc_ndcg_at_100_std
      value: 26.9297
    - type: nauc_ndcg_at_100_diff1
      value: 89.1861
    - type: nauc_ndcg_at_1000_max
      value: 84.9058
    - type: nauc_ndcg_at_1000_std
      value: 26.5904
    - type: nauc_ndcg_at_1000_diff1
      value: 89.2659
    - type: nauc_map_at_1_max
      value: 84.22319999999999
    - type: nauc_map_at_1_std
      value: 23.538999999999998
    - type: nauc_map_at_1_diff1
      value: 90.73750000000001
    - type: nauc_map_at_3_max
      value: 84.9005
    - type: nauc_map_at_3_std
      value: 24.622
    - type: nauc_map_at_3_diff1
      value: 89.74069999999999
    - type: nauc_map_at_5_max
      value: 84.8017
    - type: nauc_map_at_5_std
      value: 24.9739
    - type: nauc_map_at_5_diff1
      value: 89.61970000000001
    - type: nauc_map_at_10_max
      value: 84.7091
    - type: nauc_map_at_10_std
      value: 25.223699999999997
    - type: nauc_map_at_10_diff1
      value: 89.51639999999999
    - type: nauc_map_at_20_max
      value: 84.7458
    - type: nauc_map_at_20_std
      value: 25.3151
    - type: nauc_map_at_20_diff1
      value: 89.5589
    - type: nauc_map_at_100_max
      value: 84.75930000000001
    - type: nauc_map_at_100_std
      value: 25.318099999999998
    - type: nauc_map_at_100_diff1
      value: 89.58850000000001
    - type: nauc_map_at_1000_max
      value: 84.75880000000001
    - type: nauc_map_at_1000_std
      value: 25.3086
    - type: nauc_map_at_1000_diff1
      value: 89.591
    - type: nauc_recall_at_1_max
      value: 84.22319999999999
    - type: nauc_recall_at_1_std
      value: 23.538999999999998
    - type: nauc_recall_at_1_diff1
      value: 90.73750000000001
    - type: nauc_recall_at_3_max
      value: 85.7389
    - type: nauc_recall_at_3_std
      value: 26.4015
    - type: nauc_recall_at_3_diff1
      value: 88.1462
    - type: nauc_recall_at_5_max
      value: 85.2854
    - type: nauc_recall_at_5_std
      value: 28.9065
    - type: nauc_recall_at_5_diff1
      value: 87.15039999999999
    - type: nauc_recall_at_10_max
      value: 84.3391
    - type: nauc_recall_at_10_std
      value: 33.2602
    - type: nauc_recall_at_10_diff1
      value: 85.3733
    - type: nauc_recall_at_20_max
      value: 85.3385
    - type: nauc_recall_at_20_std
      value: 38.4429
    - type: nauc_recall_at_20_diff1
      value: 85.40299999999999
    - type: nauc_recall_at_100_max
      value: 87.3325
    - type: nauc_recall_at_100_std
      value: 48.357
    - type: nauc_recall_at_100_diff1
      value: 85.7283
    - type: nauc_recall_at_1000_max
      value: 90.63419999999999
    - type: nauc_recall_at_1000_std
      value: 63.489399999999996
    - type: nauc_recall_at_1000_diff1
      value: 85.1443
    - type: nauc_precision_at_1_max
      value: 84.22319999999999
    - type: nauc_precision_at_1_std
      value: 23.538999999999998
    - type: nauc_precision_at_1_diff1
      value: 90.73750000000001
    - type: nauc_precision_at_3_max
      value: 85.7389
    - type: nauc_precision_at_3_std
      value: 26.4015
    - type: nauc_precision_at_3_diff1
      value: 88.1462
    - type: nauc_precision_at_5_max
      value: 85.2854
    - type: nauc_precision_at_5_std
      value: 28.9065
    - type: nauc_precision_at_5_diff1
      value: 87.15039999999999
    - type: nauc_precision_at_10_max
      value: 84.3391
    - type: nauc_precision_at_10_std
      value: 33.2602
    - type: nauc_precision_at_10_diff1
      value: 85.3733
    - type: nauc_precision_at_20_max
      value: 85.3385
    - type: nauc_precision_at_20_std
      value: 38.4429
    - type: nauc_precision_at_20_diff1
      value: 85.40299999999999
    - type: nauc_precision_at_100_max
      value: 87.3325
    - type: nauc_precision_at_100_std
      value: 48.357
    - type: nauc_precision_at_100_diff1
      value: 85.7283
    - type: nauc_precision_at_1000_max
      value: 90.63419999999999
    - type: nauc_precision_at_1000_std
      value: 63.489399999999996
    - type: nauc_precision_at_1000_diff1
      value: 85.1443
    - type: nauc_mrr_at_1_max
      value: 84.1909
    - type: nauc_mrr_at_1_std
      value: 23.5506
    - type: nauc_mrr_at_1_diff1
      value: 90.7257
    - type: nauc_mrr_at_3_max
      value: 84.883
    - type: nauc_mrr_at_3_std
      value: 24.630499999999998
    - type: nauc_mrr_at_3_diff1
      value: 89.7361
    - type: nauc_mrr_at_5_max
      value: 84.783
    - type: nauc_mrr_at_5_std
      value: 24.9813
    - type: nauc_mrr_at_5_diff1
      value: 89.6132
    - type: nauc_mrr_at_10_max
      value: 84.6899
    - type: nauc_mrr_at_10_std
      value: 25.230200000000004
    - type: nauc_mrr_at_10_diff1
      value: 89.5099
    - type: nauc_mrr_at_20_max
      value: 84.7264
    - type: nauc_mrr_at_20_std
      value: 25.3216
    - type: nauc_mrr_at_20_diff1
      value: 89.5523
    - type: nauc_mrr_at_100_max
      value: 84.7398
    - type: nauc_mrr_at_100_std
      value: 25.324799999999996
    - type: nauc_mrr_at_100_diff1
      value: 89.5818
    - type: nauc_mrr_at_1000_max
      value: 84.7393
    - type: nauc_mrr_at_1000_std
      value: 25.315199999999997
    - type: nauc_mrr_at_1000_diff1
      value: 89.5843
    - type: main_score
      value: 84.407
    task:
      type: Retrieval
  - dataset:
      config: javascript
      name: MTEB COIRCodeSearchNetRetrieval (javascript)
      revision: 4adc7bc41202b5c13543c9c886a25f340634dab3
      split: test
      type: CoIR-Retrieval/CodeSearchNet
    metrics:
    - type: ndcg_at_1
      value: 22.03
    - type: ndcg_at_3
      value: 27.577
    - type: ndcg_at_5
      value: 29.465000000000003
    - type: ndcg_at_10
      value: 31.297000000000004
    - type: ndcg_at_20
      value: 32.666000000000004
    - type: ndcg_at_100
      value: 34.905
    - type: ndcg_at_1000
      value: 37.126
    - type: map_at_1
      value: 22.03
    - type: map_at_3
      value: 26.208
    - type: map_at_5
      value: 27.255000000000003
    - type: map_at_10
      value: 28.014
    - type: map_at_20
      value: 28.394000000000002
    - type: map_at_100
      value: 28.676000000000002
    - type: map_at_1000
      value: 28.747
    - type: recall_at_1
      value: 22.03
    - type: recall_at_3
      value: 31.541000000000004
    - type: recall_at_5
      value: 36.129
    - type: recall_at_10
      value: 41.781
    - type: recall_at_20
      value: 47.159
    - type: recall_at_100
      value: 59.648
    - type: recall_at_1000
      value: 77.818
    - type: precision_at_1
      value: 22.03
    - type: precision_at_3
      value: 10.514
    - type: precision_at_5
      value: 7.226000000000001
    - type: precision_at_10
      value: 4.178
    - type: precision_at_20
      value: 2.358
    - type: precision_at_100
      value: 0.596
    - type: precision_at_1000
      value: 0.078
    - type: mrr_at_1
      value: 22.029799999999998
    - type: mrr_at_3
      value: 26.2078
    - type: mrr_at_5
      value: 27.2546
    - type: mrr_at_10
      value: 28.0138
    - type: mrr_at_20
      value: 28.393800000000002
    - type: mrr_at_100
      value: 28.6755
    - type: mrr_at_1000
      value: 28.7473
    - type: nauc_ndcg_at_1_max
      value: 43.7913
    - type: nauc_ndcg_at_1_std
      value: 5.8822
    - type: nauc_ndcg_at_1_diff1
      value: 57.5892
    - type: nauc_ndcg_at_3_max
      value: 43.6608
    - type: nauc_ndcg_at_3_std
      value: 7.308199999999999
    - type: nauc_ndcg_at_3_diff1
      value: 50.727199999999996
    - type: nauc_ndcg_at_5_max
      value: 43.540099999999995
    - type: nauc_ndcg_at_5_std
      value: 8.2882
    - type: nauc_ndcg_at_5_diff1
      value: 49.7273
    - type: nauc_ndcg_at_10_max
      value: 43.290800000000004
    - type: nauc_ndcg_at_10_std
      value: 9.177
    - type: nauc_ndcg_at_10_diff1
      value: 48.6902
    - type: nauc_ndcg_at_20_max
      value: 43.1726
    - type: nauc_ndcg_at_20_std
      value: 9.9537
    - type: nauc_ndcg_at_20_diff1
      value: 48.2511
    - type: nauc_ndcg_at_100_max
      value: 43.0801
    - type: nauc_ndcg_at_100_std
      value: 11.2629
    - type: nauc_ndcg_at_100_diff1
      value: 47.7496
    - type: nauc_ndcg_at_1000_max
      value: 43.0087
    - type: nauc_ndcg_at_1000_std
      value: 11.3454
    - type: nauc_ndcg_at_1000_diff1
      value: 47.7628
    - type: nauc_map_at_1_max
      value: 43.7913
    - type: nauc_map_at_1_std
      value: 5.8822
    - type: nauc_map_at_1_diff1
      value: 57.5892
    - type: nauc_map_at_3_max
      value: 43.623200000000004
    - type: nauc_map_at_3_std
      value: 6.9021
    - type: nauc_map_at_3_diff1
      value: 52.296600000000005
    - type: nauc_map_at_5_max
      value: 43.567099999999996
    - type: nauc_map_at_5_std
      value: 7.4779
    - type: nauc_map_at_5_diff1
      value: 51.7259
    - type: nauc_map_at_10_max
      value: 43.4204
    - type: nauc_map_at_10_std
      value: 7.82
    - type: nauc_map_at_10_diff1
      value: 51.266
    - type: nauc_map_at_20_max
      value: 43.3827
    - type: nauc_map_at_20_std
      value: 8.0332
    - type: nauc_map_at_20_diff1
      value: 51.139599999999994
    - type: nauc_map_at_100_max
      value: 43.3681
    - type: nauc_map_at_100_std
      value: 8.205400000000001
    - type: nauc_map_at_100_diff1
      value: 51.054
    - type: nauc_map_at_1000_max
      value: 43.3619
    - type: nauc_map_at_1000_std
      value: 8.2009
    - type: nauc_map_at_1000_diff1
      value: 51.0517
    - type: nauc_recall_at_1_max
      value: 43.7913
    - type: nauc_recall_at_1_std
      value: 5.8822
    - type: nauc_recall_at_1_diff1
      value: 57.5892
    - type: nauc_recall_at_3_max
      value: 43.7869
    - type: nauc_recall_at_3_std
      value: 8.4252
    - type: nauc_recall_at_3_diff1
      value: 46.5268
    - type: nauc_recall_at_5_max
      value: 43.4642
    - type: nauc_recall_at_5_std
      value: 10.5594
    - type: nauc_recall_at_5_diff1
      value: 44.329800000000006
    - type: nauc_recall_at_10_max
      value: 42.9497
    - type: nauc_recall_at_10_std
      value: 13.252
    - type: nauc_recall_at_10_diff1
      value: 41.5027
    - type: nauc_recall_at_20_max
      value: 42.5357
    - type: nauc_recall_at_20_std
      value: 16.2323
    - type: nauc_recall_at_20_diff1
      value: 39.7814
    - type: nauc_recall_at_100_max
      value: 41.963899999999995
    - type: nauc_recall_at_100_std
      value: 24.3312
    - type: nauc_recall_at_100_diff1
      value: 36.321
    - type: nauc_recall_at_1000_max
      value: 40.839999999999996
    - type: nauc_recall_at_1000_std
      value: 32.861000000000004
    - type: nauc_recall_at_1000_diff1
      value: 30.7145
    - type: nauc_precision_at_1_max
      value: 43.7913
    - type: nauc_precision_at_1_std
      value: 5.8822
    - type: nauc_precision_at_1_diff1
      value: 57.5892
    - type: nauc_precision_at_3_max
      value: 43.7869
    - type: nauc_precision_at_3_std
      value: 8.4252
    - type: nauc_precision_at_3_diff1
      value: 46.5268
    - type: nauc_precision_at_5_max
      value: 43.4642
    - type: nauc_precision_at_5_std
      value: 10.5594
    - type: nauc_precision_at_5_diff1
      value: 44.329800000000006
    - type: nauc_precision_at_10_max
      value: 42.9497
    - type: nauc_precision_at_10_std
      value: 13.252
    - type: nauc_precision_at_10_diff1
      value: 41.5027
    - type: nauc_precision_at_20_max
      value: 42.5357
    - type: nauc_precision_at_20_std
      value: 16.2323
    - type: nauc_precision_at_20_diff1
      value: 39.7814
    - type: nauc_precision_at_100_max
      value: 41.963899999999995
    - type: nauc_precision_at_100_std
      value: 24.3312
    - type: nauc_precision_at_100_diff1
      value: 36.321
    - type: nauc_precision_at_1000_max
      value: 40.839999999999996
    - type: nauc_precision_at_1000_std
      value: 32.861000000000004
    - type: nauc_precision_at_1000_diff1
      value: 30.7145
    - type: nauc_mrr_at_1_max
      value: 43.7913
    - type: nauc_mrr_at_1_std
      value: 5.8822
    - type: nauc_mrr_at_1_diff1
      value: 57.5892
    - type: nauc_mrr_at_3_max
      value: 43.623200000000004
    - type: nauc_mrr_at_3_std
      value: 6.9021
    - type: nauc_mrr_at_3_diff1
      value: 52.296600000000005
    - type: nauc_mrr_at_5_max
      value: 43.567099999999996
    - type: nauc_mrr_at_5_std
      value: 7.4779
    - type: nauc_mrr_at_5_diff1
      value: 51.7259
    - type: nauc_mrr_at_10_max
      value: 43.4204
    - type: nauc_mrr_at_10_std
      value: 7.82
    - type: nauc_mrr_at_10_diff1
      value: 51.266
    - type: nauc_mrr_at_20_max
      value: 43.3827
    - type: nauc_mrr_at_20_std
      value: 8.0332
    - type: nauc_mrr_at_20_diff1
      value: 51.139599999999994
    - type: nauc_mrr_at_100_max
      value: 43.3681
    - type: nauc_mrr_at_100_std
      value: 8.2055
    - type: nauc_mrr_at_100_diff1
      value: 51.054100000000005
    - type: nauc_mrr_at_1000_max
      value: 43.3619
    - type: nauc_mrr_at_1000_std
      value: 8.2009
    - type: nauc_mrr_at_1000_diff1
      value: 51.0518
    - type: main_score
      value: 31.297000000000004
    task:
      type: Retrieval
  - dataset:
      config: go
      name: MTEB COIRCodeSearchNetRetrieval (go)
      revision: 4adc7bc41202b5c13543c9c886a25f340634dab3
      split: test
      type: CoIR-Retrieval/CodeSearchNet
    metrics:
    - type: ndcg_at_1
      value: 36.58
    - type: ndcg_at_3
      value: 44.633
    - type: ndcg_at_5
      value: 46.766000000000005
    - type: ndcg_at_10
      value: 48.921
    - type: ndcg_at_20
      value: 50.52100000000001
    - type: ndcg_at_100
      value: 52.795
    - type: ndcg_at_1000
      value: 54.291
    - type: map_at_1
      value: 36.58
    - type: map_at_3
      value: 42.666
    - type: map_at_5
      value: 43.852000000000004
    - type: map_at_10
      value: 44.744
    - type: map_at_20
      value: 45.188
    - type: map_at_100
      value: 45.493
    - type: map_at_1000
      value: 45.544000000000004
    - type: recall_at_1
      value: 36.58
    - type: recall_at_3
      value: 50.32
    - type: recall_at_5
      value: 55.491
    - type: recall_at_10
      value: 62.13999999999999
    - type: recall_at_20
      value: 68.431
    - type: recall_at_100
      value: 80.83
    - type: recall_at_1000
      value: 92.896
    - type: precision_at_1
      value: 36.58
    - type: precision_at_3
      value: 16.773
    - type: precision_at_5
      value: 11.097999999999999
    - type: precision_at_10
      value: 6.214
    - type: precision_at_20
      value: 3.422
    - type: precision_at_100
      value: 0.808
    - type: precision_at_1000
      value: 0.093
    - type: mrr_at_1
      value: 36.579699999999995
    - type: mrr_at_3
      value: 42.666
    - type: mrr_at_5
      value: 43.8517
    - type: mrr_at_10
      value: 44.7436
    - type: mrr_at_20
      value: 45.1875
    - type: mrr_at_100
      value: 45.493
    - type: mrr_at_1000
      value: 45.544200000000004
    - type: nauc_ndcg_at_1_max
      value: 41.7601
    - type: nauc_ndcg_at_1_std
      value: 4.5455000000000005
    - type: nauc_ndcg_at_1_diff1
      value: 58.6454
    - type: nauc_ndcg_at_3_max
      value: 42.3992
    - type: nauc_ndcg_at_3_std
      value: 6.3083
    - type: nauc_ndcg_at_3_diff1
      value: 52.4271
    - type: nauc_ndcg_at_5_max
      value: 42.2462
    - type: nauc_ndcg_at_5_std
      value: 6.8773
    - type: nauc_ndcg_at_5_diff1
      value: 51.75880000000001
    - type: nauc_ndcg_at_10_max
      value: 41.7943
    - type: nauc_ndcg_at_10_std
      value: 7.2982000000000005
    - type: nauc_ndcg_at_10_diff1
      value: 51.0016
    - type: nauc_ndcg_at_20_max
      value: 41.5875
    - type: nauc_ndcg_at_20_std
      value: 7.8825
    - type: nauc_ndcg_at_20_diff1
      value: 50.7648
    - type: nauc_ndcg_at_100_max
      value: 41.6971
    - type: nauc_ndcg_at_100_std
      value: 8.4077
    - type: nauc_ndcg_at_100_diff1
      value: 50.9386
    - type: nauc_ndcg_at_1000_max
      value: 41.7837
    - type: nauc_ndcg_at_1000_std
      value: 8.250300000000001
    - type: nauc_ndcg_at_1000_diff1
      value: 51.4691
    - type: nauc_map_at_1_max
      value: 41.7601
    - type: nauc_map_at_1_std
      value: 4.5455000000000005
    - type: nauc_map_at_1_diff1
      value: 58.6454
    - type: nauc_map_at_3_max
      value: 42.2864
    - type: nauc_map_at_3_std
      value: 5.8461
    - type: nauc_map_at_3_diff1
      value: 53.9381
    - type: nauc_map_at_5_max
      value: 42.1957
    - type: nauc_map_at_5_std
      value: 6.142
    - type: nauc_map_at_5_diff1
      value: 53.600300000000004
    - type: nauc_map_at_10_max
      value: 42.005900000000004
    - type: nauc_map_at_10_std
      value: 6.2986
    - type: nauc_map_at_10_diff1
      value: 53.296200000000006
    - type: nauc_map_at_20_max
      value: 41.946099999999994
    - type: nauc_map_at_20_std
      value: 6.452299999999999
    - type: nauc_map_at_20_diff1
      value: 53.2485
    - type: nauc_map_at_100_max
      value: 41.9563
    - type: nauc_map_at_100_std
      value: 6.511
    - type: nauc_map_at_100_diff1
      value: 53.2816
    - type: nauc_map_at_1000_max
      value: 41.9598
    - type: nauc_map_at_1000_std
      value: 6.5069
    - type: nauc_map_at_1000_diff1
      value: 53.3008
    - type: nauc_recall_at_1_max
      value: 41.7601
    - type: nauc_recall_at_1_std
      value: 4.5455000000000005
    - type: nauc_recall_at_1_diff1
      value: 58.6454
    - type: nauc_recall_at_3_max
      value: 42.7117
    - type: nauc_recall_at_3_std
      value: 7.674799999999999
    - type: nauc_recall_at_3_diff1
      value: 48.0061
    - type: nauc_recall_at_5_max
      value: 42.365399999999994
    - type: nauc_recall_at_5_std
      value: 9.2378
    - type: nauc_recall_at_5_diff1
      value: 46.0218
    - type: nauc_recall_at_10_max
      value: 40.8705
    - type: nauc_recall_at_10_std
      value: 10.9253
    - type: nauc_recall_at_10_diff1
      value: 43.0092
    - type: nauc_recall_at_20_max
      value: 39.818599999999996
    - type: nauc_recall_at_20_std
      value: 14.1425
    - type: nauc_recall_at_20_diff1
      value: 40.8455
    - type: nauc_recall_at_100_max
      value: 40.1229
    - type: nauc_recall_at_100_std
      value: 22.0804
    - type: nauc_recall_at_100_diff1
      value: 37.6538
    - type: nauc_recall_at_1000_max
      value: 40.4194
    - type: nauc_recall_at_1000_std
      value: 36.7051
    - type: nauc_recall_at_1000_diff1
      value: 35.3088
    - type: nauc_precision_at_1_max
      value: 41.7601
    - type: nauc_precision_at_1_std
      value: 4.5455000000000005
    - type: nauc_precision_at_1_diff1
      value: 58.6454
    - type: nauc_precision_at_3_max
      value: 42.7117
    - type: nauc_precision_at_3_std
      value: 7.674799999999999
    - type: nauc_precision_at_3_diff1
      value: 48.0061
    - type: nauc_precision_at_5_max
      value: 42.365399999999994
    - type: nauc_precision_at_5_std
      value: 9.2378
    - type: nauc_precision_at_5_diff1
      value: 46.0218
    - type: nauc_precision_at_10_max
      value: 40.8705
    - type: nauc_precision_at_10_std
      value: 10.9253
    - type: nauc_precision_at_10_diff1
      value: 43.0092
    - type: nauc_precision_at_20_max
      value: 39.818599999999996
    - type: nauc_precision_at_20_std
      value: 14.1425
    - type: nauc_precision_at_20_diff1
      value: 40.8455
    - type: nauc_precision_at_100_max
      value: 40.1229
    - type: nauc_precision_at_100_std
      value: 22.0804
    - type: nauc_precision_at_100_diff1
      value: 37.6538
    - type: nauc_precision_at_1000_max
      value: 40.4194
    - type: nauc_precision_at_1000_std
      value: 36.7051
    - type: nauc_precision_at_1000_diff1
      value: 35.3088
    - type: nauc_mrr_at_1_max
      value: 41.7601
    - type: nauc_mrr_at_1_std
      value: 4.5455000000000005
    - type: nauc_mrr_at_1_diff1
      value: 58.6454
    - type: nauc_mrr_at_3_max
      value: 42.2864
    - type: nauc_mrr_at_3_std
      value: 5.8461
    - type: nauc_mrr_at_3_diff1
      value: 53.9381
    - type: nauc_mrr_at_5_max
      value: 42.1957
    - type: nauc_mrr_at_5_std
      value: 6.142
    - type: nauc_mrr_at_5_diff1
      value: 53.600300000000004
    - type: nauc_mrr_at_10_max
      value: 42.005900000000004
    - type: nauc_mrr_at_10_std
      value: 6.2986
    - type: nauc_mrr_at_10_diff1
      value: 53.296200000000006
    - type: nauc_mrr_at_20_max
      value: 41.946099999999994
    - type: nauc_mrr_at_20_std
      value: 6.452299999999999
    - type: nauc_mrr_at_20_diff1
      value: 53.2485
    - type: nauc_mrr_at_100_max
      value: 41.9563
    - type: nauc_mrr_at_100_std
      value: 6.511
    - type: nauc_mrr_at_100_diff1
      value: 53.2816
    - type: nauc_mrr_at_1000_max
      value: 41.9598
    - type: nauc_mrr_at_1000_std
      value: 6.5069
    - type: nauc_mrr_at_1000_diff1
      value: 53.3008
    - type: main_score
      value: 48.921
    task:
      type: Retrieval
  - dataset:
      config: ruby
      name: MTEB COIRCodeSearchNetRetrieval (ruby)
      revision: 4adc7bc41202b5c13543c9c886a25f340634dab3
      split: test
      type: CoIR-Retrieval/CodeSearchNet
    metrics:
    - type: ndcg_at_1
      value: 27.359
    - type: ndcg_at_3
      value: 33.405
    - type: ndcg_at_5
      value: 35.111
    - type: ndcg_at_10
      value: 37.124
    - type: ndcg_at_20
      value: 38.637
    - type: ndcg_at_100
      value: 40.809
    - type: ndcg_at_1000
      value: 43.206
    - type: map_at_1
      value: 27.359
    - type: map_at_3
      value: 31.906000000000002
    - type: map_at_5
      value: 32.838
    - type: map_at_10
      value: 33.677
    - type: map_at_20
      value: 34.086
    - type: map_at_100
      value: 34.379
    - type: map_at_1000
      value: 34.458
    - type: recall_at_1
      value: 27.359
    - type: recall_at_3
      value: 37.748
    - type: recall_at_5
      value: 41.951
    - type: recall_at_10
      value: 48.136
    - type: recall_at_20
      value: 54.163
    - type: recall_at_100
      value: 65.979
    - type: recall_at_1000
      value: 85.488
    - type: precision_at_1
      value: 27.359
    - type: precision_at_3
      value: 12.583
    - type: precision_at_5
      value: 8.39
    - type: precision_at_10
      value: 4.814
    - type: precision_at_20
      value: 2.708
    - type: precision_at_100
      value: 0.66
    - type: precision_at_1000
      value: 0.08499999999999999
    - type: mrr_at_1
      value: 27.3592
    - type: mrr_at_3
      value: 31.9059
    - type: mrr_at_5
      value: 32.8377
    - type: mrr_at_10
      value: 33.677099999999996
    - type: mrr_at_20
      value: 34.086
    - type: mrr_at_100
      value: 34.3787
    - type: mrr_at_1000
      value: 34.4575
    - type: nauc_ndcg_at_1_max
      value: 41.336
    - type: nauc_ndcg_at_1_std
      value: 4.9167000000000005
    - type: nauc_ndcg_at_1_diff1
      value: 59.489599999999996
    - type: nauc_ndcg_at_3_max
      value: 42.3939
    - type: nauc_ndcg_at_3_std
      value: 9.324200000000001
    - type: nauc_ndcg_at_3_diff1
      value: 53.886
    - type: nauc_ndcg_at_5_max
      value: 41.523700000000005
    - type: nauc_ndcg_at_5_std
      value: 8.7661
    - type: nauc_ndcg_at_5_diff1
      value: 52.6116
    - type: nauc_ndcg_at_10_max
      value: 40.7362
    - type: nauc_ndcg_at_10_std
      value: 9.3454
    - type: nauc_ndcg_at_10_diff1
      value: 51.226000000000006
    - type: nauc_ndcg_at_20_max
      value: 40.1284
    - type: nauc_ndcg_at_20_std
      value: 10.1067
    - type: nauc_ndcg_at_20_diff1
      value: 50.6354
    - type: nauc_ndcg_at_100_max
      value: 40.109899999999996
    - type: nauc_ndcg_at_100_std
      value: 11.125599999999999
    - type: nauc_ndcg_at_100_diff1
      value: 50.021499999999996
    - type: nauc_ndcg_at_1000_max
      value: 39.9325
    - type: nauc_ndcg_at_1000_std
      value: 10.9899
    - type: nauc_ndcg_at_1000_diff1
      value: 50.3713
    - type: nauc_map_at_1_max
      value: 41.336
    - type: nauc_map_at_1_std
      value: 4.9167000000000005
    - type: nauc_map_at_1_diff1
      value: 59.489599999999996
    - type: nauc_map_at_3_max
      value: 42.1793
    - type: nauc_map_at_3_std
      value: 8.149099999999999
    - type: nauc_map_at_3_diff1
      value: 55.1967
    - type: nauc_map_at_5_max
      value: 41.6768
    - type: nauc_map_at_5_std
      value: 7.8223
    - type: nauc_map_at_5_diff1
      value: 54.4705
    - type: nauc_map_at_10_max
      value: 41.3395
    - type: nauc_map_at_10_std
      value: 8.076
    - type: nauc_map_at_10_diff1
      value: 53.87929999999999
    - type: nauc_map_at_20_max
      value: 41.1762
    - type: nauc_map_at_20_std
      value: 8.2845
    - type: nauc_map_at_20_diff1
      value: 53.7144
    - type: nauc_map_at_100_max
      value: 41.1731
    - type: nauc_map_at_100_std
      value: 8.394
    - type: nauc_map_at_100_diff1
      value: 53.64919999999999
    - type: nauc_map_at_1000_max
      value: 41.165600000000005
    - type: nauc_map_at_1000_std
      value: 8.3923
    - type: nauc_map_at_1000_diff1
      value: 53.654199999999996
    - type: nauc_recall_at_1_max
      value: 41.336
    - type: nauc_recall_at_1_std
      value: 4.9167000000000005
    - type: nauc_recall_at_1_diff1
      value: 59.489599999999996
    - type: nauc_recall_at_3_max
      value: 42.9746
    - type: nauc_recall_at_3_std
      value: 12.632399999999999
    - type: nauc_recall_at_3_diff1
      value: 50.259100000000004
    - type: nauc_recall_at_5_max
      value: 40.9855
    - type: nauc_recall_at_5_std
      value: 11.368300000000001
    - type: nauc_recall_at_5_diff1
      value: 47.3165
    - type: nauc_recall_at_10_max
      value: 38.6473
    - type: nauc_recall_at_10_std
      value: 13.1083
    - type: nauc_recall_at_10_diff1
      value: 43.1086
    - type: nauc_recall_at_20_max
      value: 36.0858
    - type: nauc_recall_at_20_std
      value: 16.345100000000002
    - type: nauc_recall_at_20_diff1
      value: 40.3971
    - type: nauc_recall_at_100_max
      value: 35.3344
    - type: nauc_recall_at_100_std
      value: 24.4293
    - type: nauc_recall_at_100_diff1
      value: 34.4263
    - type: nauc_recall_at_1000_max
      value: 27.814
    - type: nauc_recall_at_1000_std
      value: 34.5865
    - type: nauc_recall_at_1000_diff1
      value: 26.621
    - type: nauc_precision_at_1_max
      value: 41.336
    - type: nauc_precision_at_1_std
      value: 4.9167000000000005
    - type: nauc_precision_at_1_diff1
      value: 59.489599999999996
    - type: nauc_precision_at_3_max
      value: 42.9746
    - type: nauc_precision_at_3_std
      value: 12.632399999999999
    - type: nauc_precision_at_3_diff1
      value: 50.259100000000004
    - type: nauc_precision_at_5_max
      value: 40.9855
    - type: nauc_precision_at_5_std
      value: 11.368300000000001
    - type: nauc_precision_at_5_diff1
      value: 47.3165
    - type: nauc_precision_at_10_max
      value: 38.6473
    - type: nauc_precision_at_10_std
      value: 13.1083
    - type: nauc_precision_at_10_diff1
      value: 43.1086
    - type: nauc_precision_at_20_max
      value: 36.0858
    - type: nauc_precision_at_20_std
      value: 16.345100000000002
    - type: nauc_precision_at_20_diff1
      value: 40.3971
    - type: nauc_precision_at_100_max
      value: 35.3344
    - type: nauc_precision_at_100_std
      value: 24.4293
    - type: nauc_precision_at_100_diff1
      value: 34.4263
    - type: nauc_precision_at_1000_max
      value: 27.814
    - type: nauc_precision_at_1000_std
      value: 34.5865
    - type: nauc_precision_at_1000_diff1
      value: 26.621
    - type: nauc_mrr_at_1_max
      value: 41.336
    - type: nauc_mrr_at_1_std
      value: 4.9167000000000005
    - type: nauc_mrr_at_1_diff1
      value: 59.489599999999996
    - type: nauc_mrr_at_3_max
      value: 42.1793
    - type: nauc_mrr_at_3_std
      value: 8.149099999999999
    - type: nauc_mrr_at_3_diff1
      value: 55.1967
    - type: nauc_mrr_at_5_max
      value: 41.6768
    - type: nauc_mrr_at_5_std
      value: 7.8223
    - type: nauc_mrr_at_5_diff1
      value: 54.4705
    - type: nauc_mrr_at_10_max
      value: 41.3395
    - type: nauc_mrr_at_10_std
      value: 8.076
    - type: nauc_mrr_at_10_diff1
      value: 53.87929999999999
    - type: nauc_mrr_at_20_max
      value: 41.1762
    - type: nauc_mrr_at_20_std
      value: 8.2845
    - type: nauc_mrr_at_20_diff1
      value: 53.7144
    - type: nauc_mrr_at_100_max
      value: 41.1731
    - type: nauc_mrr_at_100_std
      value: 8.394
    - type: nauc_mrr_at_100_diff1
      value: 53.64919999999999
    - type: nauc_mrr_at_1000_max
      value: 41.165600000000005
    - type: nauc_mrr_at_1000_std
      value: 8.3923
    - type: nauc_mrr_at_1000_diff1
      value: 53.654199999999996
    - type: main_score
      value: 37.124
    task:
      type: Retrieval
  - dataset:
      config: java
      name: MTEB COIRCodeSearchNetRetrieval (java)
      revision: 4adc7bc41202b5c13543c9c886a25f340634dab3
      split: test
      type: CoIR-Retrieval/CodeSearchNet
    metrics:
    - type: ndcg_at_1
      value: 29.621
    - type: ndcg_at_3
      value: 36.388999999999996
    - type: ndcg_at_5
      value: 38.071
    - type: ndcg_at_10
      value: 39.856
    - type: ndcg_at_20
      value: 41.189
    - type: ndcg_at_100
      value: 43.391999999999996
    - type: ndcg_at_1000
      value: 45.080999999999996
    - type: map_at_1
      value: 29.621
    - type: map_at_3
      value: 34.733000000000004
    - type: map_at_5
      value: 35.668
    - type: map_at_10
      value: 36.411
    - type: map_at_20
      value: 36.778
    - type: map_at_100
      value: 37.077
    - type: map_at_1000
      value: 37.133
    - type: recall_at_1
      value: 29.621
    - type: recall_at_3
      value: 41.178
    - type: recall_at_5
      value: 45.257999999999996
    - type: recall_at_10
      value: 50.744
    - type: recall_at_20
      value: 56.001999999999995
    - type: recall_at_100
      value: 67.96
    - type: recall_at_1000
      value: 81.707
    - type: precision_at_1
      value: 29.621
    - type: precision_at_3
      value: 13.725999999999999
    - type: precision_at_5
      value: 9.052
    - type: precision_at_10
      value: 5.074
    - type: precision_at_20
      value: 2.8000000000000003
    - type: precision_at_100
      value: 0.6799999999999999
    - type: precision_at_1000
      value: 0.082
    - type: mrr_at_1
      value: 29.593799999999998
    - type: mrr_at_3
      value: 34.7254
    - type: mrr_at_5
      value: 35.6583
    - type: mrr_at_10
      value: 36.4022
    - type: mrr_at_20
      value: 36.7689
    - type: mrr_at_100
      value: 37.0681
    - type: mrr_at_1000
      value: 37.124
    - type: nauc_ndcg_at_1_max
      value: 39.7113
    - type: nauc_ndcg_at_1_std
      value: -1.3535
    - type: nauc_ndcg_at_1_diff1
      value: 57.7222
    - type: nauc_ndcg_at_3_max
      value: 40.4493
    - type: nauc_ndcg_at_3_std
      value: 1.4639
    - type: nauc_ndcg_at_3_diff1
      value: 52.145799999999994
    - type: nauc_ndcg_at_5_max
      value: 40.1219
    - type: nauc_ndcg_at_5_std
      value: 2.1448
    - type: nauc_ndcg_at_5_diff1
      value: 51.2694
    - type: nauc_ndcg_at_10_max
      value: 39.4187
    - type: nauc_ndcg_at_10_std
      value: 2.5085
    - type: nauc_ndcg_at_10_diff1
      value: 50.171699999999994
    - type: nauc_ndcg_at_20_max
      value: 39.2822
    - type: nauc_ndcg_at_20_std
      value: 3.1015
    - type: nauc_ndcg_at_20_diff1
      value: 49.8837
    - type: nauc_ndcg_at_100_max
      value: 39.1352
    - type: nauc_ndcg_at_100_std
      value: 3.8505
    - type: nauc_ndcg_at_100_diff1
      value: 49.7104
    - type: nauc_ndcg_at_1000_max
      value: 39.1441
    - type: nauc_ndcg_at_1000_std
      value: 4.1791
    - type: nauc_ndcg_at_1000_diff1
      value: 49.806200000000004
    - type: nauc_map_at_1_max
      value: 39.7113
    - type: nauc_map_at_1_std
      value: -1.3535
    - type: nauc_map_at_1_diff1
      value: 57.7222
    - type: nauc_map_at_3_max
      value: 40.3518
    - type: nauc_map_at_3_std
      value: 0.7879
    - type: nauc_map_at_3_diff1
      value: 53.4756
    - type: nauc_map_at_5_max
      value: 40.1793
    - type: nauc_map_at_5_std
      value: 1.1596
    - type: nauc_map_at_5_diff1
      value: 52.993900000000004
    - type: nauc_map_at_10_max
      value: 39.8893
    - type: nauc_map_at_10_std
      value: 1.3074000000000001
    - type: nauc_map_at_10_diff1
      value: 52.53679999999999
    - type: nauc_map_at_20_max
      value: 39.8583
    - type: nauc_map_at_20_std
      value: 1.4666000000000001
    - type: nauc_map_at_20_diff1
      value: 52.4664
    - type: nauc_map_at_100_max
      value: 39.8303
    - type: nauc_map_at_100_std
      value: 1.5578
    - type: nauc_map_at_100_diff1
      value: 52.44950000000001
    - type: nauc_map_at_1000_max
      value: 39.827400000000004
    - type: nauc_map_at_1000_std
      value: 1.568
    - type: nauc_map_at_1000_diff1
      value: 52.452600000000004
    - type: nauc_recall_at_1_max
      value: 39.7113
    - type: nauc_recall_at_1_std
      value: -1.3535
    - type: nauc_recall_at_1_diff1
      value: 57.7222
    - type: nauc_recall_at_3_max
      value: 40.6926
    - type: nauc_recall_at_3_std
      value: 3.3686000000000003
    - type: nauc_recall_at_3_diff1
      value: 48.4023
    - type: nauc_recall_at_5_max
      value: 39.8681
    - type: nauc_recall_at_5_std
      value: 5.0524
    - type: nauc_recall_at_5_diff1
      value: 46.2361
    - type: nauc_recall_at_10_max
      value: 37.6778
    - type: nauc_recall_at_10_std
      value: 6.2486
    - type: nauc_recall_at_10_diff1
      value: 42.7533
    - type: nauc_recall_at_20_max
      value: 36.9831
    - type: nauc_recall_at_20_std
      value: 8.9021
    - type: nauc_recall_at_20_diff1
      value: 41.1453
    - type: nauc_recall_at_100_max
      value: 35.6903
    - type: nauc_recall_at_100_std
      value: 15.161
    - type: nauc_recall_at_100_diff1
      value: 38.1673
    - type: nauc_recall_at_1000_max
      value: 34.2718
    - type: nauc_recall_at_1000_std
      value: 26.3982
    - type: nauc_recall_at_1000_diff1
      value: 33.3322
    - type: nauc_precision_at_1_max
      value: 39.7113
    - type: nauc_precision_at_1_std
      value: -1.3535
    - type: nauc_precision_at_1_diff1
      value: 57.7222
    - type: nauc_precision_at_3_max
      value: 40.6926
    - type: nauc_precision_at_3_std
      value: 3.3686000000000003
    - type: nauc_precision_at_3_diff1
      value: 48.4023
    - type: nauc_precision_at_5_max
      value: 39.8681
    - type: nauc_precision_at_5_std
      value: 5.0524
    - type: nauc_precision_at_5_diff1
      value: 46.2361
    - type: nauc_precision_at_10_max
      value: 37.6778
    - type: nauc_precision_at_10_std
      value: 6.2486
    - type: nauc_precision_at_10_diff1
      value: 42.7533
    - type: nauc_precision_at_20_max
      value: 36.9831
    - type: nauc_precision_at_20_std
      value: 8.9021
    - type: nauc_precision_at_20_diff1
      value: 41.1453
    - type: nauc_precision_at_100_max
      value: 35.6903
    - type: nauc_precision_at_100_std
      value: 15.161
    - type: nauc_precision_at_100_diff1
      value: 38.1673
    - type: nauc_precision_at_1000_max
      value: 34.2718
    - type: nauc_precision_at_1000_std
      value: 26.3982
    - type: nauc_precision_at_1000_diff1
      value: 33.3322
    - type: nauc_mrr_at_1_max
      value: 39.6284
    - type: nauc_mrr_at_1_std
      value: -1.345
    - type: nauc_mrr_at_1_diff1
      value: 57.828
    - type: nauc_mrr_at_3_max
      value: 40.3036
    - type: nauc_mrr_at_3_std
      value: 0.7952000000000001
    - type: nauc_mrr_at_3_diff1
      value: 53.524499999999996
    - type: nauc_mrr_at_5_max
      value: 40.1366
    - type: nauc_mrr_at_5_std
      value: 1.1708
    - type: nauc_mrr_at_5_diff1
      value: 53.0405
    - type: nauc_mrr_at_10_max
      value: 39.848
    - type: nauc_mrr_at_10_std
      value: 1.3195000000000001
    - type: nauc_mrr_at_10_diff1
      value: 52.5868
    - type: nauc_mrr_at_20_max
      value: 39.815400000000004
    - type: nauc_mrr_at_20_std
      value: 1.4787
    - type: nauc_mrr_at_20_diff1
      value: 52.513299999999994
    - type: nauc_mrr_at_100_max
      value: 39.787299999999995
    - type: nauc_mrr_at_100_std
      value: 1.5699999999999998
    - type: nauc_mrr_at_100_diff1
      value: 52.496500000000005
    - type: nauc_mrr_at_1000_max
      value: 39.7844
    - type: nauc_mrr_at_1000_std
      value: 1.5803
    - type: nauc_mrr_at_1000_diff1
      value: 52.4996
    - type: main_score
      value: 39.856
    task:
      type: Retrieval
  - dataset:
      config: php
      name: MTEB COIRCodeSearchNetRetrieval (php)
      revision: 4adc7bc41202b5c13543c9c886a25f340634dab3
      split: test
      type: CoIR-Retrieval/CodeSearchNet
    metrics:
    - type: ndcg_at_1
      value: 25.211
    - type: ndcg_at_3
      value: 31.994
    - type: ndcg_at_5
      value: 33.986
    - type: ndcg_at_10
      value: 36.086
    - type: ndcg_at_20
      value: 37.638
    - type: ndcg_at_100
      value: 40.268
    - type: ndcg_at_1000
      value: 42.309999999999995
    - type: map_at_1
      value: 25.211
    - type: map_at_3
      value: 30.346
    - type: map_at_5
      value: 31.452
    - type: map_at_10
      value: 32.323
    - type: map_at_20
      value: 32.751000000000005
    - type: map_at_100
      value: 33.097
    - type: map_at_1000
      value: 33.165
    - type: recall_at_1
      value: 25.211
    - type: recall_at_3
      value: 36.756
    - type: recall_at_5
      value: 41.587
    - type: recall_at_10
      value: 48.059000000000005
    - type: recall_at_20
      value: 54.189
    - type: recall_at_100
      value: 68.61
    - type: recall_at_1000
      value: 85.172
    - type: precision_at_1
      value: 25.211
    - type: precision_at_3
      value: 12.252
    - type: precision_at_5
      value: 8.317
    - type: precision_at_10
      value: 4.806
    - type: precision_at_20
      value: 2.709
    - type: precision_at_100
      value: 0.6859999999999999
    - type: precision_at_1000
      value: 0.08499999999999999
    - type: mrr_at_1
      value: 25.1962
    - type: mrr_at_3
      value: 30.335099999999997
    - type: mrr_at_5
      value: 31.4426
    - type: mrr_at_10
      value: 32.3121
    - type: mrr_at_20
      value: 32.741
    - type: mrr_at_100
      value: 33.0877
    - type: mrr_at_1000
      value: 33.1558
    - type: nauc_ndcg_at_1_max
      value: 38.358799999999995
    - type: nauc_ndcg_at_1_std
      value: 4.3283000000000005
    - type: nauc_ndcg_at_1_diff1
      value: 53.33520000000001
    - type: nauc_ndcg_at_3_max
      value: 38.0766
    - type: nauc_ndcg_at_3_std
      value: 6.0852
    - type: nauc_ndcg_at_3_diff1
      value: 45.5009
    - type: nauc_ndcg_at_5_max
      value: 37.788199999999996
    - type: nauc_ndcg_at_5_std
      value: 7.0073
    - type: nauc_ndcg_at_5_diff1
      value: 44.3577
    - type: nauc_ndcg_at_10_max
      value: 37.674
    - type: nauc_ndcg_at_10_std
      value: 7.954700000000001
    - type: nauc_ndcg_at_10_diff1
      value: 43.6869
    - type: nauc_ndcg_at_20_max
      value: 37.4368
    - type: nauc_ndcg_at_20_std
      value: 8.4592
    - type: nauc_ndcg_at_20_diff1
      value: 43.3112
    - type: nauc_ndcg_at_100_max
      value: 37.5955
    - type: nauc_ndcg_at_100_std
      value: 9.5313
    - type: nauc_ndcg_at_100_diff1
      value: 42.9187
    - type: nauc_ndcg_at_1000_max
      value: 37.8056
    - type: nauc_ndcg_at_1000_std
      value: 9.7477
    - type: nauc_ndcg_at_1000_diff1
      value: 43.3862
    - type: nauc_map_at_1_max
      value: 38.358799999999995
    - type: nauc_map_at_1_std
      value: 4.3283000000000005
    - type: nauc_map_at_1_diff1
      value: 53.33520000000001
    - type: nauc_map_at_3_max
      value: 38.1738
    - type: nauc_map_at_3_std
      value: 5.6814
    - type: nauc_map_at_3_diff1
      value: 47.229
    - type: nauc_map_at_5_max
      value: 38.005100000000006
    - type: nauc_map_at_5_std
      value: 6.1966
    - type: nauc_map_at_5_diff1
      value: 46.559200000000004
    - type: nauc_map_at_10_max
      value: 37.9741
    - type: nauc_map_at_10_std
      value: 6.5971
    - type: nauc_map_at_10_diff1
      value: 46.285
    - type: nauc_map_at_20_max
      value: 37.9009
    - type: nauc_map_at_20_std
      value: 6.7273
    - type: nauc_map_at_20_diff1
      value: 46.1825
    - type: nauc_map_at_100_max
      value: 37.9135
    - type: nauc_map_at_100_std
      value: 6.8602
    - type: nauc_map_at_100_diff1
      value: 46.1376
    - type: nauc_map_at_1000_max
      value: 37.918
    - type: nauc_map_at_1000_std
      value: 6.8636
    - type: nauc_map_at_1000_diff1
      value: 46.1515
    - type: nauc_recall_at_1_max
      value: 38.358799999999995
    - type: nauc_recall_at_1_std
      value: 4.3283000000000005
    - type: nauc_recall_at_1_diff1
      value: 53.33520000000001
    - type: nauc_recall_at_3_max
      value: 37.7993
    - type: nauc_recall_at_3_std
      value: 7.1854000000000005
    - type: nauc_recall_at_3_diff1
      value: 40.8217
    - type: nauc_recall_at_5_max
      value: 37.1564
    - type: nauc_recall_at_5_std
      value: 9.3324
    - type: nauc_recall_at_5_diff1
      value: 38.2991
    - type: nauc_recall_at_10_max
      value: 36.721399999999996
    - type: nauc_recall_at_10_std
      value: 12.1836
    - type: nauc_recall_at_10_diff1
      value: 36.1617
    - type: nauc_recall_at_20_max
      value: 35.7969
    - type: nauc_recall_at_20_std
      value: 14.4368
    - type: nauc_recall_at_20_diff1
      value: 34.3383
    - type: nauc_recall_at_100_max
      value: 36.6044
    - type: nauc_recall_at_100_std
      value: 23.055500000000002
    - type: nauc_recall_at_100_diff1
      value: 29.555500000000002
    - type: nauc_recall_at_1000_max
      value: 39.7315
    - type: nauc_recall_at_1000_std
      value: 38.601600000000005
    - type: nauc_recall_at_1000_diff1
      value: 26.7047
    - type: nauc_precision_at_1_max
      value: 38.358799999999995
    - type: nauc_precision_at_1_std
      value: 4.3283000000000005
    - type: nauc_precision_at_1_diff1
      value: 53.33520000000001
    - type: nauc_precision_at_3_max
      value: 37.7993
    - type: nauc_precision_at_3_std
      value: 7.1854000000000005
    - type: nauc_precision_at_3_diff1
      value: 40.8217
    - type: nauc_precision_at_5_max
      value: 37.1564
    - type: nauc_precision_at_5_std
      value: 9.3324
    - type: nauc_precision_at_5_diff1
      value: 38.2991
    - type: nauc_precision_at_10_max
      value: 36.721399999999996
    - type: nauc_precision_at_10_std
      value: 12.1836
    - type: nauc_precision_at_10_diff1
      value: 36.1617
    - type: nauc_precision_at_20_max
      value: 35.7969
    - type: nauc_precision_at_20_std
      value: 14.4368
    - type: nauc_precision_at_20_diff1
      value: 34.3383
    - type: nauc_precision_at_100_max
      value: 36.6044
    - type: nauc_precision_at_100_std
      value: 23.055500000000002
    - type: nauc_precision_at_100_diff1
      value: 29.555500000000002
    - type: nauc_precision_at_1000_max
      value: 39.7315
    - type: nauc_precision_at_1000_std
      value: 38.601600000000005
    - type: nauc_precision_at_1000_diff1
      value: 26.7047
    - type: nauc_mrr_at_1_max
      value: 38.3753
    - type: nauc_mrr_at_1_std
      value: 4.3651
    - type: nauc_mrr_at_1_diff1
      value: 53.3935
    - type: nauc_mrr_at_3_max
      value: 38.183299999999996
    - type: nauc_mrr_at_3_std
      value: 5.7071
    - type: nauc_mrr_at_3_diff1
      value: 47.2578
    - type: nauc_mrr_at_5_max
      value: 38.0161
    - type: nauc_mrr_at_5_std
      value: 6.2222
    - type: nauc_mrr_at_5_diff1
      value: 46.5907
    - type: nauc_mrr_at_10_max
      value: 37.9882
    - type: nauc_mrr_at_10_std
      value: 6.6221000000000005
    - type: nauc_mrr_at_10_diff1
      value: 46.3178
    - type: nauc_mrr_at_20_max
      value: 37.912
    - type: nauc_mrr_at_20_std
      value: 6.752700000000001
    - type: nauc_mrr_at_20_diff1
      value: 46.2141
    - type: nauc_mrr_at_100_max
      value: 37.9247
    - type: nauc_mrr_at_100_std
      value: 6.8857
    - type: nauc_mrr_at_100_diff1
      value: 46.169399999999996
    - type: nauc_mrr_at_1000_max
      value: 37.9292
    - type: nauc_mrr_at_1000_std
      value: 6.889099999999999
    - type: nauc_mrr_at_1000_diff1
      value: 46.1833
    - type: main_score
      value: 36.086
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB CQADupstackAndroidRetrieval (default)
      revision: f46a197baaae43b4f621051089b82a364682dfeb
      split: test
      type: mteb/cqadupstack-android
    metrics:
    - type: ndcg_at_1
      value: 41.059
    - type: ndcg_at_3
      value: 45.091
    - type: ndcg_at_5
      value: 47.754000000000005
    - type: ndcg_at_10
      value: 50.403
    - type: ndcg_at_20
      value: 52.629999999999995
    - type: ndcg_at_100
      value: 55.669999999999995
    - type: ndcg_at_1000
      value: 57.645
    - type: map_at_1
      value: 33.304
    - type: map_at_3
      value: 40.428999999999995
    - type: map_at_5
      value: 42.638999999999996
    - type: map_at_10
      value: 44.239
    - type: map_at_20
      value: 45.144
    - type: map_at_100
      value: 45.783
    - type: map_at_1000
      value: 45.911
    - type: recall_at_1
      value: 33.304
    - type: recall_at_3
      value: 46.509
    - type: recall_at_5
      value: 53.849999999999994
    - type: recall_at_10
      value: 61.694
    - type: recall_at_20
      value: 69.708
    - type: recall_at_100
      value: 83.314
    - type: recall_at_1000
      value: 95.955
    - type: precision_at_1
      value: 41.059
    - type: precision_at_3
      value: 21.316
    - type: precision_at_5
      value: 15.651000000000002
    - type: precision_at_10
      value: 9.642000000000001
    - type: precision_at_20
      value: 5.744
    - type: precision_at_100
      value: 1.538
    - type: precision_at_1000
      value: 0.20500000000000002
    - type: mrr_at_1
      value: 41.058699999999995
    - type: mrr_at_3
      value: 47.258
    - type: mrr_at_5
      value: 49.082
    - type: mrr_at_10
      value: 50.0836
    - type: mrr_at_20
      value: 50.5221
    - type: mrr_at_100
      value: 50.8217
    - type: mrr_at_1000
      value: 50.8713
    - type: nauc_ndcg_at_1_max
      value: 40.6525
    - type: nauc_ndcg_at_1_std
      value: -9.376
    - type: nauc_ndcg_at_1_diff1
      value: 50.0125
    - type: nauc_ndcg_at_3_max
      value: 40.9809
    - type: nauc_ndcg_at_3_std
      value: -7.1297
    - type: nauc_ndcg_at_3_diff1
      value: 47.0051
    - type: nauc_ndcg_at_5_max
      value: 40.037800000000004
    - type: nauc_ndcg_at_5_std
      value: -4.3972999999999995
    - type: nauc_ndcg_at_5_diff1
      value: 45.8909
    - type: nauc_ndcg_at_10_max
      value: 39.939400000000006
    - type: nauc_ndcg_at_10_std
      value: -4.5747
    - type: nauc_ndcg_at_10_diff1
      value: 45.0088
    - type: nauc_ndcg_at_20_max
      value: 40.144999999999996
    - type: nauc_ndcg_at_20_std
      value: -4.2649
    - type: nauc_ndcg_at_20_diff1
      value: 45.6565
    - type: nauc_ndcg_at_100_max
      value: 41.2015
    - type: nauc_ndcg_at_100_std
      value: -3.0772
    - type: nauc_ndcg_at_100_diff1
      value: 45.8564
    - type: nauc_ndcg_at_1000_max
      value: 41.2273
    - type: nauc_ndcg_at_1000_std
      value: -3.8580000000000005
    - type: nauc_ndcg_at_1000_diff1
      value: 46.0075
    - type: nauc_map_at_1_max
      value: 33.681400000000004
    - type: nauc_map_at_1_std
      value: -10.792499999999999
    - type: nauc_map_at_1_diff1
      value: 51.6292
    - type: nauc_map_at_3_max
      value: 38.5132
    - type: nauc_map_at_3_std
      value: -9.085899999999999
    - type: nauc_map_at_3_diff1
      value: 48.516
    - type: nauc_map_at_5_max
      value: 38.7849
    - type: nauc_map_at_5_std
      value: -7.2336
    - type: nauc_map_at_5_diff1
      value: 47.9868
    - type: nauc_map_at_10_max
      value: 39.3231
    - type: nauc_map_at_10_std
      value: -7.1676
    - type: nauc_map_at_10_diff1
      value: 47.446
    - type: nauc_map_at_20_max
      value: 39.589
    - type: nauc_map_at_20_std
      value: -6.8943
    - type: nauc_map_at_20_diff1
      value: 47.4397
    - type: nauc_map_at_100_max
      value: 39.875
    - type: nauc_map_at_100_std
      value: -6.549199999999999
    - type: nauc_map_at_100_diff1
      value: 47.4459
    - type: nauc_map_at_1000_max
      value: 39.8847
    - type: nauc_map_at_1000_std
      value: -6.5965
    - type: nauc_map_at_1000_diff1
      value: 47.4298
    - type: nauc_recall_at_1_max
      value: 33.681400000000004
    - type: nauc_recall_at_1_std
      value: -10.792499999999999
    - type: nauc_recall_at_1_diff1
      value: 51.6292
    - type: nauc_recall_at_3_max
      value: 37.3654
    - type: nauc_recall_at_3_std
      value: -6.1476999999999995
    - type: nauc_recall_at_3_diff1
      value: 43.147400000000005
    - type: nauc_recall_at_5_max
      value: 35.3328
    - type: nauc_recall_at_5_std
      value: 1.0517
    - type: nauc_recall_at_5_diff1
      value: 39.7709
    - type: nauc_recall_at_10_max
      value: 34.6109
    - type: nauc_recall_at_10_std
      value: 1.5653000000000001
    - type: nauc_recall_at_10_diff1
      value: 35.5858
    - type: nauc_recall_at_20_max
      value: 34.2941
    - type: nauc_recall_at_20_std
      value: 3.9570000000000003
    - type: nauc_recall_at_20_diff1
      value: 36.910199999999996
    - type: nauc_recall_at_100_max
      value: 41.6344
    - type: nauc_recall_at_100_std
      value: 18.614
    - type: nauc_recall_at_100_diff1
      value: 35.9742
    - type: nauc_recall_at_1000_max
      value: 53.67960000000001
    - type: nauc_recall_at_1000_std
      value: 46.8911
    - type: nauc_recall_at_1000_diff1
      value: 35.167500000000004
    - type: nauc_precision_at_1_max
      value: 40.6525
    - type: nauc_precision_at_1_std
      value: -9.376
    - type: nauc_precision_at_1_diff1
      value: 50.0125
    - type: nauc_precision_at_3_max
      value: 40.7269
    - type: nauc_precision_at_3_std
      value: -1.2473
    - type: nauc_precision_at_3_diff1
      value: 31.521500000000003
    - type: nauc_precision_at_5_max
      value: 34.9193
    - type: nauc_precision_at_5_std
      value: 6.758699999999999
    - type: nauc_precision_at_5_diff1
      value: 20.958399999999997
    - type: nauc_precision_at_10_max
      value: 29.1675
    - type: nauc_precision_at_10_std
      value: 8.4146
    - type: nauc_precision_at_10_diff1
      value: 9.517000000000001
    - type: nauc_precision_at_20_max
      value: 23.0603
    - type: nauc_precision_at_20_std
      value: 9.5615
    - type: nauc_precision_at_20_diff1
      value: 3.3520000000000003
    - type: nauc_precision_at_100_max
      value: 10.3906
    - type: nauc_precision_at_100_std
      value: 8.8378
    - type: nauc_precision_at_100_diff1
      value: -8.2594
    - type: nauc_precision_at_1000_max
      value: -4.7287
    - type: nauc_precision_at_1000_std
      value: -2.5721000000000003
    - type: nauc_precision_at_1000_diff1
      value: -19.5341
    - type: nauc_mrr_at_1_max
      value: 40.6525
    - type: nauc_mrr_at_1_std
      value: -9.376
    - type: nauc_mrr_at_1_diff1
      value: 50.0125
    - type: nauc_mrr_at_3_max
      value: 42.4409
    - type: nauc_mrr_at_3_std
      value: -7.4642
    - type: nauc_mrr_at_3_diff1
      value: 47.773199999999996
    - type: nauc_mrr_at_5_max
      value: 41.8687
    - type: nauc_mrr_at_5_std
      value: -6.0165999999999995
    - type: nauc_mrr_at_5_diff1
      value: 46.929500000000004
    - type: nauc_mrr_at_10_max
      value: 41.6607
    - type: nauc_mrr_at_10_std
      value: -5.8776
    - type: nauc_mrr_at_10_diff1
      value: 46.5117
    - type: nauc_mrr_at_20_max
      value: 41.6088
    - type: nauc_mrr_at_20_std
      value: -6.0403
    - type: nauc_mrr_at_20_diff1
      value: 46.7355
    - type: nauc_mrr_at_100_max
      value: 41.6881
    - type: nauc_mrr_at_100_std
      value: -6.0445
    - type: nauc_mrr_at_100_diff1
      value: 46.7504
    - type: nauc_mrr_at_1000_max
      value: 41.6981
    - type: nauc_mrr_at_1000_std
      value: -6.0584
    - type: nauc_mrr_at_1000_diff1
      value: 46.7686
    - type: main_score
      value: 50.403
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB CQADupstackEnglishRetrieval (default)
      revision: ad9991cb51e31e31e430383c75ffb2885547b5f0
      split: test
      type: mteb/cqadupstack-english
    metrics:
    - type: ndcg_at_1
      value: 32.293
    - type: ndcg_at_3
      value: 35.357
    - type: ndcg_at_5
      value: 37.135
    - type: ndcg_at_10
      value: 39.682
    - type: ndcg_at_20
      value: 41.477000000000004
    - type: ndcg_at_100
      value: 44.594
    - type: ndcg_at_1000
      value: 46.938
    - type: map_at_1
      value: 25.084
    - type: map_at_3
      value: 31.134
    - type: map_at_5
      value: 32.693
    - type: map_at_10
      value: 34.072
    - type: map_at_20
      value: 34.719
    - type: map_at_100
      value: 35.327999999999996
    - type: map_at_1000
      value: 35.461
    - type: recall_at_1
      value: 25.084
    - type: recall_at_3
      value: 36.678
    - type: recall_at_5
      value: 41.839999999999996
    - type: recall_at_10
      value: 49.782
    - type: recall_at_20
      value: 56.442
    - type: recall_at_100
      value: 71.114
    - type: recall_at_1000
      value: 86.372
    - type: precision_at_1
      value: 32.293
    - type: precision_at_3
      value: 17.452
    - type: precision_at_5
      value: 12.446
    - type: precision_at_10
      value: 7.758
    - type: precision_at_20
      value: 4.634
    - type: precision_at_100
      value: 1.324
    - type: precision_at_1000
      value: 0.184
    - type: mrr_at_1
      value: 32.293
    - type: mrr_at_3
      value: 37.8344
    - type: mrr_at_5
      value: 39.0223
    - type: mrr_at_10
      value: 40.1805
    - type: mrr_at_20
      value: 40.6083
    - type: mrr_at_100
      value: 40.928799999999995
    - type: mrr_at_1000
      value: 40.9754
    - type: nauc_ndcg_at_1_max
      value: 45.3161
    - type: nauc_ndcg_at_1_std
      value: 4.444
    - type: nauc_ndcg_at_1_diff1
      value: 46.0858
    - type: nauc_ndcg_at_3_max
      value: 46.1152
    - type: nauc_ndcg_at_3_std
      value: 3.2603
    - type: nauc_ndcg_at_3_diff1
      value: 42.6324
    - type: nauc_ndcg_at_5_max
      value: 46.3649
    - type: nauc_ndcg_at_5_std
      value: 2.5442
    - type: nauc_ndcg_at_5_diff1
      value: 42.9534
    - type: nauc_ndcg_at_10_max
      value: 45.9638
    - type: nauc_ndcg_at_10_std
      value: 3.849
    - type: nauc_ndcg_at_10_diff1
      value: 42.3058
    - type: nauc_ndcg_at_20_max
      value: 45.6402
    - type: nauc_ndcg_at_20_std
      value: 4.6758
    - type: nauc_ndcg_at_20_diff1
      value: 41.8551
    - type: nauc_ndcg_at_100_max
      value: 45.7963
    - type: nauc_ndcg_at_100_std
      value: 6.154599999999999
    - type: nauc_ndcg_at_100_diff1
      value: 41.1414
    - type: nauc_ndcg_at_1000_max
      value: 45.9794
    - type: nauc_ndcg_at_1000_std
      value: 6.9567000000000005
    - type: nauc_ndcg_at_1000_diff1
      value: 40.8964
    - type: nauc_map_at_1_max
      value: 40.1856
    - type: nauc_map_at_1_std
      value: -4.0307
    - type: nauc_map_at_1_diff1
      value: 49.675999999999995
    - type: nauc_map_at_3_max
      value: 43.8311
    - type: nauc_map_at_3_std
      value: -1.2912
    - type: nauc_map_at_3_diff1
      value: 45.9441
    - type: nauc_map_at_5_max
      value: 44.818400000000004
    - type: nauc_map_at_5_std
      value: -0.7452000000000001
    - type: nauc_map_at_5_diff1
      value: 45.6591
    - type: nauc_map_at_10_max
      value: 44.9988
    - type: nauc_map_at_10_std
      value: 0.41960000000000003
    - type: nauc_map_at_10_diff1
      value: 45.1582
    - type: nauc_map_at_20_max
      value: 45.0395
    - type: nauc_map_at_20_std
      value: 0.9468000000000001
    - type: nauc_map_at_20_diff1
      value: 44.890600000000006
    - type: nauc_map_at_100_max
      value: 45.311
    - type: nauc_map_at_100_std
      value: 1.5421
    - type: nauc_map_at_100_diff1
      value: 44.7203
    - type: nauc_map_at_1000_max
      value: 45.364399999999996
    - type: nauc_map_at_1000_std
      value: 1.6643000000000001
    - type: nauc_map_at_1000_diff1
      value: 44.6926
    - type: nauc_recall_at_1_max
      value: 40.1856
    - type: nauc_recall_at_1_std
      value: -4.0307
    - type: nauc_recall_at_1_diff1
      value: 49.675999999999995
    - type: nauc_recall_at_3_max
      value: 43.0698
    - type: nauc_recall_at_3_std
      value: 0.4071
    - type: nauc_recall_at_3_diff1
      value: 39.6364
    - type: nauc_recall_at_5_max
      value: 44.056200000000004
    - type: nauc_recall_at_5_std
      value: 0.6597000000000001
    - type: nauc_recall_at_5_diff1
      value: 38.5431
    - type: nauc_recall_at_10_max
      value: 42.5643
    - type: nauc_recall_at_10_std
      value: 5.446899999999999
    - type: nauc_recall_at_10_diff1
      value: 35.3363
    - type: nauc_recall_at_20_max
      value: 40.9176
    - type: nauc_recall_at_20_std
      value: 8.6434
    - type: nauc_recall_at_20_diff1
      value: 33.0525
    - type: nauc_recall_at_100_max
      value: 41.2899
    - type: nauc_recall_at_100_std
      value: 17.3979
    - type: nauc_recall_at_100_diff1
      value: 28.0707
    - type: nauc_recall_at_1000_max
      value: 43.2786
    - type: nauc_recall_at_1000_std
      value: 33.6676
    - type: nauc_recall_at_1000_diff1
      value: 19.6489
    - type: nauc_precision_at_1_max
      value: 45.3161
    - type: nauc_precision_at_1_std
      value: 4.444
    - type: nauc_precision_at_1_diff1
      value: 46.0858
    - type: nauc_precision_at_3_max
      value: 45.937400000000004
    - type: nauc_precision_at_3_std
      value: 13.606599999999998
    - type: nauc_precision_at_3_diff1
      value: 28.8887
    - type: nauc_precision_at_5_max
      value: 43.6409
    - type: nauc_precision_at_5_std
      value: 15.3222
    - type: nauc_precision_at_5_diff1
      value: 23.5428
    - type: nauc_precision_at_10_max
      value: 38.8973
    - type: nauc_precision_at_10_std
      value: 21.049300000000002
    - type: nauc_precision_at_10_diff1
      value: 15.912200000000002
    - type: nauc_precision_at_20_max
      value: 33.1485
    - type: nauc_precision_at_20_std
      value: 26.1451
    - type: nauc_precision_at_20_diff1
      value: 7.7276
    - type: nauc_precision_at_100_max
      value: 24.1577
    - type: nauc_precision_at_100_std
      value: 31.4656
    - type: nauc_precision_at_100_diff1
      value: -4.0066999999999995
    - type: nauc_precision_at_1000_max
      value: 12.3639
    - type: nauc_precision_at_1000_std
      value: 28.9285
    - type: nauc_precision_at_1000_diff1
      value: -11.7577
    - type: nauc_mrr_at_1_max
      value: 45.3161
    - type: nauc_mrr_at_1_std
      value: 4.444
    - type: nauc_mrr_at_1_diff1
      value: 46.0858
    - type: nauc_mrr_at_3_max
      value: 45.9129
    - type: nauc_mrr_at_3_std
      value: 5.743
    - type: nauc_mrr_at_3_diff1
      value: 41.6507
    - type: nauc_mrr_at_5_max
      value: 45.8273
    - type: nauc_mrr_at_5_std
      value: 5.57
    - type: nauc_mrr_at_5_diff1
      value: 41.531400000000005
    - type: nauc_mrr_at_10_max
      value: 45.8144
    - type: nauc_mrr_at_10_std
      value: 6.263000000000001
    - type: nauc_mrr_at_10_diff1
      value: 41.2348
    - type: nauc_mrr_at_20_max
      value: 45.7975
    - type: nauc_mrr_at_20_std
      value: 6.392200000000001
    - type: nauc_mrr_at_20_diff1
      value: 41.259499999999996
    - type: nauc_mrr_at_100_max
      value: 45.7286
    - type: nauc_mrr_at_100_std
      value: 6.456099999999999
    - type: nauc_mrr_at_100_diff1
      value: 41.185100000000006
    - type: nauc_mrr_at_1000_max
      value: 45.7325
    - type: nauc_mrr_at_1000_std
      value: 6.4614
    - type: nauc_mrr_at_1000_diff1
      value: 41.188
    - type: main_score
      value: 39.682
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB CQADupstackGamingRetrieval (default)
      revision: 4885aa143210c98657558c04aaf3dc47cfb54340
      split: test
      type: mteb/cqadupstack-gaming
    metrics:
    - type: ndcg_at_1
      value: 41.379
    - type: ndcg_at_3
      value: 48.789
    - type: ndcg_at_5
      value: 51.535
    - type: ndcg_at_10
      value: 53.654999999999994
    - type: ndcg_at_20
      value: 55.559999999999995
    - type: ndcg_at_100
      value: 57.911
    - type: ndcg_at_1000
      value: 59.275
    - type: map_at_1
      value: 36.224000000000004
    - type: map_at_3
      value: 45.190999999999995
    - type: map_at_5
      value: 47.012
    - type: map_at_10
      value: 48.141
    - type: map_at_20
      value: 48.802
    - type: map_at_100
      value: 49.214
    - type: map_at_1000
      value: 49.278
    - type: recall_at_1
      value: 36.224000000000004
    - type: recall_at_3
      value: 53.513
    - type: recall_at_5
      value: 60.221000000000004
    - type: recall_at_10
      value: 66.346
    - type: recall_at_20
      value: 73.359
    - type: recall_at_100
      value: 84.77
    - type: recall_at_1000
      value: 94.547
    - type: precision_at_1
      value: 41.379
    - type: precision_at_3
      value: 21.902
    - type: precision_at_5
      value: 15.197
    - type: precision_at_10
      value: 8.639
    - type: precision_at_20
      value: 4.887
    - type: precision_at_100
      value: 1.164
    - type: precision_at_1000
      value: 0.133
    - type: mrr_at_1
      value: 41.3793
    - type: mrr_at_3
      value: 49.0282
    - type: mrr_at_5
      value: 50.7022
    - type: mrr_at_10
      value: 51.462399999999995
    - type: mrr_at_20
      value: 51.9372
    - type: mrr_at_100
      value: 52.1984
    - type: mrr_at_1000
      value: 52.2374
    - type: nauc_ndcg_at_1_max
      value: 45.521499999999996
    - type: nauc_ndcg_at_1_std
      value: -3.2632000000000003
    - type: nauc_ndcg_at_1_diff1
      value: 55.017799999999994
    - type: nauc_ndcg_at_3_max
      value: 43.343399999999995
    - type: nauc_ndcg_at_3_std
      value: -4.4684
    - type: nauc_ndcg_at_3_diff1
      value: 49.7562
    - type: nauc_ndcg_at_5_max
      value: 44.034600000000005
    - type: nauc_ndcg_at_5_std
      value: -2.8813
    - type: nauc_ndcg_at_5_diff1
      value: 48.7767
    - type: nauc_ndcg_at_10_max
      value: 45.0674
    - type: nauc_ndcg_at_10_std
      value: -1.332
    - type: nauc_ndcg_at_10_diff1
      value: 48.448600000000006
    - type: nauc_ndcg_at_20_max
      value: 45.6717
    - type: nauc_ndcg_at_20_std
      value: 0.0107
    - type: nauc_ndcg_at_20_diff1
      value: 48.6492
    - type: nauc_ndcg_at_100_max
      value: 45.974
    - type: nauc_ndcg_at_100_std
      value: 1.1665999999999999
    - type: nauc_ndcg_at_100_diff1
      value: 48.9852
    - type: nauc_ndcg_at_1000_max
      value: 46.0653
    - type: nauc_ndcg_at_1000_std
      value: 0.7539
    - type: nauc_ndcg_at_1000_diff1
      value: 49.453399999999995
    - type: nauc_map_at_1_max
      value: 39.5162
    - type: nauc_map_at_1_std
      value: -4.4784
    - type: nauc_map_at_1_diff1
      value: 54.076
    - type: nauc_map_at_3_max
      value: 42.022999999999996
    - type: nauc_map_at_3_std
      value: -5.5131
    - type: nauc_map_at_3_diff1
      value: 50.727199999999996
    - type: nauc_map_at_5_max
      value: 42.700700000000005
    - type: nauc_map_at_5_std
      value: -4.3487
    - type: nauc_map_at_5_diff1
      value: 50.058499999999995
    - type: nauc_map_at_10_max
      value: 43.4533
    - type: nauc_map_at_10_std
      value: -3.3632000000000004
    - type: nauc_map_at_10_diff1
      value: 49.8247
    - type: nauc_map_at_20_max
      value: 43.7821
    - type: nauc_map_at_20_std
      value: -2.8057
    - type: nauc_map_at_20_diff1
      value: 49.8795
    - type: nauc_map_at_100_max
      value: 43.9125
    - type: nauc_map_at_100_std
      value: -2.5162
    - type: nauc_map_at_100_diff1
      value: 49.9437
    - type: nauc_map_at_1000_max
      value: 43.9371
    - type: nauc_map_at_1000_std
      value: -2.5118
    - type: nauc_map_at_1000_diff1
      value: 49.973600000000005
    - type: nauc_recall_at_1_max
      value: 39.5162
    - type: nauc_recall_at_1_std
      value: -4.4784
    - type: nauc_recall_at_1_diff1
      value: 54.076
    - type: nauc_recall_at_3_max
      value: 40.1719
    - type: nauc_recall_at_3_std
      value: -5.8908000000000005
    - type: nauc_recall_at_3_diff1
      value: 46.1075
    - type: nauc_recall_at_5_max
      value: 41.3221
    - type: nauc_recall_at_5_std
      value: -1.7418
    - type: nauc_recall_at_5_diff1
      value: 42.4571
    - type: nauc_recall_at_10_max
      value: 44.1382
    - type: nauc_recall_at_10_std
      value: 3.0869
    - type: nauc_recall_at_10_diff1
      value: 40.6674
    - type: nauc_recall_at_20_max
      value: 47.0264
    - type: nauc_recall_at_20_std
      value: 10.7409
    - type: nauc_recall_at_20_diff1
      value: 39.8838
    - type: nauc_recall_at_100_max
      value: 49.660700000000006
    - type: nauc_recall_at_100_std
      value: 26.1413
    - type: nauc_recall_at_100_diff1
      value: 38.1192
    - type: nauc_recall_at_1000_max
      value: 58.9341
    - type: nauc_recall_at_1000_std
      value: 47.4146
    - type: nauc_recall_at_1000_diff1
      value: 39.7378
    - type: nauc_precision_at_1_max
      value: 45.521499999999996
    - type: nauc_precision_at_1_std
      value: -3.2632000000000003
    - type: nauc_precision_at_1_diff1
      value: 55.017799999999994
    - type: nauc_precision_at_3_max
      value: 41.9576
    - type: nauc_precision_at_3_std
      value: 0.3431
    - type: nauc_precision_at_3_diff1
      value: 33.5013
    - type: nauc_precision_at_5_max
      value: 41.024
    - type: nauc_precision_at_5_std
      value: 6.962400000000001
    - type: nauc_precision_at_5_diff1
      value: 26.0905
    - type: nauc_precision_at_10_max
      value: 38.4505
    - type: nauc_precision_at_10_std
      value: 13.459
    - type: nauc_precision_at_10_diff1
      value: 18.2984
    - type: nauc_precision_at_20_max
      value: 35.6898
    - type: nauc_precision_at_20_std
      value: 19.7287
    - type: nauc_precision_at_20_diff1
      value: 12.3455
    - type: nauc_precision_at_100_max
      value: 29.284
    - type: nauc_precision_at_100_std
      value: 26.509100000000004
    - type: nauc_precision_at_100_diff1
      value: 4.118200000000001
    - type: nauc_precision_at_1000_max
      value: 22.5188
    - type: nauc_precision_at_1000_std
      value: 26.6978
    - type: nauc_precision_at_1000_diff1
      value: -2.4383
    - type: nauc_mrr_at_1_max
      value: 45.521499999999996
    - type: nauc_mrr_at_1_std
      value: -3.2632000000000003
    - type: nauc_mrr_at_1_diff1
      value: 55.017799999999994
    - type: nauc_mrr_at_3_max
      value: 45.2583
    - type: nauc_mrr_at_3_std
      value: -4.0796
    - type: nauc_mrr_at_3_diff1
      value: 51.3842
    - type: nauc_mrr_at_5_max
      value: 45.683099999999996
    - type: nauc_mrr_at_5_std
      value: -3.0403
    - type: nauc_mrr_at_5_diff1
      value: 50.928
    - type: nauc_mrr_at_10_max
      value: 46.0254
    - type: nauc_mrr_at_10_std
      value: -2.5618
    - type: nauc_mrr_at_10_diff1
      value: 50.9016
    - type: nauc_mrr_at_20_max
      value: 46.1397
    - type: nauc_mrr_at_20_std
      value: -2.2378
    - type: nauc_mrr_at_20_diff1
      value: 50.983900000000006
    - type: nauc_mrr_at_100_max
      value: 46.0813
    - type: nauc_mrr_at_100_std
      value: -2.1819
    - type: nauc_mrr_at_100_diff1
      value: 50.9924
    - type: nauc_mrr_at_1000_max
      value: 46.075700000000005
    - type: nauc_mrr_at_1000_std
      value: -2.2086
    - type: nauc_mrr_at_1000_diff1
      value: 51.004400000000004
    - type: main_score
      value: 53.654999999999994
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB CQADupstackGisRetrieval (default)
      revision: 5003b3064772da1887988e05400cf3806fe491f2
      split: test
      type: mteb/cqadupstack-gis
    metrics:
    - type: ndcg_at_1
      value: 28.701
    - type: ndcg_at_3
      value: 35.095
    - type: ndcg_at_5
      value: 37.533
    - type: ndcg_at_10
      value: 40.224
    - type: ndcg_at_20
      value: 41.818
    - type: ndcg_at_100
      value: 44.651999999999994
    - type: ndcg_at_1000
      value: 47.05
    - type: map_at_1
      value: 26.251
    - type: map_at_3
      value: 32.49
    - type: map_at_5
      value: 33.931
    - type: map_at_10
      value: 35.154
    - type: map_at_20
      value: 35.641
    - type: map_at_100
      value: 36.032
    - type: map_at_1000
      value: 36.132
    - type: recall_at_1
      value: 26.251
    - type: recall_at_3
      value: 39.76
    - type: recall_at_5
      value: 45.739999999999995
    - type: recall_at_10
      value: 53.698
    - type: recall_at_20
      value: 59.48
    - type: recall_at_100
      value: 74.298
    - type: recall_at_1000
      value: 92.06299999999999
    - type: precision_at_1
      value: 28.701
    - type: precision_at_3
      value: 14.953
    - type: precision_at_5
      value: 10.328
    - type: precision_at_10
      value: 6.158
    - type: precision_at_20
      value: 3.469
    - type: precision_at_100
      value: 0.886
    - type: precision_at_1000
      value: 0.11199999999999999
    - type: mrr_at_1
      value: 28.700599999999998
    - type: mrr_at_3
      value: 34.9906
    - type: mrr_at_5
      value: 36.3917
    - type: mrr_at_10
      value: 37.4735
    - type: mrr_at_20
      value: 37.896
    - type: mrr_at_100
      value: 38.229600000000005
    - type: mrr_at_1000
      value: 38.3107
    - type: nauc_ndcg_at_1_max
      value: 35.5663
    - type: nauc_ndcg_at_1_std
      value: -11.130700000000001
    - type: nauc_ndcg_at_1_diff1
      value: 47.2971
    - type: nauc_ndcg_at_3_max
      value: 33.591300000000004
    - type: nauc_ndcg_at_3_std
      value: -8.8712
    - type: nauc_ndcg_at_3_diff1
      value: 43.9366
    - type: nauc_ndcg_at_5_max
      value: 32.8546
    - type: nauc_ndcg_at_5_std
      value: -7.764799999999999
    - type: nauc_ndcg_at_5_diff1
      value: 42.896699999999996
    - type: nauc_ndcg_at_10_max
      value: 33.8862
    - type: nauc_ndcg_at_10_std
      value: -5.8975
    - type: nauc_ndcg_at_10_diff1
      value: 42.0493
    - type: nauc_ndcg_at_20_max
      value: 34.4891
    - type: nauc_ndcg_at_20_std
      value: -4.7832
    - type: nauc_ndcg_at_20_diff1
      value: 41.857499999999995
    - type: nauc_ndcg_at_100_max
      value: 34.2737
    - type: nauc_ndcg_at_100_std
      value: -4.8904000000000005
    - type: nauc_ndcg_at_100_diff1
      value: 41.3476
    - type: nauc_ndcg_at_1000_max
      value: 34.031800000000004
    - type: nauc_ndcg_at_1000_std
      value: -5.5376
    - type: nauc_ndcg_at_1000_diff1
      value: 41.8603
    - type: nauc_map_at_1_max
      value: 33.128299999999996
    - type: nauc_map_at_1_std
      value: -12.1157
    - type: nauc_map_at_1_diff1
      value: 49.8448
    - type: nauc_map_at_3_max
      value: 33.283699999999996
    - type: nauc_map_at_3_std
      value: -9.7518
    - type: nauc_map_at_3_diff1
      value: 45.4875
    - type: nauc_map_at_5_max
      value: 32.9355
    - type: nauc_map_at_5_std
      value: -9.1755
    - type: nauc_map_at_5_diff1
      value: 44.8675
    - type: nauc_map_at_10_max
      value: 33.5532
    - type: nauc_map_at_10_std
      value: -8.3763
    - type: nauc_map_at_10_diff1
      value: 44.670700000000004
    - type: nauc_map_at_20_max
      value: 33.8065
    - type: nauc_map_at_20_std
      value: -8.0253
    - type: nauc_map_at_20_diff1
      value: 44.5987
    - type: nauc_map_at_100_max
      value: 33.7647
    - type: nauc_map_at_100_std
      value: -8.0399
    - type: nauc_map_at_100_diff1
      value: 44.5212
    - type: nauc_map_at_1000_max
      value: 33.752700000000004
    - type: nauc_map_at_1000_std
      value: -8.0557
    - type: nauc_map_at_1000_diff1
      value: 44.5285
    - type: nauc_recall_at_1_max
      value: 33.128299999999996
    - type: nauc_recall_at_1_std
      value: -12.1157
    - type: nauc_recall_at_1_diff1
      value: 49.8448
    - type: nauc_recall_at_3_max
      value: 31.5403
    - type: nauc_recall_at_3_std
      value: -6.862699999999999
    - type: nauc_recall_at_3_diff1
      value: 40.4438
    - type: nauc_recall_at_5_max
      value: 29.549300000000002
    - type: nauc_recall_at_5_std
      value: -4.8186
    - type: nauc_recall_at_5_diff1
      value: 37.7652
    - type: nauc_recall_at_10_max
      value: 32.0106
    - type: nauc_recall_at_10_std
      value: 1.1384999999999998
    - type: nauc_recall_at_10_diff1
      value: 34.4037
    - type: nauc_recall_at_20_max
      value: 34.1547
    - type: nauc_recall_at_20_std
      value: 6.0514
    - type: nauc_recall_at_20_diff1
      value: 33.4793
    - type: nauc_recall_at_100_max
      value: 32.610099999999996
    - type: nauc_recall_at_100_std
      value: 9.046899999999999
    - type: nauc_recall_at_100_diff1
      value: 27.256999999999998
    - type: nauc_recall_at_1000_max
      value: 26.3079
    - type: nauc_recall_at_1000_std
      value: 16.963900000000002
    - type: nauc_recall_at_1000_diff1
      value: 22.1857
    - type: nauc_precision_at_1_max
      value: 35.5663
    - type: nauc_precision_at_1_std
      value: -11.130700000000001
    - type: nauc_precision_at_1_diff1
      value: 47.2971
    - type: nauc_precision_at_3_max
      value: 34.8919
    - type: nauc_precision_at_3_std
      value: -4.6598
    - type: nauc_precision_at_3_diff1
      value: 36.1773
    - type: nauc_precision_at_5_max
      value: 32.9054
    - type: nauc_precision_at_5_std
      value: -2.0126999999999997
    - type: nauc_precision_at_5_diff1
      value: 32.6994
    - type: nauc_precision_at_10_max
      value: 33.683600000000006
    - type: nauc_precision_at_10_std
      value: 3.2531999999999996
    - type: nauc_precision_at_10_diff1
      value: 28.099800000000002
    - type: nauc_precision_at_20_max
      value: 33.7297
    - type: nauc_precision_at_20_std
      value: 7.0116
    - type: nauc_precision_at_20_diff1
      value: 23.663999999999998
    - type: nauc_precision_at_100_max
      value: 26.119300000000003
    - type: nauc_precision_at_100_std
      value: 7.8559
    - type: nauc_precision_at_100_diff1
      value: 9.9931
    - type: nauc_precision_at_1000_max
      value: 11.0973
    - type: nauc_precision_at_1000_std
      value: 4.6916
    - type: nauc_precision_at_1000_diff1
      value: -6.2033
    - type: nauc_mrr_at_1_max
      value: 35.5663
    - type: nauc_mrr_at_1_std
      value: -11.130700000000001
    - type: nauc_mrr_at_1_diff1
      value: 47.2971
    - type: nauc_mrr_at_3_max
      value: 35.0322
    - type: nauc_mrr_at_3_std
      value: -8.6242
    - type: nauc_mrr_at_3_diff1
      value: 43.435
    - type: nauc_mrr_at_5_max
      value: 34.796899999999994
    - type: nauc_mrr_at_5_std
      value: -8.1215
    - type: nauc_mrr_at_5_diff1
      value: 42.9234
    - type: nauc_mrr_at_10_max
      value: 35.0315
    - type: nauc_mrr_at_10_std
      value: -7.4498
    - type: nauc_mrr_at_10_diff1
      value: 42.348
    - type: nauc_mrr_at_20_max
      value: 35.0761
    - type: nauc_mrr_at_20_std
      value: -7.246700000000001
    - type: nauc_mrr_at_20_diff1
      value: 42.3282
    - type: nauc_mrr_at_100_max
      value: 35.0173
    - type: nauc_mrr_at_100_std
      value: -7.269699999999999
    - type: nauc_mrr_at_100_diff1
      value: 42.306
    - type: nauc_mrr_at_1000_max
      value: 35.015
    - type: nauc_mrr_at_1000_std
      value: -7.2973
    - type: nauc_mrr_at_1000_diff1
      value: 42.3292
    - type: main_score
      value: 40.224
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB CQADupstackMathematicaRetrieval (default)
      revision: 90fceea13679c63fe563ded68f3b6f06e50061de
      split: test
      type: mteb/cqadupstack-mathematica
    metrics:
    - type: ndcg_at_1
      value: 20.398
    - type: ndcg_at_3
      value: 25.701
    - type: ndcg_at_5
      value: 27.503
    - type: ndcg_at_10
      value: 30.016
    - type: ndcg_at_20
      value: 31.941000000000003
    - type: ndcg_at_100
      value: 35.995
    - type: ndcg_at_1000
      value: 38.732
    - type: map_at_1
      value: 15.827
    - type: map_at_3
      value: 22.185
    - type: map_at_5
      value: 23.398
    - type: map_at_10
      value: 24.576
    - type: map_at_20
      value: 25.158
    - type: map_at_100
      value: 25.790000000000003
    - type: map_at_1000
      value: 25.906000000000002
    - type: recall_at_1
      value: 15.827
    - type: recall_at_3
      value: 29.404000000000003
    - type: recall_at_5
      value: 34.408
    - type: recall_at_10
      value: 41.802
    - type: recall_at_20
      value: 48.775
    - type: recall_at_100
      value: 68.643
    - type: recall_at_1000
      value: 88.022
    - type: precision_at_1
      value: 20.398
    - type: precision_at_3
      value: 12.769
    - type: precision_at_5
      value: 9.030000000000001
    - type: precision_at_10
      value: 5.684
    - type: precision_at_20
      value: 3.408
    - type: precision_at_100
      value: 1.004
    - type: precision_at_1000
      value: 0.13699999999999998
    - type: mrr_at_1
      value: 20.398
    - type: mrr_at_3
      value: 27.1144
    - type: mrr_at_5
      value: 28.4453
    - type: mrr_at_10
      value: 29.5935
    - type: mrr_at_20
      value: 30.0591
    - type: mrr_at_100
      value: 30.516399999999997
    - type: mrr_at_1000
      value: 30.5831
    - type: nauc_ndcg_at_1_max
      value: 26.8727
    - type: nauc_ndcg_at_1_std
      value: -2.0329
    - type: nauc_ndcg_at_1_diff1
      value: 28.792099999999998
    - type: nauc_ndcg_at_3_max
      value: 29.210900000000002
    - type: nauc_ndcg_at_3_std
      value: 1.357
    - type: nauc_ndcg_at_3_diff1
      value: 25.153399999999998
    - type: nauc_ndcg_at_5_max
      value: 28.031499999999998
    - type: nauc_ndcg_at_5_std
      value: 1.546
    - type: nauc_ndcg_at_5_diff1
      value: 23.6489
    - type: nauc_ndcg_at_10_max
      value: 27.2909
    - type: nauc_ndcg_at_10_std
      value: 1.8301
    - type: nauc_ndcg_at_10_diff1
      value: 21.7899
    - type: nauc_ndcg_at_20_max
      value: 27.934900000000003
    - type: nauc_ndcg_at_20_std
      value: 2.3472
    - type: nauc_ndcg_at_20_diff1
      value: 22.322
    - type: nauc_ndcg_at_100_max
      value: 28.1958
    - type: nauc_ndcg_at_100_std
      value: 3.5208000000000004
    - type: nauc_ndcg_at_100_diff1
      value: 23.156499999999998
    - type: nauc_ndcg_at_1000_max
      value: 28.766000000000002
    - type: nauc_ndcg_at_1000_std
      value: 3.4803
    - type: nauc_ndcg_at_1000_diff1
      value: 23.096600000000002
    - type: nauc_map_at_1_max
      value: 26.271099999999997
    - type: nauc_map_at_1_std
      value: -0.8499
    - type: nauc_map_at_1_diff1
      value: 32.0953
    - type: nauc_map_at_3_max
      value: 28.1188
    - type: nauc_map_at_3_std
      value: 0.42040000000000005
    - type: nauc_map_at_3_diff1
      value: 26.6573
    - type: nauc_map_at_5_max
      value: 27.5138
    - type: nauc_map_at_5_std
      value: 0.43010000000000004
    - type: nauc_map_at_5_diff1
      value: 25.6081
    - type: nauc_map_at_10_max
      value: 27.313900000000004
    - type: nauc_map_at_10_std
      value: 0.644
    - type: nauc_map_at_10_diff1
      value: 24.6459
    - type: nauc_map_at_20_max
      value: 27.5519
    - type: nauc_map_at_20_std
      value: 0.7802
    - type: nauc_map_at_20_diff1
      value: 24.7392
    - type: nauc_map_at_100_max
      value: 27.717999999999996
    - type: nauc_map_at_100_std
      value: 1.078
    - type: nauc_map_at_100_diff1
      value: 24.884500000000003
    - type: nauc_map_at_1000_max
      value: 27.7366
    - type: nauc_map_at_1000_std
      value: 1.0739
    - type: nauc_map_at_1000_diff1
      value: 24.9131
    - type: nauc_recall_at_1_max
      value: 26.271099999999997
    - type: nauc_recall_at_1_std
      value: -0.8499
    - type: nauc_recall_at_1_diff1
      value: 32.0953
    - type: nauc_recall_at_3_max
      value: 28.034399999999998
    - type: nauc_recall_at_3_std
      value: 2.7848
    - type: nauc_recall_at_3_diff1
      value: 21.845
    - type: nauc_recall_at_5_max
      value: 25.510899999999996
    - type: nauc_recall_at_5_std
      value: 3.2032
    - type: nauc_recall_at_5_diff1
      value: 18.1497
    - type: nauc_recall_at_10_max
      value: 23.6985
    - type: nauc_recall_at_10_std
      value: 4.2382
    - type: nauc_recall_at_10_diff1
      value: 13.4018
    - type: nauc_recall_at_20_max
      value: 25.0105
    - type: nauc_recall_at_20_std
      value: 6.2892
    - type: nauc_recall_at_20_diff1
      value: 14.6347
    - type: nauc_recall_at_100_max
      value: 23.6484
    - type: nauc_recall_at_100_std
      value: 12.826299999999998
    - type: nauc_recall_at_100_diff1
      value: 16.372999999999998
    - type: nauc_recall_at_1000_max
      value: 34.1999
    - type: nauc_recall_at_1000_std
      value: 26.1497
    - type: nauc_recall_at_1000_diff1
      value: 7.666199999999999
    - type: nauc_precision_at_1_max
      value: 26.8727
    - type: nauc_precision_at_1_std
      value: -2.0329
    - type: nauc_precision_at_1_diff1
      value: 28.792099999999998
    - type: nauc_precision_at_3_max
      value: 31.689
    - type: nauc_precision_at_3_std
      value: 4.5703000000000005
    - type: nauc_precision_at_3_diff1
      value: 20.0233
    - type: nauc_precision_at_5_max
      value: 27.807
    - type: nauc_precision_at_5_std
      value: 4.209899999999999
    - type: nauc_precision_at_5_diff1
      value: 15.3505
    - type: nauc_precision_at_10_max
      value: 22.672800000000002
    - type: nauc_precision_at_10_std
      value: 3.624
    - type: nauc_precision_at_10_diff1
      value: 8.4378
    - type: nauc_precision_at_20_max
      value: 23.3401
    - type: nauc_precision_at_20_std
      value: 3.6032
    - type: nauc_precision_at_20_diff1
      value: 9.2764
    - type: nauc_precision_at_100_max
      value: 16.516000000000002
    - type: nauc_precision_at_100_std
      value: 5.7479000000000005
    - type: nauc_precision_at_100_diff1
      value: 5.733499999999999
    - type: nauc_precision_at_1000_max
      value: 6.1677
    - type: nauc_precision_at_1000_std
      value: 0.4491
    - type: nauc_precision_at_1000_diff1
      value: 0.2477
    - type: nauc_mrr_at_1_max
      value: 26.8727
    - type: nauc_mrr_at_1_std
      value: -2.0329
    - type: nauc_mrr_at_1_diff1
      value: 28.792099999999998
    - type: nauc_mrr_at_3_max
      value: 29.6131
    - type: nauc_mrr_at_3_std
      value: 0.6053000000000001
    - type: nauc_mrr_at_3_diff1
      value: 25.8043
    - type: nauc_mrr_at_5_max
      value: 29.0205
    - type: nauc_mrr_at_5_std
      value: 0.8692
    - type: nauc_mrr_at_5_diff1
      value: 24.8413
    - type: nauc_mrr_at_10_max
      value: 28.459400000000002
    - type: nauc_mrr_at_10_std
      value: 0.5887
    - type: nauc_mrr_at_10_diff1
      value: 24.364
    - type: nauc_mrr_at_20_max
      value: 28.5242
    - type: nauc_mrr_at_20_std
      value: 0.6396
    - type: nauc_mrr_at_20_diff1
      value: 24.4579
    - type: nauc_mrr_at_100_max
      value: 28.540599999999998
    - type: nauc_mrr_at_100_std
      value: 0.7425
    - type: nauc_mrr_at_100_diff1
      value: 24.5761
    - type: nauc_mrr_at_1000_max
      value: 28.5429
    - type: nauc_mrr_at_1000_std
      value: 0.7348
    - type: nauc_mrr_at_1000_diff1
      value: 24.562800000000003
    - type: main_score
      value: 30.016
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB CQADupstackPhysicsRetrieval (default)
      revision: 79531abbd1fb92d06c6d6315a0cbbbf5bb247ea4
      split: test
      type: mteb/cqadupstack-physics
    metrics:
    - type: ndcg_at_1
      value: 34.937000000000005
    - type: ndcg_at_3
      value: 39.366
    - type: ndcg_at_5
      value: 41.980000000000004
    - type: ndcg_at_10
      value: 44.674
    - type: ndcg_at_20
      value: 46.671
    - type: ndcg_at_100
      value: 50.041999999999994
    - type: ndcg_at_1000
      value: 52.120999999999995
    - type: map_at_1
      value: 27.750000000000004
    - type: map_at_3
      value: 35.027
    - type: map_at_5
      value: 36.952
    - type: map_at_10
      value: 38.382
    - type: map_at_20
      value: 39.072
    - type: map_at_100
      value: 39.694
    - type: map_at_1000
      value: 39.81
    - type: recall_at_1
      value: 27.750000000000004
    - type: recall_at_3
      value: 42.321999999999996
    - type: recall_at_5
      value: 49.209
    - type: recall_at_10
      value: 57.282
    - type: recall_at_20
      value: 64.30399999999999
    - type: recall_at_100
      value: 80.143
    - type: recall_at_1000
      value: 93.664
    - type: precision_at_1
      value: 34.937000000000005
    - type: precision_at_3
      value: 18.993
    - type: precision_at_5
      value: 13.648
    - type: precision_at_10
      value: 8.412
    - type: precision_at_20
      value: 4.885
    - type: precision_at_100
      value: 1.302
    - type: precision_at_1000
      value: 0.167
    - type: mrr_at_1
      value: 34.937400000000004
    - type: mrr_at_3
      value: 41.7389
    - type: mrr_at_5
      value: 43.4184
    - type: mrr_at_10
      value: 44.4776
    - type: mrr_at_20
      value: 44.8859
    - type: mrr_at_100
      value: 45.2197
    - type: mrr_at_1000
      value: 45.2704
    - type: nauc_ndcg_at_1_max
      value: 41.1314
    - type: nauc_ndcg_at_1_std
      value: 0.6393
    - type: nauc_ndcg_at_1_diff1
      value: 52.494
    - type: nauc_ndcg_at_3_max
      value: 38.8915
    - type: nauc_ndcg_at_3_std
      value: -1.1358
    - type: nauc_ndcg_at_3_diff1
      value: 48.8256
    - type: nauc_ndcg_at_5_max
      value: 38.6924
    - type: nauc_ndcg_at_5_std
      value: -2.2843999999999998
    - type: nauc_ndcg_at_5_diff1
      value: 47.9194
    - type: nauc_ndcg_at_10_max
      value: 37.8751
    - type: nauc_ndcg_at_10_std
      value: -1.5187000000000002
    - type: nauc_ndcg_at_10_diff1
      value: 46.455400000000004
    - type: nauc_ndcg_at_20_max
      value: 38.1022
    - type: nauc_ndcg_at_20_std
      value: -0.7692
    - type: nauc_ndcg_at_20_diff1
      value: 46.5041
    - type: nauc_ndcg_at_100_max
      value: 40.396100000000004
    - type: nauc_ndcg_at_100_std
      value: 1.8087
    - type: nauc_ndcg_at_100_diff1
      value: 47.2332
    - type: nauc_ndcg_at_1000_max
      value: 40.2539
    - type: nauc_ndcg_at_1000_std
      value: 2.1609
    - type: nauc_ndcg_at_1000_diff1
      value: 47.185700000000004
    - type: nauc_map_at_1_max
      value: 34.3255
    - type: nauc_map_at_1_std
      value: -6.783599999999999
    - type: nauc_map_at_1_diff1
      value: 54.6668
    - type: nauc_map_at_3_max
      value: 36.5777
    - type: nauc_map_at_3_std
      value: -3.8482000000000003
    - type: nauc_map_at_3_diff1
      value: 50.1703
    - type: nauc_map_at_5_max
      value: 37.229
    - type: nauc_map_at_5_std
      value: -3.9170000000000003
    - type: nauc_map_at_5_diff1
      value: 49.5882
    - type: nauc_map_at_10_max
      value: 37.318400000000004
    - type: nauc_map_at_10_std
      value: -3.2477
    - type: nauc_map_at_10_diff1
      value: 48.8387
    - type: nauc_map_at_20_max
      value: 37.5075
    - type: nauc_map_at_20_std
      value: -2.8737
    - type: nauc_map_at_20_diff1
      value: 48.896699999999996
    - type: nauc_map_at_100_max
      value: 37.965199999999996
    - type: nauc_map_at_100_std
      value: -2.3644
    - type: nauc_map_at_100_diff1
      value: 48.9583
    - type: nauc_map_at_1000_max
      value: 37.9824
    - type: nauc_map_at_1000_std
      value: -2.2945
    - type: nauc_map_at_1000_diff1
      value: 48.9472
    - type: nauc_recall_at_1_max
      value: 34.3255
    - type: nauc_recall_at_1_std
      value: -6.783599999999999
    - type: nauc_recall_at_1_diff1
      value: 54.6668
    - type: nauc_recall_at_3_max
      value: 33.823100000000004
    - type: nauc_recall_at_3_std
      value: -3.7593
    - type: nauc_recall_at_3_diff1
      value: 44.3225
    - type: nauc_recall_at_5_max
      value: 34.271499999999996
    - type: nauc_recall_at_5_std
      value: -4.8704
    - type: nauc_recall_at_5_diff1
      value: 41.3594
    - type: nauc_recall_at_10_max
      value: 32.2652
    - type: nauc_recall_at_10_std
      value: -1.5755000000000001
    - type: nauc_recall_at_10_diff1
      value: 35.9057
    - type: nauc_recall_at_20_max
      value: 32.1614
    - type: nauc_recall_at_20_std
      value: 0.8789
    - type: nauc_recall_at_20_diff1
      value: 34.6074
    - type: nauc_recall_at_100_max
      value: 44.527499999999996
    - type: nauc_recall_at_100_std
      value: 17.735500000000002
    - type: nauc_recall_at_100_diff1
      value: 36.446
    - type: nauc_recall_at_1000_max
      value: 47.751
    - type: nauc_recall_at_1000_std
      value: 41.8399
    - type: nauc_recall_at_1000_diff1
      value: 26.7075
    - type: nauc_precision_at_1_max
      value: 41.1314
    - type: nauc_precision_at_1_std
      value: 0.6393
    - type: nauc_precision_at_1_diff1
      value: 52.494
    - type: nauc_precision_at_3_max
      value: 40.7504
    - type: nauc_precision_at_3_std
      value: 8.6914
    - type: nauc_precision_at_3_diff1
      value: 34.590900000000005
    - type: nauc_precision_at_5_max
      value: 38.5891
    - type: nauc_precision_at_5_std
      value: 8.7898
    - type: nauc_precision_at_5_diff1
      value: 27.122200000000003
    - type: nauc_precision_at_10_max
      value: 32.5422
    - type: nauc_precision_at_10_std
      value: 13.9757
    - type: nauc_precision_at_10_diff1
      value: 15.504000000000001
    - type: nauc_precision_at_20_max
      value: 28.212799999999998
    - type: nauc_precision_at_20_std
      value: 17.0921
    - type: nauc_precision_at_20_diff1
      value: 10.264800000000001
    - type: nauc_precision_at_100_max
      value: 23.9818
    - type: nauc_precision_at_100_std
      value: 24.7802
    - type: nauc_precision_at_100_diff1
      value: -0.1275
    - type: nauc_precision_at_1000_max
      value: 11.8968
    - type: nauc_precision_at_1000_std
      value: 24.0201
    - type: nauc_precision_at_1000_diff1
      value: -12.1507
    - type: nauc_mrr_at_1_max
      value: 41.1314
    - type: nauc_mrr_at_1_std
      value: 0.6393
    - type: nauc_mrr_at_1_diff1
      value: 52.494
    - type: nauc_mrr_at_3_max
      value: 41.0145
    - type: nauc_mrr_at_3_std
      value: 1.7641
    - type: nauc_mrr_at_3_diff1
      value: 49.3663
    - type: nauc_mrr_at_5_max
      value: 41.4664
    - type: nauc_mrr_at_5_std
      value: 1.6695000000000002
    - type: nauc_mrr_at_5_diff1
      value: 49.0033
    - type: nauc_mrr_at_10_max
      value: 41.2351
    - type: nauc_mrr_at_10_std
      value: 2.0388
    - type: nauc_mrr_at_10_diff1
      value: 48.7703
    - type: nauc_mrr_at_20_max
      value: 41.2064
    - type: nauc_mrr_at_20_std
      value: 2.081
    - type: nauc_mrr_at_20_diff1
      value: 48.6787
    - type: nauc_mrr_at_100_max
      value: 41.3966
    - type: nauc_mrr_at_100_std
      value: 2.2723
    - type: nauc_mrr_at_100_diff1
      value: 48.746
    - type: nauc_mrr_at_1000_max
      value: 41.3803
    - type: nauc_mrr_at_1000_std
      value: 2.2632
    - type: nauc_mrr_at_1000_diff1
      value: 48.7541
    - type: main_score
      value: 44.674
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB CQADupstackProgrammersRetrieval (default)
      revision: 6184bc1440d2dbc7612be22b50686b8826d22b32
      split: test
      type: mteb/cqadupstack-programmers
    metrics:
    - type: ndcg_at_1
      value: 29.909000000000002
    - type: ndcg_at_3
      value: 35.056
    - type: ndcg_at_5
      value: 37.076
    - type: ndcg_at_10
      value: 40.093
    - type: ndcg_at_20
      value: 42.254999999999995
    - type: ndcg_at_100
      value: 45.692
    - type: ndcg_at_1000
      value: 48.204
    - type: map_at_1
      value: 24.68
    - type: map_at_3
      value: 31.379
    - type: map_at_5
      value: 32.92
    - type: map_at_10
      value: 34.391
    - type: map_at_20
      value: 35.109
    - type: map_at_100
      value: 35.686
    - type: map_at_1000
      value: 35.804
    - type: recall_at_1
      value: 24.68
    - type: recall_at_3
      value: 38.190000000000005
    - type: recall_at_5
      value: 43.519999999999996
    - type: recall_at_10
      value: 52.364999999999995
    - type: recall_at_20
      value: 60.02499999999999
    - type: recall_at_100
      value: 76.229
    - type: recall_at_1000
      value: 93.31099999999999
    - type: precision_at_1
      value: 29.909000000000002
    - type: precision_at_3
      value: 16.667
    - type: precision_at_5
      value: 11.781
    - type: precision_at_10
      value: 7.340000000000001
    - type: precision_at_20
      value: 4.315
    - type: precision_at_100
      value: 1.18
    - type: precision_at_1000
      value: 0.158
    - type: mrr_at_1
      value: 29.9087
    - type: mrr_at_3
      value: 36.6438
    - type: mrr_at_5
      value: 37.939499999999995
    - type: mrr_at_10
      value: 39.1699
    - type: mrr_at_20
      value: 39.6872
    - type: mrr_at_100
      value: 40.0648
    - type: mrr_at_1000
      value: 40.1254
    - type: nauc_ndcg_at_1_max
      value: 37.3397
    - type: nauc_ndcg_at_1_std
      value: 5.9699
    - type: nauc_ndcg_at_1_diff1
      value: 46.6563
    - type: nauc_ndcg_at_3_max
      value: 39.0153
    - type: nauc_ndcg_at_3_std
      value: 8.5756
    - type: nauc_ndcg_at_3_diff1
      value: 41.2988
    - type: nauc_ndcg_at_5_max
      value: 39.4932
    - type: nauc_ndcg_at_5_std
      value: 9.4963
    - type: nauc_ndcg_at_5_diff1
      value: 40.0798
    - type: nauc_ndcg_at_10_max
      value: 40.0787
    - type: nauc_ndcg_at_10_std
      value: 10.312100000000001
    - type: nauc_ndcg_at_10_diff1
      value: 39.6584
    - type: nauc_ndcg_at_20_max
      value: 40.9003
    - type: nauc_ndcg_at_20_std
      value: 11.991100000000001
    - type: nauc_ndcg_at_20_diff1
      value: 39.4373
    - type: nauc_ndcg_at_100_max
      value: 41.4069
    - type: nauc_ndcg_at_100_std
      value: 13.6103
    - type: nauc_ndcg_at_100_diff1
      value: 40.0088
    - type: nauc_ndcg_at_1000_max
      value: 41.505900000000004
    - type: nauc_ndcg_at_1000_std
      value: 12.742400000000002
    - type: nauc_ndcg_at_1000_diff1
      value: 40.1457
    - type: nauc_map_at_1_max
      value: 34.739
    - type: nauc_map_at_1_std
      value: 0.9294
    - type: nauc_map_at_1_diff1
      value: 48.1138
    - type: nauc_map_at_3_max
      value: 37.0441
    - type: nauc_map_at_3_std
      value: 5.5666
    - type: nauc_map_at_3_diff1
      value: 42.7429
    - type: nauc_map_at_5_max
      value: 37.891799999999996
    - type: nauc_map_at_5_std
      value: 6.7185999999999995
    - type: nauc_map_at_5_diff1
      value: 41.9849
    - type: nauc_map_at_10_max
      value: 38.556000000000004
    - type: nauc_map_at_10_std
      value: 7.4627
    - type: nauc_map_at_10_diff1
      value: 41.8061
    - type: nauc_map_at_20_max
      value: 38.8822
    - type: nauc_map_at_20_std
      value: 8.0747
    - type: nauc_map_at_20_diff1
      value: 41.7518
    - type: nauc_map_at_100_max
      value: 39.0912
    - type: nauc_map_at_100_std
      value: 8.4627
    - type: nauc_map_at_100_diff1
      value: 41.8958
    - type: nauc_map_at_1000_max
      value: 39.112700000000004
    - type: nauc_map_at_1000_std
      value: 8.4459
    - type: nauc_map_at_1000_diff1
      value: 41.903400000000005
    - type: nauc_recall_at_1_max
      value: 34.739
    - type: nauc_recall_at_1_std
      value: 0.9294
    - type: nauc_recall_at_1_diff1
      value: 48.1138
    - type: nauc_recall_at_3_max
      value: 37.3971
    - type: nauc_recall_at_3_std
      value: 9.2075
    - type: nauc_recall_at_3_diff1
      value: 36.4624
    - type: nauc_recall_at_5_max
      value: 38.1516
    - type: nauc_recall_at_5_std
      value: 11.5318
    - type: nauc_recall_at_5_diff1
      value: 33.3421
    - type: nauc_recall_at_10_max
      value: 38.8221
    - type: nauc_recall_at_10_std
      value: 14.0268
    - type: nauc_recall_at_10_diff1
      value: 31.4088
    - type: nauc_recall_at_20_max
      value: 40.9493
    - type: nauc_recall_at_20_std
      value: 20.2136
    - type: nauc_recall_at_20_diff1
      value: 29.9447
    - type: nauc_recall_at_100_max
      value: 43.149300000000004
    - type: nauc_recall_at_100_std
      value: 33.7709
    - type: nauc_recall_at_100_diff1
      value: 29.3082
    - type: nauc_recall_at_1000_max
      value: 55.435500000000005
    - type: nauc_recall_at_1000_std
      value: 51.8958
    - type: nauc_recall_at_1000_diff1
      value: 19.3816
    - type: nauc_precision_at_1_max
      value: 37.3397
    - type: nauc_precision_at_1_std
      value: 5.9699
    - type: nauc_precision_at_1_diff1
      value: 46.6563
    - type: nauc_precision_at_3_max
      value: 40.3693
    - type: nauc_precision_at_3_std
      value: 17.0552
    - type: nauc_precision_at_3_diff1
      value: 29.498400000000004
    - type: nauc_precision_at_5_max
      value: 39.7607
    - type: nauc_precision_at_5_std
      value: 20.274
    - type: nauc_precision_at_5_diff1
      value: 23.061300000000003
    - type: nauc_precision_at_10_max
      value: 38.0299
    - type: nauc_precision_at_10_std
      value: 22.256899999999998
    - type: nauc_precision_at_10_diff1
      value: 17.0507
    - type: nauc_precision_at_20_max
      value: 36.0867
    - type: nauc_precision_at_20_std
      value: 25.936700000000002
    - type: nauc_precision_at_20_diff1
      value: 12.1754
    - type: nauc_precision_at_100_max
      value: 24.1493
    - type: nauc_precision_at_100_std
      value: 23.8361
    - type: nauc_precision_at_100_diff1
      value: 5.2714
    - type: nauc_precision_at_1000_max
      value: 7.033499999999999
    - type: nauc_precision_at_1000_std
      value: 9.0198
    - type: nauc_precision_at_1000_diff1
      value: -4.8427999999999995
    - type: nauc_mrr_at_1_max
      value: 37.3397
    - type: nauc_mrr_at_1_std
      value: 5.9699
    - type: nauc_mrr_at_1_diff1
      value: 46.6563
    - type: nauc_mrr_at_3_max
      value: 40.2205
    - type: nauc_mrr_at_3_std
      value: 9.8833
    - type: nauc_mrr_at_3_diff1
      value: 42.3963
    - type: nauc_mrr_at_5_max
      value: 40.1911
    - type: nauc_mrr_at_5_std
      value: 10.3282
    - type: nauc_mrr_at_5_diff1
      value: 41.796499999999995
    - type: nauc_mrr_at_10_max
      value: 40.3748
    - type: nauc_mrr_at_10_std
      value: 10.567699999999999
    - type: nauc_mrr_at_10_diff1
      value: 41.643299999999996
    - type: nauc_mrr_at_20_max
      value: 40.4527
    - type: nauc_mrr_at_20_std
      value: 10.8016
    - type: nauc_mrr_at_20_diff1
      value: 41.594300000000004
    - type: nauc_mrr_at_100_max
      value: 40.395199999999996
    - type: nauc_mrr_at_100_std
      value: 10.8396
    - type: nauc_mrr_at_100_diff1
      value: 41.706700000000005
    - type: nauc_mrr_at_1000_max
      value: 40.3932
    - type: nauc_mrr_at_1000_std
      value: 10.8097
    - type: nauc_mrr_at_1000_diff1
      value: 41.7124
    - type: main_score
      value: 40.093
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB CQADupstackRetrieval (default)
      revision: 160c094312a0e1facb97e55eeddb698c0abe3571
      split: test
      type: CQADupstackRetrieval_is_a_combined_dataset
    metrics:
    - type: ndcg_at_1
      value: 30.19958333333333
    - type: ndcg_at_3
      value: 35.01541666666667
    - type: ndcg_at_5
      value: 37.22058333333334
    - type: ndcg_at_10
      value: 39.84525000000001
    - type: ndcg_at_20
      value: 41.81666666666667
    - type: ndcg_at_100
      value: 44.973
    - type: ndcg_at_1000
      value: 47.338583333333325
    - type: map_at_1
      value: 25.296916666666668
    - type: map_at_3
      value: 31.593166666666665
    - type: map_at_5
      value: 33.145916666666665
    - type: map_at_10
      value: 34.45275
    - type: map_at_20
      value: 35.10883333333334
    - type: map_at_100
      value: 35.647499999999994
    - type: map_at_1000
      value: 35.768166666666666
    - type: recall_at_1
      value: 25.296916666666668
    - type: recall_at_3
      value: 38.05166666666666
    - type: recall_at_5
      value: 43.82625
    - type: recall_at_10
      value: 51.58916666666668
    - type: recall_at_20
      value: 58.77308333333334
    - type: recall_at_100
      value: 74.15658333333333
    - type: recall_at_1000
      value: 90.51333333333335
    - type: precision_at_1
      value: 30.19958333333333
    - type: precision_at_3
      value: 16.167999999999996
    - type: precision_at_5
      value: 11.49225
    - type: precision_at_10
      value: 7.057666666666666
    - type: precision_at_20
      value: 4.174083333333333
    - type: precision_at_100
      value: 1.1363333333333332
    - type: precision_at_1000
      value: 0.15383333333333332
    - type: mrr_at_1
      value: 30.199658333333335
    - type: mrr_at_3
      value: 36.21564166666667
    - type: mrr_at_5
      value: 37.627291666666665
    - type: mrr_at_10
      value: 38.70535
    - type: mrr_at_20
      value: 39.193799999999996
    - type: mrr_at_100
      value: 39.55041666666666
    - type: mrr_at_1000
      value: 39.61140833333333
    - type: nauc_ndcg_at_1_max
      value: 39.3715
    - type: nauc_ndcg_at_1_std
      value: -1.2167000000000008
    - type: nauc_ndcg_at_1_diff1
      value: 47.05770833333333
    - type: nauc_ndcg_at_3_max
      value: 38.67278333333333
    - type: nauc_ndcg_at_3_std
      value: -0.10360000000000005
    - type: nauc_ndcg_at_3_diff1
      value: 42.23506666666667
    - type: nauc_ndcg_at_5_max
      value: 38.421591666666664
    - type: nauc_ndcg_at_5_std
      value: 0.9004833333333335
    - type: nauc_ndcg_at_5_diff1
      value: 41.46895
    - type: nauc_ndcg_at_10_max
      value: 38.31713333333333
    - type: nauc_ndcg_at_10_std
      value: 1.6739333333333335
    - type: nauc_ndcg_at_10_diff1
      value: 40.52259166666667
    - type: nauc_ndcg_at_20_max
      value: 38.61266666666667
    - type: nauc_ndcg_at_20_std
      value: 2.7783666666666673
    - type: nauc_ndcg_at_20_diff1
      value: 40.28085833333333
    - type: nauc_ndcg_at_100_max
      value: 39.27558333333333
    - type: nauc_ndcg_at_100_std
      value: 3.9398000000000004
    - type: nauc_ndcg_at_100_diff1
      value: 40.39787499999999
    - type: nauc_ndcg_at_1000_max
      value: 39.44075
    - type: nauc_ndcg_at_1000_std
      value: 3.9607833333333327
    - type: nauc_ndcg_at_1000_diff1
      value: 40.683225
    - type: nauc_map_at_1_max
      value: 35.66645
    - type: nauc_map_at_1_std
      value: -4.276391666666667
    - type: nauc_map_at_1_diff1
      value: 48.810141666666674
    - type: nauc_map_at_3_max
      value: 37.424108333333336
    - type: nauc_map_at_3_std
      value: -2.064866666666667
    - type: nauc_map_at_3_diff1
      value: 44.115075
    - type: nauc_map_at_5_max
      value: 37.693016666666665
    - type: nauc_map_at_5_std
      value: -1.1872749999999994
    - type: nauc_map_at_5_diff1
      value: 43.554458333333336
    - type: nauc_map_at_10_max
      value: 37.9333
    - type: nauc_map_at_10_std
      value: -0.6246583333333332
    - type: nauc_map_at_10_diff1
      value: 43.05175
    - type: nauc_map_at_20_max
      value: 38.11316666666667
    - type: nauc_map_at_20_std
      value: -0.17139166666666622
    - type: nauc_map_at_20_diff1
      value: 42.929925000000004
    - type: nauc_map_at_100_max
      value: 38.296825
    - type: nauc_map_at_100_std
      value: 0.1448500000000002
    - type: nauc_map_at_100_diff1
      value: 42.91681666666667
    - type: nauc_map_at_1000_max
      value: 38.308891666666675
    - type: nauc_map_at_1000_std
      value: 0.17599166666666682
    - type: nauc_map_at_1000_diff1
      value: 42.91478333333333
    - type: nauc_recall_at_1_max
      value: 35.66645
    - type: nauc_recall_at_1_std
      value: -4.276391666666667
    - type: nauc_recall_at_1_diff1
      value: 48.810141666666674
    - type: nauc_recall_at_3_max
      value: 36.144949999999994
    - type: nauc_recall_at_3_std
      value: -0.07622500000000007
    - type: nauc_recall_at_3_diff1
      value: 38.39805833333333
    - type: nauc_recall_at_5_max
      value: 35.599016666666664
    - type: nauc_recall_at_5_std
      value: 2.6147583333333335
    - type: nauc_recall_at_5_diff1
      value: 35.84809166666666
    - type: nauc_recall_at_10_max
      value: 34.73115833333333
    - type: nauc_recall_at_10_std
      value: 5.2187166666666664
    - type: nauc_recall_at_10_diff1
      value: 32.22850833333333
    - type: nauc_recall_at_20_max
      value: 35.11221666666667
    - type: nauc_recall_at_20_std
      value: 9.564958333333331
    - type: nauc_recall_at_20_diff1
      value: 30.415991666666663
    - type: nauc_recall_at_100_max
      value: 37.735958333333336
    - type: nauc_recall_at_100_std
      value: 19.1386
    - type: nauc_recall_at_100_diff1
      value: 28.129675
    - type: nauc_recall_at_1000_max
      value: 43.71879166666667
    - type: nauc_recall_at_1000_std
      value: 39.80074166666667
    - type: nauc_recall_at_1000_diff1
      value: 23.800666666666668
    - type: nauc_precision_at_1_max
      value: 39.3715
    - type: nauc_precision_at_1_std
      value: -1.2167000000000008
    - type: nauc_precision_at_1_diff1
      value: 47.05770833333333
    - type: nauc_precision_at_3_max
      value: 39.00785833333333
    - type: nauc_precision_at_3_std
      value: 5.753050000000001
    - type: nauc_precision_at_3_diff1
      value: 31.4196
    - type: nauc_precision_at_5_max
      value: 36.98677500000001
    - type: nauc_precision_at_5_std
      value: 9.464608333333333
    - type: nauc_precision_at_5_diff1
      value: 25.906116666666662
    - type: nauc_precision_at_10_max
      value: 33.26575833333333
    - type: nauc_precision_at_10_std
      value: 12.540025
    - type: nauc_precision_at_10_diff1
      value: 18.274116666666668
    - type: nauc_precision_at_20_max
      value: 30.13705833333334
    - type: nauc_precision_at_20_std
      value: 16.549291666666665
    - type: nauc_precision_at_20_diff1
      value: 12.541983333333334
    - type: nauc_precision_at_100_max
      value: 22.078525000000003
    - type: nauc_precision_at_100_std
      value: 19.263416666666664
    - type: nauc_precision_at_100_diff1
      value: 2.293625
    - type: nauc_precision_at_1000_max
      value: 8.336641666666667
    - type: nauc_precision_at_1000_std
      value: 14.828683333333334
    - type: nauc_precision_at_1000_diff1
      value: -8.852525
    - type: nauc_mrr_at_1_max
      value: 39.3715
    - type: nauc_mrr_at_1_std
      value: -1.2167000000000008
    - type: nauc_mrr_at_1_diff1
      value: 47.05770833333333
    - type: nauc_mrr_at_3_max
      value: 39.90615
    - type: nauc_mrr_at_3_std
      value: 0.7366500000000004
    - type: nauc_mrr_at_3_diff1
      value: 42.96046666666666
    - type: nauc_mrr_at_5_max
      value: 39.78708333333334
    - type: nauc_mrr_at_5_std
      value: 1.3970916666666666
    - type: nauc_mrr_at_5_diff1
      value: 42.44258333333333
    - type: nauc_mrr_at_10_max
      value: 39.65595
    - type: nauc_mrr_at_10_std
      value: 1.6633916666666666
    - type: nauc_mrr_at_10_diff1
      value: 42.084358333333334
    - type: nauc_mrr_at_20_max
      value: 39.67735
    - type: nauc_mrr_at_20_std
      value: 1.8360749999999995
    - type: nauc_mrr_at_20_diff1
      value: 42.04530833333333
    - type: nauc_mrr_at_100_max
      value: 39.71681666666667
    - type: nauc_mrr_at_100_std
      value: 1.8971666666666671
    - type: nauc_mrr_at_100_diff1
      value: 42.075141666666674
    - type: nauc_mrr_at_1000_max
      value: 39.72038333333334
    - type: nauc_mrr_at_1000_std
      value: 1.8916749999999996
    - type: nauc_mrr_at_1000_diff1
      value: 42.091208333333334
    - type: main_score
      value: 39.84525000000001
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB CQADupstackRetrieval (default)
      revision: CQADupstackRetrieval_is_a_combined_dataset
      split: test
      type: CQADupstackRetrieval_is_a_combined_dataset
    metrics:
    - type: main_score
      value: 39.84525000000001
    - type: ndcg_at_10
      value: 39.84525000000001
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB CQADupstackStatsRetrieval (default)
      revision: 65ac3a16b8e91f9cee4c9828cc7c335575432a2a
      split: test
      type: mteb/cqadupstack-stats
    metrics:
    - type: ndcg_at_1
      value: 27.454
    - type: ndcg_at_3
      value: 31.464
    - type: ndcg_at_5
      value: 33.533
    - type: ndcg_at_10
      value: 35.477
    - type: ndcg_at_20
      value: 37.092999999999996
    - type: ndcg_at_100
      value: 39.808
    - type: ndcg_at_1000
      value: 42.309000000000005
    - type: map_at_1
      value: 24.489
    - type: map_at_3
      value: 29.204
    - type: map_at_5
      value: 30.496000000000002
    - type: map_at_10
      value: 31.415
    - type: map_at_20
      value: 31.897
    - type: map_at_100
      value: 32.259
    - type: map_at_1000
      value: 32.361000000000004
    - type: recall_at_1
      value: 24.489
    - type: recall_at_3
      value: 34.333999999999996
    - type: recall_at_5
      value: 39.550999999999995
    - type: recall_at_10
      value: 45.275999999999996
    - type: recall_at_20
      value: 51.241
    - type: recall_at_100
      value: 65.398
    - type: recall_at_1000
      value: 83.685
    - type: precision_at_1
      value: 27.454
    - type: precision_at_3
      value: 13.344000000000001
    - type: precision_at_5
      value: 9.417
    - type: precision_at_10
      value: 5.567
    - type: precision_at_20
      value: 3.221
    - type: precision_at_100
      value: 0.845
    - type: precision_at_1000
      value: 0.11499999999999999
    - type: mrr_at_1
      value: 27.454
    - type: mrr_at_3
      value: 32.1063
    - type: mrr_at_5
      value: 33.2797
    - type: mrr_at_10
      value: 34.0563
    - type: mrr_at_20
      value: 34.4952
    - type: mrr_at_100
      value: 34.8327
    - type: mrr_at_1000
      value: 34.9002
    - type: nauc_ndcg_at_1_max
      value: 45.7913
    - type: nauc_ndcg_at_1_std
      value: 10.6304
    - type: nauc_ndcg_at_1_diff1
      value: 51.58160000000001
    - type: nauc_ndcg_at_3_max
      value: 42.992599999999996
    - type: nauc_ndcg_at_3_std
      value: 10.1454
    - type: nauc_ndcg_at_3_diff1
      value: 45.330799999999996
    - type: nauc_ndcg_at_5_max
      value: 43.081399999999995
    - type: nauc_ndcg_at_5_std
      value: 11.7829
    - type: nauc_ndcg_at_5_diff1
      value: 45.8734
    - type: nauc_ndcg_at_10_max
      value: 45.2554
    - type: nauc_ndcg_at_10_std
      value: 14.2953
    - type: nauc_ndcg_at_10_diff1
      value: 45.908
    - type: nauc_ndcg_at_20_max
      value: 45.7565
    - type: nauc_ndcg_at_20_std
      value: 15.1327
    - type: nauc_ndcg_at_20_diff1
      value: 45.512
    - type: nauc_ndcg_at_100_max
      value: 45.602599999999995
    - type: nauc_ndcg_at_100_std
      value: 15.6507
    - type: nauc_ndcg_at_100_diff1
      value: 44.3626
    - type: nauc_ndcg_at_1000_max
      value: 45.6835
    - type: nauc_ndcg_at_1000_std
      value: 16.3352
    - type: nauc_ndcg_at_1000_diff1
      value: 44.9838
    - type: nauc_map_at_1_max
      value: 41.989900000000006
    - type: nauc_map_at_1_std
      value: 5.3356
    - type: nauc_map_at_1_diff1
      value: 52.711200000000005
    - type: nauc_map_at_3_max
      value: 42.363
    - type: nauc_map_at_3_std
      value: 8.1615
    - type: nauc_map_at_3_diff1
      value: 47.1827
    - type: nauc_map_at_5_max
      value: 42.6039
    - type: nauc_map_at_5_std
      value: 9.500300000000001
    - type: nauc_map_at_5_diff1
      value: 47.4177
    - type: nauc_map_at_10_max
      value: 43.703399999999995
    - type: nauc_map_at_10_std
      value: 10.729
    - type: nauc_map_at_10_diff1
      value: 47.4334
    - type: nauc_map_at_20_max
      value: 43.9336
    - type: nauc_map_at_20_std
      value: 11.0612
    - type: nauc_map_at_20_diff1
      value: 47.321600000000004
    - type: nauc_map_at_100_max
      value: 43.978899999999996
    - type: nauc_map_at_100_std
      value: 11.148299999999999
    - type: nauc_map_at_100_diff1
      value: 47.1738
    - type: nauc_map_at_1000_max
      value: 43.985400000000006
    - type: nauc_map_at_1000_std
      value: 11.1754
    - type: nauc_map_at_1000_diff1
      value: 47.197
    - type: nauc_recall_at_1_max
      value: 41.989900000000006
    - type: nauc_recall_at_1_std
      value: 5.3356
    - type: nauc_recall_at_1_diff1
      value: 52.711200000000005
    - type: nauc_recall_at_3_max
      value: 40.8671
    - type: nauc_recall_at_3_std
      value: 9.4511
    - type: nauc_recall_at_3_diff1
      value: 41.2041
    - type: nauc_recall_at_5_max
      value: 40.9279
    - type: nauc_recall_at_5_std
      value: 13.688600000000001
    - type: nauc_recall_at_5_diff1
      value: 41.9126
    - type: nauc_recall_at_10_max
      value: 46.1436
    - type: nauc_recall_at_10_std
      value: 20.8837
    - type: nauc_recall_at_10_diff1
      value: 41.0814
    - type: nauc_recall_at_20_max
      value: 47.245599999999996
    - type: nauc_recall_at_20_std
      value: 23.405
    - type: nauc_recall_at_20_diff1
      value: 38.864599999999996
    - type: nauc_recall_at_100_max
      value: 45.457
    - type: nauc_recall_at_100_std
      value: 28.075
    - type: nauc_recall_at_100_diff1
      value: 30.213600000000003
    - type: nauc_recall_at_1000_max
      value: 48.8291
    - type: nauc_recall_at_1000_std
      value: 47.8416
    - type: nauc_recall_at_1000_diff1
      value: 30.387199999999996
    - type: nauc_precision_at_1_max
      value: 45.7913
    - type: nauc_precision_at_1_std
      value: 10.6304
    - type: nauc_precision_at_1_diff1
      value: 51.58160000000001
    - type: nauc_precision_at_3_max
      value: 44.710899999999995
    - type: nauc_precision_at_3_std
      value: 17.7458
    - type: nauc_precision_at_3_diff1
      value: 36.7588
    - type: nauc_precision_at_5_max
      value: 44.0582
    - type: nauc_precision_at_5_std
      value: 22.7864
    - type: nauc_precision_at_5_diff1
      value: 35.3597
    - type: nauc_precision_at_10_max
      value: 45.5849
    - type: nauc_precision_at_10_std
      value: 28.758899999999997
    - type: nauc_precision_at_10_diff1
      value: 30.3452
    - type: nauc_precision_at_20_max
      value: 43.6996
    - type: nauc_precision_at_20_std
      value: 30.314799999999998
    - type: nauc_precision_at_20_diff1
      value: 25.916299999999996
    - type: nauc_precision_at_100_max
      value: 33.6976
    - type: nauc_precision_at_100_std
      value: 28.7876
    - type: nauc_precision_at_100_diff1
      value: 11.670300000000001
    - type: nauc_precision_at_1000_max
      value: 14.089599999999999
    - type: nauc_precision_at_1000_std
      value: 23.8288
    - type: nauc_precision_at_1000_diff1
      value: -1.8387
    - type: nauc_mrr_at_1_max
      value: 45.7913
    - type: nauc_mrr_at_1_std
      value: 10.6304
    - type: nauc_mrr_at_1_diff1
      value: 51.58160000000001
    - type: nauc_mrr_at_3_max
      value: 45.5677
    - type: nauc_mrr_at_3_std
      value: 12.692800000000002
    - type: nauc_mrr_at_3_diff1
      value: 46.578599999999994
    - type: nauc_mrr_at_5_max
      value: 45.4634
    - type: nauc_mrr_at_5_std
      value: 13.386999999999999
    - type: nauc_mrr_at_5_diff1
      value: 46.7306
    - type: nauc_mrr_at_10_max
      value: 46.1532
    - type: nauc_mrr_at_10_std
      value: 14.3297
    - type: nauc_mrr_at_10_diff1
      value: 46.6835
    - type: nauc_mrr_at_20_max
      value: 46.1552
    - type: nauc_mrr_at_20_std
      value: 14.492099999999999
    - type: nauc_mrr_at_20_diff1
      value: 46.611000000000004
    - type: nauc_mrr_at_100_max
      value: 46.1171
    - type: nauc_mrr_at_100_std
      value: 14.4984
    - type: nauc_mrr_at_100_diff1
      value: 46.4837
    - type: nauc_mrr_at_1000_max
      value: 46.1231
    - type: nauc_mrr_at_1000_std
      value: 14.516000000000002
    - type: nauc_mrr_at_1000_diff1
      value: 46.5135
    - type: main_score
      value: 35.477
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB CQADupstackTexRetrieval (default)
      revision: 46989137a86843e03a6195de44b09deda022eec7
      split: test
      type: mteb/cqadupstack-tex
    metrics:
    - type: ndcg_at_1
      value: 21.266
    - type: ndcg_at_3
      value: 25.337
    - type: ndcg_at_5
      value: 27.18
    - type: ndcg_at_10
      value: 29.452
    - type: ndcg_at_20
      value: 31.226
    - type: ndcg_at_100
      value: 34.409
    - type: ndcg_at_1000
      value: 37.577
    - type: map_at_1
      value: 17.363
    - type: map_at_3
      value: 22.448999999999998
    - type: map_at_5
      value: 23.686
    - type: map_at_10
      value: 24.769
    - type: map_at_20
      value: 25.295
    - type: map_at_100
      value: 25.790999999999997
    - type: map_at_1000
      value: 25.929000000000002
    - type: recall_at_1
      value: 17.363
    - type: recall_at_3
      value: 28.022000000000002
    - type: recall_at_5
      value: 32.817
    - type: recall_at_10
      value: 39.639
    - type: recall_at_20
      value: 46.245999999999995
    - type: recall_at_100
      value: 61.934
    - type: recall_at_1000
      value: 84.507
    - type: precision_at_1
      value: 21.266
    - type: precision_at_3
      value: 12.056000000000001
    - type: precision_at_5
      value: 8.727
    - type: precision_at_10
      value: 5.382
    - type: precision_at_20
      value: 3.2300000000000004
    - type: precision_at_100
      value: 0.922
    - type: precision_at_1000
      value: 0.13799999999999998
    - type: mrr_at_1
      value: 21.266299999999998
    - type: mrr_at_3
      value: 26.5887
    - type: mrr_at_5
      value: 27.7931
    - type: mrr_at_10
      value: 28.7136
    - type: mrr_at_20
      value: 29.1995
    - type: mrr_at_100
      value: 29.5953
    - type: mrr_at_1000
      value: 29.677999999999997
    - type: nauc_ndcg_at_1_max
      value: 32.1973
    - type: nauc_ndcg_at_1_std
      value: -3.8459
    - type: nauc_ndcg_at_1_diff1
      value: 40.2485
    - type: nauc_ndcg_at_3_max
      value: 31.338300000000004
    - type: nauc_ndcg_at_3_std
      value: -3.2641000000000004
    - type: nauc_ndcg_at_3_diff1
      value: 34.212199999999996
    - type: nauc_ndcg_at_5_max
      value: 30.9515
    - type: nauc_ndcg_at_5_std
      value: -2.5583
    - type: nauc_ndcg_at_5_diff1
      value: 33.3896
    - type: nauc_ndcg_at_10_max
      value: 31.1472
    - type: nauc_ndcg_at_10_std
      value: -1.4321000000000002
    - type: nauc_ndcg_at_10_diff1
      value: 33.057700000000004
    - type: nauc_ndcg_at_20_max
      value: 31.513099999999998
    - type: nauc_ndcg_at_20_std
      value: 0.4013
    - type: nauc_ndcg_at_20_diff1
      value: 32.2353
    - type: nauc_ndcg_at_100_max
      value: 31.8931
    - type: nauc_ndcg_at_100_std
      value: 2.0259
    - type: nauc_ndcg_at_100_diff1
      value: 31.966499999999996
    - type: nauc_ndcg_at_1000_max
      value: 32.1421
    - type: nauc_ndcg_at_1000_std
      value: 1.9602000000000002
    - type: nauc_ndcg_at_1000_diff1
      value: 32.6747
    - type: nauc_map_at_1_max
      value: 28.973
    - type: nauc_map_at_1_std
      value: -4.6768
    - type: nauc_map_at_1_diff1
      value: 40.726600000000005
    - type: nauc_map_at_3_max
      value: 29.9942
    - type: nauc_map_at_3_std
      value: -3.7635
    - type: nauc_map_at_3_diff1
      value: 35.5655
    - type: nauc_map_at_5_max
      value: 30.157099999999996
    - type: nauc_map_at_5_std
      value: -3.3414
    - type: nauc_map_at_5_diff1
      value: 35.085699999999996
    - type: nauc_map_at_10_max
      value: 30.4178
    - type: nauc_map_at_10_std
      value: -2.7081999999999997
    - type: nauc_map_at_10_diff1
      value: 34.834700000000005
    - type: nauc_map_at_20_max
      value: 30.5785
    - type: nauc_map_at_20_std
      value: -2.1469
    - type: nauc_map_at_20_diff1
      value: 34.6132
    - type: nauc_map_at_100_max
      value: 30.755100000000002
    - type: nauc_map_at_100_std
      value: -1.846
    - type: nauc_map_at_100_diff1
      value: 34.5596
    - type: nauc_map_at_1000_max
      value: 30.818800000000003
    - type: nauc_map_at_1000_std
      value: -1.8256000000000001
    - type: nauc_map_at_1000_diff1
      value: 34.602199999999996
    - type: nauc_recall_at_1_max
      value: 28.973
    - type: nauc_recall_at_1_std
      value: -4.6768
    - type: nauc_recall_at_1_diff1
      value: 40.726600000000005
    - type: nauc_recall_at_3_max
      value: 28.962300000000003
    - type: nauc_recall_at_3_std
      value: -2.8797
    - type: nauc_recall_at_3_diff1
      value: 29.9765
    - type: nauc_recall_at_5_max
      value: 28.193
    - type: nauc_recall_at_5_std
      value: -1.6741
    - type: nauc_recall_at_5_diff1
      value: 27.825100000000003
    - type: nauc_recall_at_10_max
      value: 28.266099999999998
    - type: nauc_recall_at_10_std
      value: 0.9544
    - type: nauc_recall_at_10_diff1
      value: 26.365499999999997
    - type: nauc_recall_at_20_max
      value: 28.839
    - type: nauc_recall_at_20_std
      value: 6.809
    - type: nauc_recall_at_20_diff1
      value: 22.761400000000002
    - type: nauc_recall_at_100_max
      value: 29.2235
    - type: nauc_recall_at_100_std
      value: 15.3679
    - type: nauc_recall_at_100_diff1
      value: 19.3302
    - type: nauc_recall_at_1000_max
      value: 27.954800000000002
    - type: nauc_recall_at_1000_std
      value: 25.5618
    - type: nauc_recall_at_1000_diff1
      value: 17.749100000000002
    - type: nauc_precision_at_1_max
      value: 32.1973
    - type: nauc_precision_at_1_std
      value: -3.8459
    - type: nauc_precision_at_1_diff1
      value: 40.2485
    - type: nauc_precision_at_3_max
      value: 33.3915
    - type: nauc_precision_at_3_std
      value: -1.7868
    - type: nauc_precision_at_3_diff1
      value: 29.0619
    - type: nauc_precision_at_5_max
      value: 33.0357
    - type: nauc_precision_at_5_std
      value: 0.7308
    - type: nauc_precision_at_5_diff1
      value: 25.966299999999997
    - type: nauc_precision_at_10_max
      value: 33.1657
    - type: nauc_precision_at_10_std
      value: 4.3635
    - type: nauc_precision_at_10_diff1
      value: 23.5546
    - type: nauc_precision_at_20_max
      value: 32.9354
    - type: nauc_precision_at_20_std
      value: 10.2754
    - type: nauc_precision_at_20_diff1
      value: 18.9755
    - type: nauc_precision_at_100_max
      value: 30.0047
    - type: nauc_precision_at_100_std
      value: 14.9007
    - type: nauc_precision_at_100_diff1
      value: 10.6748
    - type: nauc_precision_at_1000_max
      value: 24.2685
    - type: nauc_precision_at_1000_std
      value: 10.8307
    - type: nauc_precision_at_1000_diff1
      value: 1.3375
    - type: nauc_mrr_at_1_max
      value: 32.1973
    - type: nauc_mrr_at_1_std
      value: -3.8459
    - type: nauc_mrr_at_1_diff1
      value: 40.2485
    - type: nauc_mrr_at_3_max
      value: 32.670100000000005
    - type: nauc_mrr_at_3_std
      value: -2.7189
    - type: nauc_mrr_at_3_diff1
      value: 35.8073
    - type: nauc_mrr_at_5_max
      value: 32.4756
    - type: nauc_mrr_at_5_std
      value: -2.2318000000000002
    - type: nauc_mrr_at_5_diff1
      value: 35.2567
    - type: nauc_mrr_at_10_max
      value: 32.594699999999996
    - type: nauc_mrr_at_10_std
      value: -1.8573
    - type: nauc_mrr_at_10_diff1
      value: 35.268100000000004
    - type: nauc_mrr_at_20_max
      value: 32.7337
    - type: nauc_mrr_at_20_std
      value: -1.3544
    - type: nauc_mrr_at_20_diff1
      value: 35.0493
    - type: nauc_mrr_at_100_max
      value: 32.775999999999996
    - type: nauc_mrr_at_100_std
      value: -1.2326
    - type: nauc_mrr_at_100_diff1
      value: 35.0304
    - type: nauc_mrr_at_1000_max
      value: 32.7772
    - type: nauc_mrr_at_1000_std
      value: -1.2438
    - type: nauc_mrr_at_1000_diff1
      value: 35.0535
    - type: main_score
      value: 29.452
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB CQADupstackUnixRetrieval (default)
      revision: 6c6430d3a6d36f8d2a829195bc5dc94d7e063e53
      split: test
      type: mteb/cqadupstack-unix
    metrics:
    - type: ndcg_at_1
      value: 32.556000000000004
    - type: ndcg_at_3
      value: 36.928
    - type: ndcg_at_5
      value: 39.116
    - type: ndcg_at_10
      value: 41.801
    - type: ndcg_at_20
      value: 44.080999999999996
    - type: ndcg_at_100
      value: 47.138999999999996
    - type: ndcg_at_1000
      value: 49.372
    - type: map_at_1
      value: 27.062
    - type: map_at_3
      value: 33.616
    - type: map_at_5
      value: 35.181000000000004
    - type: map_at_10
      value: 36.431000000000004
    - type: map_at_20
      value: 37.15
    - type: map_at_100
      value: 37.662
    - type: map_at_1000
      value: 37.763999999999996
    - type: recall_at_1
      value: 27.062
    - type: recall_at_3
      value: 40.199
    - type: recall_at_5
      value: 46.025
    - type: recall_at_10
      value: 53.973000000000006
    - type: recall_at_20
      value: 61.989000000000004
    - type: recall_at_100
      value: 76.537
    - type: recall_at_1000
      value: 92.087
    - type: precision_at_1
      value: 32.556000000000004
    - type: precision_at_3
      value: 16.915
    - type: precision_at_5
      value: 11.791
    - type: precision_at_10
      value: 7.034
    - type: precision_at_20
      value: 4.1739999999999995
    - type: precision_at_100
      value: 1.089
    - type: precision_at_1000
      value: 0.13799999999999998
    - type: mrr_at_1
      value: 32.556000000000004
    - type: mrr_at_3
      value: 38.339600000000004
    - type: mrr_at_5
      value: 39.696799999999996
    - type: mrr_at_10
      value: 40.7987
    - type: mrr_at_20
      value: 41.3962
    - type: mrr_at_100
      value: 41.7337
    - type: mrr_at_1000
      value: 41.794399999999996
    - type: nauc_ndcg_at_1_max
      value: 43.5112
    - type: nauc_ndcg_at_1_std
      value: -9.9968
    - type: nauc_ndcg_at_1_diff1
      value: 54.4148
    - type: nauc_ndcg_at_3_max
      value: 44.4173
    - type: nauc_ndcg_at_3_std
      value: -4.9704999999999995
    - type: nauc_ndcg_at_3_diff1
      value: 49.746
    - type: nauc_ndcg_at_5_max
      value: 43.944100000000006
    - type: nauc_ndcg_at_5_std
      value: -3.8952
    - type: nauc_ndcg_at_5_diff1
      value: 48.2127
    - type: nauc_ndcg_at_10_max
      value: 43.0905
    - type: nauc_ndcg_at_10_std
      value: -3.6698
    - type: nauc_ndcg_at_10_diff1
      value: 46.8763
    - type: nauc_ndcg_at_20_max
      value: 42.6245
    - type: nauc_ndcg_at_20_std
      value: -4.1508
    - type: nauc_ndcg_at_20_diff1
      value: 46.0823
    - type: nauc_ndcg_at_100_max
      value: 42.9829
    - type: nauc_ndcg_at_100_std
      value: -3.2881
    - type: nauc_ndcg_at_100_diff1
      value: 46.9669
    - type: nauc_ndcg_at_1000_max
      value: 43.3769
    - type: nauc_ndcg_at_1000_std
      value: -2.6679
    - type: nauc_ndcg_at_1000_diff1
      value: 47.3983
    - type: nauc_map_at_1_max
      value: 41.5528
    - type: nauc_map_at_1_std
      value: -11.307599999999999
    - type: nauc_map_at_1_diff1
      value: 54.931700000000006
    - type: nauc_map_at_3_max
      value: 43.2776
    - type: nauc_map_at_3_std
      value: -7.421800000000001
    - type: nauc_map_at_3_diff1
      value: 51.1883
    - type: nauc_map_at_5_max
      value: 43.4821
    - type: nauc_map_at_5_std
      value: -6.2339
    - type: nauc_map_at_5_diff1
      value: 50.1494
    - type: nauc_map_at_10_max
      value: 43.3333
    - type: nauc_map_at_10_std
      value: -6.065
    - type: nauc_map_at_10_diff1
      value: 49.661100000000005
    - type: nauc_map_at_20_max
      value: 43.231
    - type: nauc_map_at_20_std
      value: -6.2244
    - type: nauc_map_at_20_diff1
      value: 49.407000000000004
    - type: nauc_map_at_100_max
      value: 43.3803
    - type: nauc_map_at_100_std
      value: -5.9752
    - type: nauc_map_at_100_diff1
      value: 49.5411
    - type: nauc_map_at_1000_max
      value: 43.4007
    - type: nauc_map_at_1000_std
      value: -5.9336
    - type: nauc_map_at_1000_diff1
      value: 49.5578
    - type: nauc_recall_at_1_max
      value: 41.5528
    - type: nauc_recall_at_1_std
      value: -11.307599999999999
    - type: nauc_recall_at_1_diff1
      value: 54.931700000000006
    - type: nauc_recall_at_3_max
      value: 42.6893
    - type: nauc_recall_at_3_std
      value: -2.3828
    - type: nauc_recall_at_3_diff1
      value: 46.050999999999995
    - type: nauc_recall_at_5_max
      value: 41.6989
    - type: nauc_recall_at_5_std
      value: 1.0116
    - type: nauc_recall_at_5_diff1
      value: 41.5014
    - type: nauc_recall_at_10_max
      value: 37.9823
    - type: nauc_recall_at_10_std
      value: 1.9809
    - type: nauc_recall_at_10_diff1
      value: 36.3968
    - type: nauc_recall_at_20_max
      value: 35.5843
    - type: nauc_recall_at_20_std
      value: 0.1044
    - type: nauc_recall_at_20_diff1
      value: 32.377
    - type: nauc_recall_at_100_max
      value: 35.316900000000004
    - type: nauc_recall_at_100_std
      value: 5.6158
    - type: nauc_recall_at_100_diff1
      value: 34.8474
    - type: nauc_recall_at_1000_max
      value: 40.3589
    - type: nauc_recall_at_1000_std
      value: 36.2315
    - type: nauc_recall_at_1000_diff1
      value: 32.7652
    - type: nauc_precision_at_1_max
      value: 43.5112
    - type: nauc_precision_at_1_std
      value: -9.9968
    - type: nauc_precision_at_1_diff1
      value: 54.4148
    - type: nauc_precision_at_3_max
      value: 43.5357
    - type: nauc_precision_at_3_std
      value: 1.8129
    - type: nauc_precision_at_3_diff1
      value: 39.4033
    - type: nauc_precision_at_5_max
      value: 41.2383
    - type: nauc_precision_at_5_std
      value: 5.952500000000001
    - type: nauc_precision_at_5_diff1
      value: 32.6387
    - type: nauc_precision_at_10_max
      value: 35.8673
    - type: nauc_precision_at_10_std
      value: 6.9601
    - type: nauc_precision_at_10_diff1
      value: 25.1842
    - type: nauc_precision_at_20_max
      value: 28.9362
    - type: nauc_precision_at_20_std
      value: 7.607800000000001
    - type: nauc_precision_at_20_diff1
      value: 16.7232
    - type: nauc_precision_at_100_max
      value: 18.434800000000003
    - type: nauc_precision_at_100_std
      value: 12.987000000000002
    - type: nauc_precision_at_100_diff1
      value: 6.9893
    - type: nauc_precision_at_1000_max
      value: 1.0569
    - type: nauc_precision_at_1000_std
      value: 12.5503
    - type: nauc_precision_at_1000_diff1
      value: -7.3416
    - type: nauc_mrr_at_1_max
      value: 43.5112
    - type: nauc_mrr_at_1_std
      value: -9.9968
    - type: nauc_mrr_at_1_diff1
      value: 54.4148
    - type: nauc_mrr_at_3_max
      value: 44.642900000000004
    - type: nauc_mrr_at_3_std
      value: -5.3517
    - type: nauc_mrr_at_3_diff1
      value: 50.2935
    - type: nauc_mrr_at_5_max
      value: 44.4732
    - type: nauc_mrr_at_5_std
      value: -4.608099999999999
    - type: nauc_mrr_at_5_diff1
      value: 49.346000000000004
    - type: nauc_mrr_at_10_max
      value: 43.9489
    - type: nauc_mrr_at_10_std
      value: -4.5868
    - type: nauc_mrr_at_10_diff1
      value: 48.7018
    - type: nauc_mrr_at_20_max
      value: 43.7826
    - type: nauc_mrr_at_20_std
      value: -4.8502
    - type: nauc_mrr_at_20_diff1
      value: 48.5755
    - type: nauc_mrr_at_100_max
      value: 43.7991
    - type: nauc_mrr_at_100_std
      value: -4.8094
    - type: nauc_mrr_at_100_diff1
      value: 48.7361
    - type: nauc_mrr_at_1000_max
      value: 43.8348
    - type: nauc_mrr_at_1000_std
      value: -4.7897
    - type: nauc_mrr_at_1000_diff1
      value: 48.7638
    - type: main_score
      value: 41.801
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB CQADupstackWebmastersRetrieval (default)
      revision: 160c094312a0e1facb97e55eeddb698c0abe3571
      split: test
      type: mteb/cqadupstack-webmasters
    metrics:
    - type: ndcg_at_1
      value: 30.631999999999998
    - type: ndcg_at_3
      value: 34.528999999999996
    - type: ndcg_at_5
      value: 36.547000000000004
    - type: ndcg_at_10
      value: 40.105000000000004
    - type: ndcg_at_20
      value: 42.34
    - type: ndcg_at_100
      value: 45.712
    - type: ndcg_at_1000
      value: 48.314
    - type: map_at_1
      value: 25.19
    - type: map_at_3
      value: 30.656
    - type: map_at_5
      value: 32.161
    - type: map_at_10
      value: 33.928000000000004
    - type: map_at_20
      value: 34.782999999999994
    - type: map_at_100
      value: 35.493
    - type: map_at_1000
      value: 35.713
    - type: recall_at_1
      value: 25.19
    - type: recall_at_3
      value: 36.007
    - type: recall_at_5
      value: 41.772
    - type: recall_at_10
      value: 52.117999999999995
    - type: recall_at_20
      value: 60.458
    - type: recall_at_100
      value: 77.34400000000001
    - type: recall_at_1000
      value: 93.77
    - type: precision_at_1
      value: 30.631999999999998
    - type: precision_at_3
      value: 15.942
    - type: precision_at_5
      value: 11.462
    - type: precision_at_10
      value: 7.826
    - type: precision_at_20
      value: 4.9799999999999995
    - type: precision_at_100
      value: 1.528
    - type: precision_at_1000
      value: 0.242
    - type: mrr_at_1
      value: 30.632399999999997
    - type: mrr_at_3
      value: 35.8037
    - type: mrr_at_5
      value: 37.2661
    - type: mrr_at_10
      value: 38.8381
    - type: mrr_at_20
      value: 39.4229
    - type: mrr_at_100
      value: 39.7673
    - type: mrr_at_1000
      value: 39.8227
    - type: nauc_ndcg_at_1_max
      value: 45.7418
    - type: nauc_ndcg_at_1_std
      value: 7.7497
    - type: nauc_ndcg_at_1_diff1
      value: 47.656
    - type: nauc_ndcg_at_3_max
      value: 45.6597
    - type: nauc_ndcg_at_3_std
      value: 9.6418
    - type: nauc_ndcg_at_3_diff1
      value: 43.1631
    - type: nauc_ndcg_at_5_max
      value: 44.893100000000004
    - type: nauc_ndcg_at_5_std
      value: 12.2393
    - type: nauc_ndcg_at_5_diff1
      value: 42.7159
    - type: nauc_ndcg_at_10_max
      value: 43.6388
    - type: nauc_ndcg_at_10_std
      value: 12.0574
    - type: nauc_ndcg_at_10_diff1
      value: 41.4018
    - type: nauc_ndcg_at_20_max
      value: 43.8549
    - type: nauc_ndcg_at_20_std
      value: 14.065900000000001
    - type: nauc_ndcg_at_20_diff1
      value: 41.056
    - type: nauc_ndcg_at_100_max
      value: 44.770700000000005
    - type: nauc_ndcg_at_100_std
      value: 14.8343
    - type: nauc_ndcg_at_100_diff1
      value: 42.2405
    - type: nauc_ndcg_at_1000_max
      value: 45.524100000000004
    - type: nauc_ndcg_at_1000_std
      value: 14.578199999999999
    - type: nauc_ndcg_at_1000_diff1
      value: 42.3126
    - type: nauc_map_at_1_max
      value: 44.1517
    - type: nauc_map_at_1_std
      value: 3.4579
    - type: nauc_map_at_1_diff1
      value: 53.915
    - type: nauc_map_at_3_max
      value: 45.8324
    - type: nauc_map_at_3_std
      value: 6.8385
    - type: nauc_map_at_3_diff1
      value: 47.8444
    - type: nauc_map_at_5_max
      value: 45.4063
    - type: nauc_map_at_5_std
      value: 8.3539
    - type: nauc_map_at_5_diff1
      value: 47.0671
    - type: nauc_map_at_10_max
      value: 45.0727
    - type: nauc_map_at_10_std
      value: 8.6699
    - type: nauc_map_at_10_diff1
      value: 46.050200000000004
    - type: nauc_map_at_20_max
      value: 45.2504
    - type: nauc_map_at_20_std
      value: 9.7359
    - type: nauc_map_at_20_diff1
      value: 45.711200000000005
    - type: nauc_map_at_100_max
      value: 45.2055
    - type: nauc_map_at_100_std
      value: 10.2755
    - type: nauc_map_at_100_diff1
      value: 45.5556
    - type: nauc_map_at_1000_max
      value: 45.1304
    - type: nauc_map_at_1000_std
      value: 10.3956
    - type: nauc_map_at_1000_diff1
      value: 45.4084
    - type: nauc_recall_at_1_max
      value: 44.1517
    - type: nauc_recall_at_1_std
      value: 3.4579
    - type: nauc_recall_at_1_diff1
      value: 53.915
    - type: nauc_recall_at_3_max
      value: 44.349199999999996
    - type: nauc_recall_at_3_std
      value: 9.464599999999999
    - type: nauc_recall_at_3_diff1
      value: 41.302499999999995
    - type: nauc_recall_at_5_max
      value: 42.2726
    - type: nauc_recall_at_5_std
      value: 14.7778
    - type: nauc_recall_at_5_diff1
      value: 38.1663
    - type: nauc_recall_at_10_max
      value: 37.0689
    - type: nauc_recall_at_10_std
      value: 14.760699999999998
    - type: nauc_recall_at_10_diff1
      value: 32.1674
    - type: nauc_recall_at_20_max
      value: 36.1879
    - type: nauc_recall_at_20_std
      value: 22.6902
    - type: nauc_recall_at_20_diff1
      value: 28.933999999999997
    - type: nauc_recall_at_100_max
      value: 38.5222
    - type: nauc_recall_at_100_std
      value: 31.595299999999998
    - type: nauc_recall_at_100_diff1
      value: 30.495499999999996
    - type: nauc_recall_at_1000_max
      value: 59.5012
    - type: nauc_recall_at_1000_std
      value: 61.421499999999995
    - type: nauc_recall_at_1000_diff1
      value: 30.153000000000002
    - type: nauc_precision_at_1_max
      value: 45.7418
    - type: nauc_precision_at_1_std
      value: 7.7497
    - type: nauc_precision_at_1_diff1
      value: 47.656
    - type: nauc_precision_at_3_max
      value: 41.5197
    - type: nauc_precision_at_3_std
      value: 14.416200000000002
    - type: nauc_precision_at_3_diff1
      value: 27.4448
    - type: nauc_precision_at_5_max
      value: 37.372699999999995
    - type: nauc_precision_at_5_std
      value: 20.4825
    - type: nauc_precision_at_5_diff1
      value: 20.4335
    - type: nauc_precision_at_10_max
      value: 26.792899999999996
    - type: nauc_precision_at_10_std
      value: 20.895
    - type: nauc_precision_at_10_diff1
      value: 6.9729
    - type: nauc_precision_at_20_max
      value: 19.3562
    - type: nauc_precision_at_20_std
      value: 26.9338
    - type: nauc_precision_at_20_diff1
      value: -2.5024
    - type: nauc_precision_at_100_max
      value: 2.6254
    - type: nauc_precision_at_100_std
      value: 24.4194
    - type: nauc_precision_at_100_diff1
      value: -14.6956
    - type: nauc_precision_at_1000_max
      value: -7.0939000000000005
    - type: nauc_precision_at_1000_std
      value: 17.2116
    - type: nauc_precision_at_1000_diff1
      value: -23.3519
    - type: nauc_mrr_at_1_max
      value: 45.7418
    - type: nauc_mrr_at_1_std
      value: 7.7497
    - type: nauc_mrr_at_1_diff1
      value: 47.656
    - type: nauc_mrr_at_3_max
      value: 44.974799999999995
    - type: nauc_mrr_at_3_std
      value: 10.0484
    - type: nauc_mrr_at_3_diff1
      value: 42.5053
    - type: nauc_mrr_at_5_max
      value: 45.0004
    - type: nauc_mrr_at_5_std
      value: 11.505700000000001
    - type: nauc_mrr_at_5_diff1
      value: 42.0568
    - type: nauc_mrr_at_10_max
      value: 44.5236
    - type: nauc_mrr_at_10_std
      value: 11.6009
    - type: nauc_mrr_at_10_diff1
      value: 41.5394
    - type: nauc_mrr_at_20_max
      value: 44.568400000000004
    - type: nauc_mrr_at_20_std
      value: 11.9612
    - type: nauc_mrr_at_20_diff1
      value: 41.4954
    - type: nauc_mrr_at_100_max
      value: 44.6377
    - type: nauc_mrr_at_100_std
      value: 12.0293
    - type: nauc_mrr_at_100_diff1
      value: 41.6504
    - type: nauc_mrr_at_1000_max
      value: 44.650099999999995
    - type: nauc_mrr_at_1000_std
      value: 12.0106
    - type: nauc_mrr_at_1000_diff1
      value: 41.6595
    - type: main_score
      value: 40.105000000000004
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB CQADupstackWordpressRetrieval (default)
      revision: 4ffe81d471b1924886b33c7567bfb200e9eec5c4
      split: test
      type: mteb/cqadupstack-wordpress
    metrics:
    - type: ndcg_at_1
      value: 21.811
    - type: ndcg_at_3
      value: 27.472
    - type: ndcg_at_5
      value: 29.755
    - type: ndcg_at_10
      value: 32.561
    - type: ndcg_at_20
      value: 34.708
    - type: ndcg_at_100
      value: 38.052
    - type: ndcg_at_1000
      value: 40.526
    - type: map_at_1
      value: 20.339
    - type: map_at_3
      value: 25.358000000000004
    - type: map_at_5
      value: 26.682
    - type: map_at_10
      value: 27.935
    - type: map_at_20
      value: 28.536
    - type: map_at_100
      value: 29.038000000000004
    - type: map_at_1000
      value: 29.149
    - type: recall_at_1
      value: 20.339
    - type: recall_at_3
      value: 31.682
    - type: recall_at_5
      value: 36.962
    - type: recall_at_10
      value: 45.095
    - type: recall_at_20
      value: 53.25
    - type: recall_at_100
      value: 70.155
    - type: recall_at_1000
      value: 88.177
    - type: precision_at_1
      value: 21.811
    - type: precision_at_3
      value: 11.706999999999999
    - type: precision_at_5
      value: 8.429
    - type: precision_at_10
      value: 5.25
    - type: precision_at_20
      value: 3.1419999999999995
    - type: precision_at_100
      value: 0.8540000000000001
    - type: precision_at_1000
      value: 0.117
    - type: mrr_at_1
      value: 21.8115
    - type: mrr_at_3
      value: 27.1411
    - type: mrr_at_5
      value: 28.490399999999998
    - type: mrr_at_10
      value: 29.616500000000002
    - type: mrr_at_20
      value: 30.215999999999998
    - type: mrr_at_100
      value: 30.6966
    - type: mrr_at_1000
      value: 30.767899999999997
    - type: nauc_ndcg_at_1_max
      value: 32.8162
    - type: nauc_ndcg_at_1_std
      value: -4.388199999999999
    - type: nauc_ndcg_at_1_diff1
      value: 44.436
    - type: nauc_ndcg_at_3_max
      value: 28.517
    - type: nauc_ndcg_at_3_std
      value: -4.3836
    - type: nauc_ndcg_at_3_diff1
      value: 35.7606
    - type: nauc_ndcg_at_5_max
      value: 28.68
    - type: nauc_ndcg_at_5_std
      value: -3.0216
    - type: nauc_ndcg_at_5_diff1
      value: 35.27
    - type: nauc_ndcg_at_10_max
      value: 26.572200000000002
    - type: nauc_ndcg_at_10_std
      value: -3.8319
    - type: nauc_ndcg_at_10_diff1
      value: 33.311099999999996
    - type: nauc_ndcg_at_20_max
      value: 26.7196
    - type: nauc_ndcg_at_20_std
      value: -1.3162
    - type: nauc_ndcg_at_20_diff1
      value: 32.202999999999996
    - type: nauc_ndcg_at_100_max
      value: 28.8134
    - type: nauc_ndcg_at_100_std
      value: -0.2386
    - type: nauc_ndcg_at_100_diff1
      value: 31.5089
    - type: nauc_ndcg_at_1000_max
      value: 28.732799999999997
    - type: nauc_ndcg_at_1000_std
      value: 0.6251
    - type: nauc_ndcg_at_1000_diff1
      value: 32.1837
    - type: nauc_map_at_1_max
      value: 29.4829
    - type: nauc_map_at_1_std
      value: -6.0044
    - type: nauc_map_at_1_diff1
      value: 43.3353
    - type: nauc_map_at_3_max
      value: 28.230499999999996
    - type: nauc_map_at_3_std
      value: -5.0899
    - type: nauc_map_at_3_diff1
      value: 37.3547
    - type: nauc_map_at_5_max
      value: 28.7927
    - type: nauc_map_at_5_std
      value: -4.254899999999999
    - type: nauc_map_at_5_diff1
      value: 37.1805
    - type: nauc_map_at_10_max
      value: 28.1557
    - type: nauc_map_at_10_std
      value: -4.4931
    - type: nauc_map_at_10_diff1
      value: 36.2513
    - type: nauc_map_at_20_max
      value: 28.205799999999996
    - type: nauc_map_at_20_std
      value: -3.6852000000000005
    - type: nauc_map_at_20_diff1
      value: 35.9099
    - type: nauc_map_at_100_max
      value: 28.604499999999998
    - type: nauc_map_at_100_std
      value: -3.4775
    - type: nauc_map_at_100_diff1
      value: 35.802
    - type: nauc_map_at_1000_max
      value: 28.6008
    - type: nauc_map_at_1000_std
      value: -3.4255
    - type: nauc_map_at_1000_diff1
      value: 35.8238
    - type: nauc_recall_at_1_max
      value: 29.4829
    - type: nauc_recall_at_1_std
      value: -6.0044
    - type: nauc_recall_at_1_diff1
      value: 43.3353
    - type: nauc_recall_at_3_max
      value: 25.4695
    - type: nauc_recall_at_3_std
      value: -4.3068
    - type: nauc_recall_at_3_diff1
      value: 30.2776
    - type: nauc_recall_at_5_max
      value: 25.901400000000002
    - type: nauc_recall_at_5_std
      value: -1.4424
    - type: nauc_recall_at_5_diff1
      value: 29.3842
    - type: nauc_recall_at_10_max
      value: 19.203200000000002
    - type: nauc_recall_at_10_std
      value: -3.8822
    - type: nauc_recall_at_10_diff1
      value: 24.0215
    - type: nauc_recall_at_20_max
      value: 18.9758
    - type: nauc_recall_at_20_std
      value: 4.9965
    - type: nauc_recall_at_20_diff1
      value: 19.5423
    - type: nauc_recall_at_100_max
      value: 27.7916
    - type: nauc_recall_at_100_std
      value: 13.4764
    - type: nauc_recall_at_100_diff1
      value: 11.1211
    - type: nauc_recall_at_1000_max
      value: 28.3949
    - type: nauc_recall_at_1000_std
      value: 41.7299
    - type: nauc_recall_at_1000_diff1
      value: 4.0583
    - type: nauc_precision_at_1_max
      value: 32.8162
    - type: nauc_precision_at_1_std
      value: -4.388199999999999
    - type: nauc_precision_at_1_diff1
      value: 44.436
    - type: nauc_precision_at_3_max
      value: 28.614
    - type: nauc_precision_at_3_std
      value: -1.5110000000000001
    - type: nauc_precision_at_3_diff1
      value: 30.165
    - type: nauc_precision_at_5_max
      value: 29.49
    - type: nauc_precision_at_5_std
      value: 3.3188000000000004
    - type: nauc_precision_at_5_diff1
      value: 27.6501
    - type: nauc_precision_at_10_max
      value: 24.334500000000002
    - type: nauc_precision_at_10_std
      value: 3.4701000000000004
    - type: nauc_precision_at_10_diff1
      value: 20.4126
    - type: nauc_precision_at_20_max
      value: 23.4494
    - type: nauc_precision_at_20_std
      value: 14.380799999999999
    - type: nauc_precision_at_20_diff1
      value: 12.5855
    - type: nauc_precision_at_100_max
      value: 25.5811
    - type: nauc_precision_at_100_std
      value: 21.0337
    - type: nauc_precision_at_100_diff1
      value: 0.1621
    - type: nauc_precision_at_1000_max
      value: 1.3693
    - type: nauc_precision_at_1000_std
      value: 22.288
    - type: nauc_precision_at_1000_diff1
      value: -18.3564
    - type: nauc_mrr_at_1_max
      value: 32.8162
    - type: nauc_mrr_at_1_std
      value: -4.388199999999999
    - type: nauc_mrr_at_1_diff1
      value: 44.436
    - type: nauc_mrr_at_3_max
      value: 31.5259
    - type: nauc_mrr_at_3_std
      value: -3.6585
    - type: nauc_mrr_at_3_diff1
      value: 38.5309
    - type: nauc_mrr_at_5_max
      value: 31.1784
    - type: nauc_mrr_at_5_std
      value: -2.5462
    - type: nauc_mrr_at_5_diff1
      value: 37.9675
    - type: nauc_mrr_at_10_max
      value: 30.0497
    - type: nauc_mrr_at_10_std
      value: -3.0947999999999998
    - type: nauc_mrr_at_10_diff1
      value: 37.0458
    - type: nauc_mrr_at_20_max
      value: 30.082900000000002
    - type: nauc_mrr_at_20_std
      value: -2.6054
    - type: nauc_mrr_at_20_diff1
      value: 36.774499999999996
    - type: nauc_mrr_at_100_max
      value: 30.424200000000003
    - type: nauc_mrr_at_100_std
      value: -2.5341
    - type: nauc_mrr_at_100_diff1
      value: 36.7384
    - type: nauc_mrr_at_1000_max
      value: 30.4217
    - type: nauc_mrr_at_1000_std
      value: -2.4978
    - type: nauc_mrr_at_1000_diff1
      value: 36.7847
    - type: main_score
      value: 32.561
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB ClimateFEVER (default)
      revision: 47f2ac6acb640fc46020b02a5b59fdda04d39380
      split: test
      type: mteb/climate-fever
    metrics:
    - type: ndcg_at_1
      value: 23.388
    - type: ndcg_at_3
      value: 20.198
    - type: ndcg_at_5
      value: 21.959
    - type: ndcg_at_10
      value: 24.97
    - type: ndcg_at_20
      value: 27.26
    - type: ndcg_at_100
      value: 31.244
    - type: ndcg_at_1000
      value: 34.694
    - type: map_at_1
      value: 10.738
    - type: map_at_3
      value: 14.707
    - type: map_at_5
      value: 16.123
    - type: map_at_10
      value: 17.45
    - type: map_at_20
      value: 18.251
    - type: map_at_100
      value: 18.979
    - type: map_at_1000
      value: 19.154
    - type: recall_at_1
      value: 10.738
    - type: recall_at_3
      value: 18.590999999999998
    - type: recall_at_5
      value: 23.427
    - type: recall_at_10
      value: 30.144
    - type: recall_at_20
      value: 36.586999999999996
    - type: recall_at_100
      value: 51.757
    - type: recall_at_1000
      value: 71.353
    - type: precision_at_1
      value: 23.388
    - type: precision_at_3
      value: 14.527999999999999
    - type: precision_at_5
      value: 11.375
    - type: precision_at_10
      value: 7.674
    - type: precision_at_20
      value: 4.824
    - type: precision_at_100
      value: 1.4460000000000002
    - type: precision_at_1000
      value: 0.208
    - type: mrr_at_1
      value: 23.3876
    - type: mrr_at_3
      value: 30.640600000000003
    - type: mrr_at_5
      value: 32.7416
    - type: mrr_at_10
      value: 34.2082
    - type: mrr_at_20
      value: 34.696
    - type: mrr_at_100
      value: 35.0613
    - type: mrr_at_1000
      value: 35.1158
    - type: nauc_ndcg_at_1_max
      value: 34.0809
    - type: nauc_ndcg_at_1_std
      value: 11.4587
    - type: nauc_ndcg_at_1_diff1
      value: 24.7702
    - type: nauc_ndcg_at_3_max
      value: 36.7061
    - type: nauc_ndcg_at_3_std
      value: 15.8194
    - type: nauc_ndcg_at_3_diff1
      value: 22.0991
    - type: nauc_ndcg_at_5_max
      value: 40.0278
    - type: nauc_ndcg_at_5_std
      value: 19.442
    - type: nauc_ndcg_at_5_diff1
      value: 22.0353
    - type: nauc_ndcg_at_10_max
      value: 41.8522
    - type: nauc_ndcg_at_10_std
      value: 22.2665
    - type: nauc_ndcg_at_10_diff1
      value: 21.9219
    - type: nauc_ndcg_at_20_max
      value: 42.111599999999996
    - type: nauc_ndcg_at_20_std
      value: 24.7003
    - type: nauc_ndcg_at_20_diff1
      value: 21.1493
    - type: nauc_ndcg_at_100_max
      value: 41.4285
    - type: nauc_ndcg_at_100_std
      value: 26.8766
    - type: nauc_ndcg_at_100_diff1
      value: 20.658
    - type: nauc_ndcg_at_1000_max
      value: 41.7107
    - type: nauc_ndcg_at_1000_std
      value: 27.8879
    - type: nauc_ndcg_at_1000_diff1
      value: 20.249
    - type: nauc_map_at_1_max
      value: 39.0907
    - type: nauc_map_at_1_std
      value: 10.9155
    - type: nauc_map_at_1_diff1
      value: 27.478799999999996
    - type: nauc_map_at_3_max
      value: 39.1964
    - type: nauc_map_at_3_std
      value: 14.1844
    - type: nauc_map_at_3_diff1
      value: 24.5869
    - type: nauc_map_at_5_max
      value: 40.8907
    - type: nauc_map_at_5_std
      value: 16.6955
    - type: nauc_map_at_5_diff1
      value: 24.1453
    - type: nauc_map_at_10_max
      value: 41.8968
    - type: nauc_map_at_10_std
      value: 18.4835
    - type: nauc_map_at_10_diff1
      value: 24.0071
    - type: nauc_map_at_20_max
      value: 42.1779
    - type: nauc_map_at_20_std
      value: 19.831599999999998
    - type: nauc_map_at_20_diff1
      value: 23.6712
    - type: nauc_map_at_100_max
      value: 42.0617
    - type: nauc_map_at_100_std
      value: 20.524700000000003
    - type: nauc_map_at_100_diff1
      value: 23.5193
    - type: nauc_map_at_1000_max
      value: 42.080400000000004
    - type: nauc_map_at_1000_std
      value: 20.6099
    - type: nauc_map_at_1000_diff1
      value: 23.48
    - type: nauc_recall_at_1_max
      value: 39.0907
    - type: nauc_recall_at_1_std
      value: 10.9155
    - type: nauc_recall_at_1_diff1
      value: 27.478799999999996
    - type: nauc_recall_at_3_max
      value: 36.479099999999995
    - type: nauc_recall_at_3_std
      value: 16.370199999999997
    - type: nauc_recall_at_3_diff1
      value: 21.0061
    - type: nauc_recall_at_5_max
      value: 39.3227
    - type: nauc_recall_at_5_std
      value: 21.753800000000002
    - type: nauc_recall_at_5_diff1
      value: 18.6069
    - type: nauc_recall_at_10_max
      value: 40.7894
    - type: nauc_recall_at_10_std
      value: 25.6917
    - type: nauc_recall_at_10_diff1
      value: 17.7339
    - type: nauc_recall_at_20_max
      value: 39.6829
    - type: nauc_recall_at_20_std
      value: 30.0384
    - type: nauc_recall_at_20_diff1
      value: 15.3931
    - type: nauc_recall_at_100_max
      value: 34.9178
    - type: nauc_recall_at_100_std
      value: 34.6884
    - type: nauc_recall_at_100_diff1
      value: 13.1482
    - type: nauc_recall_at_1000_max
      value: 34.3804
    - type: nauc_recall_at_1000_std
      value: 41.778
    - type: nauc_recall_at_1000_diff1
      value: 9.3052
    - type: nauc_precision_at_1_max
      value: 34.0809
    - type: nauc_precision_at_1_std
      value: 11.4587
    - type: nauc_precision_at_1_diff1
      value: 24.7702
    - type: nauc_precision_at_3_max
      value: 31.784000000000002
    - type: nauc_precision_at_3_std
      value: 18.567700000000002
    - type: nauc_precision_at_3_diff1
      value: 16.1653
    - type: nauc_precision_at_5_max
      value: 34.9086
    - type: nauc_precision_at_5_std
      value: 25.0212
    - type: nauc_precision_at_5_diff1
      value: 14.2787
    - type: nauc_precision_at_10_max
      value: 35.1734
    - type: nauc_precision_at_10_std
      value: 30.2243
    - type: nauc_precision_at_10_diff1
      value: 11.4396
    - type: nauc_precision_at_20_max
      value: 31.347599999999996
    - type: nauc_precision_at_20_std
      value: 33.2444
    - type: nauc_precision_at_20_diff1
      value: 8.0151
    - type: nauc_precision_at_100_max
      value: 21.0705
    - type: nauc_precision_at_100_std
      value: 33.561800000000005
    - type: nauc_precision_at_100_diff1
      value: 3.1647000000000003
    - type: nauc_precision_at_1000_max
      value: 10.1267
    - type: nauc_precision_at_1000_std
      value: 28.746199999999998
    - type: nauc_precision_at_1000_diff1
      value: -4.6774000000000004
    - type: nauc_mrr_at_1_max
      value: 34.0809
    - type: nauc_mrr_at_1_std
      value: 11.4587
    - type: nauc_mrr_at_1_diff1
      value: 24.7702
    - type: nauc_mrr_at_3_max
      value: 33.799
    - type: nauc_mrr_at_3_std
      value: 16.0923
    - type: nauc_mrr_at_3_diff1
      value: 20.8456
    - type: nauc_mrr_at_5_max
      value: 35.1249
    - type: nauc_mrr_at_5_std
      value: 17.8145
    - type: nauc_mrr_at_5_diff1
      value: 20.467299999999998
    - type: nauc_mrr_at_10_max
      value: 35.856500000000004
    - type: nauc_mrr_at_10_std
      value: 18.4864
    - type: nauc_mrr_at_10_diff1
      value: 20.6532
    - type: nauc_mrr_at_20_max
      value: 35.787200000000006
    - type: nauc_mrr_at_20_std
      value: 18.607599999999998
    - type: nauc_mrr_at_20_diff1
      value: 20.6192
    - type: nauc_mrr_at_100_max
      value: 35.7134
    - type: nauc_mrr_at_100_std
      value: 18.5964
    - type: nauc_mrr_at_100_diff1
      value: 20.5979
    - type: nauc_mrr_at_1000_max
      value: 35.713499999999996
    - type: nauc_mrr_at_1000_std
      value: 18.5792
    - type: nauc_mrr_at_1000_diff1
      value: 20.610300000000002
    - type: main_score
      value: 24.97
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB CodeFeedbackMT (default)
      revision: b0f12fa0c0dd67f59c95a5c33d02aeeb4c398c5f
      split: test
      type: CoIR-Retrieval/codefeedback-mt
    metrics:
    - type: ndcg_at_1
      value: 15.403
    - type: ndcg_at_3
      value: 20.087
    - type: ndcg_at_5
      value: 21.72
    - type: ndcg_at_10
      value: 23.458000000000002
    - type: ndcg_at_20
      value: 24.990000000000002
    - type: ndcg_at_100
      value: 27.933000000000003
    - type: ndcg_at_1000
      value: 30.642999999999997
    - type: map_at_1
      value: 15.403
    - type: map_at_3
      value: 18.925
    - type: map_at_5
      value: 19.832
    - type: map_at_10
      value: 20.549999999999997
    - type: map_at_20
      value: 20.97
    - type: map_at_100
      value: 21.358
    - type: map_at_1000
      value: 21.447
    - type: recall_at_1
      value: 15.403
    - type: recall_at_3
      value: 23.454
    - type: recall_at_5
      value: 27.416
    - type: recall_at_10
      value: 32.786
    - type: recall_at_20
      value: 38.849000000000004
    - type: recall_at_100
      value: 54.99699999999999
    - type: recall_at_1000
      value: 77.096
    - type: precision_at_1
      value: 15.403
    - type: precision_at_3
      value: 7.818
    - type: precision_at_5
      value: 5.483
    - type: precision_at_10
      value: 3.279
    - type: precision_at_20
      value: 1.942
    - type: precision_at_100
      value: 0.5499999999999999
    - type: precision_at_1000
      value: 0.077
    - type: mrr_at_1
      value: 15.4026
    - type: mrr_at_3
      value: 18.925
    - type: mrr_at_5
      value: 19.8322
    - type: mrr_at_10
      value: 20.5497
    - type: mrr_at_20
      value: 20.9696
    - type: mrr_at_100
      value: 21.3582
    - type: mrr_at_1000
      value: 21.4471
    - type: nauc_ndcg_at_1_max
      value: 14.524799999999999
    - type: nauc_ndcg_at_1_std
      value: -14.704500000000001
    - type: nauc_ndcg_at_1_diff1
      value: 45.3337
    - type: nauc_ndcg_at_3_max
      value: 12.3014
    - type: nauc_ndcg_at_3_std
      value: -14.977199999999998
    - type: nauc_ndcg_at_3_diff1
      value: 37.6118
    - type: nauc_ndcg_at_5_max
      value: 12.015099999999999
    - type: nauc_ndcg_at_5_std
      value: -14.844399999999998
    - type: nauc_ndcg_at_5_diff1
      value: 36.439
    - type: nauc_ndcg_at_10_max
      value: 11.886800000000001
    - type: nauc_ndcg_at_10_std
      value: -14.274600000000001
    - type: nauc_ndcg_at_10_diff1
      value: 35.0552
    - type: nauc_ndcg_at_20_max
      value: 11.843
    - type: nauc_ndcg_at_20_std
      value: -13.729099999999999
    - type: nauc_ndcg_at_20_diff1
      value: 34.172999999999995
    - type: nauc_ndcg_at_100_max
      value: 12.570700000000002
    - type: nauc_ndcg_at_100_std
      value: -11.956999999999999
    - type: nauc_ndcg_at_100_diff1
      value: 33.5916
    - type: nauc_ndcg_at_1000_max
      value: 13.3025
    - type: nauc_ndcg_at_1000_std
      value: -10.6411
    - type: nauc_ndcg_at_1000_diff1
      value: 33.535900000000005
    - type: nauc_map_at_1_max
      value: 14.524799999999999
    - type: nauc_map_at_1_std
      value: -14.704500000000001
    - type: nauc_map_at_1_diff1
      value: 45.3337
    - type: nauc_map_at_3_max
      value: 12.7833
    - type: nauc_map_at_3_std
      value: -14.9312
    - type: nauc_map_at_3_diff1
      value: 39.2273
    - type: nauc_map_at_5_max
      value: 12.606200000000001
    - type: nauc_map_at_5_std
      value: -14.846200000000001
    - type: nauc_map_at_5_diff1
      value: 38.5015
    - type: nauc_map_at_10_max
      value: 12.5202
    - type: nauc_map_at_10_std
      value: -14.5979
    - type: nauc_map_at_10_diff1
      value: 37.8521
    - type: nauc_map_at_20_max
      value: 12.5101
    - type: nauc_map_at_20_std
      value: -14.444899999999999
    - type: nauc_map_at_20_diff1
      value: 37.5942
    - type: nauc_map_at_100_max
      value: 12.601399999999998
    - type: nauc_map_at_100_std
      value: -14.2092
    - type: nauc_map_at_100_diff1
      value: 37.4992
    - type: nauc_map_at_1000_max
      value: 12.6334
    - type: nauc_map_at_1000_std
      value: -14.1545
    - type: nauc_map_at_1000_diff1
      value: 37.4959
    - type: nauc_recall_at_1_max
      value: 14.524799999999999
    - type: nauc_recall_at_1_std
      value: -14.704500000000001
    - type: nauc_recall_at_1_diff1
      value: 45.3337
    - type: nauc_recall_at_3_max
      value: 11.0823
    - type: nauc_recall_at_3_std
      value: -15.088899999999999
    - type: nauc_recall_at_3_diff1
      value: 33.5456
    - type: nauc_recall_at_5_max
      value: 10.5617
    - type: nauc_recall_at_5_std
      value: -14.8289
    - type: nauc_recall_at_5_diff1
      value: 31.3732
    - type: nauc_recall_at_10_max
      value: 10.4061
    - type: nauc_recall_at_10_std
      value: -13.3346
    - type: nauc_recall_at_10_diff1
      value: 28.131099999999996
    - type: nauc_recall_at_20_max
      value: 10.2817
    - type: nauc_recall_at_20_std
      value: -11.5314
    - type: nauc_recall_at_20_diff1
      value: 25.3998
    - type: nauc_recall_at_100_max
      value: 13.818
    - type: nauc_recall_at_100_std
      value: -2.6188
    - type: nauc_recall_at_100_diff1
      value: 22.0747
    - type: nauc_recall_at_1000_max
      value: 21.893099999999997
    - type: nauc_recall_at_1000_std
      value: 16.1546
    - type: nauc_recall_at_1000_diff1
      value: 15.1476
    - type: nauc_precision_at_1_max
      value: 14.524799999999999
    - type: nauc_precision_at_1_std
      value: -14.704500000000001
    - type: nauc_precision_at_1_diff1
      value: 45.3337
    - type: nauc_precision_at_3_max
      value: 11.0823
    - type: nauc_precision_at_3_std
      value: -15.088899999999999
    - type: nauc_precision_at_3_diff1
      value: 33.5456
    - type: nauc_precision_at_5_max
      value: 10.5617
    - type: nauc_precision_at_5_std
      value: -14.8289
    - type: nauc_precision_at_5_diff1
      value: 31.3732
    - type: nauc_precision_at_10_max
      value: 10.4061
    - type: nauc_precision_at_10_std
      value: -13.3346
    - type: nauc_precision_at_10_diff1
      value: 28.131099999999996
    - type: nauc_precision_at_20_max
      value: 10.2817
    - type: nauc_precision_at_20_std
      value: -11.5314
    - type: nauc_precision_at_20_diff1
      value: 25.3998
    - type: nauc_precision_at_100_max
      value: 13.818
    - type: nauc_precision_at_100_std
      value: -2.6188
    - type: nauc_precision_at_100_diff1
      value: 22.0747
    - type: nauc_precision_at_1000_max
      value: 21.893099999999997
    - type: nauc_precision_at_1000_std
      value: 16.1546
    - type: nauc_precision_at_1000_diff1
      value: 15.1476
    - type: nauc_mrr_at_1_max
      value: 14.524799999999999
    - type: nauc_mrr_at_1_std
      value: -14.704500000000001
    - type: nauc_mrr_at_1_diff1
      value: 45.3337
    - type: nauc_mrr_at_3_max
      value: 12.7833
    - type: nauc_mrr_at_3_std
      value: -14.9312
    - type: nauc_mrr_at_3_diff1
      value: 39.2273
    - type: nauc_mrr_at_5_max
      value: 12.606200000000001
    - type: nauc_mrr_at_5_std
      value: -14.846200000000001
    - type: nauc_mrr_at_5_diff1
      value: 38.5015
    - type: nauc_mrr_at_10_max
      value: 12.5202
    - type: nauc_mrr_at_10_std
      value: -14.5979
    - type: nauc_mrr_at_10_diff1
      value: 37.8521
    - type: nauc_mrr_at_20_max
      value: 12.5101
    - type: nauc_mrr_at_20_std
      value: -14.444899999999999
    - type: nauc_mrr_at_20_diff1
      value: 37.5942
    - type: nauc_mrr_at_100_max
      value: 12.601399999999998
    - type: nauc_mrr_at_100_std
      value: -14.2092
    - type: nauc_mrr_at_100_diff1
      value: 37.4992
    - type: nauc_mrr_at_1000_max
      value: 12.6334
    - type: nauc_mrr_at_1000_std
      value: -14.1545
    - type: nauc_mrr_at_1000_diff1
      value: 37.4959
    - type: main_score
      value: 23.458000000000002
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB CodeFeedbackST (default)
      revision: d213819e87aab9010628da8b73ab4eb337c89340
      split: test
      type: CoIR-Retrieval/codefeedback-st
    metrics:
    - type: ndcg_at_1
      value: 42.781000000000006
    - type: ndcg_at_3
      value: 53.547999999999995
    - type: ndcg_at_5
      value: 56.184999999999995
    - type: ndcg_at_10
      value: 58.455
    - type: ndcg_at_20
      value: 59.897
    - type: ndcg_at_100
      value: 61.806000000000004
    - type: ndcg_at_1000
      value: 62.769
    - type: map_at_1
      value: 42.781000000000006
    - type: map_at_3
      value: 50.92100000000001
    - type: map_at_5
      value: 52.38699999999999
    - type: map_at_10
      value: 53.335
    - type: map_at_20
      value: 53.733
    - type: map_at_100
      value: 53.998999999999995
    - type: map_at_1000
      value: 54.035
    - type: recall_at_1
      value: 42.781000000000006
    - type: recall_at_3
      value: 61.141999999999996
    - type: recall_at_5
      value: 67.533
    - type: recall_at_10
      value: 74.491
    - type: recall_at_20
      value: 80.17999999999999
    - type: recall_at_100
      value: 90.443
    - type: recall_at_1000
      value: 98.051
    - type: precision_at_1
      value: 42.781000000000006
    - type: precision_at_3
      value: 20.381
    - type: precision_at_5
      value: 13.507
    - type: precision_at_10
      value: 7.449
    - type: precision_at_20
      value: 4.009
    - type: precision_at_100
      value: 0.9039999999999999
    - type: precision_at_1000
      value: 0.098
    - type: mrr_at_1
      value: 42.8193
    - type: mrr_at_3
      value: 50.9333
    - type: mrr_at_5
      value: 52.4157
    - type: mrr_at_10
      value: 53.3551
    - type: mrr_at_20
      value: 53.7532
    - type: mrr_at_100
      value: 54.0192
    - type: mrr_at_1000
      value: 54.0547
    - type: nauc_ndcg_at_1_max
      value: 8.1476
    - type: nauc_ndcg_at_1_std
      value: -18.415599999999998
    - type: nauc_ndcg_at_1_diff1
      value: 61.467499999999994
    - type: nauc_ndcg_at_3_max
      value: 14.5702
    - type: nauc_ndcg_at_3_std
      value: -18.4765
    - type: nauc_ndcg_at_3_diff1
      value: 54.7928
    - type: nauc_ndcg_at_5_max
      value: 15.2642
    - type: nauc_ndcg_at_5_std
      value: -18.2014
    - type: nauc_ndcg_at_5_diff1
      value: 53.9847
    - type: nauc_ndcg_at_10_max
      value: 15.0742
    - type: nauc_ndcg_at_10_std
      value: -17.8811
    - type: nauc_ndcg_at_10_diff1
      value: 53.9565
    - type: nauc_ndcg_at_20_max
      value: 14.7067
    - type: nauc_ndcg_at_20_std
      value: -17.618000000000002
    - type: nauc_ndcg_at_20_diff1
      value: 54.041399999999996
    - type: nauc_ndcg_at_100_max
      value: 14.4373
    - type: nauc_ndcg_at_100_std
      value: -17.1309
    - type: nauc_ndcg_at_100_diff1
      value: 54.5959
    - type: nauc_ndcg_at_1000_max
      value: 14.1768
    - type: nauc_ndcg_at_1000_std
      value: -17.2829
    - type: nauc_ndcg_at_1000_diff1
      value: 55.053799999999995
    - type: nauc_map_at_1_max
      value: 8.1476
    - type: nauc_map_at_1_std
      value: -18.415599999999998
    - type: nauc_map_at_1_diff1
      value: 61.467499999999994
    - type: nauc_map_at_3_max
      value: 12.961400000000001
    - type: nauc_map_at_3_std
      value: -18.4454
    - type: nauc_map_at_3_diff1
      value: 56.42
    - type: nauc_map_at_5_max
      value: 13.295599999999999
    - type: nauc_map_at_5_std
      value: -18.293599999999998
    - type: nauc_map_at_5_diff1
      value: 56.033
    - type: nauc_map_at_10_max
      value: 13.189600000000002
    - type: nauc_map_at_10_std
      value: -18.169
    - type: nauc_map_at_10_diff1
      value: 56.0467
    - type: nauc_map_at_20_max
      value: 13.0847
    - type: nauc_map_at_20_std
      value: -18.1099
    - type: nauc_map_at_20_diff1
      value: 56.0909
    - type: nauc_map_at_100_max
      value: 13.0384
    - type: nauc_map_at_100_std
      value: -18.0582
    - type: nauc_map_at_100_diff1
      value: 56.1735
    - type: nauc_map_at_1000_max
      value: 13.03
    - type: nauc_map_at_1000_std
      value: -18.0598
    - type: nauc_map_at_1000_diff1
      value: 56.1901
    - type: nauc_recall_at_1_max
      value: 8.1476
    - type: nauc_recall_at_1_std
      value: -18.415599999999998
    - type: nauc_recall_at_1_diff1
      value: 61.467499999999994
    - type: nauc_recall_at_3_max
      value: 19.6416
    - type: nauc_recall_at_3_std
      value: -18.582099999999997
    - type: nauc_recall_at_3_diff1
      value: 49.6845
    - type: nauc_recall_at_5_max
      value: 22.2239
    - type: nauc_recall_at_5_std
      value: -17.847099999999998
    - type: nauc_recall_at_5_diff1
      value: 46.739999999999995
    - type: nauc_recall_at_10_max
      value: 22.8276
    - type: nauc_recall_at_10_std
      value: -16.486600000000003
    - type: nauc_recall_at_10_diff1
      value: 45.2586
    - type: nauc_recall_at_20_max
      value: 22.2364
    - type: nauc_recall_at_20_std
      value: -14.5036
    - type: nauc_recall_at_20_diff1
      value: 43.7903
    - type: nauc_recall_at_100_max
      value: 25.254700000000003
    - type: nauc_recall_at_100_std
      value: -3.9357
    - type: nauc_recall_at_100_diff1
      value: 42.6367
    - type: nauc_recall_at_1000_max
      value: 38.3787
    - type: nauc_recall_at_1000_std
      value: 27.075100000000003
    - type: nauc_recall_at_1000_diff1
      value: 44.277
    - type: nauc_precision_at_1_max
      value: 8.1476
    - type: nauc_precision_at_1_std
      value: -18.415599999999998
    - type: nauc_precision_at_1_diff1
      value: 61.467499999999994
    - type: nauc_precision_at_3_max
      value: 19.6416
    - type: nauc_precision_at_3_std
      value: -18.582099999999997
    - type: nauc_precision_at_3_diff1
      value: 49.6845
    - type: nauc_precision_at_5_max
      value: 22.2239
    - type: nauc_precision_at_5_std
      value: -17.847099999999998
    - type: nauc_precision_at_5_diff1
      value: 46.739999999999995
    - type: nauc_precision_at_10_max
      value: 22.8276
    - type: nauc_precision_at_10_std
      value: -16.486600000000003
    - type: nauc_precision_at_10_diff1
      value: 45.2586
    - type: nauc_precision_at_20_max
      value: 22.2364
    - type: nauc_precision_at_20_std
      value: -14.5036
    - type: nauc_precision_at_20_diff1
      value: 43.7903
    - type: nauc_precision_at_100_max
      value: 25.254700000000003
    - type: nauc_precision_at_100_std
      value: -3.9357
    - type: nauc_precision_at_100_diff1
      value: 42.6367
    - type: nauc_precision_at_1000_max
      value: 38.3787
    - type: nauc_precision_at_1000_std
      value: 27.075100000000003
    - type: nauc_precision_at_1000_diff1
      value: 44.277
    - type: nauc_mrr_at_1_max
      value: 7.7336
    - type: nauc_mrr_at_1_std
      value: -18.2617
    - type: nauc_mrr_at_1_diff1
      value: 61.3653
    - type: nauc_mrr_at_3_max
      value: 12.6751
    - type: nauc_mrr_at_3_std
      value: -18.3779
    - type: nauc_mrr_at_3_diff1
      value: 56.383
    - type: nauc_mrr_at_5_max
      value: 13.031200000000002
    - type: nauc_mrr_at_5_std
      value: -18.252499999999998
    - type: nauc_mrr_at_5_diff1
      value: 55.9734
    - type: nauc_mrr_at_10_max
      value: 12.934399999999998
    - type: nauc_mrr_at_10_std
      value: -18.0918
    - type: nauc_mrr_at_10_diff1
      value: 55.9883
    - type: nauc_mrr_at_20_max
      value: 12.8271
    - type: nauc_mrr_at_20_std
      value: -18.0345
    - type: nauc_mrr_at_20_diff1
      value: 56.033100000000005
    - type: nauc_mrr_at_100_max
      value: 12.7798
    - type: nauc_mrr_at_100_std
      value: -17.983
    - type: nauc_mrr_at_100_diff1
      value: 56.115700000000004
    - type: nauc_mrr_at_1000_max
      value: 12.771099999999999
    - type: nauc_mrr_at_1000_std
      value: -17.9844
    - type: nauc_mrr_at_1000_diff1
      value: 56.1323
    - type: main_score
      value: 58.455
    task:
      type: Retrieval
  - dataset:
      config: python
      name: MTEB CodeSearchNetCCRetrieval (python)
      revision: 6e1effa2c03723c5fde48ee912b5ee08d4f211e8
      split: test
      type: CoIR-Retrieval/CodeSearchNet-ccr
    metrics:
    - type: ndcg_at_1
      value: 29.32
    - type: ndcg_at_3
      value: 37.202
    - type: ndcg_at_5
      value: 39.399
    - type: ndcg_at_10
      value: 41.583
    - type: ndcg_at_20
      value: 43.156
    - type: ndcg_at_100
      value: 45.506
    - type: ndcg_at_1000
      value: 47.28
    - type: map_at_1
      value: 29.32
    - type: map_at_3
      value: 35.266999999999996
    - type: map_at_5
      value: 36.489
    - type: map_at_10
      value: 37.399
    - type: map_at_20
      value: 37.829
    - type: map_at_100
      value: 38.149
    - type: map_at_1000
      value: 38.208
    - type: recall_at_1
      value: 29.32
    - type: recall_at_3
      value: 42.801
    - type: recall_at_5
      value: 48.123
    - type: recall_at_10
      value: 54.82599999999999
    - type: recall_at_20
      value: 61.06700000000001
    - type: recall_at_100
      value: 73.817
    - type: recall_at_1000
      value: 88.189
    - type: precision_at_1
      value: 29.32
    - type: precision_at_3
      value: 14.267
    - type: precision_at_5
      value: 9.625
    - type: precision_at_10
      value: 5.483
    - type: precision_at_20
      value: 3.053
    - type: precision_at_100
      value: 0.738
    - type: precision_at_1000
      value: 0.08800000000000001
    - type: mrr_at_1
      value: 29.3203
    - type: mrr_at_3
      value: 35.2661
    - type: mrr_at_5
      value: 36.4878
    - type: mrr_at_10
      value: 37.398399999999995
    - type: mrr_at_20
      value: 37.8278
    - type: mrr_at_100
      value: 38.1474
    - type: mrr_at_1000
      value: 38.2072
    - type: nauc_ndcg_at_1_max
      value: 27.608
    - type: nauc_ndcg_at_1_std
      value: -0.1578
    - type: nauc_ndcg_at_1_diff1
      value: 50.7213
    - type: nauc_ndcg_at_3_max
      value: 28.488799999999998
    - type: nauc_ndcg_at_3_std
      value: 0.8798
    - type: nauc_ndcg_at_3_diff1
      value: 46.4513
    - type: nauc_ndcg_at_5_max
      value: 28.2088
    - type: nauc_ndcg_at_5_std
      value: 1.536
    - type: nauc_ndcg_at_5_diff1
      value: 45.5291
    - type: nauc_ndcg_at_10_max
      value: 28.076600000000003
    - type: nauc_ndcg_at_10_std
      value: 2.4101999999999997
    - type: nauc_ndcg_at_10_diff1
      value: 45.0789
    - type: nauc_ndcg_at_20_max
      value: 28.1814
    - type: nauc_ndcg_at_20_std
      value: 3.1981999999999995
    - type: nauc_ndcg_at_20_diff1
      value: 44.8012
    - type: nauc_ndcg_at_100_max
      value: 27.9818
    - type: nauc_ndcg_at_100_std
      value: 3.8790999999999998
    - type: nauc_ndcg_at_100_diff1
      value: 44.7506
    - type: nauc_ndcg_at_1000_max
      value: 28.1483
    - type: nauc_ndcg_at_1000_std
      value: 3.8562
    - type: nauc_ndcg_at_1000_diff1
      value: 45.1726
    - type: nauc_map_at_1_max
      value: 27.608
    - type: nauc_map_at_1_std
      value: -0.1578
    - type: nauc_map_at_1_diff1
      value: 50.7213
    - type: nauc_map_at_3_max
      value: 28.3097
    - type: nauc_map_at_3_std
      value: 0.6224000000000001
    - type: nauc_map_at_3_diff1
      value: 47.4366
    - type: nauc_map_at_5_max
      value: 28.157500000000002
    - type: nauc_map_at_5_std
      value: 0.9838
    - type: nauc_map_at_5_diff1
      value: 46.9294
    - type: nauc_map_at_10_max
      value: 28.097
    - type: nauc_map_at_10_std
      value: 1.3426
    - type: nauc_map_at_10_diff1
      value: 46.7574
    - type: nauc_map_at_20_max
      value: 28.124100000000002
    - type: nauc_map_at_20_std
      value: 1.5459
    - type: nauc_map_at_20_diff1
      value: 46.6828
    - type: nauc_map_at_100_max
      value: 28.0887
    - type: nauc_map_at_100_std
      value: 1.6311
    - type: nauc_map_at_100_diff1
      value: 46.684599999999996
    - type: nauc_map_at_1000_max
      value: 28.0938
    - type: nauc_map_at_1000_std
      value: 1.6345999999999998
    - type: nauc_map_at_1000_diff1
      value: 46.6979
    - type: nauc_recall_at_1_max
      value: 27.608
    - type: nauc_recall_at_1_std
      value: -0.1578
    - type: nauc_recall_at_1_diff1
      value: 50.7213
    - type: nauc_recall_at_3_max
      value: 28.982000000000003
    - type: nauc_recall_at_3_std
      value: 1.6101
    - type: nauc_recall_at_3_diff1
      value: 43.6847
    - type: nauc_recall_at_5_max
      value: 28.297800000000002
    - type: nauc_recall_at_5_std
      value: 3.2162
    - type: nauc_recall_at_5_diff1
      value: 41.402899999999995
    - type: nauc_recall_at_10_max
      value: 27.915499999999998
    - type: nauc_recall_at_10_std
      value: 6.0788
    - type: nauc_recall_at_10_diff1
      value: 39.7106
    - type: nauc_recall_at_20_max
      value: 28.3661
    - type: nauc_recall_at_20_std
      value: 9.8068
    - type: nauc_recall_at_20_diff1
      value: 38.153
    - type: nauc_recall_at_100_max
      value: 27.114300000000004
    - type: nauc_recall_at_100_std
      value: 17.0125
    - type: nauc_recall_at_100_diff1
      value: 35.6053
    - type: nauc_recall_at_1000_max
      value: 29.8655
    - type: nauc_recall_at_1000_std
      value: 28.480800000000002
    - type: nauc_recall_at_1000_diff1
      value: 35.9375
    - type: nauc_precision_at_1_max
      value: 27.608
    - type: nauc_precision_at_1_std
      value: -0.1578
    - type: nauc_precision_at_1_diff1
      value: 50.7213
    - type: nauc_precision_at_3_max
      value: 28.982000000000003
    - type: nauc_precision_at_3_std
      value: 1.6101
    - type: nauc_precision_at_3_diff1
      value: 43.6847
    - type: nauc_precision_at_5_max
      value: 28.297800000000002
    - type: nauc_precision_at_5_std
      value: 3.2162
    - type: nauc_precision_at_5_diff1
      value: 41.402899999999995
    - type: nauc_precision_at_10_max
      value: 27.915499999999998
    - type: nauc_precision_at_10_std
      value: 6.0788
    - type: nauc_precision_at_10_diff1
      value: 39.7106
    - type: nauc_precision_at_20_max
      value: 28.3661
    - type: nauc_precision_at_20_std
      value: 9.8068
    - type: nauc_precision_at_20_diff1
      value: 38.153
    - type: nauc_precision_at_100_max
      value: 27.114300000000004
    - type: nauc_precision_at_100_std
      value: 17.0125
    - type: nauc_precision_at_100_diff1
      value: 35.6053
    - type: nauc_precision_at_1000_max
      value: 29.8655
    - type: nauc_precision_at_1000_std
      value: 28.480800000000002
    - type: nauc_precision_at_1000_diff1
      value: 35.9375
    - type: nauc_mrr_at_1_max
      value: 27.608
    - type: nauc_mrr_at_1_std
      value: -0.1578
    - type: nauc_mrr_at_1_diff1
      value: 50.7213
    - type: nauc_mrr_at_3_max
      value: 28.310200000000002
    - type: nauc_mrr_at_3_std
      value: 0.6187
    - type: nauc_mrr_at_3_diff1
      value: 47.4396
    - type: nauc_mrr_at_5_max
      value: 28.1581
    - type: nauc_mrr_at_5_std
      value: 0.9801000000000001
    - type: nauc_mrr_at_5_diff1
      value: 46.9325
    - type: nauc_mrr_at_10_max
      value: 28.097499999999997
    - type: nauc_mrr_at_10_std
      value: 1.3393
    - type: nauc_mrr_at_10_diff1
      value: 46.760600000000004
    - type: nauc_mrr_at_20_max
      value: 28.124700000000004
    - type: nauc_mrr_at_20_std
      value: 1.5427
    - type: nauc_mrr_at_20_diff1
      value: 46.686
    - type: nauc_mrr_at_100_max
      value: 28.0893
    - type: nauc_mrr_at_100_std
      value: 1.6274
    - type: nauc_mrr_at_100_diff1
      value: 46.6879
    - type: nauc_mrr_at_1000_max
      value: 28.0943
    - type: nauc_mrr_at_1000_std
      value: 1.6312
    - type: nauc_mrr_at_1000_diff1
      value: 46.7012
    - type: main_score
      value: 41.583
    task:
      type: Retrieval
  - dataset:
      config: javascript
      name: MTEB CodeSearchNetCCRetrieval (javascript)
      revision: 6e1effa2c03723c5fde48ee912b5ee08d4f211e8
      split: test
      type: CoIR-Retrieval/CodeSearchNet-ccr
    metrics:
    - type: ndcg_at_1
      value: 30.294999999999998
    - type: ndcg_at_3
      value: 38.102000000000004
    - type: ndcg_at_5
      value: 40.164
    - type: ndcg_at_10
      value: 42.041000000000004
    - type: ndcg_at_20
      value: 43.464000000000006
    - type: ndcg_at_100
      value: 45.791
    - type: ndcg_at_1000
      value: 47.689
    - type: map_at_1
      value: 30.294999999999998
    - type: map_at_3
      value: 36.19
    - type: map_at_5
      value: 37.332
    - type: map_at_10
      value: 38.112
    - type: map_at_20
      value: 38.507999999999996
    - type: map_at_100
      value: 38.812999999999995
    - type: map_at_1000
      value: 38.875
    - type: recall_at_1
      value: 30.294999999999998
    - type: recall_at_3
      value: 43.634
    - type: recall_at_5
      value: 48.648
    - type: recall_at_10
      value: 54.421
    - type: recall_at_20
      value: 60.012
    - type: recall_at_100
      value: 72.80499999999999
    - type: recall_at_1000
      value: 88.271
    - type: precision_at_1
      value: 30.294999999999998
    - type: precision_at_3
      value: 14.545
    - type: precision_at_5
      value: 9.73
    - type: precision_at_10
      value: 5.442
    - type: precision_at_20
      value: 3.001
    - type: precision_at_100
      value: 0.728
    - type: precision_at_1000
      value: 0.08800000000000001
    - type: mrr_at_1
      value: 30.294700000000002
    - type: mrr_at_3
      value: 36.1845
    - type: mrr_at_5
      value: 37.3271
    - type: mrr_at_10
      value: 38.1071
    - type: mrr_at_20
      value: 38.502700000000004
    - type: mrr_at_100
      value: 38.8081
    - type: mrr_at_1000
      value: 38.8701
    - type: nauc_ndcg_at_1_max
      value: 26.3264
    - type: nauc_ndcg_at_1_std
      value: -4.8982
    - type: nauc_ndcg_at_1_diff1
      value: 50.14189999999999
    - type: nauc_ndcg_at_3_max
      value: 27.4968
    - type: nauc_ndcg_at_3_std
      value: -4.1065
    - type: nauc_ndcg_at_3_diff1
      value: 46.0956
    - type: nauc_ndcg_at_5_max
      value: 28.409299999999998
    - type: nauc_ndcg_at_5_std
      value: -3.7853
    - type: nauc_ndcg_at_5_diff1
      value: 45.6748
    - type: nauc_ndcg_at_10_max
      value: 27.942
    - type: nauc_ndcg_at_10_std
      value: -3.3216
    - type: nauc_ndcg_at_10_diff1
      value: 44.6236
    - type: nauc_ndcg_at_20_max
      value: 27.47
    - type: nauc_ndcg_at_20_std
      value: -3.1514
    - type: nauc_ndcg_at_20_diff1
      value: 44.74
    - type: nauc_ndcg_at_100_max
      value: 27.4711
    - type: nauc_ndcg_at_100_std
      value: -3.0054999999999996
    - type: nauc_ndcg_at_100_diff1
      value: 44.5073
    - type: nauc_ndcg_at_1000_max
      value: 27.7016
    - type: nauc_ndcg_at_1000_std
      value: -3.0528
    - type: nauc_ndcg_at_1000_diff1
      value: 44.8851
    - type: nauc_map_at_1_max
      value: 26.3264
    - type: nauc_map_at_1_std
      value: -4.8982
    - type: nauc_map_at_1_diff1
      value: 50.14189999999999
    - type: nauc_map_at_3_max
      value: 27.279500000000002
    - type: nauc_map_at_3_std
      value: -4.2798
    - type: nauc_map_at_3_diff1
      value: 47.0454
    - type: nauc_map_at_5_max
      value: 27.776600000000002
    - type: nauc_map_at_5_std
      value: -4.1068
    - type: nauc_map_at_5_diff1
      value: 46.8171
    - type: nauc_map_at_10_max
      value: 27.589399999999998
    - type: nauc_map_at_10_std
      value: -3.8844
    - type: nauc_map_at_10_diff1
      value: 46.4013
    - type: nauc_map_at_20_max
      value: 27.455099999999998
    - type: nauc_map_at_20_std
      value: -3.8475
    - type: nauc_map_at_20_diff1
      value: 46.4395
    - type: nauc_map_at_100_max
      value: 27.470299999999998
    - type: nauc_map_at_100_std
      value: -3.8240000000000003
    - type: nauc_map_at_100_diff1
      value: 46.4176
    - type: nauc_map_at_1000_max
      value: 27.473
    - type: nauc_map_at_1000_std
      value: -3.8289999999999997
    - type: nauc_map_at_1000_diff1
      value: 46.427
    - type: nauc_recall_at_1_max
      value: 26.3264
    - type: nauc_recall_at_1_std
      value: -4.8982
    - type: nauc_recall_at_1_diff1
      value: 50.14189999999999
    - type: nauc_recall_at_3_max
      value: 28.089599999999997
    - type: nauc_recall_at_3_std
      value: -3.6197
    - type: nauc_recall_at_3_diff1
      value: 43.4007
    - type: nauc_recall_at_5_max
      value: 30.3494
    - type: nauc_recall_at_5_std
      value: -2.8134
    - type: nauc_recall_at_5_diff1
      value: 42.3267
    - type: nauc_recall_at_10_max
      value: 28.9106
    - type: nauc_recall_at_10_std
      value: -1.4690999999999999
    - type: nauc_recall_at_10_diff1
      value: 38.7477
    - type: nauc_recall_at_20_max
      value: 27.0023
    - type: nauc_recall_at_20_std
      value: -0.5613
    - type: nauc_recall_at_20_diff1
      value: 38.874700000000004
    - type: nauc_recall_at_100_max
      value: 26.4945
    - type: nauc_recall_at_100_std
      value: 1.1353
    - type: nauc_recall_at_100_diff1
      value: 35.297200000000004
    - type: nauc_recall_at_1000_max
      value: 31.464100000000002
    - type: nauc_recall_at_1000_std
      value: 5.16
    - type: nauc_recall_at_1000_diff1
      value: 34.5536
    - type: nauc_precision_at_1_max
      value: 26.3264
    - type: nauc_precision_at_1_std
      value: -4.8982
    - type: nauc_precision_at_1_diff1
      value: 50.14189999999999
    - type: nauc_precision_at_3_max
      value: 28.089599999999997
    - type: nauc_precision_at_3_std
      value: -3.6197
    - type: nauc_precision_at_3_diff1
      value: 43.4007
    - type: nauc_precision_at_5_max
      value: 30.3494
    - type: nauc_precision_at_5_std
      value: -2.8134
    - type: nauc_precision_at_5_diff1
      value: 42.3267
    - type: nauc_precision_at_10_max
      value: 28.9106
    - type: nauc_precision_at_10_std
      value: -1.4690999999999999
    - type: nauc_precision_at_10_diff1
      value: 38.7477
    - type: nauc_precision_at_20_max
      value: 27.0023
    - type: nauc_precision_at_20_std
      value: -0.5613
    - type: nauc_precision_at_20_diff1
      value: 38.874700000000004
    - type: nauc_precision_at_100_max
      value: 26.4945
    - type: nauc_precision_at_100_std
      value: 1.1353
    - type: nauc_precision_at_100_diff1
      value: 35.297200000000004
    - type: nauc_precision_at_1000_max
      value: 31.464100000000002
    - type: nauc_precision_at_1000_std
      value: 5.16
    - type: nauc_precision_at_1000_diff1
      value: 34.5536
    - type: nauc_mrr_at_1_max
      value: 26.464199999999998
    - type: nauc_mrr_at_1_std
      value: -4.6967
    - type: nauc_mrr_at_1_diff1
      value: 50.14189999999999
    - type: nauc_mrr_at_3_max
      value: 27.3495
    - type: nauc_mrr_at_3_std
      value: -4.1872
    - type: nauc_mrr_at_3_diff1
      value: 47.0534
    - type: nauc_mrr_at_5_max
      value: 27.8469
    - type: nauc_mrr_at_5_std
      value: -4.0137
    - type: nauc_mrr_at_5_diff1
      value: 46.8252
    - type: nauc_mrr_at_10_max
      value: 27.660200000000003
    - type: nauc_mrr_at_10_std
      value: -3.7907
    - type: nauc_mrr_at_10_diff1
      value: 46.4094
    - type: nauc_mrr_at_20_max
      value: 27.526699999999998
    - type: nauc_mrr_at_20_std
      value: -3.7532
    - type: nauc_mrr_at_20_diff1
      value: 46.448
    - type: nauc_mrr_at_100_max
      value: 27.5422
    - type: nauc_mrr_at_100_std
      value: -3.7292
    - type: nauc_mrr_at_100_diff1
      value: 46.4261
    - type: nauc_mrr_at_1000_max
      value: 27.544999999999998
    - type: nauc_mrr_at_1000_std
      value: -3.734
    - type: nauc_mrr_at_1000_diff1
      value: 46.435500000000005
    - type: main_score
      value: 42.041000000000004
    task:
      type: Retrieval
  - dataset:
      config: go
      name: MTEB CodeSearchNetCCRetrieval (go)
      revision: 6e1effa2c03723c5fde48ee912b5ee08d4f211e8
      split: test
      type: CoIR-Retrieval/CodeSearchNet-ccr
    metrics:
    - type: ndcg_at_1
      value: 23.615
    - type: ndcg_at_3
      value: 29.892999999999997
    - type: ndcg_at_5
      value: 31.953
    - type: ndcg_at_10
      value: 33.861000000000004
    - type: ndcg_at_20
      value: 35.402
    - type: ndcg_at_100
      value: 37.891000000000005
    - type: ndcg_at_1000
      value: 40.036
    - type: map_at_1
      value: 23.615
    - type: map_at_3
      value: 28.366999999999997
    - type: map_at_5
      value: 29.511
    - type: map_at_10
      value: 30.304
    - type: map_at_20
      value: 30.732
    - type: map_at_100
      value: 31.062
    - type: map_at_1000
      value: 31.133
    - type: recall_at_1
      value: 23.615
    - type: recall_at_3
      value: 34.302
    - type: recall_at_5
      value: 39.301
    - type: recall_at_10
      value: 45.174
    - type: recall_at_20
      value: 51.231
    - type: recall_at_100
      value: 64.849
    - type: recall_at_1000
      value: 82.307
    - type: precision_at_1
      value: 23.615
    - type: precision_at_3
      value: 11.434
    - type: precision_at_5
      value: 7.86
    - type: precision_at_10
      value: 4.517
    - type: precision_at_20
      value: 2.562
    - type: precision_at_100
      value: 0.6479999999999999
    - type: precision_at_1000
      value: 0.082
    - type: mrr_at_1
      value: 23.5902
    - type: mrr_at_3
      value: 28.353
    - type: mrr_at_5
      value: 29.4987
    - type: mrr_at_10
      value: 30.292099999999998
    - type: mrr_at_20
      value: 30.72
    - type: mrr_at_100
      value: 31.049599999999998
    - type: mrr_at_1000
      value: 31.120399999999997
    - type: nauc_ndcg_at_1_max
      value: 29.1258
    - type: nauc_ndcg_at_1_std
      value: 1.0401
    - type: nauc_ndcg_at_1_diff1
      value: 47.328199999999995
    - type: nauc_ndcg_at_3_max
      value: 27.8848
    - type: nauc_ndcg_at_3_std
      value: 0.2671
    - type: nauc_ndcg_at_3_diff1
      value: 41.4436
    - type: nauc_ndcg_at_5_max
      value: 27.475300000000004
    - type: nauc_ndcg_at_5_std
      value: -0.1773
    - type: nauc_ndcg_at_5_diff1
      value: 40.184999999999995
    - type: nauc_ndcg_at_10_max
      value: 27.1682
    - type: nauc_ndcg_at_10_std
      value: -0.0666
    - type: nauc_ndcg_at_10_diff1
      value: 39.698
    - type: nauc_ndcg_at_20_max
      value: 26.822699999999998
    - type: nauc_ndcg_at_20_std
      value: 0.3046
    - type: nauc_ndcg_at_20_diff1
      value: 39.0465
    - type: nauc_ndcg_at_100_max
      value: 26.55
    - type: nauc_ndcg_at_100_std
      value: 0.9386
    - type: nauc_ndcg_at_100_diff1
      value: 38.4816
    - type: nauc_ndcg_at_1000_max
      value: 26.8464
    - type: nauc_ndcg_at_1000_std
      value: 1.601
    - type: nauc_ndcg_at_1000_diff1
      value: 38.75
    - type: nauc_map_at_1_max
      value: 29.1258
    - type: nauc_map_at_1_std
      value: 1.0401
    - type: nauc_map_at_1_diff1
      value: 47.328199999999995
    - type: nauc_map_at_3_max
      value: 28.1313
    - type: nauc_map_at_3_std
      value: 0.4596
    - type: nauc_map_at_3_diff1
      value: 42.743199999999995
    - type: nauc_map_at_5_max
      value: 27.91
    - type: nauc_map_at_5_std
      value: 0.1926
    - type: nauc_map_at_5_diff1
      value: 42.0283
    - type: nauc_map_at_10_max
      value: 27.7964
    - type: nauc_map_at_10_std
      value: 0.2326
    - type: nauc_map_at_10_diff1
      value: 41.8324
    - type: nauc_map_at_20_max
      value: 27.6958
    - type: nauc_map_at_20_std
      value: 0.3369
    - type: nauc_map_at_20_diff1
      value: 41.6458
    - type: nauc_map_at_100_max
      value: 27.6475
    - type: nauc_map_at_100_std
      value: 0.4118
    - type: nauc_map_at_100_diff1
      value: 41.5667
    - type: nauc_map_at_1000_max
      value: 27.654899999999998
    - type: nauc_map_at_1000_std
      value: 0.43439999999999995
    - type: nauc_map_at_1000_diff1
      value: 41.578199999999995
    - type: nauc_recall_at_1_max
      value: 29.1258
    - type: nauc_recall_at_1_std
      value: 1.0401
    - type: nauc_recall_at_1_diff1
      value: 47.328199999999995
    - type: nauc_recall_at_3_max
      value: 27.232200000000002
    - type: nauc_recall_at_3_std
      value: -0.25980000000000003
    - type: nauc_recall_at_3_diff1
      value: 37.946200000000005
    - type: nauc_recall_at_5_max
      value: 26.266000000000002
    - type: nauc_recall_at_5_std
      value: -1.2084
    - type: nauc_recall_at_5_diff1
      value: 35.1318
    - type: nauc_recall_at_10_max
      value: 25.2762
    - type: nauc_recall_at_10_std
      value: -0.8635
    - type: nauc_recall_at_10_diff1
      value: 33.6001
    - type: nauc_recall_at_20_max
      value: 23.9389
    - type: nauc_recall_at_20_std
      value: 0.5331
    - type: nauc_recall_at_20_diff1
      value: 30.9907
    - type: nauc_recall_at_100_max
      value: 21.9631
    - type: nauc_recall_at_100_std
      value: 4.6604
    - type: nauc_recall_at_100_diff1
      value: 26.1225
    - type: nauc_recall_at_1000_max
      value: 23.450699999999998
    - type: nauc_recall_at_1000_std
      value: 17.0092
    - type: nauc_recall_at_1000_diff1
      value: 21.3813
    - type: nauc_precision_at_1_max
      value: 29.1258
    - type: nauc_precision_at_1_std
      value: 1.0401
    - type: nauc_precision_at_1_diff1
      value: 47.328199999999995
    - type: nauc_precision_at_3_max
      value: 27.232200000000002
    - type: nauc_precision_at_3_std
      value: -0.25980000000000003
    - type: nauc_precision_at_3_diff1
      value: 37.946200000000005
    - type: nauc_precision_at_5_max
      value: 26.266000000000002
    - type: nauc_precision_at_5_std
      value: -1.2084
    - type: nauc_precision_at_5_diff1
      value: 35.1318
    - type: nauc_precision_at_10_max
      value: 25.2762
    - type: nauc_precision_at_10_std
      value: -0.8635
    - type: nauc_precision_at_10_diff1
      value: 33.6001
    - type: nauc_precision_at_20_max
      value: 23.9389
    - type: nauc_precision_at_20_std
      value: 0.5331
    - type: nauc_precision_at_20_diff1
      value: 30.9907
    - type: nauc_precision_at_100_max
      value: 21.9631
    - type: nauc_precision_at_100_std
      value: 4.6604
    - type: nauc_precision_at_100_diff1
      value: 26.1225
    - type: nauc_precision_at_1000_max
      value: 23.450699999999998
    - type: nauc_precision_at_1000_std
      value: 17.0092
    - type: nauc_precision_at_1000_diff1
      value: 21.3813
    - type: nauc_mrr_at_1_max
      value: 29.1731
    - type: nauc_mrr_at_1_std
      value: 1.0801
    - type: nauc_mrr_at_1_diff1
      value: 47.429
    - type: nauc_mrr_at_3_max
      value: 28.1768
    - type: nauc_mrr_at_3_std
      value: 0.4919
    - type: nauc_mrr_at_3_diff1
      value: 42.830200000000005
    - type: nauc_mrr_at_5_max
      value: 27.9396
    - type: nauc_mrr_at_5_std
      value: 0.2168
    - type: nauc_mrr_at_5_diff1
      value: 42.0956
    - type: nauc_mrr_at_10_max
      value: 27.8301
    - type: nauc_mrr_at_10_std
      value: 0.2567
    - type: nauc_mrr_at_10_diff1
      value: 41.8926
    - type: nauc_mrr_at_20_max
      value: 27.7297
    - type: nauc_mrr_at_20_std
      value: 0.3648
    - type: nauc_mrr_at_20_diff1
      value: 41.7068
    - type: nauc_mrr_at_100_max
      value: 27.6788
    - type: nauc_mrr_at_100_std
      value: 0.43550000000000005
    - type: nauc_mrr_at_100_diff1
      value: 41.626000000000005
    - type: nauc_mrr_at_1000_max
      value: 27.6876
    - type: nauc_mrr_at_1000_std
      value: 0.4594
    - type: nauc_mrr_at_1000_diff1
      value: 41.6377
    - type: main_score
      value: 33.861000000000004
    task:
      type: Retrieval
  - dataset:
      config: ruby
      name: MTEB CodeSearchNetCCRetrieval (ruby)
      revision: 6e1effa2c03723c5fde48ee912b5ee08d4f211e8
      split: test
      type: CoIR-Retrieval/CodeSearchNet-ccr
    metrics:
    - type: ndcg_at_1
      value: 32.99
    - type: ndcg_at_3
      value: 40.416999999999994
    - type: ndcg_at_5
      value: 42.492000000000004
    - type: ndcg_at_10
      value: 44.528
    - type: ndcg_at_20
      value: 46.135999999999996
    - type: ndcg_at_100
      value: 48.33
    - type: ndcg_at_1000
      value: 50.047
    - type: map_at_1
      value: 32.99
    - type: map_at_3
      value: 38.647
    - type: map_at_5
      value: 39.789
    - type: map_at_10
      value: 40.62
    - type: map_at_20
      value: 41.062
    - type: map_at_100
      value: 41.366
    - type: map_at_1000
      value: 41.422
    - type: recall_at_1
      value: 32.99
    - type: recall_at_3
      value: 45.519
    - type: recall_at_5
      value: 50.595
    - type: recall_at_10
      value: 56.93899999999999
    - type: recall_at_20
      value: 63.283
    - type: recall_at_100
      value: 75.099
    - type: recall_at_1000
      value: 89.13600000000001
    - type: precision_at_1
      value: 32.99
    - type: precision_at_3
      value: 15.173
    - type: precision_at_5
      value: 10.119
    - type: precision_at_10
      value: 5.694
    - type: precision_at_20
      value: 3.164
    - type: precision_at_100
      value: 0.751
    - type: precision_at_1000
      value: 0.089
    - type: mrr_at_1
      value: 33.068999999999996
    - type: mrr_at_3
      value: 38.6862
    - type: mrr_at_5
      value: 39.8282
    - type: mrr_at_10
      value: 40.6593
    - type: mrr_at_20
      value: 41.1016
    - type: mrr_at_100
      value: 41.4058
    - type: mrr_at_1000
      value: 41.4614
    - type: nauc_ndcg_at_1_max
      value: 34.985699999999994
    - type: nauc_ndcg_at_1_std
      value: -7.5317
    - type: nauc_ndcg_at_1_diff1
      value: 55.82899999999999
    - type: nauc_ndcg_at_3_max
      value: 34.3163
    - type: nauc_ndcg_at_3_std
      value: -7.0863
    - type: nauc_ndcg_at_3_diff1
      value: 50.0509
    - type: nauc_ndcg_at_5_max
      value: 33.7316
    - type: nauc_ndcg_at_5_std
      value: -7.3946
    - type: nauc_ndcg_at_5_diff1
      value: 48.7525
    - type: nauc_ndcg_at_10_max
      value: 34.6192
    - type: nauc_ndcg_at_10_std
      value: -6.7839
    - type: nauc_ndcg_at_10_diff1
      value: 48.6166
    - type: nauc_ndcg_at_20_max
      value: 34.334399999999995
    - type: nauc_ndcg_at_20_std
      value: -7.0675
    - type: nauc_ndcg_at_20_diff1
      value: 48.0635
    - type: nauc_ndcg_at_100_max
      value: 34.6406
    - type: nauc_ndcg_at_100_std
      value: -6.8653
    - type: nauc_ndcg_at_100_diff1
      value: 48.617
    - type: nauc_ndcg_at_1000_max
      value: 34.2365
    - type: nauc_ndcg_at_1000_std
      value: -7.0976
    - type: nauc_ndcg_at_1000_diff1
      value: 48.464200000000005
    - type: nauc_map_at_1_max
      value: 34.985699999999994
    - type: nauc_map_at_1_std
      value: -7.5317
    - type: nauc_map_at_1_diff1
      value: 55.82899999999999
    - type: nauc_map_at_3_max
      value: 34.577000000000005
    - type: nauc_map_at_3_std
      value: -7.1427000000000005
    - type: nauc_map_at_3_diff1
      value: 51.4256
    - type: nauc_map_at_5_max
      value: 34.2296
    - type: nauc_map_at_5_std
      value: -7.322299999999999
    - type: nauc_map_at_5_diff1
      value: 50.709700000000005
    - type: nauc_map_at_10_max
      value: 34.633900000000004
    - type: nauc_map_at_10_std
      value: -7.056900000000001
    - type: nauc_map_at_10_diff1
      value: 50.714099999999995
    - type: nauc_map_at_20_max
      value: 34.5386
    - type: nauc_map_at_20_std
      value: -7.142900000000001
    - type: nauc_map_at_20_diff1
      value: 50.568900000000006
    - type: nauc_map_at_100_max
      value: 34.5697
    - type: nauc_map_at_100_std
      value: -7.1189
    - type: nauc_map_at_100_diff1
      value: 50.6351
    - type: nauc_map_at_1000_max
      value: 34.558499999999995
    - type: nauc_map_at_1000_std
      value: -7.1173
    - type: nauc_map_at_1000_diff1
      value: 50.6277
    - type: nauc_recall_at_1_max
      value: 34.985699999999994
    - type: nauc_recall_at_1_std
      value: -7.5317
    - type: nauc_recall_at_1_diff1
      value: 55.82899999999999
    - type: nauc_recall_at_3_max
      value: 33.5265
    - type: nauc_recall_at_3_std
      value: -6.9448
    - type: nauc_recall_at_3_diff1
      value: 46.1063
    - type: nauc_recall_at_5_max
      value: 32.1817
    - type: nauc_recall_at_5_std
      value: -7.6609
    - type: nauc_recall_at_5_diff1
      value: 42.8551
    - type: nauc_recall_at_10_max
      value: 34.7502
    - type: nauc_recall_at_10_std
      value: -5.7719
    - type: nauc_recall_at_10_diff1
      value: 41.7549
    - type: nauc_recall_at_20_max
      value: 33.6546
    - type: nauc_recall_at_20_std
      value: -6.862500000000001
    - type: nauc_recall_at_20_diff1
      value: 38.6947
    - type: nauc_recall_at_100_max
      value: 36.095699999999994
    - type: nauc_recall_at_100_std
      value: -5.2094000000000005
    - type: nauc_recall_at_100_diff1
      value: 40.336800000000004
    - type: nauc_recall_at_1000_max
      value: 27.8549
    - type: nauc_recall_at_1000_std
      value: -10.570699999999999
    - type: nauc_recall_at_1000_diff1
      value: 28.6812
    - type: nauc_precision_at_1_max
      value: 34.985699999999994
    - type: nauc_precision_at_1_std
      value: -7.5317
    - type: nauc_precision_at_1_diff1
      value: 55.82899999999999
    - type: nauc_precision_at_3_max
      value: 33.5265
    - type: nauc_precision_at_3_std
      value: -6.9448
    - type: nauc_precision_at_3_diff1
      value: 46.1063
    - type: nauc_precision_at_5_max
      value: 32.1817
    - type: nauc_precision_at_5_std
      value: -7.6609
    - type: nauc_precision_at_5_diff1
      value: 42.8551
    - type: nauc_precision_at_10_max
      value: 34.7502
    - type: nauc_precision_at_10_std
      value: -5.7719
    - type: nauc_precision_at_10_diff1
      value: 41.7549
    - type: nauc_precision_at_20_max
      value: 33.6546
    - type: nauc_precision_at_20_std
      value: -6.862500000000001
    - type: nauc_precision_at_20_diff1
      value: 38.6947
    - type: nauc_precision_at_100_max
      value: 36.095699999999994
    - type: nauc_precision_at_100_std
      value: -5.2094000000000005
    - type: nauc_precision_at_100_diff1
      value: 40.336800000000004
    - type: nauc_precision_at_1000_max
      value: 27.8549
    - type: nauc_precision_at_1000_std
      value: -10.570699999999999
    - type: nauc_precision_at_1000_diff1
      value: 28.6812
    - type: nauc_mrr_at_1_max
      value: 35.099599999999995
    - type: nauc_mrr_at_1_std
      value: -7.268199999999999
    - type: nauc_mrr_at_1_diff1
      value: 55.5813
    - type: nauc_mrr_at_3_max
      value: 34.6335
    - type: nauc_mrr_at_3_std
      value: -7.012300000000001
    - type: nauc_mrr_at_3_diff1
      value: 51.3038
    - type: nauc_mrr_at_5_max
      value: 34.2864
    - type: nauc_mrr_at_5_std
      value: -7.1912
    - type: nauc_mrr_at_5_diff1
      value: 50.5873
    - type: nauc_mrr_at_10_max
      value: 34.6912
    - type: nauc_mrr_at_10_std
      value: -6.9247000000000005
    - type: nauc_mrr_at_10_diff1
      value: 50.5908
    - type: nauc_mrr_at_20_max
      value: 34.596199999999996
    - type: nauc_mrr_at_20_std
      value: -7.01
    - type: nauc_mrr_at_20_diff1
      value: 50.4448
    - type: nauc_mrr_at_100_max
      value: 34.6274
    - type: nauc_mrr_at_100_std
      value: -6.984999999999999
    - type: nauc_mrr_at_100_diff1
      value: 50.510200000000005
    - type: nauc_mrr_at_1000_max
      value: 34.6163
    - type: nauc_mrr_at_1000_std
      value: -6.9832
    - type: nauc_mrr_at_1000_diff1
      value: 50.5026
    - type: main_score
      value: 44.528
    task:
      type: Retrieval
  - dataset:
      config: java
      name: MTEB CodeSearchNetCCRetrieval (java)
      revision: 6e1effa2c03723c5fde48ee912b5ee08d4f211e8
      split: test
      type: CoIR-Retrieval/CodeSearchNet-ccr
    metrics:
    - type: ndcg_at_1
      value: 26.407999999999998
    - type: ndcg_at_3
      value: 33.356
    - type: ndcg_at_5
      value: 35.143
    - type: ndcg_at_10
      value: 37.008
    - type: ndcg_at_20
      value: 38.394
    - type: ndcg_at_100
      value: 40.726
    - type: ndcg_at_1000
      value: 42.648
    - type: map_at_1
      value: 26.407999999999998
    - type: map_at_3
      value: 31.663000000000004
    - type: map_at_5
      value: 32.651
    - type: map_at_10
      value: 33.424
    - type: map_at_20
      value: 33.808
    - type: map_at_100
      value: 34.121
    - type: map_at_1000
      value: 34.184
    - type: recall_at_1
      value: 26.407999999999998
    - type: recall_at_3
      value: 38.247
    - type: recall_at_5
      value: 42.602000000000004
    - type: recall_at_10
      value: 48.352000000000004
    - type: recall_at_20
      value: 53.811
    - type: recall_at_100
      value: 66.508
    - type: recall_at_1000
      value: 82.173
    - type: precision_at_1
      value: 26.407999999999998
    - type: precision_at_3
      value: 12.748999999999999
    - type: precision_at_5
      value: 8.52
    - type: precision_at_10
      value: 4.835
    - type: precision_at_20
      value: 2.691
    - type: precision_at_100
      value: 0.6649999999999999
    - type: precision_at_1000
      value: 0.082
    - type: mrr_at_1
      value: 26.4263
    - type: mrr_at_3
      value: 31.673499999999997
    - type: mrr_at_5
      value: 32.6607
    - type: mrr_at_10
      value: 33.4314
    - type: mrr_at_20
      value: 33.8153
    - type: mrr_at_100
      value: 34.1293
    - type: mrr_at_1000
      value: 34.192499999999995
    - type: nauc_ndcg_at_1_max
      value: 29.026600000000002
    - type: nauc_ndcg_at_1_std
      value: -5.3401
    - type: nauc_ndcg_at_1_diff1
      value: 51.7505
    - type: nauc_ndcg_at_3_max
      value: 30.0657
    - type: nauc_ndcg_at_3_std
      value: -4.2413
    - type: nauc_ndcg_at_3_diff1
      value: 46.476600000000005
    - type: nauc_ndcg_at_5_max
      value: 29.7155
    - type: nauc_ndcg_at_5_std
      value: -3.8619
    - type: nauc_ndcg_at_5_diff1
      value: 45.5131
    - type: nauc_ndcg_at_10_max
      value: 29.4459
    - type: nauc_ndcg_at_10_std
      value: -3.3680000000000003
    - type: nauc_ndcg_at_10_diff1
      value: 44.6258
    - type: nauc_ndcg_at_20_max
      value: 29.135499999999997
    - type: nauc_ndcg_at_20_std
      value: -3.0517
    - type: nauc_ndcg_at_20_diff1
      value: 44.1
    - type: nauc_ndcg_at_100_max
      value: 29.131400000000003
    - type: nauc_ndcg_at_100_std
      value: -2.03
    - type: nauc_ndcg_at_100_diff1
      value: 43.7972
    - type: nauc_ndcg_at_1000_max
      value: 29.285099999999996
    - type: nauc_ndcg_at_1000_std
      value: -1.9141
    - type: nauc_ndcg_at_1000_diff1
      value: 44.1738
    - type: nauc_map_at_1_max
      value: 29.026600000000002
    - type: nauc_map_at_1_std
      value: -5.3401
    - type: nauc_map_at_1_diff1
      value: 51.7505
    - type: nauc_map_at_3_max
      value: 29.8237
    - type: nauc_map_at_3_std
      value: -4.5517
    - type: nauc_map_at_3_diff1
      value: 47.6757
    - type: nauc_map_at_5_max
      value: 29.624200000000002
    - type: nauc_map_at_5_std
      value: -4.338100000000001
    - type: nauc_map_at_5_diff1
      value: 47.1309
    - type: nauc_map_at_10_max
      value: 29.5078
    - type: nauc_map_at_10_std
      value: -4.1374
    - type: nauc_map_at_10_diff1
      value: 46.7589
    - type: nauc_map_at_20_max
      value: 29.421000000000003
    - type: nauc_map_at_20_std
      value: -4.0543000000000005
    - type: nauc_map_at_20_diff1
      value: 46.6131
    - type: nauc_map_at_100_max
      value: 29.411199999999997
    - type: nauc_map_at_100_std
      value: -3.9336
    - type: nauc_map_at_100_diff1
      value: 46.578199999999995
    - type: nauc_map_at_1000_max
      value: 29.4134
    - type: nauc_map_at_1000_std
      value: -3.9301000000000004
    - type: nauc_map_at_1000_diff1
      value: 46.5892
    - type: nauc_recall_at_1_max
      value: 29.026600000000002
    - type: nauc_recall_at_1_std
      value: -5.3401
    - type: nauc_recall_at_1_diff1
      value: 51.7505
    - type: nauc_recall_at_3_max
      value: 30.7299
    - type: nauc_recall_at_3_std
      value: -3.3682999999999996
    - type: nauc_recall_at_3_diff1
      value: 43.1978
    - type: nauc_recall_at_5_max
      value: 29.9215
    - type: nauc_recall_at_5_std
      value: -2.4814
    - type: nauc_recall_at_5_diff1
      value: 40.9532
    - type: nauc_recall_at_10_max
      value: 29.1323
    - type: nauc_recall_at_10_std
      value: -0.9436999999999999
    - type: nauc_recall_at_10_diff1
      value: 38.221199999999996
    - type: nauc_recall_at_20_max
      value: 27.889999999999997
    - type: nauc_recall_at_20_std
      value: 0.4464
    - type: nauc_recall_at_20_diff1
      value: 35.8795
    - type: nauc_recall_at_100_max
      value: 27.8094
    - type: nauc_recall_at_100_std
      value: 7.914499999999999
    - type: nauc_recall_at_100_diff1
      value: 32.3117
    - type: nauc_recall_at_1000_max
      value: 29.6608
    - type: nauc_recall_at_1000_std
      value: 15.9532
    - type: nauc_recall_at_1000_diff1
      value: 31.069799999999997
    - type: nauc_precision_at_1_max
      value: 29.026600000000002
    - type: nauc_precision_at_1_std
      value: -5.3401
    - type: nauc_precision_at_1_diff1
      value: 51.7505
    - type: nauc_precision_at_3_max
      value: 30.7299
    - type: nauc_precision_at_3_std
      value: -3.3682999999999996
    - type: nauc_precision_at_3_diff1
      value: 43.1978
    - type: nauc_precision_at_5_max
      value: 29.9215
    - type: nauc_precision_at_5_std
      value: -2.4814
    - type: nauc_precision_at_5_diff1
      value: 40.9532
    - type: nauc_precision_at_10_max
      value: 29.1323
    - type: nauc_precision_at_10_std
      value: -0.9436999999999999
    - type: nauc_precision_at_10_diff1
      value: 38.221199999999996
    - type: nauc_precision_at_20_max
      value: 27.889999999999997
    - type: nauc_precision_at_20_std
      value: 0.4464
    - type: nauc_precision_at_20_diff1
      value: 35.8795
    - type: nauc_precision_at_100_max
      value: 27.8094
    - type: nauc_precision_at_100_std
      value: 7.914499999999999
    - type: nauc_precision_at_100_diff1
      value: 32.3117
    - type: nauc_precision_at_1000_max
      value: 29.6608
    - type: nauc_precision_at_1000_std
      value: 15.9532
    - type: nauc_precision_at_1000_diff1
      value: 31.069799999999997
    - type: nauc_mrr_at_1_max
      value: 29.0947
    - type: nauc_mrr_at_1_std
      value: -5.2643
    - type: nauc_mrr_at_1_diff1
      value: 51.678000000000004
    - type: nauc_mrr_at_3_max
      value: 29.8523
    - type: nauc_mrr_at_3_std
      value: -4.5234000000000005
    - type: nauc_mrr_at_3_diff1
      value: 47.653099999999995
    - type: nauc_mrr_at_5_max
      value: 29.648799999999998
    - type: nauc_mrr_at_5_std
      value: -4.3013
    - type: nauc_mrr_at_5_diff1
      value: 47.105799999999995
    - type: nauc_mrr_at_10_max
      value: 29.5336
    - type: nauc_mrr_at_10_std
      value: -4.1075
    - type: nauc_mrr_at_10_diff1
      value: 46.733799999999995
    - type: nauc_mrr_at_20_max
      value: 29.451500000000003
    - type: nauc_mrr_at_20_std
      value: -4.0183
    - type: nauc_mrr_at_20_diff1
      value: 46.5858
    - type: nauc_mrr_at_100_max
      value: 29.440699999999996
    - type: nauc_mrr_at_100_std
      value: -3.8987000000000003
    - type: nauc_mrr_at_100_diff1
      value: 46.5526
    - type: nauc_mrr_at_1000_max
      value: 29.442899999999998
    - type: nauc_mrr_at_1000_std
      value: -3.8952
    - type: nauc_mrr_at_1000_diff1
      value: 46.563500000000005
    - type: main_score
      value: 37.008
    task:
      type: Retrieval
  - dataset:
      config: php
      name: MTEB CodeSearchNetCCRetrieval (php)
      revision: 6e1effa2c03723c5fde48ee912b5ee08d4f211e8
      split: test
      type: CoIR-Retrieval/CodeSearchNet-ccr
    metrics:
    - type: ndcg_at_1
      value: 21.022
    - type: ndcg_at_3
      value: 27.082
    - type: ndcg_at_5
      value: 28.956
    - type: ndcg_at_10
      value: 30.791
    - type: ndcg_at_20
      value: 32.301
    - type: ndcg_at_100
      value: 34.794000000000004
    - type: ndcg_at_1000
      value: 37.082
    - type: map_at_1
      value: 21.022
    - type: map_at_3
      value: 25.593
    - type: map_at_5
      value: 26.634999999999998
    - type: map_at_10
      value: 27.395000000000003
    - type: map_at_20
      value: 27.811000000000003
    - type: map_at_100
      value: 28.143
    - type: map_at_1000
      value: 28.218
    - type: recall_at_1
      value: 21.022
    - type: recall_at_3
      value: 31.39
    - type: recall_at_5
      value: 35.935
    - type: recall_at_10
      value: 41.593999999999994
    - type: recall_at_20
      value: 47.552
    - type: recall_at_100
      value: 61.18900000000001
    - type: recall_at_1000
      value: 79.827
    - type: precision_at_1
      value: 21.022
    - type: precision_at_3
      value: 10.463000000000001
    - type: precision_at_5
      value: 7.187
    - type: precision_at_10
      value: 4.159
    - type: precision_at_20
      value: 2.378
    - type: precision_at_100
      value: 0.612
    - type: precision_at_1000
      value: 0.08
    - type: mrr_at_1
      value: 21.0218
    - type: mrr_at_3
      value: 25.588699999999996
    - type: mrr_at_5
      value: 26.631899999999998
    - type: mrr_at_10
      value: 27.3915
    - type: mrr_at_20
      value: 27.807900000000004
    - type: mrr_at_100
      value: 28.138800000000003
    - type: mrr_at_1000
      value: 28.2141
    - type: nauc_ndcg_at_1_max
      value: 22.1861
    - type: nauc_ndcg_at_1_std
      value: -3.218
    - type: nauc_ndcg_at_1_diff1
      value: 46.4989
    - type: nauc_ndcg_at_3_max
      value: 21.7282
    - type: nauc_ndcg_at_3_std
      value: -2.1185
    - type: nauc_ndcg_at_3_diff1
      value: 40.8096
    - type: nauc_ndcg_at_5_max
      value: 21.339199999999998
    - type: nauc_ndcg_at_5_std
      value: -1.6541000000000001
    - type: nauc_ndcg_at_5_diff1
      value: 39.6483
    - type: nauc_ndcg_at_10_max
      value: 20.9441
    - type: nauc_ndcg_at_10_std
      value: -0.8141
    - type: nauc_ndcg_at_10_diff1
      value: 38.5517
    - type: nauc_ndcg_at_20_max
      value: 20.7702
    - type: nauc_ndcg_at_20_std
      value: -0.293
    - type: nauc_ndcg_at_20_diff1
      value: 38.2386
    - type: nauc_ndcg_at_100_max
      value: 20.569100000000002
    - type: nauc_ndcg_at_100_std
      value: 0.8404
    - type: nauc_ndcg_at_100_diff1
      value: 37.6899
    - type: nauc_ndcg_at_1000_max
      value: 20.72
    - type: nauc_ndcg_at_1000_std
      value: 0.9279000000000001
    - type: nauc_ndcg_at_1000_diff1
      value: 37.9486
    - type: nauc_map_at_1_max
      value: 22.1861
    - type: nauc_map_at_1_std
      value: -3.218
    - type: nauc_map_at_1_diff1
      value: 46.4989
    - type: nauc_map_at_3_max
      value: 21.86
    - type: nauc_map_at_3_std
      value: -2.4015999999999997
    - type: nauc_map_at_3_diff1
      value: 42.0695
    - type: nauc_map_at_5_max
      value: 21.6404
    - type: nauc_map_at_5_std
      value: -2.1305
    - type: nauc_map_at_5_diff1
      value: 41.3954
    - type: nauc_map_at_10_max
      value: 21.4897
    - type: nauc_map_at_10_std
      value: -1.76
    - type: nauc_map_at_10_diff1
      value: 40.9264
    - type: nauc_map_at_20_max
      value: 21.4368
    - type: nauc_map_at_20_std
      value: -1.6178000000000001
    - type: nauc_map_at_20_diff1
      value: 40.847
    - type: nauc_map_at_100_max
      value: 21.3978
    - type: nauc_map_at_100_std
      value: -1.4705
    - type: nauc_map_at_100_diff1
      value: 40.775
    - type: nauc_map_at_1000_max
      value: 21.4068
    - type: nauc_map_at_1000_std
      value: -1.4657
    - type: nauc_map_at_1000_diff1
      value: 40.7824
    - type: nauc_recall_at_1_max
      value: 22.1861
    - type: nauc_recall_at_1_std
      value: -3.218
    - type: nauc_recall_at_1_diff1
      value: 46.4989
    - type: nauc_recall_at_3_max
      value: 21.3684
    - type: nauc_recall_at_3_std
      value: -1.3554
    - type: nauc_recall_at_3_diff1
      value: 37.4804
    - type: nauc_recall_at_5_max
      value: 20.4902
    - type: nauc_recall_at_5_std
      value: -0.3449
    - type: nauc_recall_at_5_diff1
      value: 34.9587
    - type: nauc_recall_at_10_max
      value: 19.2959
    - type: nauc_recall_at_10_std
      value: 1.9666
    - type: nauc_recall_at_10_diff1
      value: 31.903
    - type: nauc_recall_at_20_max
      value: 18.6516
    - type: nauc_recall_at_20_std
      value: 3.9671
    - type: nauc_recall_at_20_diff1
      value: 30.576999999999998
    - type: nauc_recall_at_100_max
      value: 17.383699999999997
    - type: nauc_recall_at_100_std
      value: 11.050699999999999
    - type: nauc_recall_at_100_diff1
      value: 26.4222
    - type: nauc_recall_at_1000_max
      value: 17.1265
    - type: nauc_recall_at_1000_std
      value: 18.235699999999998
    - type: nauc_recall_at_1000_diff1
      value: 23.186300000000003
    - type: nauc_precision_at_1_max
      value: 22.1861
    - type: nauc_precision_at_1_std
      value: -3.218
    - type: nauc_precision_at_1_diff1
      value: 46.4989
    - type: nauc_precision_at_3_max
      value: 21.3684
    - type: nauc_precision_at_3_std
      value: -1.3554
    - type: nauc_precision_at_3_diff1
      value: 37.4804
    - type: nauc_precision_at_5_max
      value: 20.4902
    - type: nauc_precision_at_5_std
      value: -0.3449
    - type: nauc_precision_at_5_diff1
      value: 34.9587
    - type: nauc_precision_at_10_max
      value: 19.2959
    - type: nauc_precision_at_10_std
      value: 1.9666
    - type: nauc_precision_at_10_diff1
      value: 31.903
    - type: nauc_precision_at_20_max
      value: 18.6516
    - type: nauc_precision_at_20_std
      value: 3.9671
    - type: nauc_precision_at_20_diff1
      value: 30.576999999999998
    - type: nauc_precision_at_100_max
      value: 17.383699999999997
    - type: nauc_precision_at_100_std
      value: 11.050699999999999
    - type: nauc_precision_at_100_diff1
      value: 26.4222
    - type: nauc_precision_at_1000_max
      value: 17.1265
    - type: nauc_precision_at_1000_std
      value: 18.235699999999998
    - type: nauc_precision_at_1000_diff1
      value: 23.186300000000003
    - type: nauc_mrr_at_1_max
      value: 22.159000000000002
    - type: nauc_mrr_at_1_std
      value: -3.2346
    - type: nauc_mrr_at_1_diff1
      value: 46.4989
    - type: nauc_mrr_at_3_max
      value: 21.8304
    - type: nauc_mrr_at_3_std
      value: -2.4013
    - type: nauc_mrr_at_3_diff1
      value: 42.0356
    - type: nauc_mrr_at_5_max
      value: 21.617900000000002
    - type: nauc_mrr_at_5_std
      value: -2.1397
    - type: nauc_mrr_at_5_diff1
      value: 41.3793
    - type: nauc_mrr_at_10_max
      value: 21.467200000000002
    - type: nauc_mrr_at_10_std
      value: -1.7682
    - type: nauc_mrr_at_10_diff1
      value: 40.912
    - type: nauc_mrr_at_20_max
      value: 21.415200000000002
    - type: nauc_mrr_at_20_std
      value: -1.6295
    - type: nauc_mrr_at_20_diff1
      value: 40.8319
    - type: nauc_mrr_at_100_max
      value: 21.376800000000003
    - type: nauc_mrr_at_100_std
      value: -1.4815
    - type: nauc_mrr_at_100_diff1
      value: 40.760400000000004
    - type: nauc_mrr_at_1000_max
      value: 21.3858
    - type: nauc_mrr_at_1000_std
      value: -1.4767000000000001
    - type: nauc_mrr_at_1000_diff1
      value: 40.7677
    - type: main_score
      value: 30.791
    task:
      type: Retrieval
  - dataset:
      config: python
      name: MTEB CodeSearchNetRetrieval (python)
      revision: fdc6a9e39575768c27eb8a2a5f702bf846eb4759
      split: test
      type: code-search-net/code_search_net
    metrics:
    - type: ndcg_at_1
      value: 65.2
    - type: ndcg_at_3
      value: 76.41
    - type: ndcg_at_5
      value: 77.981
    - type: ndcg_at_10
      value: 79.044
    - type: ndcg_at_20
      value: 79.855
    - type: ndcg_at_100
      value: 80.622
    - type: ndcg_at_1000
      value: 80.806
    - type: map_at_1
      value: 65.2
    - type: map_at_3
      value: 73.65
    - type: map_at_5
      value: 74.52499999999999
    - type: map_at_10
      value: 74.98
    - type: map_at_20
      value: 75.203
    - type: map_at_100
      value: 75.319
    - type: map_at_1000
      value: 75.327
    - type: recall_at_1
      value: 65.2
    - type: recall_at_3
      value: 84.39999999999999
    - type: recall_at_5
      value: 88.2
    - type: recall_at_10
      value: 91.4
    - type: recall_at_20
      value: 94.6
    - type: recall_at_100
      value: 98.6
    - type: recall_at_1000
      value: 100.0
    - type: precision_at_1
      value: 65.2
    - type: precision_at_3
      value: 28.133000000000003
    - type: precision_at_5
      value: 17.64
    - type: precision_at_10
      value: 9.139999999999999
    - type: precision_at_20
      value: 4.73
    - type: precision_at_100
      value: 0.9860000000000001
    - type: precision_at_1000
      value: 0.1
    - type: mrr_at_1
      value: 65.2
    - type: mrr_at_3
      value: 73.65
    - type: mrr_at_5
      value: 74.52499999999999
    - type: mrr_at_10
      value: 74.9802
    - type: mrr_at_20
      value: 75.20320000000001
    - type: mrr_at_100
      value: 75.319
    - type: mrr_at_1000
      value: 75.3269
    - type: nauc_ndcg_at_1_max
      value: 36.4698
    - type: nauc_ndcg_at_1_std
      value: -10.8058
    - type: nauc_ndcg_at_1_diff1
      value: 70.5679
    - type: nauc_ndcg_at_3_max
      value: 40.582499999999996
    - type: nauc_ndcg_at_3_std
      value: -9.3767
    - type: nauc_ndcg_at_3_diff1
      value: 64.8235
    - type: nauc_ndcg_at_5_max
      value: 41.191100000000006
    - type: nauc_ndcg_at_5_std
      value: -8.6758
    - type: nauc_ndcg_at_5_diff1
      value: 64.70179999999999
    - type: nauc_ndcg_at_10_max
      value: 41.5913
    - type: nauc_ndcg_at_10_std
      value: -8.8502
    - type: nauc_ndcg_at_10_diff1
      value: 65.7197
    - type: nauc_ndcg_at_20_max
      value: 41.4419
    - type: nauc_ndcg_at_20_std
      value: -9.0406
    - type: nauc_ndcg_at_20_diff1
      value: 66.1819
    - type: nauc_ndcg_at_100_max
      value: 40.6791
    - type: nauc_ndcg_at_100_std
      value: -8.343499999999999
    - type: nauc_ndcg_at_100_diff1
      value: 66.468
    - type: nauc_ndcg_at_1000_max
      value: 40.3153
    - type: nauc_ndcg_at_1000_std
      value: -8.7689
    - type: nauc_ndcg_at_1000_diff1
      value: 66.49249999999999
    - type: nauc_map_at_1_max
      value: 36.4698
    - type: nauc_map_at_1_std
      value: -10.8058
    - type: nauc_map_at_1_diff1
      value: 70.5679
    - type: nauc_map_at_3_max
      value: 39.3299
    - type: nauc_map_at_3_std
      value: -9.4675
    - type: nauc_map_at_3_diff1
      value: 66.3583
    - type: nauc_map_at_5_max
      value: 39.5636
    - type: nauc_map_at_5_std
      value: -9.1881
    - type: nauc_map_at_5_diff1
      value: 66.37910000000001
    - type: nauc_map_at_10_max
      value: 39.6806
    - type: nauc_map_at_10_std
      value: -9.3088
    - type: nauc_map_at_10_diff1
      value: 66.8131
    - type: nauc_map_at_20_max
      value: 39.635999999999996
    - type: nauc_map_at_20_std
      value: -9.3305
    - type: nauc_map_at_20_diff1
      value: 66.93430000000001
    - type: nauc_map_at_100_max
      value: 39.536500000000004
    - type: nauc_map_at_100_std
      value: -9.1873
    - type: nauc_map_at_100_diff1
      value: 66.96419999999999
    - type: nauc_map_at_1000_max
      value: 39.5233
    - type: nauc_map_at_1000_std
      value: -9.200999999999999
    - type: nauc_map_at_1000_diff1
      value: 66.9634
    - type: nauc_recall_at_1_max
      value: 36.4698
    - type: nauc_recall_at_1_std
      value: -10.8058
    - type: nauc_recall_at_1_diff1
      value: 70.5679
    - type: nauc_recall_at_3_max
      value: 46.0932
    - type: nauc_recall_at_3_std
      value: -9.193900000000001
    - type: nauc_recall_at_3_diff1
      value: 58.2067
    - type: nauc_recall_at_5_max
      value: 50.2927
    - type: nauc_recall_at_5_std
      value: -5.8297
    - type: nauc_recall_at_5_diff1
      value: 55.6113
    - type: nauc_recall_at_10_max
      value: 55.961099999999995
    - type: nauc_recall_at_10_std
      value: -5.3568999999999996
    - type: nauc_recall_at_10_diff1
      value: 58.6075
    - type: nauc_recall_at_20_max
      value: 62.2869
    - type: nauc_recall_at_20_std
      value: -6.4927
    - type: nauc_recall_at_20_diff1
      value: 60.207699999999996
    - type: nauc_recall_at_100_max
      value: 73.4427
    - type: nauc_recall_at_100_std
      value: 31.606
    - type: nauc_recall_at_100_diff1
      value: 63.0919
    - type: nauc_recall_at_1000_max
      value: .nan
    - type: nauc_recall_at_1000_std
      value: .nan
    - type: nauc_recall_at_1000_diff1
      value: .nan
    - type: nauc_precision_at_1_max
      value: 36.4698
    - type: nauc_precision_at_1_std
      value: -10.8058
    - type: nauc_precision_at_1_diff1
      value: 70.5679
    - type: nauc_precision_at_3_max
      value: 46.0932
    - type: nauc_precision_at_3_std
      value: -9.193900000000001
    - type: nauc_precision_at_3_diff1
      value: 58.2067
    - type: nauc_precision_at_5_max
      value: 50.2927
    - type: nauc_precision_at_5_std
      value: -5.8297
    - type: nauc_precision_at_5_diff1
      value: 55.6113
    - type: nauc_precision_at_10_max
      value: 55.961099999999995
    - type: nauc_precision_at_10_std
      value: -5.3568999999999996
    - type: nauc_precision_at_10_diff1
      value: 58.6075
    - type: nauc_precision_at_20_max
      value: 62.2869
    - type: nauc_precision_at_20_std
      value: -6.4927
    - type: nauc_precision_at_20_diff1
      value: 60.207699999999996
    - type: nauc_precision_at_100_max
      value: 73.4427
    - type: nauc_precision_at_100_std
      value: 31.606
    - type: nauc_precision_at_100_diff1
      value: 63.0919
    - type: nauc_precision_at_1000_max
      value: .nan
    - type: nauc_precision_at_1000_std
      value: .nan
    - type: nauc_precision_at_1000_diff1
      value: .nan
    - type: nauc_mrr_at_1_max
      value: 36.4698
    - type: nauc_mrr_at_1_std
      value: -10.8058
    - type: nauc_mrr_at_1_diff1
      value: 70.5679
    - type: nauc_mrr_at_3_max
      value: 39.3299
    - type: nauc_mrr_at_3_std
      value: -9.4675
    - type: nauc_mrr_at_3_diff1
      value: 66.3583
    - type: nauc_mrr_at_5_max
      value: 39.5636
    - type: nauc_mrr_at_5_std
      value: -9.1881
    - type: nauc_mrr_at_5_diff1
      value: 66.37910000000001
    - type: nauc_mrr_at_10_max
      value: 39.6806
    - type: nauc_mrr_at_10_std
      value: -9.3088
    - type: nauc_mrr_at_10_diff1
      value: 66.8131
    - type: nauc_mrr_at_20_max
      value: 39.635999999999996
    - type: nauc_mrr_at_20_std
      value: -9.3305
    - type: nauc_mrr_at_20_diff1
      value: 66.93430000000001
    - type: nauc_mrr_at_100_max
      value: 39.536500000000004
    - type: nauc_mrr_at_100_std
      value: -9.1873
    - type: nauc_mrr_at_100_diff1
      value: 66.96419999999999
    - type: nauc_mrr_at_1000_max
      value: 39.5233
    - type: nauc_mrr_at_1000_std
      value: -9.200999999999999
    - type: nauc_mrr_at_1000_diff1
      value: 66.9634
    - type: main_score
      value: 79.044
    task:
      type: Retrieval
  - dataset:
      config: javascript
      name: MTEB CodeSearchNetRetrieval (javascript)
      revision: fdc6a9e39575768c27eb8a2a5f702bf846eb4759
      split: test
      type: code-search-net/code_search_net
    metrics:
    - type: ndcg_at_1
      value: 55.2
    - type: ndcg_at_3
      value: 63.709
    - type: ndcg_at_5
      value: 65.267
    - type: ndcg_at_10
      value: 67.239
    - type: ndcg_at_20
      value: 68.372
    - type: ndcg_at_100
      value: 69.854
    - type: ndcg_at_1000
      value: 70.831
    - type: map_at_1
      value: 55.2
    - type: map_at_3
      value: 61.667
    - type: map_at_5
      value: 62.527
    - type: map_at_10
      value: 63.339999999999996
    - type: map_at_20
      value: 63.648
    - type: map_at_100
      value: 63.854
    - type: map_at_1000
      value: 63.885999999999996
    - type: recall_at_1
      value: 55.2
    - type: recall_at_3
      value: 69.6
    - type: recall_at_5
      value: 73.4
    - type: recall_at_10
      value: 79.5
    - type: recall_at_20
      value: 84.0
    - type: recall_at_100
      value: 92.0
    - type: recall_at_1000
      value: 100.0
    - type: precision_at_1
      value: 55.2
    - type: precision_at_3
      value: 23.200000000000003
    - type: precision_at_5
      value: 14.680000000000001
    - type: precision_at_10
      value: 7.95
    - type: precision_at_20
      value: 4.2
    - type: precision_at_100
      value: 0.9199999999999999
    - type: precision_at_1000
      value: 0.1
    - type: mrr_at_1
      value: 55.2
    - type: mrr_at_3
      value: 61.6667
    - type: mrr_at_5
      value: 62.526700000000005
    - type: mrr_at_10
      value: 63.339999999999996
    - type: mrr_at_20
      value: 63.6484
    - type: mrr_at_100
      value: 63.854200000000006
    - type: mrr_at_1000
      value: 63.88549999999999
    - type: nauc_ndcg_at_1_max
      value: 48.821
    - type: nauc_ndcg_at_1_std
      value: 19.6886
    - type: nauc_ndcg_at_1_diff1
      value: 65.515
    - type: nauc_ndcg_at_3_max
      value: 56.316
    - type: nauc_ndcg_at_3_std
      value: 26.6555
    - type: nauc_ndcg_at_3_diff1
      value: 61.755300000000005
    - type: nauc_ndcg_at_5_max
      value: 57.566300000000005
    - type: nauc_ndcg_at_5_std
      value: 29.5288
    - type: nauc_ndcg_at_5_diff1
      value: 61.655300000000004
    - type: nauc_ndcg_at_10_max
      value: 58.89339999999999
    - type: nauc_ndcg_at_10_std
      value: 32.1136
    - type: nauc_ndcg_at_10_diff1
      value: 61.7916
    - type: nauc_ndcg_at_20_max
      value: 58.675999999999995
    - type: nauc_ndcg_at_20_std
      value: 32.2575
    - type: nauc_ndcg_at_20_diff1
      value: 62.5682
    - type: nauc_ndcg_at_100_max
      value: 57.6832
    - type: nauc_ndcg_at_100_std
      value: 31.2476
    - type: nauc_ndcg_at_100_diff1
      value: 62.356100000000005
    - type: nauc_ndcg_at_1000_max
      value: 56.9118
    - type: nauc_ndcg_at_1000_std
      value: 29.624499999999998
    - type: nauc_ndcg_at_1000_diff1
      value: 62.4914
    - type: nauc_map_at_1_max
      value: 48.821
    - type: nauc_map_at_1_std
      value: 19.6886
    - type: nauc_map_at_1_diff1
      value: 65.515
    - type: nauc_map_at_3_max
      value: 54.47260000000001
    - type: nauc_map_at_3_std
      value: 24.864800000000002
    - type: nauc_map_at_3_diff1
      value: 62.6644
    - type: nauc_map_at_5_max
      value: 55.1021
    - type: nauc_map_at_5_std
      value: 26.2921
    - type: nauc_map_at_5_diff1
      value: 62.624100000000006
    - type: nauc_map_at_10_max
      value: 55.552
    - type: nauc_map_at_10_std
      value: 27.199
    - type: nauc_map_at_10_diff1
      value: 62.7054
    - type: nauc_map_at_20_max
      value: 55.4708
    - type: nauc_map_at_20_std
      value: 27.2067
    - type: nauc_map_at_20_diff1
      value: 62.8945
    - type: nauc_map_at_100_max
      value: 55.3465
    - type: nauc_map_at_100_std
      value: 27.0926
    - type: nauc_map_at_100_diff1
      value: 62.8575
    - type: nauc_map_at_1000_max
      value: 55.3249
    - type: nauc_map_at_1000_std
      value: 27.0527
    - type: nauc_map_at_1000_diff1
      value: 62.8617
    - type: nauc_recall_at_1_max
      value: 48.821
    - type: nauc_recall_at_1_std
      value: 19.6886
    - type: nauc_recall_at_1_diff1
      value: 65.515
    - type: nauc_recall_at_3_max
      value: 62.36279999999999
    - type: nauc_recall_at_3_std
      value: 32.569199999999995
    - type: nauc_recall_at_3_diff1
      value: 58.781499999999994
    - type: nauc_recall_at_5_max
      value: 66.6246
    - type: nauc_recall_at_5_std
      value: 41.813
    - type: nauc_recall_at_5_diff1
      value: 58.1854
    - type: nauc_recall_at_10_max
      value: 74.4567
    - type: nauc_recall_at_10_std
      value: 55.835
    - type: nauc_recall_at_10_diff1
      value: 57.89189999999999
    - type: nauc_recall_at_20_max
      value: 76.9008
    - type: nauc_recall_at_20_std
      value: 62.54110000000001
    - type: nauc_recall_at_20_diff1
      value: 62.200500000000005
    - type: nauc_recall_at_100_max
      value: 76.46300000000001
    - type: nauc_recall_at_100_std
      value: 71.4723
    - type: nauc_recall_at_100_diff1
      value: 59.0844
    - type: nauc_recall_at_1000_max
      value: .nan
    - type: nauc_recall_at_1000_std
      value: .nan
    - type: nauc_recall_at_1000_diff1
      value: .nan
    - type: nauc_precision_at_1_max
      value: 48.821
    - type: nauc_precision_at_1_std
      value: 19.6886
    - type: nauc_precision_at_1_diff1
      value: 65.515
    - type: nauc_precision_at_3_max
      value: 62.36279999999999
    - type: nauc_precision_at_3_std
      value: 32.569199999999995
    - type: nauc_precision_at_3_diff1
      value: 58.781499999999994
    - type: nauc_precision_at_5_max
      value: 66.6246
    - type: nauc_precision_at_5_std
      value: 41.813
    - type: nauc_precision_at_5_diff1
      value: 58.1854
    - type: nauc_precision_at_10_max
      value: 74.4567
    - type: nauc_precision_at_10_std
      value: 55.835
    - type: nauc_precision_at_10_diff1
      value: 57.89189999999999
    - type: nauc_precision_at_20_max
      value: 76.9008
    - type: nauc_precision_at_20_std
      value: 62.54110000000001
    - type: nauc_precision_at_20_diff1
      value: 62.200500000000005
    - type: nauc_precision_at_100_max
      value: 76.46300000000001
    - type: nauc_precision_at_100_std
      value: 71.4723
    - type: nauc_precision_at_100_diff1
      value: 59.0844
    - type: nauc_precision_at_1000_max
      value: .nan
    - type: nauc_precision_at_1000_std
      value: .nan
    - type: nauc_precision_at_1000_diff1
      value: .nan
    - type: nauc_mrr_at_1_max
      value: 48.821
    - type: nauc_mrr_at_1_std
      value: 19.6886
    - type: nauc_mrr_at_1_diff1
      value: 65.515
    - type: nauc_mrr_at_3_max
      value: 54.47260000000001
    - type: nauc_mrr_at_3_std
      value: 24.864800000000002
    - type: nauc_mrr_at_3_diff1
      value: 62.6644
    - type: nauc_mrr_at_5_max
      value: 55.1021
    - type: nauc_mrr_at_5_std
      value: 26.2921
    - type: nauc_mrr_at_5_diff1
      value: 62.624100000000006
    - type: nauc_mrr_at_10_max
      value: 55.552
    - type: nauc_mrr_at_10_std
      value: 27.199
    - type: nauc_mrr_at_10_diff1
      value: 62.7054
    - type: nauc_mrr_at_20_max
      value: 55.4708
    - type: nauc_mrr_at_20_std
      value: 27.2067
    - type: nauc_mrr_at_20_diff1
      value: 62.8945
    - type: nauc_mrr_at_100_max
      value: 55.3465
    - type: nauc_mrr_at_100_std
      value: 27.0926
    - type: nauc_mrr_at_100_diff1
      value: 62.8575
    - type: nauc_mrr_at_1000_max
      value: 55.3249
    - type: nauc_mrr_at_1000_std
      value: 27.0527
    - type: nauc_mrr_at_1000_diff1
      value: 62.8617
    - type: main_score
      value: 67.239
    task:
      type: Retrieval
  - dataset:
      config: go
      name: MTEB CodeSearchNetRetrieval (go)
      revision: fdc6a9e39575768c27eb8a2a5f702bf846eb4759
      split: test
      type: code-search-net/code_search_net
    metrics:
    - type: ndcg_at_1
      value: 70.19999999999999
    - type: ndcg_at_3
      value: 79.566
    - type: ndcg_at_5
      value: 81.012
    - type: ndcg_at_10
      value: 82.217
    - type: ndcg_at_20
      value: 82.97
    - type: ndcg_at_100
      value: 83.43199999999999
    - type: ndcg_at_1000
      value: 83.597
    - type: map_at_1
      value: 70.19999999999999
    - type: map_at_3
      value: 77.333
    - type: map_at_5
      value: 78.13799999999999
    - type: map_at_10
      value: 78.641
    - type: map_at_20
      value: 78.84400000000001
    - type: map_at_100
      value: 78.908
    - type: map_at_1000
      value: 78.914
    - type: recall_at_1
      value: 70.19999999999999
    - type: recall_at_3
      value: 86.0
    - type: recall_at_5
      value: 89.5
    - type: recall_at_10
      value: 93.2
    - type: recall_at_20
      value: 96.2
    - type: recall_at_100
      value: 98.7
    - type: recall_at_1000
      value: 100.0
    - type: precision_at_1
      value: 70.19999999999999
    - type: precision_at_3
      value: 28.666999999999998
    - type: precision_at_5
      value: 17.9
    - type: precision_at_10
      value: 9.32
    - type: precision_at_20
      value: 4.81
    - type: precision_at_100
      value: 0.987
    - type: precision_at_1000
      value: 0.1
    - type: mrr_at_1
      value: 70.19999999999999
    - type: mrr_at_3
      value: 77.33330000000001
    - type: mrr_at_5
      value: 78.1383
    - type: mrr_at_10
      value: 78.6408
    - type: mrr_at_20
      value: 78.8441
    - type: mrr_at_100
      value: 78.9075
    - type: mrr_at_1000
      value: 78.91369999999999
    - type: nauc_ndcg_at_1_max
      value: 54.447199999999995
    - type: nauc_ndcg_at_1_std
      value: 5.7226
    - type: nauc_ndcg_at_1_diff1
      value: 71.1626
    - type: nauc_ndcg_at_3_max
      value: 60.4446
    - type: nauc_ndcg_at_3_std
      value: 6.2227
    - type: nauc_ndcg_at_3_diff1
      value: 69.419
    - type: nauc_ndcg_at_5_max
      value: 59.7692
    - type: nauc_ndcg_at_5_std
      value: 7.4161
    - type: nauc_ndcg_at_5_diff1
      value: 68.9958
    - type: nauc_ndcg_at_10_max
      value: 59.559
    - type: nauc_ndcg_at_10_std
      value: 6.792199999999999
    - type: nauc_ndcg_at_10_diff1
      value: 68.42099999999999
    - type: nauc_ndcg_at_20_max
      value: 59.1576
    - type: nauc_ndcg_at_20_std
      value: 6.762600000000001
    - type: nauc_ndcg_at_20_diff1
      value: 69.1402
    - type: nauc_ndcg_at_100_max
      value: 58.729699999999994
    - type: nauc_ndcg_at_100_std
      value: 6.6151
    - type: nauc_ndcg_at_100_diff1
      value: 69.3485
    - type: nauc_ndcg_at_1000_max
      value: 58.68879999999999
    - type: nauc_ndcg_at_1000_std
      value: 6.5546999999999995
    - type: nauc_ndcg_at_1000_diff1
      value: 69.3974
    - type: nauc_map_at_1_max
      value: 54.447199999999995
    - type: nauc_map_at_1_std
      value: 5.7226
    - type: nauc_map_at_1_diff1
      value: 71.1626
    - type: nauc_map_at_3_max
      value: 58.82150000000001
    - type: nauc_map_at_3_std
      value: 6.111
    - type: nauc_map_at_3_diff1
      value: 69.8853
    - type: nauc_map_at_5_max
      value: 58.4332
    - type: nauc_map_at_5_std
      value: 6.6455
    - type: nauc_map_at_5_diff1
      value: 69.6593
    - type: nauc_map_at_10_max
      value: 58.3284
    - type: nauc_map_at_10_std
      value: 6.3941
    - type: nauc_map_at_10_diff1
      value: 69.4544
    - type: nauc_map_at_20_max
      value: 58.2269
    - type: nauc_map_at_20_std
      value: 6.3983
    - type: nauc_map_at_20_diff1
      value: 69.634
    - type: nauc_map_at_100_max
      value: 58.180299999999995
    - type: nauc_map_at_100_std
      value: 6.372
    - type: nauc_map_at_100_diff1
      value: 69.6674
    - type: nauc_map_at_1000_max
      value: 58.1796
    - type: nauc_map_at_1000_std
      value: 6.3696
    - type: nauc_map_at_1000_diff1
      value: 69.6689
    - type: nauc_recall_at_1_max
      value: 54.447199999999995
    - type: nauc_recall_at_1_std
      value: 5.7226
    - type: nauc_recall_at_1_diff1
      value: 71.1626
    - type: nauc_recall_at_3_max
      value: 67.3635
    - type: nauc_recall_at_3_std
      value: 6.682499999999999
    - type: nauc_recall_at_3_diff1
      value: 67.4356
    - type: nauc_recall_at_5_max
      value: 66.6632
    - type: nauc_recall_at_5_std
      value: 11.969899999999999
    - type: nauc_recall_at_5_diff1
      value: 65.4311
    - type: nauc_recall_at_10_max
      value: 68.76339999999999
    - type: nauc_recall_at_10_std
      value: 10.0319
    - type: nauc_recall_at_10_diff1
      value: 59.6357
    - type: nauc_recall_at_20_max
      value: 69.58569999999999
    - type: nauc_recall_at_20_std
      value: 11.5374
    - type: nauc_recall_at_20_diff1
      value: 63.8926
    - type: nauc_recall_at_100_max
      value: 62.5009
    - type: nauc_recall_at_100_std
      value: 12.447
    - type: nauc_recall_at_100_diff1
      value: 65.065
    - type: nauc_recall_at_1000_max
      value: .nan
    - type: nauc_recall_at_1000_std
      value: .nan
    - type: nauc_recall_at_1000_diff1
      value: .nan
    - type: nauc_precision_at_1_max
      value: 54.447199999999995
    - type: nauc_precision_at_1_std
      value: 5.7226
    - type: nauc_precision_at_1_diff1
      value: 71.1626
    - type: nauc_precision_at_3_max
      value: 67.3635
    - type: nauc_precision_at_3_std
      value: 6.682499999999999
    - type: nauc_precision_at_3_diff1
      value: 67.4356
    - type: nauc_precision_at_5_max
      value: 66.6632
    - type: nauc_precision_at_5_std
      value: 11.969899999999999
    - type: nauc_precision_at_5_diff1
      value: 65.4311
    - type: nauc_precision_at_10_max
      value: 68.76339999999999
    - type: nauc_precision_at_10_std
      value: 10.0319
    - type: nauc_precision_at_10_diff1
      value: 59.6357
    - type: nauc_precision_at_20_max
      value: 69.58569999999999
    - type: nauc_precision_at_20_std
      value: 11.5374
    - type: nauc_precision_at_20_diff1
      value: 63.8926
    - type: nauc_precision_at_100_max
      value: 62.5009
    - type: nauc_precision_at_100_std
      value: 12.447
    - type: nauc_precision_at_100_diff1
      value: 65.065
    - type: nauc_precision_at_1000_max
      value: .nan
    - type: nauc_precision_at_1000_std
      value: .nan
    - type: nauc_precision_at_1000_diff1
      value: .nan
    - type: nauc_mrr_at_1_max
      value: 54.447199999999995
    - type: nauc_mrr_at_1_std
      value: 5.7226
    - type: nauc_mrr_at_1_diff1
      value: 71.1626
    - type: nauc_mrr_at_3_max
      value: 58.82150000000001
    - type: nauc_mrr_at_3_std
      value: 6.111
    - type: nauc_mrr_at_3_diff1
      value: 69.8853
    - type: nauc_mrr_at_5_max
      value: 58.4332
    - type: nauc_mrr_at_5_std
      value: 6.6455
    - type: nauc_mrr_at_5_diff1
      value: 69.6593
    - type: nauc_mrr_at_10_max
      value: 58.3284
    - type: nauc_mrr_at_10_std
      value: 6.3941
    - type: nauc_mrr_at_10_diff1
      value: 69.4544
    - type: nauc_mrr_at_20_max
      value: 58.2269
    - type: nauc_mrr_at_20_std
      value: 6.3983
    - type: nauc_mrr_at_20_diff1
      value: 69.634
    - type: nauc_mrr_at_100_max
      value: 58.180299999999995
    - type: nauc_mrr_at_100_std
      value: 6.372
    - type: nauc_mrr_at_100_diff1
      value: 69.6674
    - type: nauc_mrr_at_1000_max
      value: 58.1796
    - type: nauc_mrr_at_1000_std
      value: 6.3696
    - type: nauc_mrr_at_1000_diff1
      value: 69.6689
    - type: main_score
      value: 82.217
    task:
      type: Retrieval
  - dataset:
      config: ruby
      name: MTEB CodeSearchNetRetrieval (ruby)
      revision: fdc6a9e39575768c27eb8a2a5f702bf846eb4759
      split: test
      type: code-search-net/code_search_net
    metrics:
    - type: ndcg_at_1
      value: 56.49999999999999
    - type: ndcg_at_3
      value: 66.597
    - type: ndcg_at_5
      value: 68.98100000000001
    - type: ndcg_at_10
      value: 70.829
    - type: ndcg_at_20
      value: 71.77799999999999
    - type: ndcg_at_100
      value: 72.85199999999999
    - type: ndcg_at_1000
      value: 73.563
    - type: map_at_1
      value: 56.49999999999999
    - type: map_at_3
      value: 64.2
    - type: map_at_5
      value: 65.52
    - type: map_at_10
      value: 66.305
    - type: map_at_20
      value: 66.572
    - type: map_at_100
      value: 66.733
    - type: map_at_1000
      value: 66.756
    - type: recall_at_1
      value: 56.49999999999999
    - type: recall_at_3
      value: 73.5
    - type: recall_at_5
      value: 79.3
    - type: recall_at_10
      value: 84.89999999999999
    - type: recall_at_20
      value: 88.6
    - type: recall_at_100
      value: 94.19999999999999
    - type: recall_at_1000
      value: 100.0
    - type: precision_at_1
      value: 56.49999999999999
    - type: precision_at_3
      value: 24.5
    - type: precision_at_5
      value: 15.86
    - type: precision_at_10
      value: 8.49
    - type: precision_at_20
      value: 4.43
    - type: precision_at_100
      value: 0.942
    - type: precision_at_1000
      value: 0.1
    - type: mrr_at_1
      value: 56.49999999999999
    - type: mrr_at_3
      value: 64.2
    - type: mrr_at_5
      value: 65.52
    - type: mrr_at_10
      value: 66.30460000000001
    - type: mrr_at_20
      value: 66.5724
    - type: mrr_at_100
      value: 66.7334
    - type: mrr_at_1000
      value: 66.7564
    - type: nauc_ndcg_at_1_max
      value: 55.3207
    - type: nauc_ndcg_at_1_std
      value: 7.2139
    - type: nauc_ndcg_at_1_diff1
      value: 72.6385
    - type: nauc_ndcg_at_3_max
      value: 58.4997
    - type: nauc_ndcg_at_3_std
      value: 8.3729
    - type: nauc_ndcg_at_3_diff1
      value: 69.0137
    - type: nauc_ndcg_at_5_max
      value: 58.213899999999995
    - type: nauc_ndcg_at_5_std
      value: 11.8464
    - type: nauc_ndcg_at_5_diff1
      value: 67.8369
    - type: nauc_ndcg_at_10_max
      value: 58.2068
    - type: nauc_ndcg_at_10_std
      value: 13.320000000000002
    - type: nauc_ndcg_at_10_diff1
      value: 67.8139
    - type: nauc_ndcg_at_20_max
      value: 58.0545
    - type: nauc_ndcg_at_20_std
      value: 13.601199999999999
    - type: nauc_ndcg_at_20_diff1
      value: 67.814
    - type: nauc_ndcg_at_100_max
      value: 58.1651
    - type: nauc_ndcg_at_100_std
      value: 13.946900000000001
    - type: nauc_ndcg_at_100_diff1
      value: 68.07180000000001
    - type: nauc_ndcg_at_1000_max
      value: 57.9397
    - type: nauc_ndcg_at_1000_std
      value: 12.188400000000001
    - type: nauc_ndcg_at_1000_diff1
      value: 68.6001
    - type: nauc_map_at_1_max
      value: 55.3207
    - type: nauc_map_at_1_std
      value: 7.2139
    - type: nauc_map_at_1_diff1
      value: 72.6385
    - type: nauc_map_at_3_max
      value: 57.678399999999996
    - type: nauc_map_at_3_std
      value: 7.900500000000001
    - type: nauc_map_at_3_diff1
      value: 69.8646
    - type: nauc_map_at_5_max
      value: 57.5229
    - type: nauc_map_at_5_std
      value: 9.7157
    - type: nauc_map_at_5_diff1
      value: 69.2704
    - type: nauc_map_at_10_max
      value: 57.5133
    - type: nauc_map_at_10_std
      value: 10.2078
    - type: nauc_map_at_10_diff1
      value: 69.2876
    - type: nauc_map_at_20_max
      value: 57.4843
    - type: nauc_map_at_20_std
      value: 10.2501
    - type: nauc_map_at_20_diff1
      value: 69.303
    - type: nauc_map_at_100_max
      value: 57.4927
    - type: nauc_map_at_100_std
      value: 10.3077
    - type: nauc_map_at_100_diff1
      value: 69.3295
    - type: nauc_map_at_1000_max
      value: 57.4921
    - type: nauc_map_at_1000_std
      value: 10.2661
    - type: nauc_map_at_1000_diff1
      value: 69.3497
    - type: nauc_recall_at_1_max
      value: 55.3207
    - type: nauc_recall_at_1_std
      value: 7.2139
    - type: nauc_recall_at_1_diff1
      value: 72.6385
    - type: nauc_recall_at_3_max
      value: 61.36899999999999
    - type: nauc_recall_at_3_std
      value: 10.1165
    - type: nauc_recall_at_3_diff1
      value: 66.0874
    - type: nauc_recall_at_5_max
      value: 60.956999999999994
    - type: nauc_recall_at_5_std
      value: 21.409
    - type: nauc_recall_at_5_diff1
      value: 61.770199999999996
    - type: nauc_recall_at_10_max
      value: 61.73689999999999
    - type: nauc_recall_at_10_std
      value: 32.1058
    - type: nauc_recall_at_10_diff1
      value: 59.7434
    - type: nauc_recall_at_20_max
      value: 61.2737
    - type: nauc_recall_at_20_std
      value: 39.7564
    - type: nauc_recall_at_20_diff1
      value: 57.3813
    - type: nauc_recall_at_100_max
      value: 66.6667
    - type: nauc_recall_at_100_std
      value: 69.0613
    - type: nauc_recall_at_100_diff1
      value: 53.7574
    - type: nauc_recall_at_1000_max
      value: .nan
    - type: nauc_recall_at_1000_std
      value: .nan
    - type: nauc_recall_at_1000_diff1
      value: .nan
    - type: nauc_precision_at_1_max
      value: 55.3207
    - type: nauc_precision_at_1_std
      value: 7.2139
    - type: nauc_precision_at_1_diff1
      value: 72.6385
    - type: nauc_precision_at_3_max
      value: 61.36899999999999
    - type: nauc_precision_at_3_std
      value: 10.1165
    - type: nauc_precision_at_3_diff1
      value: 66.0874
    - type: nauc_precision_at_5_max
      value: 60.956999999999994
    - type: nauc_precision_at_5_std
      value: 21.409
    - type: nauc_precision_at_5_diff1
      value: 61.770199999999996
    - type: nauc_precision_at_10_max
      value: 61.73689999999999
    - type: nauc_precision_at_10_std
      value: 32.1058
    - type: nauc_precision_at_10_diff1
      value: 59.7434
    - type: nauc_precision_at_20_max
      value: 61.2737
    - type: nauc_precision_at_20_std
      value: 39.7564
    - type: nauc_precision_at_20_diff1
      value: 57.3813
    - type: nauc_precision_at_100_max
      value: 66.6667
    - type: nauc_precision_at_100_std
      value: 69.0613
    - type: nauc_precision_at_100_diff1
      value: 53.7574
    - type: nauc_precision_at_1000_max
      value: .nan
    - type: nauc_precision_at_1000_std
      value: .nan
    - type: nauc_precision_at_1000_diff1
      value: .nan
    - type: nauc_mrr_at_1_max
      value: 55.3207
    - type: nauc_mrr_at_1_std
      value: 7.2139
    - type: nauc_mrr_at_1_diff1
      value: 72.6385
    - type: nauc_mrr_at_3_max
      value: 57.678399999999996
    - type: nauc_mrr_at_3_std
      value: 7.900500000000001
    - type: nauc_mrr_at_3_diff1
      value: 69.8646
    - type: nauc_mrr_at_5_max
      value: 57.5229
    - type: nauc_mrr_at_5_std
      value: 9.7157
    - type: nauc_mrr_at_5_diff1
      value: 69.2704
    - type: nauc_mrr_at_10_max
      value: 57.5133
    - type: nauc_mrr_at_10_std
      value: 10.2078
    - type: nauc_mrr_at_10_diff1
      value: 69.2876
    - type: nauc_mrr_at_20_max
      value: 57.4843
    - type: nauc_mrr_at_20_std
      value: 10.2501
    - type: nauc_mrr_at_20_diff1
      value: 69.303
    - type: nauc_mrr_at_100_max
      value: 57.4927
    - type: nauc_mrr_at_100_std
      value: 10.3077
    - type: nauc_mrr_at_100_diff1
      value: 69.3295
    - type: nauc_mrr_at_1000_max
      value: 57.4921
    - type: nauc_mrr_at_1000_std
      value: 10.2661
    - type: nauc_mrr_at_1000_diff1
      value: 69.3497
    - type: main_score
      value: 70.829
    task:
      type: Retrieval
  - dataset:
      config: java
      name: MTEB CodeSearchNetRetrieval (java)
      revision: fdc6a9e39575768c27eb8a2a5f702bf846eb4759
      split: test
      type: code-search-net/code_search_net
    metrics:
    - type: ndcg_at_1
      value: 50.3
    - type: ndcg_at_3
      value: 62.883
    - type: ndcg_at_5
      value: 65.11200000000001
    - type: ndcg_at_10
      value: 67.044
    - type: ndcg_at_20
      value: 68.326
    - type: ndcg_at_100
      value: 69.592
    - type: ndcg_at_1000
      value: 70.209
    - type: map_at_1
      value: 50.3
    - type: map_at_3
      value: 59.8
    - type: map_at_5
      value: 61.040000000000006
    - type: map_at_10
      value: 61.852
    - type: map_at_20
      value: 62.212999999999994
    - type: map_at_100
      value: 62.397000000000006
    - type: map_at_1000
      value: 62.416000000000004
    - type: recall_at_1
      value: 50.3
    - type: recall_at_3
      value: 71.8
    - type: recall_at_5
      value: 77.2
    - type: recall_at_10
      value: 83.1
    - type: recall_at_20
      value: 88.1
    - type: recall_at_100
      value: 94.8
    - type: recall_at_1000
      value: 100.0
    - type: precision_at_1
      value: 50.3
    - type: precision_at_3
      value: 23.933
    - type: precision_at_5
      value: 15.440000000000001
    - type: precision_at_10
      value: 8.309999999999999
    - type: precision_at_20
      value: 4.405
    - type: precision_at_100
      value: 0.9480000000000001
    - type: precision_at_1000
      value: 0.1
    - type: mrr_at_1
      value: 50.3
    - type: mrr_at_3
      value: 59.8
    - type: mrr_at_5
      value: 61.040000000000006
    - type: mrr_at_10
      value: 61.8522
    - type: mrr_at_20
      value: 62.21339999999999
    - type: mrr_at_100
      value: 62.397499999999994
    - type: mrr_at_1000
      value: 62.415600000000005
    - type: nauc_ndcg_at_1_max
      value: 27.9845
    - type: nauc_ndcg_at_1_std
      value: -16.28
    - type: nauc_ndcg_at_1_diff1
      value: 61.9927
    - type: nauc_ndcg_at_3_max
      value: 33.0521
    - type: nauc_ndcg_at_3_std
      value: -10.3558
    - type: nauc_ndcg_at_3_diff1
      value: 56.8436
    - type: nauc_ndcg_at_5_max
      value: 34.6635
    - type: nauc_ndcg_at_5_std
      value: -7.1861
    - type: nauc_ndcg_at_5_diff1
      value: 56.39999999999999
    - type: nauc_ndcg_at_10_max
      value: 36.0742
    - type: nauc_ndcg_at_10_std
      value: -6.1496
    - type: nauc_ndcg_at_10_diff1
      value: 57.239
    - type: nauc_ndcg_at_20_max
      value: 36.5836
    - type: nauc_ndcg_at_20_std
      value: -5.3723
    - type: nauc_ndcg_at_20_diff1
      value: 57.7333
    - type: nauc_ndcg_at_100_max
      value: 36.0909
    - type: nauc_ndcg_at_100_std
      value: -5.655799999999999
    - type: nauc_ndcg_at_100_diff1
      value: 58.411699999999996
    - type: nauc_ndcg_at_1000_max
      value: 34.8377
    - type: nauc_ndcg_at_1000_std
      value: -7.542999999999999
    - type: nauc_ndcg_at_1000_diff1
      value: 58.198899999999995
    - type: nauc_map_at_1_max
      value: 27.9845
    - type: nauc_map_at_1_std
      value: -16.28
    - type: nauc_map_at_1_diff1
      value: 61.9927
    - type: nauc_map_at_3_max
      value: 31.7824
    - type: nauc_map_at_3_std
      value: -11.9282
    - type: nauc_map_at_3_diff1
      value: 58.2543
    - type: nauc_map_at_5_max
      value: 32.5811
    - type: nauc_map_at_5_std
      value: -10.3315
    - type: nauc_map_at_5_diff1
      value: 58.046
    - type: nauc_map_at_10_max
      value: 33.0525
    - type: nauc_map_at_10_std
      value: -10.0071
    - type: nauc_map_at_10_diff1
      value: 58.3778
    - type: nauc_map_at_20_max
      value: 33.164
    - type: nauc_map_at_20_std
      value: -9.8753
    - type: nauc_map_at_20_diff1
      value: 58.5075
    - type: nauc_map_at_100_max
      value: 33.0857
    - type: nauc_map_at_100_std
      value: -9.9373
    - type: nauc_map_at_100_diff1
      value: 58.581399999999995
    - type: nauc_map_at_1000_max
      value: 33.0589
    - type: nauc_map_at_1000_std
      value: -9.9773
    - type: nauc_map_at_1000_diff1
      value: 58.5777
    - type: nauc_recall_at_1_max
      value: 27.9845
    - type: nauc_recall_at_1_std
      value: -16.28
    - type: nauc_recall_at_1_diff1
      value: 61.9927
    - type: nauc_recall_at_3_max
      value: 37.5284
    - type: nauc_recall_at_3_std
      value: -4.7627999999999995
    - type: nauc_recall_at_3_diff1
      value: 51.8022
    - type: nauc_recall_at_5_max
      value: 43.4852
    - type: nauc_recall_at_5_std
      value: 6.3649
    - type: nauc_recall_at_5_diff1
      value: 49.5664
    - type: nauc_recall_at_10_max
      value: 53.156000000000006
    - type: nauc_recall_at_10_std
      value: 15.4361
    - type: nauc_recall_at_10_diff1
      value: 51.865300000000005
    - type: nauc_recall_at_20_max
      value: 63.3834
    - type: nauc_recall_at_20_std
      value: 30.2094
    - type: nauc_recall_at_20_diff1
      value: 54.013999999999996
    - type: nauc_recall_at_100_max
      value: 84.36399999999999
    - type: nauc_recall_at_100_std
      value: 67.20089999999999
    - type: nauc_recall_at_100_diff1
      value: 66.6146
    - type: nauc_recall_at_1000_max
      value: .nan
    - type: nauc_recall_at_1000_std
      value: .nan
    - type: nauc_recall_at_1000_diff1
      value: .nan
    - type: nauc_precision_at_1_max
      value: 27.9845
    - type: nauc_precision_at_1_std
      value: -16.28
    - type: nauc_precision_at_1_diff1
      value: 61.9927
    - type: nauc_precision_at_3_max
      value: 37.5284
    - type: nauc_precision_at_3_std
      value: -4.7627999999999995
    - type: nauc_precision_at_3_diff1
      value: 51.8022
    - type: nauc_precision_at_5_max
      value: 43.4852
    - type: nauc_precision_at_5_std
      value: 6.3649
    - type: nauc_precision_at_5_diff1
      value: 49.5664
    - type: nauc_precision_at_10_max
      value: 53.156000000000006
    - type: nauc_precision_at_10_std
      value: 15.4361
    - type: nauc_precision_at_10_diff1
      value: 51.865300000000005
    - type: nauc_precision_at_20_max
      value: 63.3834
    - type: nauc_precision_at_20_std
      value: 30.2094
    - type: nauc_precision_at_20_diff1
      value: 54.013999999999996
    - type: nauc_precision_at_100_max
      value: 84.36399999999999
    - type: nauc_precision_at_100_std
      value: 67.20089999999999
    - type: nauc_precision_at_100_diff1
      value: 66.6146
    - type: nauc_precision_at_1000_max
      value: .nan
    - type: nauc_precision_at_1000_std
      value: .nan
    - type: nauc_precision_at_1000_diff1
      value: .nan
    - type: nauc_mrr_at_1_max
      value: 27.9845
    - type: nauc_mrr_at_1_std
      value: -16.28
    - type: nauc_mrr_at_1_diff1
      value: 61.9927
    - type: nauc_mrr_at_3_max
      value: 31.7824
    - type: nauc_mrr_at_3_std
      value: -11.9282
    - type: nauc_mrr_at_3_diff1
      value: 58.2543
    - type: nauc_mrr_at_5_max
      value: 32.5811
    - type: nauc_mrr_at_5_std
      value: -10.3315
    - type: nauc_mrr_at_5_diff1
      value: 58.046
    - type: nauc_mrr_at_10_max
      value: 33.0525
    - type: nauc_mrr_at_10_std
      value: -10.0071
    - type: nauc_mrr_at_10_diff1
      value: 58.3778
    - type: nauc_mrr_at_20_max
      value: 33.164
    - type: nauc_mrr_at_20_std
      value: -9.8753
    - type: nauc_mrr_at_20_diff1
      value: 58.5075
    - type: nauc_mrr_at_100_max
      value: 33.0857
    - type: nauc_mrr_at_100_std
      value: -9.9373
    - type: nauc_mrr_at_100_diff1
      value: 58.581399999999995
    - type: nauc_mrr_at_1000_max
      value: 33.0589
    - type: nauc_mrr_at_1000_std
      value: -9.9773
    - type: nauc_mrr_at_1000_diff1
      value: 58.5777
    - type: main_score
      value: 67.044
    task:
      type: Retrieval
  - dataset:
      config: php
      name: MTEB CodeSearchNetRetrieval (php)
      revision: fdc6a9e39575768c27eb8a2a5f702bf846eb4759
      split: test
      type: code-search-net/code_search_net
    metrics:
    - type: ndcg_at_1
      value: 52.5
    - type: ndcg_at_3
      value: 65.362
    - type: ndcg_at_5
      value: 67.797
    - type: ndcg_at_10
      value: 69.791
    - type: ndcg_at_20
      value: 70.787
    - type: ndcg_at_100
      value: 71.607
    - type: ndcg_at_1000
      value: 72.24000000000001
    - type: map_at_1
      value: 52.5
    - type: map_at_3
      value: 62.233000000000004
    - type: map_at_5
      value: 63.588
    - type: map_at_10
      value: 64.424
    - type: map_at_20
      value: 64.703
    - type: map_at_100
      value: 64.825
    - type: map_at_1000
      value: 64.84100000000001
    - type: recall_at_1
      value: 52.5
    - type: recall_at_3
      value: 74.4
    - type: recall_at_5
      value: 80.30000000000001
    - type: recall_at_10
      value: 86.4
    - type: recall_at_20
      value: 90.3
    - type: recall_at_100
      value: 94.6
    - type: recall_at_1000
      value: 100.0
    - type: precision_at_1
      value: 52.5
    - type: precision_at_3
      value: 24.8
    - type: precision_at_5
      value: 16.06
    - type: precision_at_10
      value: 8.64
    - type: precision_at_20
      value: 4.515000000000001
    - type: precision_at_100
      value: 0.946
    - type: precision_at_1000
      value: 0.1
    - type: mrr_at_1
      value: 52.5
    - type: mrr_at_3
      value: 62.2333
    - type: mrr_at_5
      value: 63.5883
    - type: mrr_at_10
      value: 64.4237
    - type: mrr_at_20
      value: 64.7029
    - type: mrr_at_100
      value: 64.8249
    - type: mrr_at_1000
      value: 64.84140000000001
    - type: nauc_ndcg_at_1_max
      value: 28.977700000000002
    - type: nauc_ndcg_at_1_std
      value: 5.5688
    - type: nauc_ndcg_at_1_diff1
      value: 62.8127
    - type: nauc_ndcg_at_3_max
      value: 42.5053
    - type: nauc_ndcg_at_3_std
      value: 13.8126
    - type: nauc_ndcg_at_3_diff1
      value: 60.791700000000006
    - type: nauc_ndcg_at_5_max
      value: 43.521100000000004
    - type: nauc_ndcg_at_5_std
      value: 14.5838
    - type: nauc_ndcg_at_5_diff1
      value: 61.267700000000005
    - type: nauc_ndcg_at_10_max
      value: 43.2523
    - type: nauc_ndcg_at_10_std
      value: 16.2237
    - type: nauc_ndcg_at_10_diff1
      value: 61.642300000000006
    - type: nauc_ndcg_at_20_max
      value: 42.7707
    - type: nauc_ndcg_at_20_std
      value: 17.0607
    - type: nauc_ndcg_at_20_diff1
      value: 61.5855
    - type: nauc_ndcg_at_100_max
      value: 42.127900000000004
    - type: nauc_ndcg_at_100_std
      value: 16.582900000000002
    - type: nauc_ndcg_at_100_diff1
      value: 61.916700000000006
    - type: nauc_ndcg_at_1000_max
      value: 40.7945
    - type: nauc_ndcg_at_1000_std
      value: 14.6562
    - type: nauc_ndcg_at_1000_diff1
      value: 61.7069
    - type: nauc_map_at_1_max
      value: 28.977700000000002
    - type: nauc_map_at_1_std
      value: 5.5688
    - type: nauc_map_at_1_diff1
      value: 62.8127
    - type: nauc_map_at_3_max
      value: 38.5313
    - type: nauc_map_at_3_std
      value: 11.2395
    - type: nauc_map_at_3_diff1
      value: 61.1888
    - type: nauc_map_at_5_max
      value: 38.8835
    - type: nauc_map_at_5_std
      value: 11.5395
    - type: nauc_map_at_5_diff1
      value: 61.449
    - type: nauc_map_at_10_max
      value: 38.6822
    - type: nauc_map_at_10_std
      value: 12.0181
    - type: nauc_map_at_10_diff1
      value: 61.5846
    - type: nauc_map_at_20_max
      value: 38.5328
    - type: nauc_map_at_20_std
      value: 12.182500000000001
    - type: nauc_map_at_20_diff1
      value: 61.578599999999994
    - type: nauc_map_at_100_max
      value: 38.4484
    - type: nauc_map_at_100_std
      value: 12.1157
    - type: nauc_map_at_100_diff1
      value: 61.6247
    - type: nauc_map_at_1000_max
      value: 38.418600000000005
    - type: nauc_map_at_1000_std
      value: 12.0795
    - type: nauc_map_at_1000_diff1
      value: 61.6214
    - type: nauc_recall_at_1_max
      value: 28.977700000000002
    - type: nauc_recall_at_1_std
      value: 5.5688
    - type: nauc_recall_at_1_diff1
      value: 62.8127
    - type: nauc_recall_at_3_max
      value: 57.338699999999996
    - type: nauc_recall_at_3_std
      value: 23.4946
    - type: nauc_recall_at_3_diff1
      value: 59.4094
    - type: nauc_recall_at_5_max
      value: 64.4058
    - type: nauc_recall_at_5_std
      value: 28.382
    - type: nauc_recall_at_5_diff1
      value: 60.671600000000005
    - type: nauc_recall_at_10_max
      value: 71.11070000000001
    - type: nauc_recall_at_10_std
      value: 43.6152
    - type: nauc_recall_at_10_diff1
      value: 62.6013
    - type: nauc_recall_at_20_max
      value: 76.3142
    - type: nauc_recall_at_20_std
      value: 61.0644
    - type: nauc_recall_at_20_diff1
      value: 62.244600000000005
    - type: nauc_recall_at_100_max
      value: 87.9526
    - type: nauc_recall_at_100_std
      value: 84.63619999999999
    - type: nauc_recall_at_100_diff1
      value: 69.6848
    - type: nauc_recall_at_1000_max
      value: .nan
    - type: nauc_recall_at_1000_std
      value: .nan
    - type: nauc_recall_at_1000_diff1
      value: .nan
    - type: nauc_precision_at_1_max
      value: 28.977700000000002
    - type: nauc_precision_at_1_std
      value: 5.5688
    - type: nauc_precision_at_1_diff1
      value: 62.8127
    - type: nauc_precision_at_3_max
      value: 57.338699999999996
    - type: nauc_precision_at_3_std
      value: 23.4946
    - type: nauc_precision_at_3_diff1
      value: 59.4094
    - type: nauc_precision_at_5_max
      value: 64.4058
    - type: nauc_precision_at_5_std
      value: 28.382
    - type: nauc_precision_at_5_diff1
      value: 60.671600000000005
    - type: nauc_precision_at_10_max
      value: 71.11070000000001
    - type: nauc_precision_at_10_std
      value: 43.6152
    - type: nauc_precision_at_10_diff1
      value: 62.6013
    - type: nauc_precision_at_20_max
      value: 76.3142
    - type: nauc_precision_at_20_std
      value: 61.0644
    - type: nauc_precision_at_20_diff1
      value: 62.244600000000005
    - type: nauc_precision_at_100_max
      value: 87.9526
    - type: nauc_precision_at_100_std
      value: 84.63619999999999
    - type: nauc_precision_at_100_diff1
      value: 69.6848
    - type: nauc_precision_at_1000_max
      value: .nan
    - type: nauc_precision_at_1000_std
      value: .nan
    - type: nauc_precision_at_1000_diff1
      value: .nan
    - type: nauc_mrr_at_1_max
      value: 28.977700000000002
    - type: nauc_mrr_at_1_std
      value: 5.5688
    - type: nauc_mrr_at_1_diff1
      value: 62.8127
    - type: nauc_mrr_at_3_max
      value: 38.5313
    - type: nauc_mrr_at_3_std
      value: 11.2395
    - type: nauc_mrr_at_3_diff1
      value: 61.1888
    - type: nauc_mrr_at_5_max
      value: 38.8835
    - type: nauc_mrr_at_5_std
      value: 11.5395
    - type: nauc_mrr_at_5_diff1
      value: 61.449
    - type: nauc_mrr_at_10_max
      value: 38.6822
    - type: nauc_mrr_at_10_std
      value: 12.0181
    - type: nauc_mrr_at_10_diff1
      value: 61.5846
    - type: nauc_mrr_at_20_max
      value: 38.5328
    - type: nauc_mrr_at_20_std
      value: 12.182500000000001
    - type: nauc_mrr_at_20_diff1
      value: 61.578599999999994
    - type: nauc_mrr_at_100_max
      value: 38.4484
    - type: nauc_mrr_at_100_std
      value: 12.1157
    - type: nauc_mrr_at_100_diff1
      value: 61.6247
    - type: nauc_mrr_at_1000_max
      value: 38.418600000000005
    - type: nauc_mrr_at_1000_std
      value: 12.0795
    - type: nauc_mrr_at_1000_diff1
      value: 61.6214
    - type: main_score
      value: 69.791
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB CodeTransOceanContest (default)
      revision: 20da4eb20a4b17300c0986ee148c90867a7f2a4d
      split: test
      type: CoIR-Retrieval/codetrans-contest
    metrics:
    - type: ndcg_at_1
      value: 33.032000000000004
    - type: ndcg_at_3
      value: 38.041000000000004
    - type: ndcg_at_5
      value: 40.67
    - type: ndcg_at_10
      value: 43.651
    - type: ndcg_at_20
      value: 45.255
    - type: ndcg_at_100
      value: 48.41
    - type: ndcg_at_1000
      value: 50.775000000000006
    - type: map_at_1
      value: 33.032000000000004
    - type: map_at_3
      value: 36.802
    - type: map_at_5
      value: 38.273
    - type: map_at_10
      value: 39.45
    - type: map_at_20
      value: 39.891
    - type: map_at_100
      value: 40.312
    - type: map_at_1000
      value: 40.396
    - type: recall_at_1
      value: 33.032000000000004
    - type: recall_at_3
      value: 41.629
    - type: recall_at_5
      value: 47.964
    - type: recall_at_10
      value: 57.465999999999994
    - type: recall_at_20
      value: 63.800999999999995
    - type: recall_at_100
      value: 80.99499999999999
    - type: recall_at_1000
      value: 100.0
    - type: precision_at_1
      value: 33.032000000000004
    - type: precision_at_3
      value: 13.876
    - type: precision_at_5
      value: 9.593
    - type: precision_at_10
      value: 5.747
    - type: precision_at_20
      value: 3.19
    - type: precision_at_100
      value: 0.8099999999999999
    - type: precision_at_1000
      value: 0.1
    - type: mrr_at_1
      value: 33.0317
    - type: mrr_at_3
      value: 36.8024
    - type: mrr_at_5
      value: 38.273
    - type: mrr_at_10
      value: 39.4504
    - type: mrr_at_20
      value: 39.8911
    - type: mrr_at_100
      value: 40.3122
    - type: mrr_at_1000
      value: 40.3955
    - type: nauc_ndcg_at_1_max
      value: 53.0197
    - type: nauc_ndcg_at_1_std
      value: 0.8863
    - type: nauc_ndcg_at_1_diff1
      value: 67.8151
    - type: nauc_ndcg_at_3_max
      value: 50.37350000000001
    - type: nauc_ndcg_at_3_std
      value: 1.3549
    - type: nauc_ndcg_at_3_diff1
      value: 61.698699999999995
    - type: nauc_ndcg_at_5_max
      value: 49.1498
    - type: nauc_ndcg_at_5_std
      value: 2.5727
    - type: nauc_ndcg_at_5_diff1
      value: 58.0748
    - type: nauc_ndcg_at_10_max
      value: 47.5197
    - type: nauc_ndcg_at_10_std
      value: 2.7498
    - type: nauc_ndcg_at_10_diff1
      value: 56.9398
    - type: nauc_ndcg_at_20_max
      value: 47.5836
    - type: nauc_ndcg_at_20_std
      value: 3.4302
    - type: nauc_ndcg_at_20_diff1
      value: 55.8913
    - type: nauc_ndcg_at_100_max
      value: 48.079499999999996
    - type: nauc_ndcg_at_100_std
      value: 3.7983999999999996
    - type: nauc_ndcg_at_100_diff1
      value: 56.7706
    - type: nauc_ndcg_at_1000_max
      value: 48.7136
    - type: nauc_ndcg_at_1000_std
      value: 2.949
    - type: nauc_ndcg_at_1000_diff1
      value: 58.0488
    - type: nauc_map_at_1_max
      value: 53.0197
    - type: nauc_map_at_1_std
      value: 0.8863
    - type: nauc_map_at_1_diff1
      value: 67.8151
    - type: nauc_map_at_3_max
      value: 51.1105
    - type: nauc_map_at_3_std
      value: 1.5191
    - type: nauc_map_at_3_diff1
      value: 63.005900000000004
    - type: nauc_map_at_5_max
      value: 50.4462
    - type: nauc_map_at_5_std
      value: 2.0751
    - type: nauc_map_at_5_diff1
      value: 61.0287
    - type: nauc_map_at_10_max
      value: 49.772499999999994
    - type: nauc_map_at_10_std
      value: 2.1092
    - type: nauc_map_at_10_diff1
      value: 60.528000000000006
    - type: nauc_map_at_20_max
      value: 49.7904
    - type: nauc_map_at_20_std
      value: 2.3456
    - type: nauc_map_at_20_diff1
      value: 60.2416
    - type: nauc_map_at_100_max
      value: 49.8742
    - type: nauc_map_at_100_std
      value: 2.3747000000000003
    - type: nauc_map_at_100_diff1
      value: 60.390600000000006
    - type: nauc_map_at_1000_max
      value: 49.8875
    - type: nauc_map_at_1000_std
      value: 2.3390999999999997
    - type: nauc_map_at_1000_diff1
      value: 60.41180000000001
    - type: nauc_recall_at_1_max
      value: 53.0197
    - type: nauc_recall_at_1_std
      value: 0.8863
    - type: nauc_recall_at_1_diff1
      value: 67.8151
    - type: nauc_recall_at_3_max
      value: 48.2306
    - type: nauc_recall_at_3_std
      value: 0.7745
    - type: nauc_recall_at_3_diff1
      value: 58.0358
    - type: nauc_recall_at_5_max
      value: 45.1577
    - type: nauc_recall_at_5_std
      value: 4.228400000000001
    - type: nauc_recall_at_5_diff1
      value: 49.0182
    - type: nauc_recall_at_10_max
      value: 39.584
    - type: nauc_recall_at_10_std
      value: 5.1647
    - type: nauc_recall_at_10_diff1
      value: 44.864399999999996
    - type: nauc_recall_at_20_max
      value: 39.1616
    - type: nauc_recall_at_20_std
      value: 7.9384
    - type: nauc_recall_at_20_diff1
      value: 39.124700000000004
    - type: nauc_recall_at_100_max
      value: 38.4356
    - type: nauc_recall_at_100_std
      value: 14.498
    - type: nauc_recall_at_100_diff1
      value: 36.8934
    - type: nauc_recall_at_1000_max
      value: .nan
    - type: nauc_recall_at_1000_std
      value: .nan
    - type: nauc_recall_at_1000_diff1
      value: .nan
    - type: nauc_precision_at_1_max
      value: 53.0197
    - type: nauc_precision_at_1_std
      value: 0.8863
    - type: nauc_precision_at_1_diff1
      value: 67.8151
    - type: nauc_precision_at_3_max
      value: 48.2306
    - type: nauc_precision_at_3_std
      value: 0.7745
    - type: nauc_precision_at_3_diff1
      value: 58.0358
    - type: nauc_precision_at_5_max
      value: 45.1577
    - type: nauc_precision_at_5_std
      value: 4.228400000000001
    - type: nauc_precision_at_5_diff1
      value: 49.0182
    - type: nauc_precision_at_10_max
      value: 39.584
    - type: nauc_precision_at_10_std
      value: 5.1647
    - type: nauc_precision_at_10_diff1
      value: 44.864399999999996
    - type: nauc_precision_at_20_max
      value: 39.1616
    - type: nauc_precision_at_20_std
      value: 7.9384
    - type: nauc_precision_at_20_diff1
      value: 39.124700000000004
    - type: nauc_precision_at_100_max
      value: 38.4356
    - type: nauc_precision_at_100_std
      value: 14.498
    - type: nauc_precision_at_100_diff1
      value: 36.8934
    - type: nauc_precision_at_1000_max
      value: 100.0
    - type: nauc_precision_at_1000_std
      value: 100.0
    - type: nauc_precision_at_1000_diff1
      value: 100.0
    - type: nauc_mrr_at_1_max
      value: 53.0197
    - type: nauc_mrr_at_1_std
      value: 0.8863
    - type: nauc_mrr_at_1_diff1
      value: 67.8151
    - type: nauc_mrr_at_3_max
      value: 51.1105
    - type: nauc_mrr_at_3_std
      value: 1.5191
    - type: nauc_mrr_at_3_diff1
      value: 63.005900000000004
    - type: nauc_mrr_at_5_max
      value: 50.4462
    - type: nauc_mrr_at_5_std
      value: 2.0751
    - type: nauc_mrr_at_5_diff1
      value: 61.0287
    - type: nauc_mrr_at_10_max
      value: 49.772499999999994
    - type: nauc_mrr_at_10_std
      value: 2.1092
    - type: nauc_mrr_at_10_diff1
      value: 60.528000000000006
    - type: nauc_mrr_at_20_max
      value: 49.7904
    - type: nauc_mrr_at_20_std
      value: 2.3456
    - type: nauc_mrr_at_20_diff1
      value: 60.2416
    - type: nauc_mrr_at_100_max
      value: 49.8742
    - type: nauc_mrr_at_100_std
      value: 2.3747000000000003
    - type: nauc_mrr_at_100_diff1
      value: 60.390600000000006
    - type: nauc_mrr_at_1000_max
      value: 49.8875
    - type: nauc_mrr_at_1000_std
      value: 2.3390999999999997
    - type: nauc_mrr_at_1000_diff1
      value: 60.41180000000001
    - type: main_score
      value: 43.651
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB CodeTransOceanDL (default)
      revision: 281562cb8a1265ab5c0824bfa6ddcd9b0a15618f
      split: test
      type: CoIR-Retrieval/codetrans-dl
    metrics:
    - type: ndcg_at_1
      value: 8.333
    - type: ndcg_at_3
      value: 9.795
    - type: ndcg_at_5
      value: 13.286999999999999
    - type: ndcg_at_10
      value: 18.151999999999997
    - type: ndcg_at_20
      value: 21.914
    - type: ndcg_at_100
      value: 28.576
    - type: ndcg_at_1000
      value: 30.407
    - type: map_at_1
      value: 8.333
    - type: map_at_3
      value: 9.352
    - type: map_at_5
      value: 11.324
    - type: map_at_10
      value: 13.233
    - type: map_at_20
      value: 14.325
    - type: map_at_100
      value: 15.153
    - type: map_at_1000
      value: 15.243
    - type: recall_at_1
      value: 8.333
    - type: recall_at_3
      value: 11.111
    - type: recall_at_5
      value: 19.444
    - type: recall_at_10
      value: 35.0
    - type: recall_at_20
      value: 49.444
    - type: recall_at_100
      value: 86.667
    - type: recall_at_1000
      value: 100.0
    - type: precision_at_1
      value: 8.333
    - type: precision_at_3
      value: 3.7039999999999997
    - type: precision_at_5
      value: 3.8890000000000002
    - type: precision_at_10
      value: 3.5000000000000004
    - type: precision_at_20
      value: 2.472
    - type: precision_at_100
      value: 0.8670000000000001
    - type: precision_at_1000
      value: 0.1
    - type: mrr_at_1
      value: 3.3333000000000004
    - type: mrr_at_3
      value: 6.6667000000000005
    - type: mrr_at_5
      value: 7.7778
    - type: mrr_at_10
      value: 10.247100000000001
    - type: mrr_at_20
      value: 11.3458
    - type: mrr_at_100
      value: 12.177
    - type: mrr_at_1000
      value: 12.2675
    - type: nauc_ndcg_at_1_max
      value: -39.772800000000004
    - type: nauc_ndcg_at_1_std
      value: -34.0524
    - type: nauc_ndcg_at_1_diff1
      value: -32.8146
    - type: nauc_ndcg_at_3_max
      value: -39.8776
    - type: nauc_ndcg_at_3_std
      value: -34.6862
    - type: nauc_ndcg_at_3_diff1
      value: -19.3707
    - type: nauc_ndcg_at_5_max
      value: -40.8597
    - type: nauc_ndcg_at_5_std
      value: -38.1022
    - type: nauc_ndcg_at_5_diff1
      value: -6.4628000000000005
    - type: nauc_ndcg_at_10_max
      value: -40.2327
    - type: nauc_ndcg_at_10_std
      value: -47.2976
    - type: nauc_ndcg_at_10_diff1
      value: -4.4762
    - type: nauc_ndcg_at_20_max
      value: -41.7987
    - type: nauc_ndcg_at_20_std
      value: -54.2481
    - type: nauc_ndcg_at_20_diff1
      value: -8.6146
    - type: nauc_ndcg_at_100_max
      value: -39.463100000000004
    - type: nauc_ndcg_at_100_std
      value: -45.7414
    - type: nauc_ndcg_at_100_diff1
      value: -9.2455
    - type: nauc_ndcg_at_1000_max
      value: -40.8904
    - type: nauc_ndcg_at_1000_std
      value: -46.5535
    - type: nauc_ndcg_at_1000_diff1
      value: -11.476799999999999
    - type: nauc_map_at_1_max
      value: -39.772800000000004
    - type: nauc_map_at_1_std
      value: -34.0524
    - type: nauc_map_at_1_diff1
      value: -32.8146
    - type: nauc_map_at_3_max
      value: -39.894200000000005
    - type: nauc_map_at_3_std
      value: -34.4818
    - type: nauc_map_at_3_diff1
      value: -23.0092
    - type: nauc_map_at_5_max
      value: -40.5148
    - type: nauc_map_at_5_std
      value: -36.6914
    - type: nauc_map_at_5_diff1
      value: -14.0244
    - type: nauc_map_at_10_max
      value: -40.3751
    - type: nauc_map_at_10_std
      value: -41.0546
    - type: nauc_map_at_10_diff1
      value: -12.7255
    - type: nauc_map_at_20_max
      value: -40.8992
    - type: nauc_map_at_20_std
      value: -43.580999999999996
    - type: nauc_map_at_20_diff1
      value: -14.1348
    - type: nauc_map_at_100_max
      value: -40.8422
    - type: nauc_map_at_100_std
      value: -42.7572
    - type: nauc_map_at_100_diff1
      value: -14.5847
    - type: nauc_map_at_1000_max
      value: -40.8622
    - type: nauc_map_at_1000_std
      value: -42.7255
    - type: nauc_map_at_1000_diff1
      value: -14.716099999999999
    - type: nauc_recall_at_1_max
      value: -39.772800000000004
    - type: nauc_recall_at_1_std
      value: -34.0524
    - type: nauc_recall_at_1_diff1
      value: -32.8146
    - type: nauc_recall_at_3_max
      value: -39.8223
    - type: nauc_recall_at_3_std
      value: -35.2166
    - type: nauc_recall_at_3_diff1
      value: -10.0944
    - type: nauc_recall_at_5_max
      value: -41.574
    - type: nauc_recall_at_5_std
      value: -41.0135
    - type: nauc_recall_at_5_diff1
      value: 8.5898
    - type: nauc_recall_at_10_max
      value: -39.7009
    - type: nauc_recall_at_10_std
      value: -59.587900000000005
    - type: nauc_recall_at_10_diff1
      value: 9.6476
    - type: nauc_recall_at_20_max
      value: -43.7116
    - type: nauc_recall_at_20_std
      value: -76.6625
    - type: nauc_recall_at_20_diff1
      value: -0.7394999999999999
    - type: nauc_recall_at_100_max
      value: -22.023799999999998
    - type: nauc_recall_at_100_std
      value: -33.848099999999995
    - type: nauc_recall_at_100_diff1
      value: 12.5282
    - type: nauc_recall_at_1000_max
      value: .nan
    - type: nauc_recall_at_1000_std
      value: .nan
    - type: nauc_recall_at_1000_diff1
      value: .nan
    - type: nauc_precision_at_1_max
      value: -39.772800000000004
    - type: nauc_precision_at_1_std
      value: -34.0524
    - type: nauc_precision_at_1_diff1
      value: -32.8146
    - type: nauc_precision_at_3_max
      value: -39.8223
    - type: nauc_precision_at_3_std
      value: -35.2166
    - type: nauc_precision_at_3_diff1
      value: -10.0944
    - type: nauc_precision_at_5_max
      value: -41.574
    - type: nauc_precision_at_5_std
      value: -41.0135
    - type: nauc_precision_at_5_diff1
      value: 8.5898
    - type: nauc_precision_at_10_max
      value: -39.7009
    - type: nauc_precision_at_10_std
      value: -59.587900000000005
    - type: nauc_precision_at_10_diff1
      value: 9.6476
    - type: nauc_precision_at_20_max
      value: -43.7116
    - type: nauc_precision_at_20_std
      value: -76.6625
    - type: nauc_precision_at_20_diff1
      value: -0.7394999999999999
    - type: nauc_precision_at_100_max
      value: -22.023799999999998
    - type: nauc_precision_at_100_std
      value: -33.848099999999995
    - type: nauc_precision_at_100_diff1
      value: 12.5282
    - type: nauc_precision_at_1000_max
      value: 100.0
    - type: nauc_precision_at_1000_std
      value: 100.0
    - type: nauc_precision_at_1000_diff1
      value: 100.0
    - type: nauc_mrr_at_1_max
      value: -37.1478
    - type: nauc_mrr_at_1_std
      value: -38.2256
    - type: nauc_mrr_at_1_diff1
      value: -19.2648
    - type: nauc_mrr_at_3_max
      value: -38.5609
    - type: nauc_mrr_at_3_std
      value: -36.7946
    - type: nauc_mrr_at_3_diff1
      value: 15.8383
    - type: nauc_mrr_at_5_max
      value: -38.6003
    - type: nauc_mrr_at_5_std
      value: -38.6368
    - type: nauc_mrr_at_5_diff1
      value: 10.5538
    - type: nauc_mrr_at_10_max
      value: -40.3107
    - type: nauc_mrr_at_10_std
      value: -44.6633
    - type: nauc_mrr_at_10_diff1
      value: 12.0739
    - type: nauc_mrr_at_20_max
      value: -40.2119
    - type: nauc_mrr_at_20_std
      value: -47.942099999999996
    - type: nauc_mrr_at_20_diff1
      value: 9.2441
    - type: nauc_mrr_at_100_max
      value: -40.095
    - type: nauc_mrr_at_100_std
      value: -46.9315
    - type: nauc_mrr_at_100_diff1
      value: 9.4182
    - type: nauc_mrr_at_1000_max
      value: -40.117799999999995
    - type: nauc_mrr_at_1000_std
      value: -46.914699999999996
    - type: nauc_mrr_at_1000_diff1
      value: 9.3917
    - type: main_score
      value: 18.151999999999997
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB CosQA (default)
      revision: bc5efb7e9d437246ce393ed19d772e08e4a79535
      split: test
      type: CoIR-Retrieval/cosqa
    metrics:
    - type: ndcg_at_1
      value: 12.6
    - type: ndcg_at_3
      value: 19.259
    - type: ndcg_at_5
      value: 24.078
    - type: ndcg_at_10
      value: 28.288999999999998
    - type: ndcg_at_20
      value: 31.706
    - type: ndcg_at_100
      value: 36.05
    - type: ndcg_at_1000
      value: 37.632
    - type: map_at_1
      value: 12.6
    - type: map_at_3
      value: 17.5
    - type: map_at_5
      value: 20.150000000000002
    - type: map_at_10
      value: 21.931
    - type: map_at_20
      value: 22.884
    - type: map_at_100
      value: 23.502000000000002
    - type: map_at_1000
      value: 23.566000000000003
    - type: recall_at_1
      value: 12.6
    - type: recall_at_3
      value: 24.4
    - type: recall_at_5
      value: 36.199999999999996
    - type: recall_at_10
      value: 49.0
    - type: recall_at_20
      value: 62.4
    - type: recall_at_100
      value: 85.6
    - type: recall_at_1000
      value: 97.8
    - type: precision_at_1
      value: 12.6
    - type: precision_at_3
      value: 8.133
    - type: precision_at_5
      value: 7.24
    - type: precision_at_10
      value: 4.9
    - type: precision_at_20
      value: 3.1199999999999997
    - type: precision_at_100
      value: 0.856
    - type: precision_at_1000
      value: 0.098
    - type: mrr_at_1
      value: 12.2
    - type: mrr_at_3
      value: 17.6333
    - type: mrr_at_5
      value: 19.453300000000002
    - type: mrr_at_10
      value: 21.3205
    - type: mrr_at_20
      value: 22.315199999999997
    - type: mrr_at_100
      value: 22.9331
    - type: mrr_at_1000
      value: 22.9955
    - type: nauc_ndcg_at_1_max
      value: 10.2948
    - type: nauc_ndcg_at_1_std
      value: -13.1709
    - type: nauc_ndcg_at_1_diff1
      value: 31.4251
    - type: nauc_ndcg_at_3_max
      value: 15.477599999999999
    - type: nauc_ndcg_at_3_std
      value: -11.7827
    - type: nauc_ndcg_at_3_diff1
      value: 17.4257
    - type: nauc_ndcg_at_5_max
      value: 17.7434
    - type: nauc_ndcg_at_5_std
      value: -10.7058
    - type: nauc_ndcg_at_5_diff1
      value: 13.955100000000002
    - type: nauc_ndcg_at_10_max
      value: 17.799100000000003
    - type: nauc_ndcg_at_10_std
      value: -8.629000000000001
    - type: nauc_ndcg_at_10_diff1
      value: 12.266399999999999
    - type: nauc_ndcg_at_20_max
      value: 18.454
    - type: nauc_ndcg_at_20_std
      value: -8.0871
    - type: nauc_ndcg_at_20_diff1
      value: 11.4802
    - type: nauc_ndcg_at_100_max
      value: 18.8607
    - type: nauc_ndcg_at_100_std
      value: -5.8566
    - type: nauc_ndcg_at_100_diff1
      value: 12.559899999999999
    - type: nauc_ndcg_at_1000_max
      value: 18.1409
    - type: nauc_ndcg_at_1000_std
      value: -6.894799999999999
    - type: nauc_ndcg_at_1000_diff1
      value: 13.9734
    - type: nauc_map_at_1_max
      value: 10.2948
    - type: nauc_map_at_1_std
      value: -13.1709
    - type: nauc_map_at_1_diff1
      value: 31.4251
    - type: nauc_map_at_3_max
      value: 14.4256
    - type: nauc_map_at_3_std
      value: -12.173
    - type: nauc_map_at_3_diff1
      value: 20.4742
    - type: nauc_map_at_5_max
      value: 15.842400000000001
    - type: nauc_map_at_5_std
      value: -11.5686
    - type: nauc_map_at_5_diff1
      value: 18.195800000000002
    - type: nauc_map_at_10_max
      value: 15.786200000000001
    - type: nauc_map_at_10_std
      value: -10.564
    - type: nauc_map_at_10_diff1
      value: 17.227899999999998
    - type: nauc_map_at_20_max
      value: 15.987199999999998
    - type: nauc_map_at_20_std
      value: -10.4241
    - type: nauc_map_at_20_diff1
      value: 17.0317
    - type: nauc_map_at_100_max
      value: 16.1125
    - type: nauc_map_at_100_std
      value: -9.9394
    - type: nauc_map_at_100_diff1
      value: 17.191100000000002
    - type: nauc_map_at_1000_max
      value: 16.0868
    - type: nauc_map_at_1000_std
      value: -9.9615
    - type: nauc_map_at_1000_diff1
      value: 17.241999999999997
    - type: nauc_recall_at_1_max
      value: 10.2948
    - type: nauc_recall_at_1_std
      value: -13.1709
    - type: nauc_recall_at_1_diff1
      value: 31.4251
    - type: nauc_recall_at_3_max
      value: 17.924799999999998
    - type: nauc_recall_at_3_std
      value: -10.84
    - type: nauc_recall_at_3_diff1
      value: 10.267800000000001
    - type: nauc_recall_at_5_max
      value: 22.0265
    - type: nauc_recall_at_5_std
      value: -8.6675
    - type: nauc_recall_at_5_diff1
      value: 4.5511
    - type: nauc_recall_at_10_max
      value: 22.5353
    - type: nauc_recall_at_10_std
      value: -3.7438
    - type: nauc_recall_at_10_diff1
      value: 1.05
    - type: nauc_recall_at_20_max
      value: 25.4119
    - type: nauc_recall_at_20_std
      value: -1.0668
    - type: nauc_recall_at_20_diff1
      value: -3.4072999999999998
    - type: nauc_recall_at_100_max
      value: 34.5952
    - type: nauc_recall_at_100_std
      value: 22.4855
    - type: nauc_recall_at_100_diff1
      value: -9.0738
    - type: nauc_recall_at_1000_max
      value: 56.485
    - type: nauc_recall_at_1000_std
      value: 72.184
    - type: nauc_recall_at_1000_diff1
      value: -5.3136
    - type: nauc_precision_at_1_max
      value: 10.2948
    - type: nauc_precision_at_1_std
      value: -13.1709
    - type: nauc_precision_at_1_diff1
      value: 31.4251
    - type: nauc_precision_at_3_max
      value: 17.924799999999998
    - type: nauc_precision_at_3_std
      value: -10.84
    - type: nauc_precision_at_3_diff1
      value: 10.267800000000001
    - type: nauc_precision_at_5_max
      value: 22.0265
    - type: nauc_precision_at_5_std
      value: -8.6675
    - type: nauc_precision_at_5_diff1
      value: 4.5511
    - type: nauc_precision_at_10_max
      value: 22.5353
    - type: nauc_precision_at_10_std
      value: -3.7438
    - type: nauc_precision_at_10_diff1
      value: 1.05
    - type: nauc_precision_at_20_max
      value: 25.4119
    - type: nauc_precision_at_20_std
      value: -1.0668
    - type: nauc_precision_at_20_diff1
      value: -3.4072999999999998
    - type: nauc_precision_at_100_max
      value: 34.5952
    - type: nauc_precision_at_100_std
      value: 22.4855
    - type: nauc_precision_at_100_diff1
      value: -9.0738
    - type: nauc_precision_at_1000_max
      value: 56.485
    - type: nauc_precision_at_1000_std
      value: 72.184
    - type: nauc_precision_at_1000_diff1
      value: -5.3136
    - type: nauc_mrr_at_1_max
      value: 12.3113
    - type: nauc_mrr_at_1_std
      value: -16.7186
    - type: nauc_mrr_at_1_diff1
      value: 32.4301
    - type: nauc_mrr_at_3_max
      value: 11.8664
    - type: nauc_mrr_at_3_std
      value: -15.562500000000002
    - type: nauc_mrr_at_3_diff1
      value: 20.180600000000002
    - type: nauc_mrr_at_5_max
      value: 11.9561
    - type: nauc_mrr_at_5_std
      value: -15.1641
    - type: nauc_mrr_at_5_diff1
      value: 19.1071
    - type: nauc_mrr_at_10_max
      value: 12.867899999999999
    - type: nauc_mrr_at_10_std
      value: -14.1707
    - type: nauc_mrr_at_10_diff1
      value: 17.613599999999998
    - type: nauc_mrr_at_20_max
      value: 13.3821
    - type: nauc_mrr_at_20_std
      value: -13.727800000000002
    - type: nauc_mrr_at_20_diff1
      value: 17.712600000000002
    - type: nauc_mrr_at_100_max
      value: 13.530100000000001
    - type: nauc_mrr_at_100_std
      value: -13.292599999999998
    - type: nauc_mrr_at_100_diff1
      value: 17.8945
    - type: nauc_mrr_at_1000_max
      value: 13.492899999999999
    - type: nauc_mrr_at_1000_std
      value: -13.3262
    - type: nauc_mrr_at_1000_diff1
      value: 17.945
    - type: main_score
      value: 28.288999999999998
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB DBPedia (default)
      revision: c0f706b76e590d620bd6618b3ca8efdd34e2d659
      split: test
      type: mteb/dbpedia
    metrics:
    - type: ndcg_at_1
      value: 46.625
    - type: ndcg_at_3
      value: 37.483
    - type: ndcg_at_5
      value: 34.943000000000005
    - type: ndcg_at_10
      value: 32.805
    - type: ndcg_at_20
      value: 31.857999999999997
    - type: ndcg_at_100
      value: 36.504
    - type: ndcg_at_1000
      value: 44.015
    - type: map_at_1
      value: 7.455
    - type: map_at_3
      value: 11.231
    - type: map_at_5
      value: 12.76
    - type: map_at_10
      value: 14.927000000000001
    - type: map_at_20
      value: 16.732
    - type: map_at_100
      value: 19.903000000000002
    - type: map_at_1000
      value: 21.227
    - type: recall_at_1
      value: 7.455
    - type: recall_at_3
      value: 12.423
    - type: recall_at_5
      value: 15.326
    - type: recall_at_10
      value: 19.858
    - type: recall_at_20
      value: 24.929000000000002
    - type: recall_at_100
      value: 42.799
    - type: recall_at_1000
      value: 66.485
    - type: precision_at_1
      value: 58.75
    - type: precision_at_3
      value: 40.916999999999994
    - type: precision_at_5
      value: 34.050000000000004
    - type: precision_at_10
      value: 25.75
    - type: precision_at_20
      value: 18.712
    - type: precision_at_100
      value: 7.904999999999999
    - type: precision_at_1000
      value: 1.754
    - type: mrr_at_1
      value: 58.75
    - type: mrr_at_3
      value: 65.2083
    - type: mrr_at_5
      value: 66.7708
    - type: mrr_at_10
      value: 67.4141
    - type: mrr_at_20
      value: 67.6811
    - type: mrr_at_100
      value: 67.8579
    - type: mrr_at_1000
      value: 67.8709
    - type: nauc_ndcg_at_1_max
      value: 29.0439
    - type: nauc_ndcg_at_1_std
      value: 20.5015
    - type: nauc_ndcg_at_1_diff1
      value: 35.499199999999995
    - type: nauc_ndcg_at_3_max
      value: 29.8709
    - type: nauc_ndcg_at_3_std
      value: 23.020699999999998
    - type: nauc_ndcg_at_3_diff1
      value: 28.618100000000002
    - type: nauc_ndcg_at_5_max
      value: 27.7184
    - type: nauc_ndcg_at_5_std
      value: 23.0527
    - type: nauc_ndcg_at_5_diff1
      value: 25.526
    - type: nauc_ndcg_at_10_max
      value: 25.145400000000002
    - type: nauc_ndcg_at_10_std
      value: 21.6828
    - type: nauc_ndcg_at_10_diff1
      value: 25.123
    - type: nauc_ndcg_at_20_max
      value: 24.1687
    - type: nauc_ndcg_at_20_std
      value: 18.192800000000002
    - type: nauc_ndcg_at_20_diff1
      value: 25.2305
    - type: nauc_ndcg_at_100_max
      value: 26.4048
    - type: nauc_ndcg_at_100_std
      value: 22.2057
    - type: nauc_ndcg_at_100_diff1
      value: 23.2848
    - type: nauc_ndcg_at_1000_max
      value: 30.6232
    - type: nauc_ndcg_at_1000_std
      value: 30.4798
    - type: nauc_ndcg_at_1000_diff1
      value: 22.5713
    - type: nauc_map_at_1_max
      value: 4.2514
    - type: nauc_map_at_1_std
      value: -16.109
    - type: nauc_map_at_1_diff1
      value: 31.521300000000004
    - type: nauc_map_at_3_max
      value: 10.5699
    - type: nauc_map_at_3_std
      value: -13.2038
    - type: nauc_map_at_3_diff1
      value: 27.992099999999997
    - type: nauc_map_at_5_max
      value: 12.110999999999999
    - type: nauc_map_at_5_std
      value: -9.2883
    - type: nauc_map_at_5_diff1
      value: 24.2311
    - type: nauc_map_at_10_max
      value: 15.5794
    - type: nauc_map_at_10_std
      value: -1.9084
    - type: nauc_map_at_10_diff1
      value: 23.5487
    - type: nauc_map_at_20_max
      value: 19.2937
    - type: nauc_map_at_20_std
      value: 5.1674
    - type: nauc_map_at_20_diff1
      value: 23.1231
    - type: nauc_map_at_100_max
      value: 23.7248
    - type: nauc_map_at_100_std
      value: 15.6969
    - type: nauc_map_at_100_diff1
      value: 22.087899999999998
    - type: nauc_map_at_1000_max
      value: 25.3616
    - type: nauc_map_at_1000_std
      value: 18.9624
    - type: nauc_map_at_1000_diff1
      value: 22.3491
    - type: nauc_recall_at_1_max
      value: 4.2514
    - type: nauc_recall_at_1_std
      value: -16.109
    - type: nauc_recall_at_1_diff1
      value: 31.521300000000004
    - type: nauc_recall_at_3_max
      value: 9.579600000000001
    - type: nauc_recall_at_3_std
      value: -14.1439
    - type: nauc_recall_at_3_diff1
      value: 24.0237
    - type: nauc_recall_at_5_max
      value: 7.7634
    - type: nauc_recall_at_5_std
      value: -11.6212
    - type: nauc_recall_at_5_diff1
      value: 15.8449
    - type: nauc_recall_at_10_max
      value: 12.070500000000001
    - type: nauc_recall_at_10_std
      value: -3.6641
    - type: nauc_recall_at_10_diff1
      value: 16.755
    - type: nauc_recall_at_20_max
      value: 16.974600000000002
    - type: nauc_recall_at_20_std
      value: 4.442
    - type: nauc_recall_at_20_diff1
      value: 16.2465
    - type: nauc_recall_at_100_max
      value: 20.0143
    - type: nauc_recall_at_100_std
      value: 19.0564
    - type: nauc_recall_at_100_diff1
      value: 11.2073
    - type: nauc_recall_at_1000_max
      value: 25.826999999999998
    - type: nauc_recall_at_1000_std
      value: 31.867600000000003
    - type: nauc_recall_at_1000_diff1
      value: 7.5985
    - type: nauc_precision_at_1_max
      value: 46.4049
    - type: nauc_precision_at_1_std
      value: 34.9663
    - type: nauc_precision_at_1_diff1
      value: 41.281099999999995
    - type: nauc_precision_at_3_max
      value: 40.3772
    - type: nauc_precision_at_3_std
      value: 39.231700000000004
    - type: nauc_precision_at_3_diff1
      value: 20.8721
    - type: nauc_precision_at_5_max
      value: 35.3251
    - type: nauc_precision_at_5_std
      value: 45.041399999999996
    - type: nauc_precision_at_5_diff1
      value: 12.377699999999999
    - type: nauc_precision_at_10_max
      value: 33.1469
    - type: nauc_precision_at_10_std
      value: 50.484700000000004
    - type: nauc_precision_at_10_diff1
      value: 9.9524
    - type: nauc_precision_at_20_max
      value: 31.897599999999997
    - type: nauc_precision_at_20_std
      value: 53.0212
    - type: nauc_precision_at_20_diff1
      value: 9.0274
    - type: nauc_precision_at_100_max
      value: 27.060499999999998
    - type: nauc_precision_at_100_std
      value: 51.7917
    - type: nauc_precision_at_100_diff1
      value: 5.3346
    - type: nauc_precision_at_1000_max
      value: 10.5127
    - type: nauc_precision_at_1000_std
      value: 27.1389
    - type: nauc_precision_at_1000_diff1
      value: 4.072
    - type: nauc_mrr_at_1_max
      value: 46.4049
    - type: nauc_mrr_at_1_std
      value: 34.9663
    - type: nauc_mrr_at_1_diff1
      value: 41.281099999999995
    - type: nauc_mrr_at_3_max
      value: 49.1925
    - type: nauc_mrr_at_3_std
      value: 38.4208
    - type: nauc_mrr_at_3_diff1
      value: 39.4442
    - type: nauc_mrr_at_5_max
      value: 49.4555
    - type: nauc_mrr_at_5_std
      value: 39.9529
    - type: nauc_mrr_at_5_diff1
      value: 39.4985
    - type: nauc_mrr_at_10_max
      value: 49.215900000000005
    - type: nauc_mrr_at_10_std
      value: 39.846199999999996
    - type: nauc_mrr_at_10_diff1
      value: 39.6351
    - type: nauc_mrr_at_20_max
      value: 49.2931
    - type: nauc_mrr_at_20_std
      value: 39.7556
    - type: nauc_mrr_at_20_diff1
      value: 39.536500000000004
    - type: nauc_mrr_at_100_max
      value: 49.236799999999995
    - type: nauc_mrr_at_100_std
      value: 39.7146
    - type: nauc_mrr_at_100_diff1
      value: 39.5436
    - type: nauc_mrr_at_1000_max
      value: 49.2376
    - type: nauc_mrr_at_1000_std
      value: 39.7079
    - type: nauc_mrr_at_1000_diff1
      value: 39.5441
    - type: main_score
      value: 32.805
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB EmotionClassification (default)
      revision: 4f58c6b202a23cf9a4da393831edf4f9183cad37
      split: test
      type: mteb/emotion
    metrics:
    - type: accuracy
      value: 33.755
    - type: f1
      value: 30.109
    - type: f1_weighted
      value: 35.891
    - type: main_score
      value: 33.755
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB FEVER (default)
      revision: bea83ef9e8fb933d90a2f1d5515737465d613e12
      split: test
      type: mteb/fever
    metrics:
    - type: ndcg_at_1
      value: 75.203
    - type: ndcg_at_3
      value: 81.208
    - type: ndcg_at_5
      value: 82.319
    - type: ndcg_at_10
      value: 83.155
    - type: ndcg_at_20
      value: 83.524
    - type: ndcg_at_100
      value: 83.852
    - type: ndcg_at_1000
      value: 84.052
    - type: map_at_1
      value: 69.63000000000001
    - type: map_at_3
      value: 77.50200000000001
    - type: map_at_5
      value: 78.251
    - type: map_at_10
      value: 78.648
    - type: map_at_20
      value: 78.767
    - type: map_at_100
      value: 78.82400000000001
    - type: map_at_1000
      value: 78.834
    - type: recall_at_1
      value: 69.63000000000001
    - type: recall_at_3
      value: 86.444
    - type: recall_at_5
      value: 89.298
    - type: recall_at_10
      value: 91.843
    - type: recall_at_20
      value: 93.195
    - type: recall_at_100
      value: 94.77799999999999
    - type: recall_at_1000
      value: 96.068
    - type: precision_at_1
      value: 75.203
    - type: precision_at_3
      value: 31.293
    - type: precision_at_5
      value: 19.448
    - type: precision_at_10
      value: 10.024
    - type: precision_at_20
      value: 5.102
    - type: precision_at_100
      value: 1.045
    - type: precision_at_1000
      value: 0.107
    - type: mrr_at_1
      value: 75.2025
    - type: mrr_at_3
      value: 83.0608
    - type: mrr_at_5
      value: 83.6871
    - type: mrr_at_10
      value: 84.0239
    - type: mrr_at_20
      value: 84.1082
    - type: mrr_at_100
      value: 84.1355
    - type: mrr_at_1000
      value: 84.137
    - type: nauc_ndcg_at_1_max
      value: 29.9781
    - type: nauc_ndcg_at_1_std
      value: -27.174799999999998
    - type: nauc_ndcg_at_1_diff1
      value: 65.8967
    - type: nauc_ndcg_at_3_max
      value: 24.2173
    - type: nauc_ndcg_at_3_std
      value: -22.2349
    - type: nauc_ndcg_at_3_diff1
      value: 48.9054
    - type: nauc_ndcg_at_5_max
      value: 22.6904
    - type: nauc_ndcg_at_5_std
      value: -21.4784
    - type: nauc_ndcg_at_5_diff1
      value: 48.186099999999996
    - type: nauc_ndcg_at_10_max
      value: 22.2573
    - type: nauc_ndcg_at_10_std
      value: -20.415
    - type: nauc_ndcg_at_10_diff1
      value: 47.7873
    - type: nauc_ndcg_at_20_max
      value: 22.0394
    - type: nauc_ndcg_at_20_std
      value: -19.7697
    - type: nauc_ndcg_at_20_diff1
      value: 47.958099999999995
    - type: nauc_ndcg_at_100_max
      value: 21.6255
    - type: nauc_ndcg_at_100_std
      value: -19.778200000000002
    - type: nauc_ndcg_at_100_diff1
      value: 48.0176
    - type: nauc_ndcg_at_1000_max
      value: 21.8334
    - type: nauc_ndcg_at_1000_std
      value: -19.947699999999998
    - type: nauc_ndcg_at_1000_diff1
      value: 48.491800000000005
    - type: nauc_map_at_1_max
      value: 22.7733
    - type: nauc_map_at_1_std
      value: -22.9147
    - type: nauc_map_at_1_diff1
      value: 54.33480000000001
    - type: nauc_map_at_3_max
      value: 21.7638
    - type: nauc_map_at_3_std
      value: -21.5291
    - type: nauc_map_at_3_diff1
      value: 48.4323
    - type: nauc_map_at_5_max
      value: 21.3712
    - type: nauc_map_at_5_std
      value: -21.1705
    - type: nauc_map_at_5_diff1
      value: 48.302499999999995
    - type: nauc_map_at_10_max
      value: 21.2869
    - type: nauc_map_at_10_std
      value: -20.826900000000002
    - type: nauc_map_at_10_diff1
      value: 48.238
    - type: nauc_map_at_20_max
      value: 21.259700000000002
    - type: nauc_map_at_20_std
      value: -20.6727
    - type: nauc_map_at_20_diff1
      value: 48.280499999999996
    - type: nauc_map_at_100_max
      value: 21.2305
    - type: nauc_map_at_100_std
      value: -20.6466
    - type: nauc_map_at_100_diff1
      value: 48.3009
    - type: nauc_map_at_1000_max
      value: 21.2364
    - type: nauc_map_at_1000_std
      value: -20.6521
    - type: nauc_map_at_1000_diff1
      value: 48.3154
    - type: nauc_recall_at_1_max
      value: 22.7733
    - type: nauc_recall_at_1_std
      value: -22.9147
    - type: nauc_recall_at_1_diff1
      value: 54.33480000000001
    - type: nauc_recall_at_3_max
      value: 17.147100000000002
    - type: nauc_recall_at_3_std
      value: -16.8494
    - type: nauc_recall_at_3_diff1
      value: 30.9712
    - type: nauc_recall_at_5_max
      value: 12.0947
    - type: nauc_recall_at_5_std
      value: -13.142000000000001
    - type: nauc_recall_at_5_diff1
      value: 24.760099999999998
    - type: nauc_recall_at_10_max
      value: 7.1945
    - type: nauc_recall_at_10_std
      value: -5.1164000000000005
    - type: nauc_recall_at_10_diff1
      value: 15.933900000000001
    - type: nauc_recall_at_20_max
      value: 2.3306
    - type: nauc_recall_at_20_std
      value: 2.748
    - type: nauc_recall_at_20_diff1
      value: 11.4733
    - type: nauc_recall_at_100_max
      value: -9.991999999999999
    - type: nauc_recall_at_100_std
      value: 7.362299999999999
    - type: nauc_recall_at_100_diff1
      value: 2.2306
    - type: nauc_recall_at_1000_max
      value: -15.401200000000001
    - type: nauc_recall_at_1000_std
      value: 10.616100000000001
    - type: nauc_recall_at_1000_diff1
      value: 1.9488999999999999
    - type: nauc_precision_at_1_max
      value: 29.9781
    - type: nauc_precision_at_1_std
      value: -27.174799999999998
    - type: nauc_precision_at_1_diff1
      value: 65.8967
    - type: nauc_precision_at_3_max
      value: 29.6113
    - type: nauc_precision_at_3_std
      value: -21.1606
    - type: nauc_precision_at_3_diff1
      value: 37.9441
    - type: nauc_precision_at_5_max
      value: 23.069300000000002
    - type: nauc_precision_at_5_std
      value: -13.168099999999999
    - type: nauc_precision_at_5_diff1
      value: 25.095299999999998
    - type: nauc_precision_at_10_max
      value: 17.7956
    - type: nauc_precision_at_10_std
      value: -0.28609999999999997
    - type: nauc_precision_at_10_diff1
      value: 9.4407
    - type: nauc_precision_at_20_max
      value: 13.2934
    - type: nauc_precision_at_20_std
      value: 10.9965
    - type: nauc_precision_at_20_diff1
      value: 0.43470000000000003
    - type: nauc_precision_at_100_max
      value: 5.1414
    - type: nauc_precision_at_100_std
      value: 16.2173
    - type: nauc_precision_at_100_diff1
      value: -10.2967
    - type: nauc_precision_at_1000_max
      value: 6.0449
    - type: nauc_precision_at_1000_std
      value: 12.698899999999998
    - type: nauc_precision_at_1000_diff1
      value: -8.3748
    - type: nauc_mrr_at_1_max
      value: 29.9781
    - type: nauc_mrr_at_1_std
      value: -27.174799999999998
    - type: nauc_mrr_at_1_diff1
      value: 65.8967
    - type: nauc_mrr_at_3_max
      value: 33.2001
    - type: nauc_mrr_at_3_std
      value: -27.142699999999998
    - type: nauc_mrr_at_3_diff1
      value: 62.546400000000006
    - type: nauc_mrr_at_5_max
      value: 32.9296
    - type: nauc_mrr_at_5_std
      value: -27.0933
    - type: nauc_mrr_at_5_diff1
      value: 62.8135
    - type: nauc_mrr_at_10_max
      value: 32.9972
    - type: nauc_mrr_at_10_std
      value: -26.7892
    - type: nauc_mrr_at_10_diff1
      value: 62.936099999999996
    - type: nauc_mrr_at_20_max
      value: 32.9283
    - type: nauc_mrr_at_20_std
      value: -26.6706
    - type: nauc_mrr_at_20_diff1
      value: 63.0346
    - type: nauc_mrr_at_100_max
      value: 32.8554
    - type: nauc_mrr_at_100_std
      value: -26.7179
    - type: nauc_mrr_at_100_diff1
      value: 63.0571
    - type: nauc_mrr_at_1000_max
      value: 32.8523
    - type: nauc_mrr_at_1000_std
      value: -26.7208
    - type: nauc_mrr_at_1000_diff1
      value: 63.0605
    - type: main_score
      value: 83.155
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB FiQA2018 (default)
      revision: 27a168819829fe9bcd655c2df245fb19452e8e06
      split: test
      type: mteb/fiqa
    metrics:
    - type: ndcg_at_1
      value: 27.468999999999998
    - type: ndcg_at_3
      value: 25.183
    - type: ndcg_at_5
      value: 26.148
    - type: ndcg_at_10
      value: 28.404
    - type: ndcg_at_20
      value: 30.891999999999996
    - type: ndcg_at_100
      value: 35.167
    - type: ndcg_at_1000
      value: 38.803
    - type: map_at_1
      value: 13.864
    - type: map_at_3
      value: 18.989
    - type: map_at_5
      value: 20.521
    - type: map_at_10
      value: 21.858
    - type: map_at_20
      value: 22.686999999999998
    - type: map_at_100
      value: 23.491
    - type: map_at_1000
      value: 23.674
    - type: recall_at_1
      value: 13.864
    - type: recall_at_3
      value: 23.327
    - type: recall_at_5
      value: 28.015
    - type: recall_at_10
      value: 34.977999999999994
    - type: recall_at_20
      value: 42.495
    - type: recall_at_100
      value: 59.967999999999996
    - type: recall_at_1000
      value: 82.39800000000001
    - type: precision_at_1
      value: 27.468999999999998
    - type: precision_at_3
      value: 16.409000000000002
    - type: precision_at_5
      value: 12.099
    - type: precision_at_10
      value: 7.701
    - type: precision_at_20
      value: 4.877
    - type: precision_at_100
      value: 1.465
    - type: precision_at_1000
      value: 0.211
    - type: mrr_at_1
      value: 27.4691
    - type: mrr_at_3
      value: 32.844699999999996
    - type: mrr_at_5
      value: 34.110099999999996
    - type: mrr_at_10
      value: 35.1631
    - type: mrr_at_20
      value: 35.869099999999996
    - type: mrr_at_100
      value: 36.2438
    - type: mrr_at_1000
      value: 36.304700000000004
    - type: nauc_ndcg_at_1_max
      value: 31.897
    - type: nauc_ndcg_at_1_std
      value: 1.7016
    - type: nauc_ndcg_at_1_diff1
      value: 46.680899999999994
    - type: nauc_ndcg_at_3_max
      value: 28.7103
    - type: nauc_ndcg_at_3_std
      value: 0.08220000000000001
    - type: nauc_ndcg_at_3_diff1
      value: 38.1892
    - type: nauc_ndcg_at_5_max
      value: 27.988000000000003
    - type: nauc_ndcg_at_5_std
      value: 2.6533
    - type: nauc_ndcg_at_5_diff1
      value: 37.1171
    - type: nauc_ndcg_at_10_max
      value: 28.205400000000004
    - type: nauc_ndcg_at_10_std
      value: 3.6081000000000003
    - type: nauc_ndcg_at_10_diff1
      value: 37.0636
    - type: nauc_ndcg_at_20_max
      value: 28.708
    - type: nauc_ndcg_at_20_std
      value: 4.999
    - type: nauc_ndcg_at_20_diff1
      value: 35.5315
    - type: nauc_ndcg_at_100_max
      value: 30.000300000000003
    - type: nauc_ndcg_at_100_std
      value: 8.0321
    - type: nauc_ndcg_at_100_diff1
      value: 35.0261
    - type: nauc_ndcg_at_1000_max
      value: 31.476399999999998
    - type: nauc_ndcg_at_1000_std
      value: 8.7892
    - type: nauc_ndcg_at_1000_diff1
      value: 35.8262
    - type: nauc_map_at_1_max
      value: 19.6103
    - type: nauc_map_at_1_std
      value: -1.459
    - type: nauc_map_at_1_diff1
      value: 43.7768
    - type: nauc_map_at_3_max
      value: 23.213800000000003
    - type: nauc_map_at_3_std
      value: -1.0172
    - type: nauc_map_at_3_diff1
      value: 38.4649
    - type: nauc_map_at_5_max
      value: 24.4147
    - type: nauc_map_at_5_std
      value: 0.6049
    - type: nauc_map_at_5_diff1
      value: 38.278800000000004
    - type: nauc_map_at_10_max
      value: 25.1577
    - type: nauc_map_at_10_std
      value: 1.5727000000000002
    - type: nauc_map_at_10_diff1
      value: 37.8236
    - type: nauc_map_at_20_max
      value: 25.5774
    - type: nauc_map_at_20_std
      value: 2.3826
    - type: nauc_map_at_20_diff1
      value: 37.2606
    - type: nauc_map_at_100_max
      value: 26.1034
    - type: nauc_map_at_100_std
      value: 3.0844
    - type: nauc_map_at_100_diff1
      value: 37.1361
    - type: nauc_map_at_1000_max
      value: 26.2481
    - type: nauc_map_at_1000_std
      value: 3.1667
    - type: nauc_map_at_1000_diff1
      value: 37.2042
    - type: nauc_recall_at_1_max
      value: 19.6103
    - type: nauc_recall_at_1_std
      value: -1.459
    - type: nauc_recall_at_1_diff1
      value: 43.7768
    - type: nauc_recall_at_3_max
      value: 21.9254
    - type: nauc_recall_at_3_std
      value: -1.2038
    - type: nauc_recall_at_3_diff1
      value: 32.2851
    - type: nauc_recall_at_5_max
      value: 21.9256
    - type: nauc_recall_at_5_std
      value: 3.1369000000000002
    - type: nauc_recall_at_5_diff1
      value: 29.456500000000002
    - type: nauc_recall_at_10_max
      value: 23.393900000000002
    - type: nauc_recall_at_10_std
      value: 5.2703
    - type: nauc_recall_at_10_diff1
      value: 28.5136
    - type: nauc_recall_at_20_max
      value: 24.5427
    - type: nauc_recall_at_20_std
      value: 9.1449
    - type: nauc_recall_at_20_diff1
      value: 23.919
    - type: nauc_recall_at_100_max
      value: 25.683600000000002
    - type: nauc_recall_at_100_std
      value: 21.0368
    - type: nauc_recall_at_100_diff1
      value: 18.8564
    - type: nauc_recall_at_1000_max
      value: 34.0063
    - type: nauc_recall_at_1000_std
      value: 38.035799999999995
    - type: nauc_recall_at_1000_diff1
      value: 17.1266
    - type: nauc_precision_at_1_max
      value: 31.897
    - type: nauc_precision_at_1_std
      value: 1.7016
    - type: nauc_precision_at_1_diff1
      value: 46.680899999999994
    - type: nauc_precision_at_3_max
      value: 33.503699999999995
    - type: nauc_precision_at_3_std
      value: 1.7436
    - type: nauc_precision_at_3_diff1
      value: 31.8292
    - type: nauc_precision_at_5_max
      value: 35.5747
    - type: nauc_precision_at_5_std
      value: 8.4447
    - type: nauc_precision_at_5_diff1
      value: 27.433600000000002
    - type: nauc_precision_at_10_max
      value: 35.7915
    - type: nauc_precision_at_10_std
      value: 12.0952
    - type: nauc_precision_at_10_diff1
      value: 23.2614
    - type: nauc_precision_at_20_max
      value: 35.421
    - type: nauc_precision_at_20_std
      value: 14.863399999999999
    - type: nauc_precision_at_20_diff1
      value: 17.186899999999998
    - type: nauc_precision_at_100_max
      value: 33.7497
    - type: nauc_precision_at_100_std
      value: 18.5334
    - type: nauc_precision_at_100_diff1
      value: 10.678600000000001
    - type: nauc_precision_at_1000_max
      value: 29.8247
    - type: nauc_precision_at_1000_std
      value: 14.4755
    - type: nauc_precision_at_1000_diff1
      value: 4.1042000000000005
    - type: nauc_mrr_at_1_max
      value: 31.897
    - type: nauc_mrr_at_1_std
      value: 1.7016
    - type: nauc_mrr_at_1_diff1
      value: 46.680899999999994
    - type: nauc_mrr_at_3_max
      value: 32.8019
    - type: nauc_mrr_at_3_std
      value: 1.609
    - type: nauc_mrr_at_3_diff1
      value: 41.2746
    - type: nauc_mrr_at_5_max
      value: 32.9538
    - type: nauc_mrr_at_5_std
      value: 2.884
    - type: nauc_mrr_at_5_diff1
      value: 40.2619
    - type: nauc_mrr_at_10_max
      value: 33.2905
    - type: nauc_mrr_at_10_std
      value: 3.024
    - type: nauc_mrr_at_10_diff1
      value: 40.7879
    - type: nauc_mrr_at_20_max
      value: 33.117000000000004
    - type: nauc_mrr_at_20_std
      value: 3.1062
    - type: nauc_mrr_at_20_diff1
      value: 40.484700000000004
    - type: nauc_mrr_at_100_max
      value: 33.083
    - type: nauc_mrr_at_100_std
      value: 3.405
    - type: nauc_mrr_at_100_diff1
      value: 40.4873
    - type: nauc_mrr_at_1000_max
      value: 33.1046
    - type: nauc_mrr_at_1000_std
      value: 3.4228
    - type: nauc_mrr_at_1000_diff1
      value: 40.5107
    - type: main_score
      value: 28.404
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB HotpotQA (default)
      revision: ab518f4d6fcca38d87c25209f94beba119d02014
      split: test
      type: mteb/hotpotqa
    metrics:
    - type: ndcg_at_1
      value: 73.801
    - type: ndcg_at_3
      value: 54.882
    - type: ndcg_at_5
      value: 56.916999999999994
    - type: ndcg_at_10
      value: 58.766
    - type: ndcg_at_20
      value: 59.946999999999996
    - type: ndcg_at_100
      value: 61.893
    - type: ndcg_at_1000
      value: 63.408
    - type: map_at_1
      value: 36.901
    - type: map_at_3
      value: 46.527
    - type: map_at_5
      value: 48.035
    - type: map_at_10
      value: 49.101
    - type: map_at_20
      value: 49.567
    - type: map_at_100
      value: 49.948
    - type: map_at_1000
      value: 50.022
    - type: recall_at_1
      value: 36.901
    - type: recall_at_3
      value: 50.176
    - type: recall_at_5
      value: 54.193000000000005
    - type: recall_at_10
      value: 58.831999999999994
    - type: recall_at_20
      value: 62.633
    - type: recall_at_100
      value: 71.242
    - type: recall_at_1000
      value: 81.337
    - type: precision_at_1
      value: 73.801
    - type: precision_at_3
      value: 33.45
    - type: precision_at_5
      value: 21.677
    - type: precision_at_10
      value: 11.766
    - type: precision_at_20
      value: 6.263000000000001
    - type: precision_at_100
      value: 1.425
    - type: precision_at_1000
      value: 0.163
    - type: mrr_at_1
      value: 73.8015
    - type: mrr_at_3
      value: 78.44250000000001
    - type: mrr_at_5
      value: 79.1204
    - type: mrr_at_10
      value: 79.4947
    - type: mrr_at_20
      value: 79.6248
    - type: mrr_at_100
      value: 79.7258
    - type: mrr_at_1000
      value: 79.7391
    - type: nauc_ndcg_at_1_max
      value: 52.782
    - type: nauc_ndcg_at_1_std
      value: -7.0408
    - type: nauc_ndcg_at_1_diff1
      value: 72.8754
    - type: nauc_ndcg_at_3_max
      value: 34.7845
    - type: nauc_ndcg_at_3_std
      value: -2.6474
    - type: nauc_ndcg_at_3_diff1
      value: 36.7492
    - type: nauc_ndcg_at_5_max
      value: 32.488299999999995
    - type: nauc_ndcg_at_5_std
      value: -1.6659
    - type: nauc_ndcg_at_5_diff1
      value: 33.1499
    - type: nauc_ndcg_at_10_max
      value: 31.2128
    - type: nauc_ndcg_at_10_std
      value: -0.6525000000000001
    - type: nauc_ndcg_at_10_diff1
      value: 31.3173
    - type: nauc_ndcg_at_20_max
      value: 30.319000000000003
    - type: nauc_ndcg_at_20_std
      value: 0.0078
    - type: nauc_ndcg_at_20_diff1
      value: 30.281799999999997
    - type: nauc_ndcg_at_100_max
      value: 29.873300000000004
    - type: nauc_ndcg_at_100_std
      value: 1.2557
    - type: nauc_ndcg_at_100_diff1
      value: 29.3753
    - type: nauc_ndcg_at_1000_max
      value: 29.8655
    - type: nauc_ndcg_at_1000_std
      value: 1.1226999999999998
    - type: nauc_ndcg_at_1000_diff1
      value: 29.602899999999998
    - type: nauc_map_at_1_max
      value: 52.782
    - type: nauc_map_at_1_std
      value: -7.0408
    - type: nauc_map_at_1_diff1
      value: 72.8754
    - type: nauc_map_at_3_max
      value: 30.2396
    - type: nauc_map_at_3_std
      value: -2.9367
    - type: nauc_map_at_3_diff1
      value: 30.315900000000003
    - type: nauc_map_at_5_max
      value: 28.6694
    - type: nauc_map_at_5_std
      value: -2.2835
    - type: nauc_map_at_5_diff1
      value: 27.9185
    - type: nauc_map_at_10_max
      value: 28.058899999999998
    - type: nauc_map_at_10_std
      value: -1.8286
    - type: nauc_map_at_10_diff1
      value: 27.106400000000004
    - type: nauc_map_at_20_max
      value: 27.763199999999998
    - type: nauc_map_at_20_std
      value: -1.5711
    - type: nauc_map_at_20_diff1
      value: 26.7588
    - type: nauc_map_at_100_max
      value: 27.700000000000003
    - type: nauc_map_at_100_std
      value: -1.3389
    - type: nauc_map_at_100_diff1
      value: 26.615499999999997
    - type: nauc_map_at_1000_max
      value: 27.701999999999998
    - type: nauc_map_at_1000_std
      value: -1.3391
    - type: nauc_map_at_1000_diff1
      value: 26.628800000000002
    - type: nauc_recall_at_1_max
      value: 52.782
    - type: nauc_recall_at_1_std
      value: -7.0408
    - type: nauc_recall_at_1_diff1
      value: 72.8754
    - type: nauc_recall_at_3_max
      value: 26.899800000000003
    - type: nauc_recall_at_3_std
      value: -0.7169
    - type: nauc_recall_at_3_diff1
      value: 21.875
    - type: nauc_recall_at_5_max
      value: 22.0409
    - type: nauc_recall_at_5_std
      value: 1.0630000000000002
    - type: nauc_recall_at_5_diff1
      value: 14.9439
    - type: nauc_recall_at_10_max
      value: 17.8827
    - type: nauc_recall_at_10_std
      value: 3.4513000000000003
    - type: nauc_recall_at_10_diff1
      value: 9.6887
    - type: nauc_recall_at_20_max
      value: 14.6979
    - type: nauc_recall_at_20_std
      value: 5.4514
    - type: nauc_recall_at_20_diff1
      value: 6.103800000000001
    - type: nauc_recall_at_100_max
      value: 10.054599999999999
    - type: nauc_recall_at_100_std
      value: 11.4136
    - type: nauc_recall_at_100_diff1
      value: -1.2643
    - type: nauc_recall_at_1000_max
      value: 3.9052000000000002
    - type: nauc_recall_at_1000_std
      value: 13.176099999999998
    - type: nauc_recall_at_1000_diff1
      value: -8.8098
    - type: nauc_precision_at_1_max
      value: 52.782
    - type: nauc_precision_at_1_std
      value: -7.0408
    - type: nauc_precision_at_1_diff1
      value: 72.8754
    - type: nauc_precision_at_3_max
      value: 26.899800000000003
    - type: nauc_precision_at_3_std
      value: -0.7169
    - type: nauc_precision_at_3_diff1
      value: 21.875
    - type: nauc_precision_at_5_max
      value: 22.0409
    - type: nauc_precision_at_5_std
      value: 1.0630000000000002
    - type: nauc_precision_at_5_diff1
      value: 14.9439
    - type: nauc_precision_at_10_max
      value: 17.8827
    - type: nauc_precision_at_10_std
      value: 3.4513000000000003
    - type: nauc_precision_at_10_diff1
      value: 9.6887
    - type: nauc_precision_at_20_max
      value: 14.6979
    - type: nauc_precision_at_20_std
      value: 5.4514
    - type: nauc_precision_at_20_diff1
      value: 6.103800000000001
    - type: nauc_precision_at_100_max
      value: 10.054599999999999
    - type: nauc_precision_at_100_std
      value: 11.4136
    - type: nauc_precision_at_100_diff1
      value: -1.2643
    - type: nauc_precision_at_1000_max
      value: 3.9052000000000002
    - type: nauc_precision_at_1000_std
      value: 13.176099999999998
    - type: nauc_precision_at_1000_diff1
      value: -8.8098
    - type: nauc_mrr_at_1_max
      value: 52.782
    - type: nauc_mrr_at_1_std
      value: -7.0408
    - type: nauc_mrr_at_1_diff1
      value: 72.8754
    - type: nauc_mrr_at_3_max
      value: 54.295700000000004
    - type: nauc_mrr_at_3_std
      value: -4.637700000000001
    - type: nauc_mrr_at_3_diff1
      value: 70.1027
    - type: nauc_mrr_at_5_max
      value: 54.3589
    - type: nauc_mrr_at_5_std
      value: -4.1942
    - type: nauc_mrr_at_5_diff1
      value: 69.9827
    - type: nauc_mrr_at_10_max
      value: 54.3287
    - type: nauc_mrr_at_10_std
      value: -3.8112
    - type: nauc_mrr_at_10_diff1
      value: 69.857
    - type: nauc_mrr_at_20_max
      value: 54.325199999999995
    - type: nauc_mrr_at_20_std
      value: -3.7948999999999997
    - type: nauc_mrr_at_20_diff1
      value: 69.92699999999999
    - type: nauc_mrr_at_100_max
      value: 54.3234
    - type: nauc_mrr_at_100_std
      value: -3.8176
    - type: nauc_mrr_at_100_diff1
      value: 69.963
    - type: nauc_mrr_at_1000_max
      value: 54.3152
    - type: nauc_mrr_at_1000_std
      value: -3.8351
    - type: nauc_mrr_at_1000_diff1
      value: 69.9678
    - type: main_score
      value: 58.766
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB ImdbClassification (default)
      revision: 3d86128a09e091d6018b6d26cad27f2739fc2db7
      split: test
      type: mteb/imdb
    metrics:
    - type: accuracy
      value: 62.91
    - type: f1
      value: 62.572799999999994
    - type: f1_weighted
      value: 62.572799999999994
    - type: ap
      value: 58.2831
    - type: ap_weighted
      value: 58.2831
    - type: main_score
      value: 62.91
    task:
      type: Classification
  - dataset:
      config: ar
      name: MTEB MIRACLRetrieval (ar)
      revision: main
      split: dev
      type: miracl/mmteb-miracl
    metrics:
    - type: ndcg_at_1
      value: 55.559000000000005
    - type: ndcg_at_3
      value: 56.43899999999999
    - type: ndcg_at_5
      value: 59.34700000000001
    - type: ndcg_at_10
      value: 62.541000000000004
    - type: ndcg_at_20
      value: 64.739
    - type: ndcg_at_100
      value: 67.101
    - type: ndcg_at_1000
      value: 68.05
    - type: map_at_1
      value: 37.009
    - type: map_at_3
      value: 49.559
    - type: map_at_5
      value: 52.766999999999996
    - type: map_at_10
      value: 54.891
    - type: map_at_20
      value: 55.818
    - type: map_at_100
      value: 56.364000000000004
    - type: map_at_1000
      value: 56.418
    - type: recall_at_1
      value: 37.009
    - type: recall_at_3
      value: 56.903000000000006
    - type: recall_at_5
      value: 65.18
    - type: recall_at_10
      value: 73.317
    - type: recall_at_20
      value: 80.205
    - type: recall_at_100
      value: 90.066
    - type: recall_at_1000
      value: 96.272
    - type: precision_at_1
      value: 55.559000000000005
    - type: precision_at_3
      value: 32.056000000000004
    - type: precision_at_5
      value: 22.942
    - type: precision_at_10
      value: 13.483999999999998
    - type: precision_at_20
      value: 7.548000000000001
    - type: precision_at_100
      value: 1.752
    - type: precision_at_1000
      value: 0.189
    - type: mrr_at_1
      value: 55.559400000000004
    - type: mrr_at_3
      value: 63.7201
    - type: mrr_at_5
      value: 65.0996
    - type: mrr_at_10
      value: 65.8096
    - type: mrr_at_20
      value: 66.1023
    - type: mrr_at_100
      value: 66.2427
    - type: mrr_at_1000
      value: 66.2595
    - type: nauc_ndcg_at_1_max
      value: 39.1686
    - type: nauc_ndcg_at_1_std
      value: 1.7862
    - type: nauc_ndcg_at_1_diff1
      value: 45.7904
    - type: nauc_ndcg_at_3_max
      value: 37.2044
    - type: nauc_ndcg_at_3_std
      value: -1.6014
    - type: nauc_ndcg_at_3_diff1
      value: 37.9844
    - type: nauc_ndcg_at_5_max
      value: 39.2524
    - type: nauc_ndcg_at_5_std
      value: -0.6319
    - type: nauc_ndcg_at_5_diff1
      value: 38.2785
    - type: nauc_ndcg_at_10_max
      value: 40.1167
    - type: nauc_ndcg_at_10_std
      value: 0.3359
    - type: nauc_ndcg_at_10_diff1
      value: 37.4785
    - type: nauc_ndcg_at_20_max
      value: 41.3886
    - type: nauc_ndcg_at_20_std
      value: 2.8987
    - type: nauc_ndcg_at_20_diff1
      value: 37.0635
    - type: nauc_ndcg_at_100_max
      value: 42.357299999999995
    - type: nauc_ndcg_at_100_std
      value: 5.2258
    - type: nauc_ndcg_at_100_diff1
      value: 37.3142
    - type: nauc_ndcg_at_1000_max
      value: 41.9076
    - type: nauc_ndcg_at_1000_std
      value: 4.539499999999999
    - type: nauc_ndcg_at_1000_diff1
      value: 37.703399999999995
    - type: nauc_map_at_1_max
      value: 21.7624
    - type: nauc_map_at_1_std
      value: -10.1554
    - type: nauc_map_at_1_diff1
      value: 45.413599999999995
    - type: nauc_map_at_3_max
      value: 32.231
    - type: nauc_map_at_3_std
      value: -5.7029000000000005
    - type: nauc_map_at_3_diff1
      value: 39.678799999999995
    - type: nauc_map_at_5_max
      value: 35.3238
    - type: nauc_map_at_5_std
      value: -3.3897999999999997
    - type: nauc_map_at_5_diff1
      value: 38.901599999999995
    - type: nauc_map_at_10_max
      value: 36.248799999999996
    - type: nauc_map_at_10_std
      value: -2.5503
    - type: nauc_map_at_10_diff1
      value: 38.2086
    - type: nauc_map_at_20_max
      value: 36.8226
    - type: nauc_map_at_20_std
      value: -1.5142
    - type: nauc_map_at_20_diff1
      value: 37.9922
    - type: nauc_map_at_100_max
      value: 37.0911
    - type: nauc_map_at_100_std
      value: -0.9837
    - type: nauc_map_at_100_diff1
      value: 37.9955
    - type: nauc_map_at_1000_max
      value: 37.0788
    - type: nauc_map_at_1000_std
      value: -0.9948
    - type: nauc_map_at_1000_diff1
      value: 38.016299999999994
    - type: nauc_recall_at_1_max
      value: 21.7624
    - type: nauc_recall_at_1_std
      value: -10.1554
    - type: nauc_recall_at_1_diff1
      value: 45.413599999999995
    - type: nauc_recall_at_3_max
      value: 32.4031
    - type: nauc_recall_at_3_std
      value: -5.2341999999999995
    - type: nauc_recall_at_3_diff1
      value: 33.6415
    - type: nauc_recall_at_5_max
      value: 37.6932
    - type: nauc_recall_at_5_std
      value: -1.2136
    - type: nauc_recall_at_5_diff1
      value: 31.629600000000003
    - type: nauc_recall_at_10_max
      value: 39.6688
    - type: nauc_recall_at_10_std
      value: 1.3085
    - type: nauc_recall_at_10_diff1
      value: 28.184900000000003
    - type: nauc_recall_at_20_max
      value: 45.1114
    - type: nauc_recall_at_20_std
      value: 11.9353
    - type: nauc_recall_at_20_diff1
      value: 24.9804
    - type: nauc_recall_at_100_max
      value: 58.7538
    - type: nauc_recall_at_100_std
      value: 40.016200000000005
    - type: nauc_recall_at_100_diff1
      value: 22.0195
    - type: nauc_recall_at_1000_max
      value: 69.68910000000001
    - type: nauc_recall_at_1000_std
      value: 61.42959999999999
    - type: nauc_recall_at_1000_diff1
      value: 18.6353
    - type: nauc_precision_at_1_max
      value: 39.1686
    - type: nauc_precision_at_1_std
      value: 1.7862
    - type: nauc_precision_at_1_diff1
      value: 45.7904
    - type: nauc_precision_at_3_max
      value: 38.101400000000005
    - type: nauc_precision_at_3_std
      value: 13.7012
    - type: nauc_precision_at_3_diff1
      value: 9.3923
    - type: nauc_precision_at_5_max
      value: 36.4465
    - type: nauc_precision_at_5_std
      value: 18.3961
    - type: nauc_precision_at_5_diff1
      value: 1.5756
    - type: nauc_precision_at_10_max
      value: 29.869600000000002
    - type: nauc_precision_at_10_std
      value: 19.869899999999998
    - type: nauc_precision_at_10_diff1
      value: -5.9939
    - type: nauc_precision_at_20_max
      value: 26.564700000000002
    - type: nauc_precision_at_20_std
      value: 24.7639
    - type: nauc_precision_at_20_diff1
      value: -10.8804
    - type: nauc_precision_at_100_max
      value: 20.137
    - type: nauc_precision_at_100_std
      value: 28.4182
    - type: nauc_precision_at_100_diff1
      value: -15.1979
    - type: nauc_precision_at_1000_max
      value: 14.4263
    - type: nauc_precision_at_1000_std
      value: 25.336199999999998
    - type: nauc_precision_at_1000_diff1
      value: -17.149800000000003
    - type: nauc_mrr_at_1_max
      value: 39.1686
    - type: nauc_mrr_at_1_std
      value: 1.7862
    - type: nauc_mrr_at_1_diff1
      value: 45.7904
    - type: nauc_mrr_at_3_max
      value: 43.3345
    - type: nauc_mrr_at_3_std
      value: 3.6245
    - type: nauc_mrr_at_3_diff1
      value: 42.332300000000004
    - type: nauc_mrr_at_5_max
      value: 43.7305
    - type: nauc_mrr_at_5_std
      value: 4.18
    - type: nauc_mrr_at_5_diff1
      value: 42.3171
    - type: nauc_mrr_at_10_max
      value: 43.8493
    - type: nauc_mrr_at_10_std
      value: 4.3809000000000005
    - type: nauc_mrr_at_10_diff1
      value: 42.3117
    - type: nauc_mrr_at_20_max
      value: 43.8121
    - type: nauc_mrr_at_20_std
      value: 4.526
    - type: nauc_mrr_at_20_diff1
      value: 42.3117
    - type: nauc_mrr_at_100_max
      value: 43.7806
    - type: nauc_mrr_at_100_std
      value: 4.5652
    - type: nauc_mrr_at_100_diff1
      value: 42.3692
    - type: nauc_mrr_at_1000_max
      value: 43.7629
    - type: nauc_mrr_at_1000_std
      value: 4.5475
    - type: nauc_mrr_at_1000_diff1
      value: 42.373
    - type: main_score
      value: 62.541000000000004
    task:
      type: Retrieval
  - dataset:
      config: bn
      name: MTEB MIRACLRetrieval (bn)
      revision: main
      split: dev
      type: miracl/mmteb-miracl
    metrics:
    - type: ndcg_at_1
      value: 56.691
    - type: ndcg_at_3
      value: 59.88
    - type: ndcg_at_5
      value: 62.717999999999996
    - type: ndcg_at_10
      value: 65.484
    - type: ndcg_at_20
      value: 67.838
    - type: ndcg_at_100
      value: 70.14200000000001
    - type: ndcg_at_1000
      value: 70.994
    - type: map_at_1
      value: 36.05
    - type: map_at_3
      value: 51.734
    - type: map_at_5
      value: 55.093
    - type: map_at_10
      value: 57.053
    - type: map_at_20
      value: 58.196999999999996
    - type: map_at_100
      value: 58.786
    - type: map_at_1000
      value: 58.841
    - type: recall_at_1
      value: 36.05
    - type: recall_at_3
      value: 61.596
    - type: recall_at_5
      value: 69.76599999999999
    - type: recall_at_10
      value: 76.854
    - type: recall_at_20
      value: 83.667
    - type: recall_at_100
      value: 92.85
    - type: recall_at_1000
      value: 97.928
    - type: precision_at_1
      value: 56.691
    - type: precision_at_3
      value: 35.848
    - type: precision_at_5
      value: 25.499
    - type: precision_at_10
      value: 14.793000000000001
    - type: precision_at_20
      value: 8.37
    - type: precision_at_100
      value: 1.925
    - type: precision_at_1000
      value: 0.20600000000000002
    - type: mrr_at_1
      value: 56.691
    - type: mrr_at_3
      value: 67.1127
    - type: mrr_at_5
      value: 68.5604
    - type: mrr_at_10
      value: 69.1703
    - type: mrr_at_20
      value: 69.35289999999999
    - type: mrr_at_100
      value: 69.4819
    - type: mrr_at_1000
      value: 69.4957
    - type: nauc_ndcg_at_1_max
      value: 41.866
    - type: nauc_ndcg_at_1_std
      value: 11.7317
    - type: nauc_ndcg_at_1_diff1
      value: 40.4762
    - type: nauc_ndcg_at_3_max
      value: 36.677
    - type: nauc_ndcg_at_3_std
      value: 0.4032
    - type: nauc_ndcg_at_3_diff1
      value: 36.459
    - type: nauc_ndcg_at_5_max
      value: 38.7948
    - type: nauc_ndcg_at_5_std
      value: 2.169
    - type: nauc_ndcg_at_5_diff1
      value: 34.9733
    - type: nauc_ndcg_at_10_max
      value: 41.2916
    - type: nauc_ndcg_at_10_std
      value: 4.6691
    - type: nauc_ndcg_at_10_diff1
      value: 34.972300000000004
    - type: nauc_ndcg_at_20_max
      value: 42.0471
    - type: nauc_ndcg_at_20_std
      value: 6.9529
    - type: nauc_ndcg_at_20_diff1
      value: 35.2909
    - type: nauc_ndcg_at_100_max
      value: 43.2206
    - type: nauc_ndcg_at_100_std
      value: 9.8597
    - type: nauc_ndcg_at_100_diff1
      value: 34.7908
    - type: nauc_ndcg_at_1000_max
      value: 42.9023
    - type: nauc_ndcg_at_1000_std
      value: 9.1978
    - type: nauc_ndcg_at_1000_diff1
      value: 35.5526
    - type: nauc_map_at_1_max
      value: 20.435
    - type: nauc_map_at_1_std
      value: -8.3764
    - type: nauc_map_at_1_diff1
      value: 45.6061
    - type: nauc_map_at_3_max
      value: 29.855900000000002
    - type: nauc_map_at_3_std
      value: -6.9869
    - type: nauc_map_at_3_diff1
      value: 39.475
    - type: nauc_map_at_5_max
      value: 33.9572
    - type: nauc_map_at_5_std
      value: -3.164
    - type: nauc_map_at_5_diff1
      value: 37.4095
    - type: nauc_map_at_10_max
      value: 35.8339
    - type: nauc_map_at_10_std
      value: -0.8439
    - type: nauc_map_at_10_diff1
      value: 36.903999999999996
    - type: nauc_map_at_20_max
      value: 36.1995
    - type: nauc_map_at_20_std
      value: 0.2973
    - type: nauc_map_at_20_diff1
      value: 36.8904
    - type: nauc_map_at_100_max
      value: 36.5903
    - type: nauc_map_at_100_std
      value: 1.2213999999999998
    - type: nauc_map_at_100_diff1
      value: 36.6721
    - type: nauc_map_at_1000_max
      value: 36.5844
    - type: nauc_map_at_1000_std
      value: 1.2026000000000001
    - type: nauc_map_at_1000_diff1
      value: 36.7259
    - type: nauc_recall_at_1_max
      value: 20.435
    - type: nauc_recall_at_1_std
      value: -8.3764
    - type: nauc_recall_at_1_diff1
      value: 45.6061
    - type: nauc_recall_at_3_max
      value: 26.366600000000002
    - type: nauc_recall_at_3_std
      value: -10.0911
    - type: nauc_recall_at_3_diff1
      value: 33.1969
    - type: nauc_recall_at_5_max
      value: 34.080799999999996
    - type: nauc_recall_at_5_std
      value: -3.2670999999999997
    - type: nauc_recall_at_5_diff1
      value: 26.939
    - type: nauc_recall_at_10_max
      value: 39.6727
    - type: nauc_recall_at_10_std
      value: 3.5848999999999998
    - type: nauc_recall_at_10_diff1
      value: 25.359399999999997
    - type: nauc_recall_at_20_max
      value: 42.824400000000004
    - type: nauc_recall_at_20_std
      value: 10.9569
    - type: nauc_recall_at_20_diff1
      value: 25.8988
    - type: nauc_recall_at_100_max
      value: 56.9357
    - type: nauc_recall_at_100_std
      value: 40.6576
    - type: nauc_recall_at_100_diff1
      value: 17.9669
    - type: nauc_recall_at_1000_max
      value: 77.9855
    - type: nauc_recall_at_1000_std
      value: 69.14519999999999
    - type: nauc_recall_at_1000_diff1
      value: 31.317
    - type: nauc_precision_at_1_max
      value: 41.866
    - type: nauc_precision_at_1_std
      value: 11.7317
    - type: nauc_precision_at_1_diff1
      value: 40.4762
    - type: nauc_precision_at_3_max
      value: 41.7292
    - type: nauc_precision_at_3_std
      value: 19.4845
    - type: nauc_precision_at_3_diff1
      value: 2.3043
    - type: nauc_precision_at_5_max
      value: 41.165600000000005
    - type: nauc_precision_at_5_std
      value: 28.4709
    - type: nauc_precision_at_5_diff1
      value: -8.5182
    - type: nauc_precision_at_10_max
      value: 36.8002
    - type: nauc_precision_at_10_std
      value: 33.0094
    - type: nauc_precision_at_10_diff1
      value: -13.6996
    - type: nauc_precision_at_20_max
      value: 29.5172
    - type: nauc_precision_at_20_std
      value: 34.6802
    - type: nauc_precision_at_20_diff1
      value: -15.762
    - type: nauc_precision_at_100_max
      value: 23.539099999999998
    - type: nauc_precision_at_100_std
      value: 38.3806
    - type: nauc_precision_at_100_diff1
      value: -21.1116
    - type: nauc_precision_at_1000_max
      value: 18.6827
    - type: nauc_precision_at_1000_std
      value: 34.7766
    - type: nauc_precision_at_1000_diff1
      value: -20.9498
    - type: nauc_mrr_at_1_max
      value: 41.866
    - type: nauc_mrr_at_1_std
      value: 11.7317
    - type: nauc_mrr_at_1_diff1
      value: 40.4762
    - type: nauc_mrr_at_3_max
      value: 47.225
    - type: nauc_mrr_at_3_std
      value: 13.6943
    - type: nauc_mrr_at_3_diff1
      value: 37.979600000000005
    - type: nauc_mrr_at_5_max
      value: 47.478500000000004
    - type: nauc_mrr_at_5_std
      value: 15.2375
    - type: nauc_mrr_at_5_diff1
      value: 36.6924
    - type: nauc_mrr_at_10_max
      value: 47.7794
    - type: nauc_mrr_at_10_std
      value: 15.620899999999999
    - type: nauc_mrr_at_10_diff1
      value: 36.9685
    - type: nauc_mrr_at_20_max
      value: 47.6434
    - type: nauc_mrr_at_20_std
      value: 15.4696
    - type: nauc_mrr_at_20_diff1
      value: 37.1096
    - type: nauc_mrr_at_100_max
      value: 47.5377
    - type: nauc_mrr_at_100_std
      value: 15.360499999999998
    - type: nauc_mrr_at_100_diff1
      value: 37.1581
    - type: nauc_mrr_at_1000_max
      value: 47.5182
    - type: nauc_mrr_at_1000_std
      value: 15.345600000000001
    - type: nauc_mrr_at_1000_diff1
      value: 37.1651
    - type: main_score
      value: 65.484
    task:
      type: Retrieval
  - dataset:
      config: de
      name: MTEB MIRACLRetrieval (de)
      revision: main
      split: dev
      type: miracl/mmteb-miracl
    metrics:
    - type: ndcg_at_1
      value: 41.967
    - type: ndcg_at_3
      value: 39.486
    - type: ndcg_at_5
      value: 41.496
    - type: ndcg_at_10
      value: 45.141
    - type: ndcg_at_20
      value: 49.012
    - type: ndcg_at_100
      value: 53.461000000000006
    - type: ndcg_at_1000
      value: 55.462999999999994
    - type: map_at_1
      value: 19.494
    - type: map_at_3
      value: 29.866999999999997
    - type: map_at_5
      value: 33.183
    - type: map_at_10
      value: 35.82
    - type: map_at_20
      value: 37.405
    - type: map_at_100
      value: 38.486
    - type: map_at_1000
      value: 38.624
    - type: recall_at_1
      value: 19.494
    - type: recall_at_3
      value: 35.56
    - type: recall_at_5
      value: 44.448
    - type: recall_at_10
      value: 53.774
    - type: recall_at_20
      value: 65.659
    - type: recall_at_100
      value: 83.314
    - type: recall_at_1000
      value: 95.045
    - type: precision_at_1
      value: 41.967
    - type: precision_at_3
      value: 28.633999999999997
    - type: precision_at_5
      value: 21.836
    - type: precision_at_10
      value: 13.869000000000002
    - type: precision_at_20
      value: 8.443000000000001
    - type: precision_at_100
      value: 2.193
    - type: precision_at_1000
      value: 0.252
    - type: mrr_at_1
      value: 41.9672
    - type: mrr_at_3
      value: 49.8361
    - type: mrr_at_5
      value: 51.9016
    - type: mrr_at_10
      value: 52.847500000000004
    - type: mrr_at_20
      value: 53.3528
    - type: mrr_at_100
      value: 53.6068
    - type: mrr_at_1000
      value: 53.632999999999996
    - type: nauc_ndcg_at_1_max
      value: 47.2596
    - type: nauc_ndcg_at_1_std
      value: 10.462100000000001
    - type: nauc_ndcg_at_1_diff1
      value: 30.1962
    - type: nauc_ndcg_at_3_max
      value: 44.2307
    - type: nauc_ndcg_at_3_std
      value: 17.5815
    - type: nauc_ndcg_at_3_diff1
      value: 29.371399999999998
    - type: nauc_ndcg_at_5_max
      value: 44.07
    - type: nauc_ndcg_at_5_std
      value: 13.7942
    - type: nauc_ndcg_at_5_diff1
      value: 31.1618
    - type: nauc_ndcg_at_10_max
      value: 43.406800000000004
    - type: nauc_ndcg_at_10_std
      value: 13.1051
    - type: nauc_ndcg_at_10_diff1
      value: 30.198399999999996
    - type: nauc_ndcg_at_20_max
      value: 44.2888
    - type: nauc_ndcg_at_20_std
      value: 16.2174
    - type: nauc_ndcg_at_20_diff1
      value: 31.1847
    - type: nauc_ndcg_at_100_max
      value: 47.042899999999996
    - type: nauc_ndcg_at_100_std
      value: 18.6719
    - type: nauc_ndcg_at_100_diff1
      value: 31.4178
    - type: nauc_ndcg_at_1000_max
      value: 47.2147
    - type: nauc_ndcg_at_1000_std
      value: 19.165
    - type: nauc_ndcg_at_1000_diff1
      value: 31.229400000000002
    - type: nauc_map_at_1_max
      value: 28.3144
    - type: nauc_map_at_1_std
      value: 4.6845
    - type: nauc_map_at_1_diff1
      value: 29.528
    - type: nauc_map_at_3_max
      value: 36.9973
    - type: nauc_map_at_3_std
      value: 11.669
    - type: nauc_map_at_3_diff1
      value: 32.3092
    - type: nauc_map_at_5_max
      value: 39.4916
    - type: nauc_map_at_5_std
      value: 12.0862
    - type: nauc_map_at_5_diff1
      value: 31.7635
    - type: nauc_map_at_10_max
      value: 40.2979
    - type: nauc_map_at_10_std
      value: 12.536
    - type: nauc_map_at_10_diff1
      value: 30.584600000000002
    - type: nauc_map_at_20_max
      value: 40.7003
    - type: nauc_map_at_20_std
      value: 13.5966
    - type: nauc_map_at_20_diff1
      value: 30.8718
    - type: nauc_map_at_100_max
      value: 41.6514
    - type: nauc_map_at_100_std
      value: 14.360500000000002
    - type: nauc_map_at_100_diff1
      value: 31.1345
    - type: nauc_map_at_1000_max
      value: 41.6996
    - type: nauc_map_at_1000_std
      value: 14.4203
    - type: nauc_map_at_1000_diff1
      value: 31.128600000000002
    - type: nauc_recall_at_1_max
      value: 28.3144
    - type: nauc_recall_at_1_std
      value: 4.6845
    - type: nauc_recall_at_1_diff1
      value: 29.528
    - type: nauc_recall_at_3_max
      value: 33.567
    - type: nauc_recall_at_3_std
      value: 12.7075
    - type: nauc_recall_at_3_diff1
      value: 27.9119
    - type: nauc_recall_at_5_max
      value: 36.5991
    - type: nauc_recall_at_5_std
      value: 8.7177
    - type: nauc_recall_at_5_diff1
      value: 28.3433
    - type: nauc_recall_at_10_max
      value: 36.5863
    - type: nauc_recall_at_10_std
      value: 8.2944
    - type: nauc_recall_at_10_diff1
      value: 26.411299999999997
    - type: nauc_recall_at_20_max
      value: 35.970200000000006
    - type: nauc_recall_at_20_std
      value: 15.487
    - type: nauc_recall_at_20_diff1
      value: 29.0362
    - type: nauc_recall_at_100_max
      value: 48.892
    - type: nauc_recall_at_100_std
      value: 30.1672
    - type: nauc_recall_at_100_diff1
      value: 29.9305
    - type: nauc_recall_at_1000_max
      value: 66.36410000000001
    - type: nauc_recall_at_1000_std
      value: 64.2413
    - type: nauc_recall_at_1000_diff1
      value: 32.7869
    - type: nauc_precision_at_1_max
      value: 47.2596
    - type: nauc_precision_at_1_std
      value: 10.462100000000001
    - type: nauc_precision_at_1_diff1
      value: 30.1962
    - type: nauc_precision_at_3_max
      value: 46.6036
    - type: nauc_precision_at_3_std
      value: 22.917
    - type: nauc_precision_at_3_diff1
      value: 21.104200000000002
    - type: nauc_precision_at_5_max
      value: 44.357
    - type: nauc_precision_at_5_std
      value: 21.4999
    - type: nauc_precision_at_5_diff1
      value: 16.378899999999998
    - type: nauc_precision_at_10_max
      value: 39.1332
    - type: nauc_precision_at_10_std
      value: 20.241500000000002
    - type: nauc_precision_at_10_diff1
      value: 10.2133
    - type: nauc_precision_at_20_max
      value: 36.7308
    - type: nauc_precision_at_20_std
      value: 26.994699999999998
    - type: nauc_precision_at_20_diff1
      value: 8.2737
    - type: nauc_precision_at_100_max
      value: 33.8289
    - type: nauc_precision_at_100_std
      value: 29.243000000000002
    - type: nauc_precision_at_100_diff1
      value: 2.6802
    - type: nauc_precision_at_1000_max
      value: 27.7792
    - type: nauc_precision_at_1000_std
      value: 30.017899999999997
    - type: nauc_precision_at_1000_diff1
      value: -2.3043
    - type: nauc_mrr_at_1_max
      value: 47.2596
    - type: nauc_mrr_at_1_std
      value: 10.462100000000001
    - type: nauc_mrr_at_1_diff1
      value: 30.1962
    - type: nauc_mrr_at_3_max
      value: 47.8206
    - type: nauc_mrr_at_3_std
      value: 15.509999999999998
    - type: nauc_mrr_at_3_diff1
      value: 28.4831
    - type: nauc_mrr_at_5_max
      value: 48.4225
    - type: nauc_mrr_at_5_std
      value: 14.0032
    - type: nauc_mrr_at_5_diff1
      value: 30.2989
    - type: nauc_mrr_at_10_max
      value: 48.2881
    - type: nauc_mrr_at_10_std
      value: 14.383199999999999
    - type: nauc_mrr_at_10_diff1
      value: 30.047800000000002
    - type: nauc_mrr_at_20_max
      value: 48.2964
    - type: nauc_mrr_at_20_std
      value: 14.7531
    - type: nauc_mrr_at_20_diff1
      value: 30.154199999999996
    - type: nauc_mrr_at_100_max
      value: 48.2656
    - type: nauc_mrr_at_100_std
      value: 14.5864
    - type: nauc_mrr_at_100_diff1
      value: 30.153299999999998
    - type: nauc_mrr_at_1000_max
      value: 48.2739
    - type: nauc_mrr_at_1000_std
      value: 14.5892
    - type: nauc_mrr_at_1000_diff1
      value: 30.1671
    - type: main_score
      value: 45.141
    task:
      type: Retrieval
  - dataset:
      config: en
      name: MTEB MIRACLRetrieval (en)
      revision: main
      split: dev
      type: miracl/mmteb-miracl
    metrics:
    - type: ndcg_at_1
      value: 41.176
    - type: ndcg_at_3
      value: 41.197
    - type: ndcg_at_5
      value: 42.086
    - type: ndcg_at_10
      value: 46.682
    - type: ndcg_at_20
      value: 50.157
    - type: ndcg_at_100
      value: 54.32599999999999
    - type: ndcg_at_1000
      value: 56.567
    - type: map_at_1
      value: 19.322
    - type: map_at_3
      value: 29.965999999999998
    - type: map_at_5
      value: 32.767
    - type: map_at_10
      value: 35.961
    - type: map_at_20
      value: 37.506
    - type: map_at_100
      value: 38.585
    - type: map_at_1000
      value: 38.756
    - type: recall_at_1
      value: 19.322
    - type: recall_at_3
      value: 37.171
    - type: recall_at_5
      value: 44.695
    - type: recall_at_10
      value: 57.721000000000004
    - type: recall_at_20
      value: 67.57
    - type: recall_at_100
      value: 83.256
    - type: recall_at_1000
      value: 95.511
    - type: precision_at_1
      value: 41.176
    - type: precision_at_3
      value: 29.328
    - type: precision_at_5
      value: 21.552
    - type: precision_at_10
      value: 14.556
    - type: precision_at_20
      value: 8.892
    - type: precision_at_100
      value: 2.325
    - type: precision_at_1000
      value: 0.27599999999999997
    - type: mrr_at_1
      value: 41.1765
    - type: mrr_at_3
      value: 52.3571
    - type: mrr_at_5
      value: 53.8214
    - type: mrr_at_10
      value: 55.2296
    - type: mrr_at_20
      value: 55.58070000000001
    - type: mrr_at_100
      value: 55.755500000000005
    - type: mrr_at_1000
      value: 55.7773
    - type: nauc_ndcg_at_1_max
      value: 34.3579
    - type: nauc_ndcg_at_1_std
      value: 4.9725
    - type: nauc_ndcg_at_1_diff1
      value: 34.5973
    - type: nauc_ndcg_at_3_max
      value: 33.4771
    - type: nauc_ndcg_at_3_std
      value: 1.4036
    - type: nauc_ndcg_at_3_diff1
      value: 28.7098
    - type: nauc_ndcg_at_5_max
      value: 32.4928
    - type: nauc_ndcg_at_5_std
      value: -0.066
    - type: nauc_ndcg_at_5_diff1
      value: 28.6068
    - type: nauc_ndcg_at_10_max
      value: 32.068999999999996
    - type: nauc_ndcg_at_10_std
      value: 1.6602
    - type: nauc_ndcg_at_10_diff1
      value: 26.9818
    - type: nauc_ndcg_at_20_max
      value: 33.9623
    - type: nauc_ndcg_at_20_std
      value: 4.261299999999999
    - type: nauc_ndcg_at_20_diff1
      value: 26.4283
    - type: nauc_ndcg_at_100_max
      value: 35.507
    - type: nauc_ndcg_at_100_std
      value: 7.991099999999999
    - type: nauc_ndcg_at_100_diff1
      value: 25.9616
    - type: nauc_ndcg_at_1000_max
      value: 35.9545
    - type: nauc_ndcg_at_1000_std
      value: 8.1357
    - type: nauc_ndcg_at_1000_diff1
      value: 26.5577
    - type: nauc_map_at_1_max
      value: 26.392300000000002
    - type: nauc_map_at_1_std
      value: -1.0763
    - type: nauc_map_at_1_diff1
      value: 32.73
    - type: nauc_map_at_3_max
      value: 29.8191
    - type: nauc_map_at_3_std
      value: -1.8852
    - type: nauc_map_at_3_diff1
      value: 29.5076
    - type: nauc_map_at_5_max
      value: 30.8727
    - type: nauc_map_at_5_std
      value: -1.3785
    - type: nauc_map_at_5_diff1
      value: 29.475299999999997
    - type: nauc_map_at_10_max
      value: 31.5092
    - type: nauc_map_at_10_std
      value: -0.1203
    - type: nauc_map_at_10_diff1
      value: 28.1841
    - type: nauc_map_at_20_max
      value: 32.6157
    - type: nauc_map_at_20_std
      value: 0.9819
    - type: nauc_map_at_20_diff1
      value: 28.339399999999998
    - type: nauc_map_at_100_max
      value: 33.1895
    - type: nauc_map_at_100_std
      value: 2.1590000000000003
    - type: nauc_map_at_100_diff1
      value: 28.180100000000003
    - type: nauc_map_at_1000_max
      value: 33.2679
    - type: nauc_map_at_1000_std
      value: 2.2186999999999997
    - type: nauc_map_at_1000_diff1
      value: 28.2088
    - type: nauc_recall_at_1_max
      value: 26.392300000000002
    - type: nauc_recall_at_1_std
      value: -1.0763
    - type: nauc_recall_at_1_diff1
      value: 32.73
    - type: nauc_recall_at_3_max
      value: 24.2787
    - type: nauc_recall_at_3_std
      value: -4.1108
    - type: nauc_recall_at_3_diff1
      value: 23.903299999999998
    - type: nauc_recall_at_5_max
      value: 23.0102
    - type: nauc_recall_at_5_std
      value: -4.4748
    - type: nauc_recall_at_5_diff1
      value: 22.4027
    - type: nauc_recall_at_10_max
      value: 20.5018
    - type: nauc_recall_at_10_std
      value: -2.1145
    - type: nauc_recall_at_10_diff1
      value: 17.5745
    - type: nauc_recall_at_20_max
      value: 23.3743
    - type: nauc_recall_at_20_std
      value: 3.8541
    - type: nauc_recall_at_20_diff1
      value: 13.4776
    - type: nauc_recall_at_100_max
      value: 27.6324
    - type: nauc_recall_at_100_std
      value: 21.3837
    - type: nauc_recall_at_100_diff1
      value: 7.174600000000001
    - type: nauc_recall_at_1000_max
      value: 45.033699999999996
    - type: nauc_recall_at_1000_std
      value: 59.160999999999994
    - type: nauc_recall_at_1000_diff1
      value: -0.5903
    - type: nauc_precision_at_1_max
      value: 34.3579
    - type: nauc_precision_at_1_std
      value: 4.9725
    - type: nauc_precision_at_1_diff1
      value: 34.5973
    - type: nauc_precision_at_3_max
      value: 33.6059
    - type: nauc_precision_at_3_std
      value: 8.9589
    - type: nauc_precision_at_3_diff1
      value: 16.9583
    - type: nauc_precision_at_5_max
      value: 30.8753
    - type: nauc_precision_at_5_std
      value: 10.080300000000001
    - type: nauc_precision_at_5_diff1
      value: 13.0574
    - type: nauc_precision_at_10_max
      value: 25.7853
    - type: nauc_precision_at_10_std
      value: 14.349700000000002
    - type: nauc_precision_at_10_diff1
      value: 4.2389
    - type: nauc_precision_at_20_max
      value: 23.3853
    - type: nauc_precision_at_20_std
      value: 18.4597
    - type: nauc_precision_at_20_diff1
      value: 0.9729
    - type: nauc_precision_at_100_max
      value: 17.3016
    - type: nauc_precision_at_100_std
      value: 23.352500000000003
    - type: nauc_precision_at_100_diff1
      value: -4.4505
    - type: nauc_precision_at_1000_max
      value: 10.7759
    - type: nauc_precision_at_1000_std
      value: 19.098699999999997
    - type: nauc_precision_at_1000_diff1
      value: -5.919
    - type: nauc_mrr_at_1_max
      value: 34.3579
    - type: nauc_mrr_at_1_std
      value: 4.9725
    - type: nauc_mrr_at_1_diff1
      value: 34.5973
    - type: nauc_mrr_at_3_max
      value: 34.8266
    - type: nauc_mrr_at_3_std
      value: 5.6232999999999995
    - type: nauc_mrr_at_3_diff1
      value: 29.5624
    - type: nauc_mrr_at_5_max
      value: 34.8732
    - type: nauc_mrr_at_5_std
      value: 5.447699999999999
    - type: nauc_mrr_at_5_diff1
      value: 29.9161
    - type: nauc_mrr_at_10_max
      value: 35.0493
    - type: nauc_mrr_at_10_std
      value: 6.1511000000000005
    - type: nauc_mrr_at_10_diff1
      value: 30.117699999999996
    - type: nauc_mrr_at_20_max
      value: 35.0425
    - type: nauc_mrr_at_20_std
      value: 6.25
    - type: nauc_mrr_at_20_diff1
      value: 29.8804
    - type: nauc_mrr_at_100_max
      value: 35.058499999999995
    - type: nauc_mrr_at_100_std
      value: 6.1998999999999995
    - type: nauc_mrr_at_100_diff1
      value: 29.9613
    - type: nauc_mrr_at_1000_max
      value: 35.0463
    - type: nauc_mrr_at_1000_std
      value: 6.1806
    - type: nauc_mrr_at_1000_diff1
      value: 29.973499999999998
    - type: main_score
      value: 46.682
    task:
      type: Retrieval
  - dataset:
      config: es
      name: MTEB MIRACLRetrieval (es)
      revision: main
      split: dev
      type: miracl/mmteb-miracl
    metrics:
    - type: ndcg_at_1
      value: 54.474999999999994
    - type: ndcg_at_3
      value: 45.78
    - type: ndcg_at_5
      value: 44.321
    - type: ndcg_at_10
      value: 46.593
    - type: ndcg_at_20
      value: 51.858000000000004
    - type: ndcg_at_100
      value: 58.079
    - type: ndcg_at_1000
      value: 60.656
    - type: map_at_1
      value: 15.966
    - type: map_at_3
      value: 25.933
    - type: map_at_5
      value: 30.171999999999997
    - type: map_at_10
      value: 34.67
    - type: map_at_20
      value: 37.501
    - type: map_at_100
      value: 39.45
    - type: map_at_1000
      value: 39.689
    - type: recall_at_1
      value: 15.966
    - type: recall_at_3
      value: 29.49
    - type: recall_at_5
      value: 37.983
    - type: recall_at_10
      value: 49.342999999999996
    - type: recall_at_20
      value: 62.367
    - type: recall_at_100
      value: 82.684
    - type: recall_at_1000
      value: 95.299
    - type: precision_at_1
      value: 54.474999999999994
    - type: precision_at_3
      value: 37.86
    - type: precision_at_5
      value: 30.586000000000002
    - type: precision_at_10
      value: 21.481
    - type: precision_at_20
      value: 13.796
    - type: precision_at_100
      value: 3.7900000000000005
    - type: precision_at_1000
      value: 0.441
    - type: mrr_at_1
      value: 54.475300000000004
    - type: mrr_at_3
      value: 62.191399999999994
    - type: mrr_at_5
      value: 63.74999999999999
    - type: mrr_at_10
      value: 64.4789
    - type: mrr_at_20
      value: 64.8911
    - type: mrr_at_100
      value: 65.0641
    - type: mrr_at_1000
      value: 65.07469999999999
    - type: nauc_ndcg_at_1_max
      value: 42.4187
    - type: nauc_ndcg_at_1_std
      value: 17.6337
    - type: nauc_ndcg_at_1_diff1
      value: 36.2923
    - type: nauc_ndcg_at_3_max
      value: 37.073499999999996
    - type: nauc_ndcg_at_3_std
      value: 16.0772
    - type: nauc_ndcg_at_3_diff1
      value: 26.4292
    - type: nauc_ndcg_at_5_max
      value: 36.1381
    - type: nauc_ndcg_at_5_std
      value: 14.585999999999999
    - type: nauc_ndcg_at_5_diff1
      value: 26.411299999999997
    - type: nauc_ndcg_at_10_max
      value: 35.5405
    - type: nauc_ndcg_at_10_std
      value: 15.0147
    - type: nauc_ndcg_at_10_diff1
      value: 26.299899999999997
    - type: nauc_ndcg_at_20_max
      value: 39.764500000000005
    - type: nauc_ndcg_at_20_std
      value: 20.311899999999998
    - type: nauc_ndcg_at_20_diff1
      value: 26.3937
    - type: nauc_ndcg_at_100_max
      value: 44.473
    - type: nauc_ndcg_at_100_std
      value: 26.6476
    - type: nauc_ndcg_at_100_diff1
      value: 26.1508
    - type: nauc_ndcg_at_1000_max
      value: 44.1126
    - type: nauc_ndcg_at_1000_std
      value: 25.8031
    - type: nauc_ndcg_at_1000_diff1
      value: 26.2323
    - type: nauc_map_at_1_max
      value: 10.2435
    - type: nauc_map_at_1_std
      value: -11.501999999999999
    - type: nauc_map_at_1_diff1
      value: 26.050800000000002
    - type: nauc_map_at_3_max
      value: 18.8877
    - type: nauc_map_at_3_std
      value: -3.9174
    - type: nauc_map_at_3_diff1
      value: 25.8438
    - type: nauc_map_at_5_max
      value: 23.7785
    - type: nauc_map_at_5_std
      value: 0.6597000000000001
    - type: nauc_map_at_5_diff1
      value: 25.2118
    - type: nauc_map_at_10_max
      value: 28.6819
    - type: nauc_map_at_10_std
      value: 6.741
    - type: nauc_map_at_10_diff1
      value: 24.6999
    - type: nauc_map_at_20_max
      value: 31.853900000000003
    - type: nauc_map_at_20_std
      value: 10.5967
    - type: nauc_map_at_20_diff1
      value: 24.8637
    - type: nauc_map_at_100_max
      value: 33.9181
    - type: nauc_map_at_100_std
      value: 13.254
    - type: nauc_map_at_100_diff1
      value: 24.759500000000003
    - type: nauc_map_at_1000_max
      value: 33.9679
    - type: nauc_map_at_1000_std
      value: 13.290199999999999
    - type: nauc_map_at_1000_diff1
      value: 24.758399999999998
    - type: nauc_recall_at_1_max
      value: 10.2435
    - type: nauc_recall_at_1_std
      value: -11.501999999999999
    - type: nauc_recall_at_1_diff1
      value: 26.050800000000002
    - type: nauc_recall_at_3_max
      value: 16.737099999999998
    - type: nauc_recall_at_3_std
      value: -4.3613
    - type: nauc_recall_at_3_diff1
      value: 23.771900000000002
    - type: nauc_recall_at_5_max
      value: 20.0168
    - type: nauc_recall_at_5_std
      value: 1.1395
    - type: nauc_recall_at_5_diff1
      value: 21.4641
    - type: nauc_recall_at_10_max
      value: 26.6231
    - type: nauc_recall_at_10_std
      value: 12.728700000000002
    - type: nauc_recall_at_10_diff1
      value: 18.947400000000002
    - type: nauc_recall_at_20_max
      value: 31.4926
    - type: nauc_recall_at_20_std
      value: 21.0613
    - type: nauc_recall_at_20_diff1
      value: 17.8382
    - type: nauc_recall_at_100_max
      value: 46.1255
    - type: nauc_recall_at_100_std
      value: 45.2197
    - type: nauc_recall_at_100_diff1
      value: 15.1202
    - type: nauc_recall_at_1000_max
      value: 54.710499999999996
    - type: nauc_recall_at_1000_std
      value: 68.72019999999999
    - type: nauc_recall_at_1000_diff1
      value: 9.2808
    - type: nauc_precision_at_1_max
      value: 42.4187
    - type: nauc_precision_at_1_std
      value: 17.6337
    - type: nauc_precision_at_1_diff1
      value: 36.2923
    - type: nauc_precision_at_3_max
      value: 42.056900000000006
    - type: nauc_precision_at_3_std
      value: 26.4648
    - type: nauc_precision_at_3_diff1
      value: 20.366500000000002
    - type: nauc_precision_at_5_max
      value: 45.4175
    - type: nauc_precision_at_5_std
      value: 32.2676
    - type: nauc_precision_at_5_diff1
      value: 14.9145
    - type: nauc_precision_at_10_max
      value: 43.9305
    - type: nauc_precision_at_10_std
      value: 37.9795
    - type: nauc_precision_at_10_diff1
      value: 8.4088
    - type: nauc_precision_at_20_max
      value: 44.183499999999995
    - type: nauc_precision_at_20_std
      value: 42.9261
    - type: nauc_precision_at_20_diff1
      value: 5.0112
    - type: nauc_precision_at_100_max
      value: 40.8771
    - type: nauc_precision_at_100_std
      value: 46.921800000000005
    - type: nauc_precision_at_100_diff1
      value: -1.6650000000000003
    - type: nauc_precision_at_1000_max
      value: 32.0705
    - type: nauc_precision_at_1000_std
      value: 39.5086
    - type: nauc_precision_at_1000_diff1
      value: -5.5237
    - type: nauc_mrr_at_1_max
      value: 42.4187
    - type: nauc_mrr_at_1_std
      value: 17.6337
    - type: nauc_mrr_at_1_diff1
      value: 36.2923
    - type: nauc_mrr_at_3_max
      value: 47.2755
    - type: nauc_mrr_at_3_std
      value: 23.8294
    - type: nauc_mrr_at_3_diff1
      value: 35.5243
    - type: nauc_mrr_at_5_max
      value: 47.6991
    - type: nauc_mrr_at_5_std
      value: 24.6507
    - type: nauc_mrr_at_5_diff1
      value: 35.5186
    - type: nauc_mrr_at_10_max
      value: 47.726
    - type: nauc_mrr_at_10_std
      value: 24.9941
    - type: nauc_mrr_at_10_diff1
      value: 35.5396
    - type: nauc_mrr_at_20_max
      value: 47.6055
    - type: nauc_mrr_at_20_std
      value: 24.9619
    - type: nauc_mrr_at_20_diff1
      value: 35.3844
    - type: nauc_mrr_at_100_max
      value: 47.5619
    - type: nauc_mrr_at_100_std
      value: 24.794
    - type: nauc_mrr_at_100_diff1
      value: 35.4683
    - type: nauc_mrr_at_1000_max
      value: 47.545700000000004
    - type: nauc_mrr_at_1000_std
      value: 24.7716
    - type: nauc_mrr_at_1000_diff1
      value: 35.4674
    - type: main_score
      value: 46.593
    task:
      type: Retrieval
  - dataset:
      config: fa
      name: MTEB MIRACLRetrieval (fa)
      revision: main
      split: dev
      type: miracl/mmteb-miracl
    metrics:
    - type: ndcg_at_1
      value: 36.709
    - type: ndcg_at_3
      value: 40.235
    - type: ndcg_at_5
      value: 42.866
    - type: ndcg_at_10
      value: 46.961000000000006
    - type: ndcg_at_20
      value: 49.891999999999996
    - type: ndcg_at_100
      value: 53.262
    - type: ndcg_at_1000
      value: 55.023999999999994
    - type: map_at_1
      value: 22.735
    - type: map_at_3
      value: 33.446
    - type: map_at_5
      value: 36.199999999999996
    - type: map_at_10
      value: 38.707
    - type: map_at_20
      value: 39.931
    - type: map_at_100
      value: 40.601
    - type: map_at_1000
      value: 40.711999999999996
    - type: recall_at_1
      value: 22.735
    - type: recall_at_3
      value: 41.781
    - type: recall_at_5
      value: 49.374
    - type: recall_at_10
      value: 59.949
    - type: recall_at_20
      value: 68.947
    - type: recall_at_100
      value: 83.867
    - type: recall_at_1000
      value: 95.00699999999999
    - type: precision_at_1
      value: 36.709
    - type: precision_at_3
      value: 24.578
    - type: precision_at_5
      value: 18.133
    - type: precision_at_10
      value: 11.661000000000001
    - type: precision_at_20
      value: 6.97
    - type: precision_at_100
      value: 1.737
    - type: precision_at_1000
      value: 0.199
    - type: mrr_at_1
      value: 36.7089
    - type: mrr_at_3
      value: 46.0443
    - type: mrr_at_5
      value: 47.7848
    - type: mrr_at_10
      value: 48.908699999999996
    - type: mrr_at_20
      value: 49.337399999999995
    - type: mrr_at_100
      value: 49.580999999999996
    - type: mrr_at_1000
      value: 49.6135
    - type: nauc_ndcg_at_1_max
      value: 40.3709
    - type: nauc_ndcg_at_1_std
      value: 8.100200000000001
    - type: nauc_ndcg_at_1_diff1
      value: 30.2274
    - type: nauc_ndcg_at_3_max
      value: 36.0603
    - type: nauc_ndcg_at_3_std
      value: 5.0052
    - type: nauc_ndcg_at_3_diff1
      value: 28.380899999999997
    - type: nauc_ndcg_at_5_max
      value: 36.235
    - type: nauc_ndcg_at_5_std
      value: 4.7146
    - type: nauc_ndcg_at_5_diff1
      value: 27.969
    - type: nauc_ndcg_at_10_max
      value: 38.9403
    - type: nauc_ndcg_at_10_std
      value: 8.66
    - type: nauc_ndcg_at_10_diff1
      value: 26.2876
    - type: nauc_ndcg_at_20_max
      value: 41.3286
    - type: nauc_ndcg_at_20_std
      value: 10.9269
    - type: nauc_ndcg_at_20_diff1
      value: 25.859900000000003
    - type: nauc_ndcg_at_100_max
      value: 42.8643
    - type: nauc_ndcg_at_100_std
      value: 14.2822
    - type: nauc_ndcg_at_100_diff1
      value: 25.3784
    - type: nauc_ndcg_at_1000_max
      value: 41.8778
    - type: nauc_ndcg_at_1000_std
      value: 13.130600000000001
    - type: nauc_ndcg_at_1000_diff1
      value: 25.9498
    - type: nauc_map_at_1_max
      value: 27.2644
    - type: nauc_map_at_1_std
      value: -2.6623
    - type: nauc_map_at_1_diff1
      value: 40.2119
    - type: nauc_map_at_3_max
      value: 32.121100000000006
    - type: nauc_map_at_3_std
      value: 0.6962999999999999
    - type: nauc_map_at_3_diff1
      value: 33.265499999999996
    - type: nauc_map_at_5_max
      value: 33.1237
    - type: nauc_map_at_5_std
      value: 1.6095000000000002
    - type: nauc_map_at_5_diff1
      value: 30.924400000000002
    - type: nauc_map_at_10_max
      value: 35.8464
    - type: nauc_map_at_10_std
      value: 4.6409
    - type: nauc_map_at_10_diff1
      value: 29.3654
    - type: nauc_map_at_20_max
      value: 36.967299999999994
    - type: nauc_map_at_20_std
      value: 5.8244
    - type: nauc_map_at_20_diff1
      value: 29.0251
    - type: nauc_map_at_100_max
      value: 37.3859
    - type: nauc_map_at_100_std
      value: 6.575499999999999
    - type: nauc_map_at_100_diff1
      value: 28.9224
    - type: nauc_map_at_1000_max
      value: 37.3438
    - type: nauc_map_at_1000_std
      value: 6.5534
    - type: nauc_map_at_1000_diff1
      value: 28.952099999999998
    - type: nauc_recall_at_1_max
      value: 27.2644
    - type: nauc_recall_at_1_std
      value: -2.6623
    - type: nauc_recall_at_1_diff1
      value: 40.2119
    - type: nauc_recall_at_3_max
      value: 29.0364
    - type: nauc_recall_at_3_std
      value: 0.8965000000000001
    - type: nauc_recall_at_3_diff1
      value: 27.651999999999997
    - type: nauc_recall_at_5_max
      value: 29.299799999999998
    - type: nauc_recall_at_5_std
      value: 1.0264
    - type: nauc_recall_at_5_diff1
      value: 23.3762
    - type: nauc_recall_at_10_max
      value: 34.4238
    - type: nauc_recall_at_10_std
      value: 10.228299999999999
    - type: nauc_recall_at_10_diff1
      value: 17.9909
    - type: nauc_recall_at_20_max
      value: 42.5987
    - type: nauc_recall_at_20_std
      value: 16.880899999999997
    - type: nauc_recall_at_20_diff1
      value: 16.4298
    - type: nauc_recall_at_100_max
      value: 55.767599999999995
    - type: nauc_recall_at_100_std
      value: 44.9392
    - type: nauc_recall_at_100_diff1
      value: 8.6006
    - type: nauc_recall_at_1000_max
      value: 60.8797
    - type: nauc_recall_at_1000_std
      value: 64.1015
    - type: nauc_recall_at_1000_diff1
      value: 5.9098
    - type: nauc_precision_at_1_max
      value: 40.3709
    - type: nauc_precision_at_1_std
      value: 8.100200000000001
    - type: nauc_precision_at_1_diff1
      value: 30.2274
    - type: nauc_precision_at_3_max
      value: 39.9513
    - type: nauc_precision_at_3_std
      value: 15.568999999999999
    - type: nauc_precision_at_3_diff1
      value: 9.9843
    - type: nauc_precision_at_5_max
      value: 38.1062
    - type: nauc_precision_at_5_std
      value: 18.7953
    - type: nauc_precision_at_5_diff1
      value: 1.4489
    - type: nauc_precision_at_10_max
      value: 37.601099999999995
    - type: nauc_precision_at_10_std
      value: 26.145699999999998
    - type: nauc_precision_at_10_diff1
      value: -6.6542
    - type: nauc_precision_at_20_max
      value: 35.5961
    - type: nauc_precision_at_20_std
      value: 29.930200000000003
    - type: nauc_precision_at_20_diff1
      value: -9.7241
    - type: nauc_precision_at_100_max
      value: 28.092299999999998
    - type: nauc_precision_at_100_std
      value: 34.0409
    - type: nauc_precision_at_100_diff1
      value: -15.037400000000002
    - type: nauc_precision_at_1000_max
      value: 17.1738
    - type: nauc_precision_at_1000_std
      value: 26.948499999999996
    - type: nauc_precision_at_1000_diff1
      value: -17.5066
    - type: nauc_mrr_at_1_max
      value: 40.3709
    - type: nauc_mrr_at_1_std
      value: 8.100200000000001
    - type: nauc_mrr_at_1_diff1
      value: 30.2274
    - type: nauc_mrr_at_3_max
      value: 41.971399999999996
    - type: nauc_mrr_at_3_std
      value: 10.34
    - type: nauc_mrr_at_3_diff1
      value: 27.5952
    - type: nauc_mrr_at_5_max
      value: 42.721599999999995
    - type: nauc_mrr_at_5_std
      value: 10.796100000000001
    - type: nauc_mrr_at_5_diff1
      value: 27.260800000000003
    - type: nauc_mrr_at_10_max
      value: 42.651
    - type: nauc_mrr_at_10_std
      value: 11.397599999999999
    - type: nauc_mrr_at_10_diff1
      value: 26.5974
    - type: nauc_mrr_at_20_max
      value: 42.7886
    - type: nauc_mrr_at_20_std
      value: 11.4316
    - type: nauc_mrr_at_20_diff1
      value: 26.724500000000003
    - type: nauc_mrr_at_100_max
      value: 42.8826
    - type: nauc_mrr_at_100_std
      value: 11.549
    - type: nauc_mrr_at_100_diff1
      value: 26.762999999999998
    - type: nauc_mrr_at_1000_max
      value: 42.8647
    - type: nauc_mrr_at_1000_std
      value: 11.522300000000001
    - type: nauc_mrr_at_1000_diff1
      value: 26.790799999999997
    - type: main_score
      value: 46.961000000000006
    task:
      type: Retrieval
  - dataset:
      config: fi
      name: MTEB MIRACLRetrieval (fi)
      revision: main
      split: dev
      type: miracl/mmteb-miracl
    metrics:
    - type: ndcg_at_1
      value: 59.245000000000005
    - type: ndcg_at_3
      value: 58.876
    - type: ndcg_at_5
      value: 61.778999999999996
    - type: ndcg_at_10
      value: 65.551
    - type: ndcg_at_20
      value: 67.552
    - type: ndcg_at_100
      value: 69.67
    - type: ndcg_at_1000
      value: 70.521
    - type: map_at_1
      value: 37.669000000000004
    - type: map_at_3
      value: 52.28
    - type: map_at_5
      value: 55.064
    - type: map_at_10
      value: 57.29
    - type: map_at_20
      value: 58.162000000000006
    - type: map_at_100
      value: 58.648999999999994
    - type: map_at_1000
      value: 58.701
    - type: recall_at_1
      value: 37.669000000000004
    - type: recall_at_3
      value: 60.234
    - type: recall_at_5
      value: 67.135
    - type: recall_at_10
      value: 76.529
    - type: recall_at_20
      value: 82.685
    - type: recall_at_100
      value: 91.56
    - type: recall_at_1000
      value: 96.977
    - type: precision_at_1
      value: 59.245000000000005
    - type: precision_at_3
      value: 34.435
    - type: precision_at_5
      value: 23.745
    - type: precision_at_10
      value: 13.980999999999998
    - type: precision_at_20
      value: 7.707
    - type: precision_at_100
      value: 1.7489999999999999
    - type: precision_at_1000
      value: 0.186
    - type: mrr_at_1
      value: 59.244699999999995
    - type: mrr_at_3
      value: 67.9517
    - type: mrr_at_5
      value: 68.9746
    - type: mrr_at_10
      value: 69.7599
    - type: mrr_at_20
      value: 69.9947
    - type: mrr_at_100
      value: 70.1058
    - type: mrr_at_1000
      value: 70.11749999999999
    - type: nauc_ndcg_at_1_max
      value: 38.7543
    - type: nauc_ndcg_at_1_std
      value: 4.2023
    - type: nauc_ndcg_at_1_diff1
      value: 50.8162
    - type: nauc_ndcg_at_3_max
      value: 36.9886
    - type: nauc_ndcg_at_3_std
      value: 2.7807
    - type: nauc_ndcg_at_3_diff1
      value: 39.9604
    - type: nauc_ndcg_at_5_max
      value: 38.567800000000005
    - type: nauc_ndcg_at_5_std
      value: 4.0823
    - type: nauc_ndcg_at_5_diff1
      value: 40.1034
    - type: nauc_ndcg_at_10_max
      value: 39.6717
    - type: nauc_ndcg_at_10_std
      value: 4.836
    - type: nauc_ndcg_at_10_diff1
      value: 39.546
    - type: nauc_ndcg_at_20_max
      value: 40.860400000000006
    - type: nauc_ndcg_at_20_std
      value: 7.385999999999999
    - type: nauc_ndcg_at_20_diff1
      value: 39.1921
    - type: nauc_ndcg_at_100_max
      value: 41.021
    - type: nauc_ndcg_at_100_std
      value: 9.0238
    - type: nauc_ndcg_at_100_diff1
      value: 39.6248
    - type: nauc_ndcg_at_1000_max
      value: 40.4034
    - type: nauc_ndcg_at_1000_std
      value: 8.204500000000001
    - type: nauc_ndcg_at_1000_diff1
      value: 40.0309
    - type: nauc_map_at_1_max
      value: 26.493499999999997
    - type: nauc_map_at_1_std
      value: -2.5927
    - type: nauc_map_at_1_diff1
      value: 46.5824
    - type: nauc_map_at_3_max
      value: 34.2786
    - type: nauc_map_at_3_std
      value: 0.5491
    - type: nauc_map_at_3_diff1
      value: 39.4368
    - type: nauc_map_at_5_max
      value: 36.2078
    - type: nauc_map_at_5_std
      value: 2.3709000000000002
    - type: nauc_map_at_5_diff1
      value: 39.3797
    - type: nauc_map_at_10_max
      value: 36.9681
    - type: nauc_map_at_10_std
      value: 2.8434999999999997
    - type: nauc_map_at_10_diff1
      value: 39.1311
    - type: nauc_map_at_20_max
      value: 37.4538
    - type: nauc_map_at_20_std
      value: 3.8388
    - type: nauc_map_at_20_diff1
      value: 38.9234
    - type: nauc_map_at_100_max
      value: 37.5899
    - type: nauc_map_at_100_std
      value: 4.2547
    - type: nauc_map_at_100_diff1
      value: 39.0103
    - type: nauc_map_at_1000_max
      value: 37.5573
    - type: nauc_map_at_1000_std
      value: 4.221699999999999
    - type: nauc_map_at_1000_diff1
      value: 39.0312
    - type: nauc_recall_at_1_max
      value: 26.493499999999997
    - type: nauc_recall_at_1_std
      value: -2.5927
    - type: nauc_recall_at_1_diff1
      value: 46.5824
    - type: nauc_recall_at_3_max
      value: 33.2212
    - type: nauc_recall_at_3_std
      value: 0.5208
    - type: nauc_recall_at_3_diff1
      value: 33.0793
    - type: nauc_recall_at_5_max
      value: 36.4292
    - type: nauc_recall_at_5_std
      value: 4.139
    - type: nauc_recall_at_5_diff1
      value: 32.357200000000006
    - type: nauc_recall_at_10_max
      value: 39.473
    - type: nauc_recall_at_10_std
      value: 5.6589
    - type: nauc_recall_at_10_diff1
      value: 28.176299999999998
    - type: nauc_recall_at_20_max
      value: 45.8088
    - type: nauc_recall_at_20_std
      value: 17.084
    - type: nauc_recall_at_20_diff1
      value: 25.1991
    - type: nauc_recall_at_100_max
      value: 53.8483
    - type: nauc_recall_at_100_std
      value: 41.8548
    - type: nauc_recall_at_100_diff1
      value: 20.316699999999997
    - type: nauc_recall_at_1000_max
      value: 57.7136
    - type: nauc_recall_at_1000_std
      value: 61.00600000000001
    - type: nauc_recall_at_1000_diff1
      value: 14.565900000000001
    - type: nauc_precision_at_1_max
      value: 38.7543
    - type: nauc_precision_at_1_std
      value: 4.2023
    - type: nauc_precision_at_1_diff1
      value: 50.8162
    - type: nauc_precision_at_3_max
      value: 30.9959
    - type: nauc_precision_at_3_std
      value: 11.363
    - type: nauc_precision_at_3_diff1
      value: 12.556899999999999
    - type: nauc_precision_at_5_max
      value: 27.8411
    - type: nauc_precision_at_5_std
      value: 15.3994
    - type: nauc_precision_at_5_diff1
      value: 5.9959
    - type: nauc_precision_at_10_max
      value: 21.067700000000002
    - type: nauc_precision_at_10_std
      value: 16.4476
    - type: nauc_precision_at_10_diff1
      value: -2.7433
    - type: nauc_precision_at_20_max
      value: 17.8813
    - type: nauc_precision_at_20_std
      value: 21.4052
    - type: nauc_precision_at_20_diff1
      value: -8.7583
    - type: nauc_precision_at_100_max
      value: 8.864700000000001
    - type: nauc_precision_at_100_std
      value: 24.1294
    - type: nauc_precision_at_100_diff1
      value: -14.3597
    - type: nauc_precision_at_1000_max
      value: 1.8260999999999998
    - type: nauc_precision_at_1000_std
      value: 20.0461
    - type: nauc_precision_at_1000_diff1
      value: -17.6062
    - type: nauc_mrr_at_1_max
      value: 38.7543
    - type: nauc_mrr_at_1_std
      value: 4.2023
    - type: nauc_mrr_at_1_diff1
      value: 50.8162
    - type: nauc_mrr_at_3_max
      value: 40.8761
    - type: nauc_mrr_at_3_std
      value: 5.5156
    - type: nauc_mrr_at_3_diff1
      value: 47.6824
    - type: nauc_mrr_at_5_max
      value: 41.1811
    - type: nauc_mrr_at_5_std
      value: 6.0588999999999995
    - type: nauc_mrr_at_5_diff1
      value: 47.9242
    - type: nauc_mrr_at_10_max
      value: 41.2511
    - type: nauc_mrr_at_10_std
      value: 6.1515
    - type: nauc_mrr_at_10_diff1
      value: 47.7245
    - type: nauc_mrr_at_20_max
      value: 41.343
    - type: nauc_mrr_at_20_std
      value: 6.4499
    - type: nauc_mrr_at_20_diff1
      value: 47.8506
    - type: nauc_mrr_at_100_max
      value: 41.3067
    - type: nauc_mrr_at_100_std
      value: 6.4111
    - type: nauc_mrr_at_100_diff1
      value: 47.876000000000005
    - type: nauc_mrr_at_1000_max
      value: 41.2977
    - type: nauc_mrr_at_1000_std
      value: 6.397899999999999
    - type: nauc_mrr_at_1000_diff1
      value: 47.8808
    - type: main_score
      value: 65.551
    task:
      type: Retrieval
  - dataset:
      config: fr
      name: MTEB MIRACLRetrieval (fr)
      revision: main
      split: dev
      type: miracl/mmteb-miracl
    metrics:
    - type: ndcg_at_1
      value: 38.775999999999996
    - type: ndcg_at_3
      value: 38.924
    - type: ndcg_at_5
      value: 42.571999999999996
    - type: ndcg_at_10
      value: 47.589
    - type: ndcg_at_20
      value: 51.202999999999996
    - type: ndcg_at_100
      value: 54.641
    - type: ndcg_at_1000
      value: 56.28999999999999
    - type: map_at_1
      value: 22.081999999999997
    - type: map_at_3
      value: 32.286
    - type: map_at_5
      value: 35.354
    - type: map_at_10
      value: 38.071
    - type: map_at_20
      value: 39.534000000000006
    - type: map_at_100
      value: 40.308
    - type: map_at_1000
      value: 40.412
    - type: recall_at_1
      value: 22.081999999999997
    - type: recall_at_3
      value: 39.527
    - type: recall_at_5
      value: 48.983
    - type: recall_at_10
      value: 61.619
    - type: recall_at_20
      value: 72.68900000000001
    - type: recall_at_100
      value: 87.237
    - type: recall_at_1000
      value: 97.449
    - type: precision_at_1
      value: 38.775999999999996
    - type: precision_at_3
      value: 24.976000000000003
    - type: precision_at_5
      value: 18.659
    - type: precision_at_10
      value: 12.157
    - type: precision_at_20
      value: 7.405
    - type: precision_at_100
      value: 1.831
    - type: precision_at_1000
      value: 0.20600000000000002
    - type: mrr_at_1
      value: 38.7755
    - type: mrr_at_3
      value: 47.4733
    - type: mrr_at_5
      value: 49.5578
    - type: mrr_at_10
      value: 51.119400000000006
    - type: mrr_at_20
      value: 51.6826
    - type: mrr_at_100
      value: 51.8472
    - type: mrr_at_1000
      value: 51.87969999999999
    - type: nauc_ndcg_at_1_max
      value: 37.6869
    - type: nauc_ndcg_at_1_std
      value: 19.3059
    - type: nauc_ndcg_at_1_diff1
      value: 24.1548
    - type: nauc_ndcg_at_3_max
      value: 33.0185
    - type: nauc_ndcg_at_3_std
      value: 19.4304
    - type: nauc_ndcg_at_3_diff1
      value: 18.152099999999997
    - type: nauc_ndcg_at_5_max
      value: 35.7529
    - type: nauc_ndcg_at_5_std
      value: 20.8762
    - type: nauc_ndcg_at_5_diff1
      value: 20.9497
    - type: nauc_ndcg_at_10_max
      value: 35.9846
    - type: nauc_ndcg_at_10_std
      value: 21.7196
    - type: nauc_ndcg_at_10_diff1
      value: 19.3302
    - type: nauc_ndcg_at_20_max
      value: 38.313199999999995
    - type: nauc_ndcg_at_20_std
      value: 23.2567
    - type: nauc_ndcg_at_20_diff1
      value: 20.1896
    - type: nauc_ndcg_at_100_max
      value: 38.2753
    - type: nauc_ndcg_at_100_std
      value: 25.048399999999997
    - type: nauc_ndcg_at_100_diff1
      value: 19.5028
    - type: nauc_ndcg_at_1000_max
      value: 37.8159
    - type: nauc_ndcg_at_1000_std
      value: 23.8262
    - type: nauc_ndcg_at_1000_diff1
      value: 19.4799
    - type: nauc_map_at_1_max
      value: 25.040200000000002
    - type: nauc_map_at_1_std
      value: 11.5183
    - type: nauc_map_at_1_diff1
      value: 23.7651
    - type: nauc_map_at_3_max
      value: 30.5355
    - type: nauc_map_at_3_std
      value: 17.7343
    - type: nauc_map_at_3_diff1
      value: 19.0017
    - type: nauc_map_at_5_max
      value: 33.492
    - type: nauc_map_at_5_std
      value: 19.7752
    - type: nauc_map_at_5_diff1
      value: 20.4072
    - type: nauc_map_at_10_max
      value: 33.3246
    - type: nauc_map_at_10_std
      value: 19.8087
    - type: nauc_map_at_10_diff1
      value: 19.184
    - type: nauc_map_at_20_max
      value: 34.3329
    - type: nauc_map_at_20_std
      value: 20.6622
    - type: nauc_map_at_20_diff1
      value: 19.625
    - type: nauc_map_at_100_max
      value: 34.407700000000006
    - type: nauc_map_at_100_std
      value: 21.0478
    - type: nauc_map_at_100_diff1
      value: 19.4432
    - type: nauc_map_at_1000_max
      value: 34.4128
    - type: nauc_map_at_1000_std
      value: 21.0078
    - type: nauc_map_at_1000_diff1
      value: 19.4386
    - type: nauc_recall_at_1_max
      value: 25.040200000000002
    - type: nauc_recall_at_1_std
      value: 11.5183
    - type: nauc_recall_at_1_diff1
      value: 23.7651
    - type: nauc_recall_at_3_max
      value: 28.0362
    - type: nauc_recall_at_3_std
      value: 18.1405
    - type: nauc_recall_at_3_diff1
      value: 14.0979
    - type: nauc_recall_at_5_max
      value: 32.6536
    - type: nauc_recall_at_5_std
      value: 19.763
    - type: nauc_recall_at_5_diff1
      value: 18.5941
    - type: nauc_recall_at_10_max
      value: 32.736399999999996
    - type: nauc_recall_at_10_std
      value: 20.5625
    - type: nauc_recall_at_10_diff1
      value: 15.4366
    - type: nauc_recall_at_20_max
      value: 41.0178
    - type: nauc_recall_at_20_std
      value: 25.4559
    - type: nauc_recall_at_20_diff1
      value: 17.8615
    - type: nauc_recall_at_100_max
      value: 47.700700000000005
    - type: nauc_recall_at_100_std
      value: 47.386
    - type: nauc_recall_at_100_diff1
      value: 15.1722
    - type: nauc_recall_at_1000_max
      value: 75.13119999999999
    - type: nauc_recall_at_1000_std
      value: 70.6818
    - type: nauc_recall_at_1000_diff1
      value: 17.7539
    - type: nauc_precision_at_1_max
      value: 37.6869
    - type: nauc_precision_at_1_std
      value: 19.3059
    - type: nauc_precision_at_1_diff1
      value: 24.1548
    - type: nauc_precision_at_3_max
      value: 37.0296
    - type: nauc_precision_at_3_std
      value: 24.5362
    - type: nauc_precision_at_3_diff1
      value: 10.0428
    - type: nauc_precision_at_5_max
      value: 38.770700000000005
    - type: nauc_precision_at_5_std
      value: 27.290399999999998
    - type: nauc_precision_at_5_diff1
      value: 11.1247
    - type: nauc_precision_at_10_max
      value: 31.2623
    - type: nauc_precision_at_10_std
      value: 25.794099999999997
    - type: nauc_precision_at_10_diff1
      value: 2.1571
    - type: nauc_precision_at_20_max
      value: 29.2963
    - type: nauc_precision_at_20_std
      value: 25.241000000000003
    - type: nauc_precision_at_20_diff1
      value: 1.8568000000000002
    - type: nauc_precision_at_100_max
      value: 18.620800000000003
    - type: nauc_precision_at_100_std
      value: 22.6874
    - type: nauc_precision_at_100_diff1
      value: -5.2441
    - type: nauc_precision_at_1000_max
      value: 10.2324
    - type: nauc_precision_at_1000_std
      value: 13.1045
    - type: nauc_precision_at_1000_diff1
      value: -9.7662
    - type: nauc_mrr_at_1_max
      value: 37.6869
    - type: nauc_mrr_at_1_std
      value: 19.3059
    - type: nauc_mrr_at_1_diff1
      value: 24.1548
    - type: nauc_mrr_at_3_max
      value: 36.3742
    - type: nauc_mrr_at_3_std
      value: 19.2165
    - type: nauc_mrr_at_3_diff1
      value: 20.883399999999998
    - type: nauc_mrr_at_5_max
      value: 37.196400000000004
    - type: nauc_mrr_at_5_std
      value: 19.839399999999998
    - type: nauc_mrr_at_5_diff1
      value: 21.6132
    - type: nauc_mrr_at_10_max
      value: 37.7804
    - type: nauc_mrr_at_10_std
      value: 20.7829
    - type: nauc_mrr_at_10_diff1
      value: 21.9443
    - type: nauc_mrr_at_20_max
      value: 37.7391
    - type: nauc_mrr_at_20_std
      value: 20.4514
    - type: nauc_mrr_at_20_diff1
      value: 21.7569
    - type: nauc_mrr_at_100_max
      value: 37.6639
    - type: nauc_mrr_at_100_std
      value: 20.450499999999998
    - type: nauc_mrr_at_100_diff1
      value: 21.7914
    - type: nauc_mrr_at_1000_max
      value: 37.6357
    - type: nauc_mrr_at_1000_std
      value: 20.414099999999998
    - type: nauc_mrr_at_1000_diff1
      value: 21.7914
    - type: main_score
      value: 47.589
    task:
      type: Retrieval
  - dataset:
      config: hi
      name: MTEB MIRACLRetrieval (hi)
      revision: main
      split: dev
      type: miracl/mmteb-miracl
    metrics:
    - type: ndcg_at_1
      value: 33.143
    - type: ndcg_at_3
      value: 34.988
    - type: ndcg_at_5
      value: 37.938
    - type: ndcg_at_10
      value: 42.083999999999996
    - type: ndcg_at_20
      value: 45.399
    - type: ndcg_at_100
      value: 48.647
    - type: ndcg_at_1000
      value: 50.712
    - type: map_at_1
      value: 17.852
    - type: map_at_3
      value: 27.405
    - type: map_at_5
      value: 30.781999999999996
    - type: map_at_10
      value: 33.391999999999996
    - type: map_at_20
      value: 34.833
    - type: map_at_100
      value: 35.501
    - type: map_at_1000
      value: 35.611
    - type: recall_at_1
      value: 17.852
    - type: recall_at_3
      value: 33.765
    - type: recall_at_5
      value: 43.828
    - type: recall_at_10
      value: 55.217000000000006
    - type: recall_at_20
      value: 65.231
    - type: recall_at_100
      value: 79.92899999999999
    - type: recall_at_1000
      value: 93.434
    - type: precision_at_1
      value: 33.143
    - type: precision_at_3
      value: 23.429
    - type: precision_at_5
      value: 18.229
    - type: precision_at_10
      value: 11.657
    - type: precision_at_20
      value: 7.142999999999999
    - type: precision_at_100
      value: 1.7229999999999999
    - type: precision_at_1000
      value: 0.201
    - type: mrr_at_1
      value: 33.1429
    - type: mrr_at_3
      value: 41.428599999999996
    - type: mrr_at_5
      value: 43.7857
    - type: mrr_at_10
      value: 44.9745
    - type: mrr_at_20
      value: 45.4552
    - type: mrr_at_100
      value: 45.7257
    - type: mrr_at_1000
      value: 45.7671
    - type: nauc_ndcg_at_1_max
      value: 51.2111
    - type: nauc_ndcg_at_1_std
      value: 15.146799999999999
    - type: nauc_ndcg_at_1_diff1
      value: 40.127
    - type: nauc_ndcg_at_3_max
      value: 44.1081
    - type: nauc_ndcg_at_3_std
      value: 11.708599999999999
    - type: nauc_ndcg_at_3_diff1
      value: 26.8834
    - type: nauc_ndcg_at_5_max
      value: 43.077799999999996
    - type: nauc_ndcg_at_5_std
      value: 13.570599999999999
    - type: nauc_ndcg_at_5_diff1
      value: 27.5263
    - type: nauc_ndcg_at_10_max
      value: 45.1081
    - type: nauc_ndcg_at_10_std
      value: 14.758299999999998
    - type: nauc_ndcg_at_10_diff1
      value: 29.3043
    - type: nauc_ndcg_at_20_max
      value: 47.5349
    - type: nauc_ndcg_at_20_std
      value: 17.8
    - type: nauc_ndcg_at_20_diff1
      value: 28.416400000000003
    - type: nauc_ndcg_at_100_max
      value: 48.395500000000006
    - type: nauc_ndcg_at_100_std
      value: 18.9621
    - type: nauc_ndcg_at_100_diff1
      value: 28.799500000000002
    - type: nauc_ndcg_at_1000_max
      value: 48.4885
    - type: nauc_ndcg_at_1000_std
      value: 18.296100000000003
    - type: nauc_ndcg_at_1000_diff1
      value: 29.5616
    - type: nauc_map_at_1_max
      value: 31.3083
    - type: nauc_map_at_1_std
      value: 6.462700000000001
    - type: nauc_map_at_1_diff1
      value: 36.2382
    - type: nauc_map_at_3_max
      value: 35.841699999999996
    - type: nauc_map_at_3_std
      value: 7.013800000000001
    - type: nauc_map_at_3_diff1
      value: 28.991699999999998
    - type: nauc_map_at_5_max
      value: 39.0977
    - type: nauc_map_at_5_std
      value: 9.8928
    - type: nauc_map_at_5_diff1
      value: 28.6183
    - type: nauc_map_at_10_max
      value: 41.8538
    - type: nauc_map_at_10_std
      value: 11.5648
    - type: nauc_map_at_10_diff1
      value: 29.1635
    - type: nauc_map_at_20_max
      value: 43.6057
    - type: nauc_map_at_20_std
      value: 13.382900000000001
    - type: nauc_map_at_20_diff1
      value: 28.6067
    - type: nauc_map_at_100_max
      value: 43.962
    - type: nauc_map_at_100_std
      value: 13.7517
    - type: nauc_map_at_100_diff1
      value: 28.841299999999997
    - type: nauc_map_at_1000_max
      value: 43.9824
    - type: nauc_map_at_1000_std
      value: 13.732099999999999
    - type: nauc_map_at_1000_diff1
      value: 28.8971
    - type: nauc_recall_at_1_max
      value: 31.3083
    - type: nauc_recall_at_1_std
      value: 6.462700000000001
    - type: nauc_recall_at_1_diff1
      value: 36.2382
    - type: nauc_recall_at_3_max
      value: 30.605300000000003
    - type: nauc_recall_at_3_std
      value: 7.5045
    - type: nauc_recall_at_3_diff1
      value: 19.0642
    - type: nauc_recall_at_5_max
      value: 33.4179
    - type: nauc_recall_at_5_std
      value: 13.1973
    - type: nauc_recall_at_5_diff1
      value: 20.1321
    - type: nauc_recall_at_10_max
      value: 36.6194
    - type: nauc_recall_at_10_std
      value: 15.8973
    - type: nauc_recall_at_10_diff1
      value: 23.1043
    - type: nauc_recall_at_20_max
      value: 42.0702
    - type: nauc_recall_at_20_std
      value: 24.1871
    - type: nauc_recall_at_20_diff1
      value: 20.7213
    - type: nauc_recall_at_100_max
      value: 47.0142
    - type: nauc_recall_at_100_std
      value: 34.8802
    - type: nauc_recall_at_100_diff1
      value: 18.8255
    - type: nauc_recall_at_1000_max
      value: 59.413700000000006
    - type: nauc_recall_at_1000_std
      value: 50.051199999999994
    - type: nauc_recall_at_1000_diff1
      value: 30.682
    - type: nauc_precision_at_1_max
      value: 51.2111
    - type: nauc_precision_at_1_std
      value: 15.146799999999999
    - type: nauc_precision_at_1_diff1
      value: 40.127
    - type: nauc_precision_at_3_max
      value: 49.2718
    - type: nauc_precision_at_3_std
      value: 15.658
    - type: nauc_precision_at_3_diff1
      value: 17.163700000000002
    - type: nauc_precision_at_5_max
      value: 51.77349999999999
    - type: nauc_precision_at_5_std
      value: 21.1016
    - type: nauc_precision_at_5_diff1
      value: 15.0559
    - type: nauc_precision_at_10_max
      value: 51.843799999999995
    - type: nauc_precision_at_10_std
      value: 23.2912
    - type: nauc_precision_at_10_diff1
      value: 14.191799999999999
    - type: nauc_precision_at_20_max
      value: 50.41
    - type: nauc_precision_at_20_std
      value: 28.2005
    - type: nauc_precision_at_20_diff1
      value: 8.2714
    - type: nauc_precision_at_100_max
      value: 45.522600000000004
    - type: nauc_precision_at_100_std
      value: 28.199
    - type: nauc_precision_at_100_diff1
      value: 7.180400000000001
    - type: nauc_precision_at_1000_max
      value: 38.663399999999996
    - type: nauc_precision_at_1000_std
      value: 22.781399999999998
    - type: nauc_precision_at_1000_diff1
      value: 3.8605
    - type: nauc_mrr_at_1_max
      value: 51.2111
    - type: nauc_mrr_at_1_std
      value: 15.146799999999999
    - type: nauc_mrr_at_1_diff1
      value: 40.127
    - type: nauc_mrr_at_3_max
      value: 48.0836
    - type: nauc_mrr_at_3_std
      value: 13.9619
    - type: nauc_mrr_at_3_diff1
      value: 30.8736
    - type: nauc_mrr_at_5_max
      value: 49.0073
    - type: nauc_mrr_at_5_std
      value: 15.6308
    - type: nauc_mrr_at_5_diff1
      value: 31.8004
    - type: nauc_mrr_at_10_max
      value: 49.554700000000004
    - type: nauc_mrr_at_10_std
      value: 15.7261
    - type: nauc_mrr_at_10_diff1
      value: 32.8141
    - type: nauc_mrr_at_20_max
      value: 49.6722
    - type: nauc_mrr_at_20_std
      value: 15.873000000000001
    - type: nauc_mrr_at_20_diff1
      value: 32.8857
    - type: nauc_mrr_at_100_max
      value: 49.5869
    - type: nauc_mrr_at_100_std
      value: 15.8044
    - type: nauc_mrr_at_100_diff1
      value: 32.811099999999996
    - type: nauc_mrr_at_1000_max
      value: 49.5787
    - type: nauc_mrr_at_1000_std
      value: 15.7836
    - type: nauc_mrr_at_1000_diff1
      value: 32.8438
    - type: main_score
      value: 42.083999999999996
    task:
      type: Retrieval
  - dataset:
      config: id
      name: MTEB MIRACLRetrieval (id)
      revision: main
      split: dev
      type: miracl/mmteb-miracl
    metrics:
    - type: ndcg_at_1
      value: 43.854
    - type: ndcg_at_3
      value: 41.041
    - type: ndcg_at_5
      value: 42.235
    - type: ndcg_at_10
      value: 45.458999999999996
    - type: ndcg_at_20
      value: 48.795
    - type: ndcg_at_100
      value: 53.642999999999994
    - type: ndcg_at_1000
      value: 56.052
    - type: map_at_1
      value: 19.192999999999998
    - type: map_at_3
      value: 29.125
    - type: map_at_5
      value: 32.42
    - type: map_at_10
      value: 35.181000000000004
    - type: map_at_20
      value: 36.775000000000006
    - type: map_at_100
      value: 38.06
    - type: map_at_1000
      value: 38.246
    - type: recall_at_1
      value: 19.192999999999998
    - type: recall_at_3
      value: 35.431000000000004
    - type: recall_at_5
      value: 43.348
    - type: recall_at_10
      value: 52.89
    - type: recall_at_20
      value: 61.812999999999995
    - type: recall_at_100
      value: 79.649
    - type: recall_at_1000
      value: 92.937
    - type: precision_at_1
      value: 43.854
    - type: precision_at_3
      value: 29.757
    - type: precision_at_5
      value: 23.208000000000002
    - type: precision_at_10
      value: 15.177
    - type: precision_at_20
      value: 9.286
    - type: precision_at_100
      value: 2.524
    - type: precision_at_1000
      value: 0.299
    - type: mrr_at_1
      value: 43.8542
    - type: mrr_at_3
      value: 53.4549
    - type: mrr_at_5
      value: 55.2674
    - type: mrr_at_10
      value: 56.2576
    - type: mrr_at_20
      value: 56.592699999999994
    - type: mrr_at_100
      value: 56.7841
    - type: mrr_at_1000
      value: 56.8049
    - type: nauc_ndcg_at_1_max
      value: 32.205600000000004
    - type: nauc_ndcg_at_1_std
      value: 11.343499999999999
    - type: nauc_ndcg_at_1_diff1
      value: 32.8768
    - type: nauc_ndcg_at_3_max
      value: 25.8163
    - type: nauc_ndcg_at_3_std
      value: 5.037599999999999
    - type: nauc_ndcg_at_3_diff1
      value: 26.118799999999997
    - type: nauc_ndcg_at_5_max
      value: 27.159
    - type: nauc_ndcg_at_5_std
      value: 2.9204999999999997
    - type: nauc_ndcg_at_5_diff1
      value: 26.429399999999998
    - type: nauc_ndcg_at_10_max
      value: 28.6049
    - type: nauc_ndcg_at_10_std
      value: 3.7817000000000003
    - type: nauc_ndcg_at_10_diff1
      value: 25.904300000000003
    - type: nauc_ndcg_at_20_max
      value: 30.5254
    - type: nauc_ndcg_at_20_std
      value: 6.6297999999999995
    - type: nauc_ndcg_at_20_diff1
      value: 25.155300000000004
    - type: nauc_ndcg_at_100_max
      value: 32.3477
    - type: nauc_ndcg_at_100_std
      value: 11.7329
    - type: nauc_ndcg_at_100_diff1
      value: 24.038
    - type: nauc_ndcg_at_1000_max
      value: 32.1871
    - type: nauc_ndcg_at_1000_std
      value: 12.266
    - type: nauc_ndcg_at_1000_diff1
      value: 24.5005
    - type: nauc_map_at_1_max
      value: 19.5131
    - type: nauc_map_at_1_std
      value: 0.7939999999999999
    - type: nauc_map_at_1_diff1
      value: 35.4824
    - type: nauc_map_at_3_max
      value: 21.1372
    - type: nauc_map_at_3_std
      value: -1.4297
    - type: nauc_map_at_3_diff1
      value: 28.7825
    - type: nauc_map_at_5_max
      value: 23.301099999999998
    - type: nauc_map_at_5_std
      value: -1.6149
    - type: nauc_map_at_5_diff1
      value: 28.353
    - type: nauc_map_at_10_max
      value: 25.0545
    - type: nauc_map_at_10_std
      value: 0.29650000000000004
    - type: nauc_map_at_10_diff1
      value: 27.6041
    - type: nauc_map_at_20_max
      value: 26.1938
    - type: nauc_map_at_20_std
      value: 1.8739999999999999
    - type: nauc_map_at_20_diff1
      value: 26.9804
    - type: nauc_map_at_100_max
      value: 26.9981
    - type: nauc_map_at_100_std
      value: 3.4286
    - type: nauc_map_at_100_diff1
      value: 26.703599999999998
    - type: nauc_map_at_1000_max
      value: 27.005200000000002
    - type: nauc_map_at_1000_std
      value: 3.5663
    - type: nauc_map_at_1000_diff1
      value: 26.7073
    - type: nauc_recall_at_1_max
      value: 19.5131
    - type: nauc_recall_at_1_std
      value: 0.7939999999999999
    - type: nauc_recall_at_1_diff1
      value: 35.4824
    - type: nauc_recall_at_3_max
      value: 16.8845
    - type: nauc_recall_at_3_std
      value: -4.3322
    - type: nauc_recall_at_3_diff1
      value: 21.232400000000002
    - type: nauc_recall_at_5_max
      value: 20.1938
    - type: nauc_recall_at_5_std
      value: -4.638599999999999
    - type: nauc_recall_at_5_diff1
      value: 19.724
    - type: nauc_recall_at_10_max
      value: 22.7792
    - type: nauc_recall_at_10_std
      value: -0.7303999999999999
    - type: nauc_recall_at_10_diff1
      value: 17.5686
    - type: nauc_recall_at_20_max
      value: 27.1692
    - type: nauc_recall_at_20_std
      value: 4.6297
    - type: nauc_recall_at_20_diff1
      value: 15.5287
    - type: nauc_recall_at_100_max
      value: 33.9833
    - type: nauc_recall_at_100_std
      value: 26.366899999999998
    - type: nauc_recall_at_100_diff1
      value: 6.823799999999999
    - type: nauc_recall_at_1000_max
      value: 44.722
    - type: nauc_recall_at_1000_std
      value: 49.6373
    - type: nauc_recall_at_1000_diff1
      value: -1.5053
    - type: nauc_precision_at_1_max
      value: 32.205600000000004
    - type: nauc_precision_at_1_std
      value: 11.343499999999999
    - type: nauc_precision_at_1_diff1
      value: 32.8768
    - type: nauc_precision_at_3_max
      value: 24.2364
    - type: nauc_precision_at_3_std
      value: 8.0909
    - type: nauc_precision_at_3_diff1
      value: 12.090399999999999
    - type: nauc_precision_at_5_max
      value: 26.0005
    - type: nauc_precision_at_5_std
      value: 10.2623
    - type: nauc_precision_at_5_diff1
      value: 8.2296
    - type: nauc_precision_at_10_max
      value: 24.6876
    - type: nauc_precision_at_10_std
      value: 16.8067
    - type: nauc_precision_at_10_diff1
      value: 1.6472
    - type: nauc_precision_at_20_max
      value: 22.5879
    - type: nauc_precision_at_20_std
      value: 22.4936
    - type: nauc_precision_at_20_diff1
      value: -2.8762
    - type: nauc_precision_at_100_max
      value: 17.6199
    - type: nauc_precision_at_100_std
      value: 29.5456
    - type: nauc_precision_at_100_diff1
      value: -8.3992
    - type: nauc_precision_at_1000_max
      value: 10.8473
    - type: nauc_precision_at_1000_std
      value: 27.394600000000004
    - type: nauc_precision_at_1000_diff1
      value: -9.8316
    - type: nauc_mrr_at_1_max
      value: 32.205600000000004
    - type: nauc_mrr_at_1_std
      value: 11.343499999999999
    - type: nauc_mrr_at_1_diff1
      value: 32.8768
    - type: nauc_mrr_at_3_max
      value: 32.2439
    - type: nauc_mrr_at_3_std
      value: 11.927999999999999
    - type: nauc_mrr_at_3_diff1
      value: 28.501900000000003
    - type: nauc_mrr_at_5_max
      value: 33.063500000000005
    - type: nauc_mrr_at_5_std
      value: 12.5223
    - type: nauc_mrr_at_5_diff1
      value: 28.5765
    - type: nauc_mrr_at_10_max
      value: 33.0845
    - type: nauc_mrr_at_10_std
      value: 12.7026
    - type: nauc_mrr_at_10_diff1
      value: 28.5328
    - type: nauc_mrr_at_20_max
      value: 33.1039
    - type: nauc_mrr_at_20_std
      value: 12.7458
    - type: nauc_mrr_at_20_diff1
      value: 28.6635
    - type: nauc_mrr_at_100_max
      value: 33.058
    - type: nauc_mrr_at_100_std
      value: 12.8462
    - type: nauc_mrr_at_100_diff1
      value: 28.656599999999997
    - type: nauc_mrr_at_1000_max
      value: 33.0462
    - type: nauc_mrr_at_1000_std
      value: 12.829699999999999
    - type: nauc_mrr_at_1000_diff1
      value: 28.6562
    - type: main_score
      value: 45.458999999999996
    task:
      type: Retrieval
  - dataset:
      config: ja
      name: MTEB MIRACLRetrieval (ja)
      revision: main
      split: dev
      type: miracl/mmteb-miracl
    metrics:
    - type: ndcg_at_1
      value: 53.256
    - type: ndcg_at_3
      value: 53.717000000000006
    - type: ndcg_at_5
      value: 56.523
    - type: ndcg_at_10
      value: 59.922
    - type: ndcg_at_20
      value: 62.596
    - type: ndcg_at_100
      value: 65.40700000000001
    - type: ndcg_at_1000
      value: 66.484
    - type: map_at_1
      value: 34.555
    - type: map_at_3
      value: 45.667
    - type: map_at_5
      value: 48.888
    - type: map_at_10
      value: 51.214000000000006
    - type: map_at_20
      value: 52.325
    - type: map_at_100
      value: 53.032000000000004
    - type: map_at_1000
      value: 53.11
    - type: recall_at_1
      value: 34.555
    - type: recall_at_3
      value: 53.482
    - type: recall_at_5
      value: 62.327
    - type: recall_at_10
      value: 71.476
    - type: recall_at_20
      value: 79.81099999999999
    - type: recall_at_100
      value: 91.152
    - type: recall_at_1000
      value: 97.72800000000001
    - type: precision_at_1
      value: 53.256
    - type: precision_at_3
      value: 30.697999999999997
    - type: precision_at_5
      value: 22.419
    - type: precision_at_10
      value: 13.453000000000001
    - type: precision_at_20
      value: 7.756
    - type: precision_at_100
      value: 1.856
    - type: precision_at_1000
      value: 0.203
    - type: mrr_at_1
      value: 53.2558
    - type: mrr_at_3
      value: 61.860499999999995
    - type: mrr_at_5
      value: 63.558099999999996
    - type: mrr_at_10
      value: 64.4037
    - type: mrr_at_20
      value: 64.78960000000001
    - type: mrr_at_100
      value: 64.9286
    - type: mrr_at_1000
      value: 64.9426
    - type: nauc_ndcg_at_1_max
      value: 40.0831
    - type: nauc_ndcg_at_1_std
      value: 5.4576
    - type: nauc_ndcg_at_1_diff1
      value: 43.1468
    - type: nauc_ndcg_at_3_max
      value: 32.8799
    - type: nauc_ndcg_at_3_std
      value: -3.7643000000000004
    - type: nauc_ndcg_at_3_diff1
      value: 33.0607
    - type: nauc_ndcg_at_5_max
      value: 32.6847
    - type: nauc_ndcg_at_5_std
      value: -4.4878
    - type: nauc_ndcg_at_5_diff1
      value: 33.7729
    - type: nauc_ndcg_at_10_max
      value: 34.0334
    - type: nauc_ndcg_at_10_std
      value: -3.2938
    - type: nauc_ndcg_at_10_diff1
      value: 33.9215
    - type: nauc_ndcg_at_20_max
      value: 35.032799999999995
    - type: nauc_ndcg_at_20_std
      value: -0.9834
    - type: nauc_ndcg_at_20_diff1
      value: 33.4568
    - type: nauc_ndcg_at_100_max
      value: 37.2464
    - type: nauc_ndcg_at_100_std
      value: 1.9361
    - type: nauc_ndcg_at_100_diff1
      value: 34.844
    - type: nauc_ndcg_at_1000_max
      value: 37.0714
    - type: nauc_ndcg_at_1000_std
      value: 1.7745
    - type: nauc_ndcg_at_1000_diff1
      value: 35.123
    - type: nauc_map_at_1_max
      value: 21.2553
    - type: nauc_map_at_1_std
      value: -11.0112
    - type: nauc_map_at_1_diff1
      value: 38.4142
    - type: nauc_map_at_3_max
      value: 25.6791
    - type: nauc_map_at_3_std
      value: -10.7165
    - type: nauc_map_at_3_diff1
      value: 33.1602
    - type: nauc_map_at_5_max
      value: 27.790300000000002
    - type: nauc_map_at_5_std
      value: -9.0268
    - type: nauc_map_at_5_diff1
      value: 33.2551
    - type: nauc_map_at_10_max
      value: 29.4317
    - type: nauc_map_at_10_std
      value: -7.606300000000001
    - type: nauc_map_at_10_diff1
      value: 33.456399999999995
    - type: nauc_map_at_20_max
      value: 30.0805
    - type: nauc_map_at_20_std
      value: -6.482
    - type: nauc_map_at_20_diff1
      value: 33.3844
    - type: nauc_map_at_100_max
      value: 30.7427
    - type: nauc_map_at_100_std
      value: -5.6065
    - type: nauc_map_at_100_diff1
      value: 33.650600000000004
    - type: nauc_map_at_1000_max
      value: 30.763099999999998
    - type: nauc_map_at_1000_std
      value: -5.5541
    - type: nauc_map_at_1000_diff1
      value: 33.677
    - type: nauc_recall_at_1_max
      value: 21.2553
    - type: nauc_recall_at_1_std
      value: -11.0112
    - type: nauc_recall_at_1_diff1
      value: 38.4142
    - type: nauc_recall_at_3_max
      value: 22.537399999999998
    - type: nauc_recall_at_3_std
      value: -12.565000000000001
    - type: nauc_recall_at_3_diff1
      value: 26.549
    - type: nauc_recall_at_5_max
      value: 23.329900000000002
    - type: nauc_recall_at_5_std
      value: -10.4524
    - type: nauc_recall_at_5_diff1
      value: 24.7008
    - type: nauc_recall_at_10_max
      value: 26.0061
    - type: nauc_recall_at_10_std
      value: -6.1622
    - type: nauc_recall_at_10_diff1
      value: 22.880300000000002
    - type: nauc_recall_at_20_max
      value: 26.820300000000003
    - type: nauc_recall_at_20_std
      value: 0.49820000000000003
    - type: nauc_recall_at_20_diff1
      value: 17.1066
    - type: nauc_recall_at_100_max
      value: 41.4851
    - type: nauc_recall_at_100_std
      value: 24.1372
    - type: nauc_recall_at_100_diff1
      value: 20.2474
    - type: nauc_recall_at_1000_max
      value: 46.699
    - type: nauc_recall_at_1000_std
      value: 43.6571
    - type: nauc_recall_at_1000_diff1
      value: 12.969800000000001
    - type: nauc_precision_at_1_max
      value: 40.0831
    - type: nauc_precision_at_1_std
      value: 5.4576
    - type: nauc_precision_at_1_diff1
      value: 43.1468
    - type: nauc_precision_at_3_max
      value: 35.862500000000004
    - type: nauc_precision_at_3_std
      value: 12.6798
    - type: nauc_precision_at_3_diff1
      value: 13.8812
    - type: nauc_precision_at_5_max
      value: 34.525800000000004
    - type: nauc_precision_at_5_std
      value: 19.4325
    - type: nauc_precision_at_5_diff1
      value: 8.5877
    - type: nauc_precision_at_10_max
      value: 31.776500000000002
    - type: nauc_precision_at_10_std
      value: 24.4128
    - type: nauc_precision_at_10_diff1
      value: 2.8872999999999998
    - type: nauc_precision_at_20_max
      value: 27.1526
    - type: nauc_precision_at_20_std
      value: 29.1072
    - type: nauc_precision_at_20_diff1
      value: -1.5491
    - type: nauc_precision_at_100_max
      value: 23.9636
    - type: nauc_precision_at_100_std
      value: 34.5439
    - type: nauc_precision_at_100_diff1
      value: -3.8294
    - type: nauc_precision_at_1000_max
      value: 19.2461
    - type: nauc_precision_at_1000_std
      value: 33.466499999999996
    - type: nauc_precision_at_1000_diff1
      value: -5.7622
    - type: nauc_mrr_at_1_max
      value: 40.0831
    - type: nauc_mrr_at_1_std
      value: 5.4576
    - type: nauc_mrr_at_1_diff1
      value: 43.1468
    - type: nauc_mrr_at_3_max
      value: 44.1712
    - type: nauc_mrr_at_3_std
      value: 6.1216
    - type: nauc_mrr_at_3_diff1
      value: 41.1386
    - type: nauc_mrr_at_5_max
      value: 44.0165
    - type: nauc_mrr_at_5_std
      value: 6.9895
    - type: nauc_mrr_at_5_diff1
      value: 41.124
    - type: nauc_mrr_at_10_max
      value: 43.9807
    - type: nauc_mrr_at_10_std
      value: 7.1412
    - type: nauc_mrr_at_10_diff1
      value: 41.0447
    - type: nauc_mrr_at_20_max
      value: 43.9406
    - type: nauc_mrr_at_20_std
      value: 7.2738
    - type: nauc_mrr_at_20_diff1
      value: 40.9775
    - type: nauc_mrr_at_100_max
      value: 43.9141
    - type: nauc_mrr_at_100_std
      value: 7.212300000000001
    - type: nauc_mrr_at_100_diff1
      value: 41.112700000000004
    - type: nauc_mrr_at_1000_max
      value: 43.9012
    - type: nauc_mrr_at_1000_std
      value: 7.1947
    - type: nauc_mrr_at_1000_diff1
      value: 41.1126
    - type: main_score
      value: 59.922
    task:
      type: Retrieval
  - dataset:
      config: ko
      name: MTEB MIRACLRetrieval (ko)
      revision: main
      split: dev
      type: miracl/mmteb-miracl
    metrics:
    - type: ndcg_at_1
      value: 54.93
    - type: ndcg_at_3
      value: 53.068000000000005
    - type: ndcg_at_5
      value: 55.202
    - type: ndcg_at_10
      value: 58.413000000000004
    - type: ndcg_at_20
      value: 61.732
    - type: ndcg_at_100
      value: 64.374
    - type: ndcg_at_1000
      value: 65.655
    - type: map_at_1
      value: 32.602
    - type: map_at_3
      value: 42.591
    - type: map_at_5
      value: 46.466
    - type: map_at_10
      value: 49.38
    - type: map_at_20
      value: 51.044999999999995
    - type: map_at_100
      value: 51.842
    - type: map_at_1000
      value: 51.92
    - type: recall_at_1
      value: 32.602
    - type: recall_at_3
      value: 49.173
    - type: recall_at_5
      value: 58.269999999999996
    - type: recall_at_10
      value: 68.647
    - type: recall_at_20
      value: 78.089
    - type: recall_at_100
      value: 87.746
    - type: recall_at_1000
      value: 95.524
    - type: precision_at_1
      value: 54.93
    - type: precision_at_3
      value: 31.455
    - type: precision_at_5
      value: 24.413
    - type: precision_at_10
      value: 15.399
    - type: precision_at_20
      value: 9.366
    - type: precision_at_100
      value: 2.235
    - type: precision_at_1000
      value: 0.246
    - type: mrr_at_1
      value: 54.9296
    - type: mrr_at_3
      value: 62.0501
    - type: mrr_at_5
      value: 63.7167
    - type: mrr_at_10
      value: 64.7179
    - type: mrr_at_20
      value: 65.0792
    - type: mrr_at_100
      value: 65.1651
    - type: mrr_at_1000
      value: 65.1775
    - type: nauc_ndcg_at_1_max
      value: 56.11150000000001
    - type: nauc_ndcg_at_1_std
      value: 30.1071
    - type: nauc_ndcg_at_1_diff1
      value: 34.2026
    - type: nauc_ndcg_at_3_max
      value: 34.164899999999996
    - type: nauc_ndcg_at_3_std
      value: 8.9616
    - type: nauc_ndcg_at_3_diff1
      value: 33.8594
    - type: nauc_ndcg_at_5_max
      value: 35.988
    - type: nauc_ndcg_at_5_std
      value: 9.1819
    - type: nauc_ndcg_at_5_diff1
      value: 34.3302
    - type: nauc_ndcg_at_10_max
      value: 33.9669
    - type: nauc_ndcg_at_10_std
      value: 9.9015
    - type: nauc_ndcg_at_10_diff1
      value: 34.7522
    - type: nauc_ndcg_at_20_max
      value: 38.7156
    - type: nauc_ndcg_at_20_std
      value: 13.478299999999999
    - type: nauc_ndcg_at_20_diff1
      value: 34.5892
    - type: nauc_ndcg_at_100_max
      value: 43.2542
    - type: nauc_ndcg_at_100_std
      value: 19.6461
    - type: nauc_ndcg_at_100_diff1
      value: 33.5102
    - type: nauc_ndcg_at_1000_max
      value: 43.5965
    - type: nauc_ndcg_at_1000_std
      value: 20.1448
    - type: nauc_ndcg_at_1000_diff1
      value: 33.508500000000005
    - type: nauc_map_at_1_max
      value: 4.7901
    - type: nauc_map_at_1_std
      value: -11.3406
    - type: nauc_map_at_1_diff1
      value: 47.3089
    - type: nauc_map_at_3_max
      value: 10.8067
    - type: nauc_map_at_3_std
      value: -11.149000000000001
    - type: nauc_map_at_3_diff1
      value: 40.8163
    - type: nauc_map_at_5_max
      value: 19.4936
    - type: nauc_map_at_5_std
      value: -4.9421
    - type: nauc_map_at_5_diff1
      value: 38.1108
    - type: nauc_map_at_10_max
      value: 23.4772
    - type: nauc_map_at_10_std
      value: 0.5471
    - type: nauc_map_at_10_diff1
      value: 37.0351
    - type: nauc_map_at_20_max
      value: 27.0291
    - type: nauc_map_at_20_std
      value: 3.2716000000000003
    - type: nauc_map_at_20_diff1
      value: 36.835
    - type: nauc_map_at_100_max
      value: 28.7591
    - type: nauc_map_at_100_std
      value: 5.4503
    - type: nauc_map_at_100_diff1
      value: 36.3655
    - type: nauc_map_at_1000_max
      value: 28.8292
    - type: nauc_map_at_1000_std
      value: 5.5265
    - type: nauc_map_at_1000_diff1
      value: 36.3425
    - type: nauc_recall_at_1_max
      value: 4.7901
    - type: nauc_recall_at_1_std
      value: -11.3406
    - type: nauc_recall_at_1_diff1
      value: 47.3089
    - type: nauc_recall_at_3_max
      value: 6.1487
    - type: nauc_recall_at_3_std
      value: -16.451999999999998
    - type: nauc_recall_at_3_diff1
      value: 35.876200000000004
    - type: nauc_recall_at_5_max
      value: 17.4052
    - type: nauc_recall_at_5_std
      value: -8.3001
    - type: nauc_recall_at_5_diff1
      value: 31.986700000000003
    - type: nauc_recall_at_10_max
      value: 19.932
    - type: nauc_recall_at_10_std
      value: -0.6047
    - type: nauc_recall_at_10_diff1
      value: 29.7464
    - type: nauc_recall_at_20_max
      value: 27.2026
    - type: nauc_recall_at_20_std
      value: 3.4061
    - type: nauc_recall_at_20_diff1
      value: 29.7029
    - type: nauc_recall_at_100_max
      value: 49.4794
    - type: nauc_recall_at_100_std
      value: 33.5322
    - type: nauc_recall_at_100_diff1
      value: 25.5531
    - type: nauc_recall_at_1000_max
      value: 66.1815
    - type: nauc_recall_at_1000_std
      value: 62.81529999999999
    - type: nauc_recall_at_1000_diff1
      value: 27.209699999999998
    - type: nauc_precision_at_1_max
      value: 56.11150000000001
    - type: nauc_precision_at_1_std
      value: 30.1071
    - type: nauc_precision_at_1_diff1
      value: 34.2026
    - type: nauc_precision_at_3_max
      value: 56.5357
    - type: nauc_precision_at_3_std
      value: 34.1074
    - type: nauc_precision_at_3_diff1
      value: 2.1084
    - type: nauc_precision_at_5_max
      value: 67.0257
    - type: nauc_precision_at_5_std
      value: 48.780699999999996
    - type: nauc_precision_at_5_diff1
      value: -9.4319
    - type: nauc_precision_at_10_max
      value: 64.3278
    - type: nauc_precision_at_10_std
      value: 57.504
    - type: nauc_precision_at_10_diff1
      value: -15.3767
    - type: nauc_precision_at_20_max
      value: 65.8933
    - type: nauc_precision_at_20_std
      value: 60.3452
    - type: nauc_precision_at_20_diff1
      value: -19.1514
    - type: nauc_precision_at_100_max
      value: 63.3574
    - type: nauc_precision_at_100_std
      value: 64.9713
    - type: nauc_precision_at_100_diff1
      value: -22.4344
    - type: nauc_precision_at_1000_max
      value: 59.358599999999996
    - type: nauc_precision_at_1000_std
      value: 62.943000000000005
    - type: nauc_precision_at_1000_diff1
      value: -24.9167
    - type: nauc_mrr_at_1_max
      value: 56.11150000000001
    - type: nauc_mrr_at_1_std
      value: 30.1071
    - type: nauc_mrr_at_1_diff1
      value: 34.2026
    - type: nauc_mrr_at_3_max
      value: 59.3661
    - type: nauc_mrr_at_3_std
      value: 30.759999999999998
    - type: nauc_mrr_at_3_diff1
      value: 31.9662
    - type: nauc_mrr_at_5_max
      value: 60.6752
    - type: nauc_mrr_at_5_std
      value: 32.477000000000004
    - type: nauc_mrr_at_5_diff1
      value: 32.235200000000006
    - type: nauc_mrr_at_10_max
      value: 60.222500000000004
    - type: nauc_mrr_at_10_std
      value: 32.4976
    - type: nauc_mrr_at_10_diff1
      value: 31.8963
    - type: nauc_mrr_at_20_max
      value: 60.0608
    - type: nauc_mrr_at_20_std
      value: 32.421
    - type: nauc_mrr_at_20_diff1
      value: 31.812600000000003
    - type: nauc_mrr_at_100_max
      value: 60.0846
    - type: nauc_mrr_at_100_std
      value: 32.3954
    - type: nauc_mrr_at_100_diff1
      value: 31.8055
    - type: nauc_mrr_at_1000_max
      value: 60.0763
    - type: nauc_mrr_at_1000_std
      value: 32.403999999999996
    - type: nauc_mrr_at_1000_diff1
      value: 31.8195
    - type: main_score
      value: 58.413000000000004
    task:
      type: Retrieval
  - dataset:
      config: ru
      name: MTEB MIRACLRetrieval (ru)
      revision: main
      split: dev
      type: miracl/mmteb-miracl
    metrics:
    - type: ndcg_at_1
      value: 43.131
    - type: ndcg_at_3
      value: 42.808
    - type: ndcg_at_5
      value: 44.373000000000005
    - type: ndcg_at_10
      value: 48.262
    - type: ndcg_at_20
      value: 52.022999999999996
    - type: ndcg_at_100
      value: 56.157999999999994
    - type: ndcg_at_1000
      value: 57.928999999999995
    - type: map_at_1
      value: 22.017999999999997
    - type: map_at_3
      value: 32.41
    - type: map_at_5
      value: 35.558
    - type: map_at_10
      value: 38.449
    - type: map_at_20
      value: 40.144000000000005
    - type: map_at_100
      value: 41.219
    - type: map_at_1000
      value: 41.355
    - type: recall_at_1
      value: 22.017999999999997
    - type: recall_at_3
      value: 39.306999999999995
    - type: recall_at_5
      value: 47.077000000000005
    - type: recall_at_10
      value: 58.034
    - type: recall_at_20
      value: 68.60300000000001
    - type: recall_at_100
      value: 84.074
    - type: recall_at_1000
      value: 93.938
    - type: precision_at_1
      value: 43.131
    - type: precision_at_3
      value: 29.127
    - type: precision_at_5
      value: 22.076999999999998
    - type: precision_at_10
      value: 14.441
    - type: precision_at_20
      value: 8.958
    - type: precision_at_100
      value: 2.331
    - type: precision_at_1000
      value: 0.267
    - type: mrr_at_1
      value: 43.131
    - type: mrr_at_3
      value: 53.28810000000001
    - type: mrr_at_5
      value: 54.785700000000006
    - type: mrr_at_10
      value: 55.948100000000004
    - type: mrr_at_20
      value: 56.422799999999995
    - type: mrr_at_100
      value: 56.5998
    - type: mrr_at_1000
      value: 56.615
    - type: nauc_ndcg_at_1_max
      value: 37.0316
    - type: nauc_ndcg_at_1_std
      value: 16.0392
    - type: nauc_ndcg_at_1_diff1
      value: 35.6661
    - type: nauc_ndcg_at_3_max
      value: 32.547
    - type: nauc_ndcg_at_3_std
      value: 12.7791
    - type: nauc_ndcg_at_3_diff1
      value: 27.252599999999997
    - type: nauc_ndcg_at_5_max
      value: 33.2141
    - type: nauc_ndcg_at_5_std
      value: 12.16
    - type: nauc_ndcg_at_5_diff1
      value: 26.5849
    - type: nauc_ndcg_at_10_max
      value: 34.6417
    - type: nauc_ndcg_at_10_std
      value: 13.350699999999998
    - type: nauc_ndcg_at_10_diff1
      value: 26.616600000000002
    - type: nauc_ndcg_at_20_max
      value: 36.94
    - type: nauc_ndcg_at_20_std
      value: 16.3221
    - type: nauc_ndcg_at_20_diff1
      value: 26.3159
    - type: nauc_ndcg_at_100_max
      value: 39.050200000000004
    - type: nauc_ndcg_at_100_std
      value: 19.5849
    - type: nauc_ndcg_at_100_diff1
      value: 26.6473
    - type: nauc_ndcg_at_1000_max
      value: 39.030300000000004
    - type: nauc_ndcg_at_1000_std
      value: 19.6508
    - type: nauc_ndcg_at_1000_diff1
      value: 27.0546
    - type: nauc_map_at_1_max
      value: 21.368599999999997
    - type: nauc_map_at_1_std
      value: -0.9005000000000001
    - type: nauc_map_at_1_diff1
      value: 35.212500000000006
    - type: nauc_map_at_3_max
      value: 26.070700000000002
    - type: nauc_map_at_3_std
      value: 3.9229
    - type: nauc_map_at_3_diff1
      value: 29.1293
    - type: nauc_map_at_5_max
      value: 29.032999999999998
    - type: nauc_map_at_5_std
      value: 6.5134
    - type: nauc_map_at_5_diff1
      value: 27.908699999999996
    - type: nauc_map_at_10_max
      value: 30.7252
    - type: nauc_map_at_10_std
      value: 8.2968
    - type: nauc_map_at_10_diff1
      value: 27.6959
    - type: nauc_map_at_20_max
      value: 31.926900000000003
    - type: nauc_map_at_20_std
      value: 9.7313
    - type: nauc_map_at_20_diff1
      value: 27.441300000000002
    - type: nauc_map_at_100_max
      value: 32.7179
    - type: nauc_map_at_100_std
      value: 10.8331
    - type: nauc_map_at_100_diff1
      value: 27.458
    - type: nauc_map_at_1000_max
      value: 32.7499
    - type: nauc_map_at_1000_std
      value: 10.898900000000001
    - type: nauc_map_at_1000_diff1
      value: 27.476699999999997
    - type: nauc_recall_at_1_max
      value: 21.368599999999997
    - type: nauc_recall_at_1_std
      value: -0.9005000000000001
    - type: nauc_recall_at_1_diff1
      value: 35.212500000000006
    - type: nauc_recall_at_3_max
      value: 22.0607
    - type: nauc_recall_at_3_std
      value: 3.9726
    - type: nauc_recall_at_3_diff1
      value: 21.705
    - type: nauc_recall_at_5_max
      value: 25.915300000000002
    - type: nauc_recall_at_5_std
      value: 7.4636
    - type: nauc_recall_at_5_diff1
      value: 18.7443
    - type: nauc_recall_at_10_max
      value: 28.7142
    - type: nauc_recall_at_10_std
      value: 11.5264
    - type: nauc_recall_at_10_diff1
      value: 16.7709
    - type: nauc_recall_at_20_max
      value: 33.5513
    - type: nauc_recall_at_20_std
      value: 18.5489
    - type: nauc_recall_at_20_diff1
      value: 14.751900000000001
    - type: nauc_recall_at_100_max
      value: 45.7418
    - type: nauc_recall_at_100_std
      value: 37.693
    - type: nauc_recall_at_100_diff1
      value: 13.589699999999999
    - type: nauc_recall_at_1000_max
      value: 62.0517
    - type: nauc_recall_at_1000_std
      value: 61.5653
    - type: nauc_recall_at_1000_diff1
      value: 12.8732
    - type: nauc_precision_at_1_max
      value: 37.0316
    - type: nauc_precision_at_1_std
      value: 16.0392
    - type: nauc_precision_at_1_diff1
      value: 35.6661
    - type: nauc_precision_at_3_max
      value: 36.3558
    - type: nauc_precision_at_3_std
      value: 24.7253
    - type: nauc_precision_at_3_diff1
      value: 13.029499999999999
    - type: nauc_precision_at_5_max
      value: 36.3254
    - type: nauc_precision_at_5_std
      value: 26.7762
    - type: nauc_precision_at_5_diff1
      value: 7.561
    - type: nauc_precision_at_10_max
      value: 32.2831
    - type: nauc_precision_at_10_std
      value: 27.621499999999997
    - type: nauc_precision_at_10_diff1
      value: 2.9292
    - type: nauc_precision_at_20_max
      value: 30.0072
    - type: nauc_precision_at_20_std
      value: 30.3405
    - type: nauc_precision_at_20_diff1
      value: -1.4427
    - type: nauc_precision_at_100_max
      value: 23.4879
    - type: nauc_precision_at_100_std
      value: 30.9203
    - type: nauc_precision_at_100_diff1
      value: -5.0680000000000005
    - type: nauc_precision_at_1000_max
      value: 16.6706
    - type: nauc_precision_at_1000_std
      value: 26.621899999999997
    - type: nauc_precision_at_1000_diff1
      value: -6.5622
    - type: nauc_mrr_at_1_max
      value: 37.0316
    - type: nauc_mrr_at_1_std
      value: 16.0392
    - type: nauc_mrr_at_1_diff1
      value: 35.6661
    - type: nauc_mrr_at_3_max
      value: 39.3089
    - type: nauc_mrr_at_3_std
      value: 19.7933
    - type: nauc_mrr_at_3_diff1
      value: 30.968600000000002
    - type: nauc_mrr_at_5_max
      value: 39.641
    - type: nauc_mrr_at_5_std
      value: 20.052300000000002
    - type: nauc_mrr_at_5_diff1
      value: 31.3307
    - type: nauc_mrr_at_10_max
      value: 40.1004
    - type: nauc_mrr_at_10_std
      value: 20.5772
    - type: nauc_mrr_at_10_diff1
      value: 31.423000000000002
    - type: nauc_mrr_at_20_max
      value: 40.14
    - type: nauc_mrr_at_20_std
      value: 20.677400000000002
    - type: nauc_mrr_at_20_diff1
      value: 31.568800000000003
    - type: nauc_mrr_at_100_max
      value: 40.0878
    - type: nauc_mrr_at_100_std
      value: 20.6034
    - type: nauc_mrr_at_100_diff1
      value: 31.5872
    - type: nauc_mrr_at_1000_max
      value: 40.078
    - type: nauc_mrr_at_1000_std
      value: 20.589399999999998
    - type: nauc_mrr_at_1000_diff1
      value: 31.591599999999996
    - type: main_score
      value: 48.262
    task:
      type: Retrieval
  - dataset:
      config: sw
      name: MTEB MIRACLRetrieval (sw)
      revision: main
      split: dev
      type: miracl/mmteb-miracl
    metrics:
    - type: ndcg_at_1
      value: 50.415
    - type: ndcg_at_3
      value: 53.04
    - type: ndcg_at_5
      value: 56.138999999999996
    - type: ndcg_at_10
      value: 59.111000000000004
    - type: ndcg_at_20
      value: 61.651
    - type: ndcg_at_100
      value: 64.312
    - type: ndcg_at_1000
      value: 65.089
    - type: map_at_1
      value: 33.267
    - type: map_at_3
      value: 46.152
    - type: map_at_5
      value: 49.293
    - type: map_at_10
      value: 51.06699999999999
    - type: map_at_20
      value: 52.051
    - type: map_at_100
      value: 52.632
    - type: map_at_1000
      value: 52.686
    - type: recall_at_1
      value: 33.267
    - type: recall_at_3
      value: 55.48
    - type: recall_at_5
      value: 64.302
    - type: recall_at_10
      value: 72.08200000000001
    - type: recall_at_20
      value: 79.943
    - type: recall_at_100
      value: 91.377
    - type: recall_at_1000
      value: 96.152
    - type: precision_at_1
      value: 50.415
    - type: precision_at_3
      value: 30.152
    - type: precision_at_5
      value: 21.576999999999998
    - type: precision_at_10
      value: 12.49
    - type: precision_at_20
      value: 7.199
    - type: precision_at_100
      value: 1.699
    - type: precision_at_1000
      value: 0.182
    - type: mrr_at_1
      value: 50.414899999999996
    - type: mrr_at_3
      value: 58.9903
    - type: mrr_at_5
      value: 60.7123
    - type: mrr_at_10
      value: 61.388799999999996
    - type: mrr_at_20
      value: 61.804700000000004
    - type: mrr_at_100
      value: 61.9677
    - type: mrr_at_1000
      value: 61.9774
    - type: nauc_ndcg_at_1_max
      value: 38.0582
    - type: nauc_ndcg_at_1_std
      value: 10.7971
    - type: nauc_ndcg_at_1_diff1
      value: 39.3361
    - type: nauc_ndcg_at_3_max
      value: 36.1772
    - type: nauc_ndcg_at_3_std
      value: 6.7326
    - type: nauc_ndcg_at_3_diff1
      value: 35.3446
    - type: nauc_ndcg_at_5_max
      value: 34.8851
    - type: nauc_ndcg_at_5_std
      value: 6.4693000000000005
    - type: nauc_ndcg_at_5_diff1
      value: 36.4089
    - type: nauc_ndcg_at_10_max
      value: 38.800200000000004
    - type: nauc_ndcg_at_10_std
      value: 5.9294
    - type: nauc_ndcg_at_10_diff1
      value: 36.1487
    - type: nauc_ndcg_at_20_max
      value: 39.557700000000004
    - type: nauc_ndcg_at_20_std
      value: 7.1913
    - type: nauc_ndcg_at_20_diff1
      value: 35.476200000000006
    - type: nauc_ndcg_at_100_max
      value: 40.7973
    - type: nauc_ndcg_at_100_std
      value: 12.0762
    - type: nauc_ndcg_at_100_diff1
      value: 35.9479
    - type: nauc_ndcg_at_1000_max
      value: 41.133900000000004
    - type: nauc_ndcg_at_1000_std
      value: 12.3712
    - type: nauc_ndcg_at_1000_diff1
      value: 35.6136
    - type: nauc_map_at_1_max
      value: 16.2887
    - type: nauc_map_at_1_std
      value: -5.9883
    - type: nauc_map_at_1_diff1
      value: 44.4133
    - type: nauc_map_at_3_max
      value: 30.484499999999997
    - type: nauc_map_at_3_std
      value: 2.8722000000000003
    - type: nauc_map_at_3_diff1
      value: 37.9749
    - type: nauc_map_at_5_max
      value: 31.883499999999998
    - type: nauc_map_at_5_std
      value: 3.7571
    - type: nauc_map_at_5_diff1
      value: 37.655300000000004
    - type: nauc_map_at_10_max
      value: 34.440799999999996
    - type: nauc_map_at_10_std
      value: 3.7608
    - type: nauc_map_at_10_diff1
      value: 37.2883
    - type: nauc_map_at_20_max
      value: 34.9033
    - type: nauc_map_at_20_std
      value: 4.3576
    - type: nauc_map_at_20_diff1
      value: 37.0318
    - type: nauc_map_at_100_max
      value: 35.2377
    - type: nauc_map_at_100_std
      value: 5.3088999999999995
    - type: nauc_map_at_100_diff1
      value: 37.1107
    - type: nauc_map_at_1000_max
      value: 35.281099999999995
    - type: nauc_map_at_1000_std
      value: 5.3637999999999995
    - type: nauc_map_at_1000_diff1
      value: 37.0696
    - type: nauc_recall_at_1_max
      value: 16.2887
    - type: nauc_recall_at_1_std
      value: -5.9883
    - type: nauc_recall_at_1_diff1
      value: 44.4133
    - type: nauc_recall_at_3_max
      value: 28.2547
    - type: nauc_recall_at_3_std
      value: 1.4864
    - type: nauc_recall_at_3_diff1
      value: 32.121100000000006
    - type: nauc_recall_at_5_max
      value: 27.503899999999998
    - type: nauc_recall_at_5_std
      value: 2.3485
    - type: nauc_recall_at_5_diff1
      value: 31.1749
    - type: nauc_recall_at_10_max
      value: 37.1037
    - type: nauc_recall_at_10_std
      value: -1.0915
    - type: nauc_recall_at_10_diff1
      value: 30.7288
    - type: nauc_recall_at_20_max
      value: 38.685900000000004
    - type: nauc_recall_at_20_std
      value: -0.39540000000000003
    - type: nauc_recall_at_20_diff1
      value: 26.9173
    - type: nauc_recall_at_100_max
      value: 52.7177
    - type: nauc_recall_at_100_std
      value: 45.8168
    - type: nauc_recall_at_100_diff1
      value: 29.572599999999998
    - type: nauc_recall_at_1000_max
      value: 81.5773
    - type: nauc_recall_at_1000_std
      value: 86.1207
    - type: nauc_recall_at_1000_diff1
      value: 26.2688
    - type: nauc_precision_at_1_max
      value: 38.0582
    - type: nauc_precision_at_1_std
      value: 10.7971
    - type: nauc_precision_at_1_diff1
      value: 39.3361
    - type: nauc_precision_at_3_max
      value: 48.16
    - type: nauc_precision_at_3_std
      value: 25.037100000000002
    - type: nauc_precision_at_3_diff1
      value: 9.8087
    - type: nauc_precision_at_5_max
      value: 45.5463
    - type: nauc_precision_at_5_std
      value: 25.275399999999998
    - type: nauc_precision_at_5_diff1
      value: 3.3124000000000002
    - type: nauc_precision_at_10_max
      value: 45.3542
    - type: nauc_precision_at_10_std
      value: 21.1762
    - type: nauc_precision_at_10_diff1
      value: -3.5867999999999998
    - type: nauc_precision_at_20_max
      value: 40.4771
    - type: nauc_precision_at_20_std
      value: 25.006800000000002
    - type: nauc_precision_at_20_diff1
      value: -10.331700000000001
    - type: nauc_precision_at_100_max
      value: 32.6887
    - type: nauc_precision_at_100_std
      value: 34.5781
    - type: nauc_precision_at_100_diff1
      value: -16.628999999999998
    - type: nauc_precision_at_1000_max
      value: 29.033399999999997
    - type: nauc_precision_at_1000_std
      value: 33.129
    - type: nauc_precision_at_1000_diff1
      value: -19.7542
    - type: nauc_mrr_at_1_max
      value: 38.0582
    - type: nauc_mrr_at_1_std
      value: 10.7971
    - type: nauc_mrr_at_1_diff1
      value: 39.3361
    - type: nauc_mrr_at_3_max
      value: 42.2985
    - type: nauc_mrr_at_3_std
      value: 13.949900000000001
    - type: nauc_mrr_at_3_diff1
      value: 36.0085
    - type: nauc_mrr_at_5_max
      value: 42.3132
    - type: nauc_mrr_at_5_std
      value: 14.8284
    - type: nauc_mrr_at_5_diff1
      value: 36.0635
    - type: nauc_mrr_at_10_max
      value: 42.6836
    - type: nauc_mrr_at_10_std
      value: 14.1374
    - type: nauc_mrr_at_10_diff1
      value: 36.2117
    - type: nauc_mrr_at_20_max
      value: 42.6572
    - type: nauc_mrr_at_20_std
      value: 14.2714
    - type: nauc_mrr_at_20_diff1
      value: 36.0993
    - type: nauc_mrr_at_100_max
      value: 42.663000000000004
    - type: nauc_mrr_at_100_std
      value: 14.5399
    - type: nauc_mrr_at_100_diff1
      value: 36.214600000000004
    - type: nauc_mrr_at_1000_max
      value: 42.6543
    - type: nauc_mrr_at_1000_std
      value: 14.5232
    - type: nauc_mrr_at_1000_diff1
      value: 36.219699999999996
    - type: main_score
      value: 59.111000000000004
    task:
      type: Retrieval
  - dataset:
      config: te
      name: MTEB MIRACLRetrieval (te)
      revision: main
      split: dev
      type: miracl/mmteb-miracl
    metrics:
    - type: ndcg_at_1
      value: 64.372
    - type: ndcg_at_3
      value: 74.856
    - type: ndcg_at_5
      value: 77.128
    - type: ndcg_at_10
      value: 78.175
    - type: ndcg_at_20
      value: 78.826
    - type: ndcg_at_100
      value: 79.523
    - type: ndcg_at_1000
      value: 79.774
    - type: map_at_1
      value: 63.688
    - type: map_at_3
      value: 72.262
    - type: map_at_5
      value: 73.56700000000001
    - type: map_at_10
      value: 74.022
    - type: map_at_20
      value: 74.217
    - type: map_at_100
      value: 74.316
    - type: map_at_1000
      value: 74.32600000000001
    - type: recall_at_1
      value: 63.688
    - type: recall_at_3
      value: 81.804
    - type: recall_at_5
      value: 87.198
    - type: recall_at_10
      value: 90.358
    - type: recall_at_20
      value: 92.834
    - type: recall_at_100
      value: 96.55799999999999
    - type: recall_at_1000
      value: 98.47
    - type: precision_at_1
      value: 64.372
    - type: precision_at_3
      value: 27.858
    - type: precision_at_5
      value: 17.849999999999998
    - type: precision_at_10
      value: 9.263
    - type: precision_at_20
      value: 4.771
    - type: precision_at_100
      value: 0.993
    - type: precision_at_1000
      value: 0.101
    - type: mrr_at_1
      value: 64.372
    - type: mrr_at_3
      value: 72.7456
    - type: mrr_at_5
      value: 73.9654
    - type: mrr_at_10
      value: 74.3824
    - type: mrr_at_20
      value: 74.5572
    - type: mrr_at_100
      value: 74.6496
    - type: mrr_at_1000
      value: 74.65889999999999
    - type: nauc_ndcg_at_1_max
      value: 39.271699999999996
    - type: nauc_ndcg_at_1_std
      value: -24.310499999999998
    - type: nauc_ndcg_at_1_diff1
      value: 58.76440000000001
    - type: nauc_ndcg_at_3_max
      value: 42.7376
    - type: nauc_ndcg_at_3_std
      value: -25.2897
    - type: nauc_ndcg_at_3_diff1
      value: 55.2624
    - type: nauc_ndcg_at_5_max
      value: 45.5625
    - type: nauc_ndcg_at_5_std
      value: -22.595299999999998
    - type: nauc_ndcg_at_5_diff1
      value: 54.2902
    - type: nauc_ndcg_at_10_max
      value: 46.581
    - type: nauc_ndcg_at_10_std
      value: -20.4188
    - type: nauc_ndcg_at_10_diff1
      value: 53.76800000000001
    - type: nauc_ndcg_at_20_max
      value: 45.912
    - type: nauc_ndcg_at_20_std
      value: -20.7345
    - type: nauc_ndcg_at_20_diff1
      value: 53.597300000000004
    - type: nauc_ndcg_at_100_max
      value: 45.4388
    - type: nauc_ndcg_at_100_std
      value: -20.569499999999998
    - type: nauc_ndcg_at_100_diff1
      value: 54.1768
    - type: nauc_ndcg_at_1000_max
      value: 44.8662
    - type: nauc_ndcg_at_1000_std
      value: -20.9083
    - type: nauc_ndcg_at_1000_diff1
      value: 54.316900000000004
    - type: nauc_map_at_1_max
      value: 38.1714
    - type: nauc_map_at_1_std
      value: -25.8547
    - type: nauc_map_at_1_diff1
      value: 58.801700000000004
    - type: nauc_map_at_3_max
      value: 41.6072
    - type: nauc_map_at_3_std
      value: -25.716299999999997
    - type: nauc_map_at_3_diff1
      value: 55.9906
    - type: nauc_map_at_5_max
      value: 43.061899999999994
    - type: nauc_map_at_5_std
      value: -24.2147
    - type: nauc_map_at_5_diff1
      value: 55.4852
    - type: nauc_map_at_10_max
      value: 43.452
    - type: nauc_map_at_10_std
      value: -23.4256
    - type: nauc_map_at_10_diff1
      value: 55.3427
    - type: nauc_map_at_20_max
      value: 43.305
    - type: nauc_map_at_20_std
      value: -23.424500000000002
    - type: nauc_map_at_20_diff1
      value: 55.31120000000001
    - type: nauc_map_at_100_max
      value: 43.2512
    - type: nauc_map_at_100_std
      value: -23.3786
    - type: nauc_map_at_100_diff1
      value: 55.3755
    - type: nauc_map_at_1000_max
      value: 43.2306
    - type: nauc_map_at_1000_std
      value: -23.380699999999997
    - type: nauc_map_at_1000_diff1
      value: 55.378899999999994
    - type: nauc_recall_at_1_max
      value: 38.1714
    - type: nauc_recall_at_1_std
      value: -25.8547
    - type: nauc_recall_at_1_diff1
      value: 58.801700000000004
    - type: nauc_recall_at_3_max
      value: 46.7953
    - type: nauc_recall_at_3_std
      value: -25.092100000000002
    - type: nauc_recall_at_3_diff1
      value: 52.0717
    - type: nauc_recall_at_5_max
      value: 58.675399999999996
    - type: nauc_recall_at_5_std
      value: -15.456100000000001
    - type: nauc_recall_at_5_diff1
      value: 47.4131
    - type: nauc_recall_at_10_max
      value: 67.7093
    - type: nauc_recall_at_10_std
      value: -0.5740000000000001
    - type: nauc_recall_at_10_diff1
      value: 42.2693
    - type: nauc_recall_at_20_max
      value: 68.11160000000001
    - type: nauc_recall_at_20_std
      value: 1.8836
    - type: nauc_recall_at_20_diff1
      value: 36.960300000000004
    - type: nauc_recall_at_100_max
      value: 78.39620000000001
    - type: nauc_recall_at_100_std
      value: 27.515299999999996
    - type: nauc_recall_at_100_diff1
      value: 35.8977
    - type: nauc_recall_at_1000_max
      value: 71.4983
    - type: nauc_recall_at_1000_std
      value: 50.89939999999999
    - type: nauc_recall_at_1000_diff1
      value: 28.7768
    - type: nauc_precision_at_1_max
      value: 39.271699999999996
    - type: nauc_precision_at_1_std
      value: -24.310499999999998
    - type: nauc_precision_at_1_diff1
      value: 58.76440000000001
    - type: nauc_precision_at_3_max
      value: 46.5473
    - type: nauc_precision_at_3_std
      value: -16.3903
    - type: nauc_precision_at_3_diff1
      value: 43.1862
    - type: nauc_precision_at_5_max
      value: 53.557500000000005
    - type: nauc_precision_at_5_std
      value: -1.2877
    - type: nauc_precision_at_5_diff1
      value: 31.9181
    - type: nauc_precision_at_10_max
      value: 55.428599999999996
    - type: nauc_precision_at_10_std
      value: 12.8033
    - type: nauc_precision_at_10_diff1
      value: 22.756
    - type: nauc_precision_at_20_max
      value: 49.0193
    - type: nauc_precision_at_20_std
      value: 19.6821
    - type: nauc_precision_at_20_diff1
      value: 12.0609
    - type: nauc_precision_at_100_max
      value: 40.4145
    - type: nauc_precision_at_100_std
      value: 38.3506
    - type: nauc_precision_at_100_diff1
      value: -1.6396000000000002
    - type: nauc_precision_at_1000_max
      value: 19.25
    - type: nauc_precision_at_1000_std
      value: 41.2279
    - type: nauc_precision_at_1000_diff1
      value: -17.3722
    - type: nauc_mrr_at_1_max
      value: 39.271699999999996
    - type: nauc_mrr_at_1_std
      value: -24.310499999999998
    - type: nauc_mrr_at_1_diff1
      value: 58.76440000000001
    - type: nauc_mrr_at_3_max
      value: 41.6685
    - type: nauc_mrr_at_3_std
      value: -24.4404
    - type: nauc_mrr_at_3_diff1
      value: 56.1212
    - type: nauc_mrr_at_5_max
      value: 42.9495
    - type: nauc_mrr_at_5_std
      value: -23.378899999999998
    - type: nauc_mrr_at_5_diff1
      value: 55.7671
    - type: nauc_mrr_at_10_max
      value: 43.371900000000004
    - type: nauc_mrr_at_10_std
      value: -22.5248
    - type: nauc_mrr_at_10_diff1
      value: 55.5427
    - type: nauc_mrr_at_20_max
      value: 43.1738
    - type: nauc_mrr_at_20_std
      value: -22.6888
    - type: nauc_mrr_at_20_diff1
      value: 55.5207
    - type: nauc_mrr_at_100_max
      value: 43.1156
    - type: nauc_mrr_at_100_std
      value: -22.6434
    - type: nauc_mrr_at_100_diff1
      value: 55.5733
    - type: nauc_mrr_at_1000_max
      value: 43.0971
    - type: nauc_mrr_at_1000_std
      value: -22.6431
    - type: nauc_mrr_at_1000_diff1
      value: 55.5782
    - type: main_score
      value: 78.175
    task:
      type: Retrieval
  - dataset:
      config: th
      name: MTEB MIRACLRetrieval (th)
      revision: main
      split: dev
      type: miracl/mmteb-miracl
    metrics:
    - type: ndcg_at_1
      value: 65.484
    - type: ndcg_at_3
      value: 66.199
    - type: ndcg_at_5
      value: 68.451
    - type: ndcg_at_10
      value: 71.774
    - type: ndcg_at_20
      value: 73.709
    - type: ndcg_at_100
      value: 75.362
    - type: ndcg_at_1000
      value: 75.898
    - type: map_at_1
      value: 45.911
    - type: map_at_3
      value: 59.53000000000001
    - type: map_at_5
      value: 62.150000000000006
    - type: map_at_10
      value: 64.336
    - type: map_at_20
      value: 65.262
    - type: map_at_100
      value: 65.659
    - type: map_at_1000
      value: 65.694
    - type: recall_at_1
      value: 45.911
    - type: recall_at_3
      value: 67.437
    - type: recall_at_5
      value: 73.786
    - type: recall_at_10
      value: 82.619
    - type: recall_at_20
      value: 88.447
    - type: recall_at_100
      value: 95.515
    - type: recall_at_1000
      value: 98.854
    - type: precision_at_1
      value: 65.484
    - type: precision_at_3
      value: 35.471000000000004
    - type: precision_at_5
      value: 24.229
    - type: precision_at_10
      value: 14.188
    - type: precision_at_20
      value: 7.843999999999999
    - type: precision_at_100
      value: 1.733
    - type: precision_at_1000
      value: 0.181
    - type: mrr_at_1
      value: 65.48429999999999
    - type: mrr_at_3
      value: 73.2378
    - type: mrr_at_5
      value: 74.1314
    - type: mrr_at_10
      value: 74.8844
    - type: mrr_at_20
      value: 75.07639999999999
    - type: mrr_at_100
      value: 75.1632
    - type: mrr_at_1000
      value: 75.1698
    - type: nauc_ndcg_at_1_max
      value: 42.345
    - type: nauc_ndcg_at_1_std
      value: 12.6892
    - type: nauc_ndcg_at_1_diff1
      value: 42.4669
    - type: nauc_ndcg_at_3_max
      value: 38.8148
    - type: nauc_ndcg_at_3_std
      value: 3.5637000000000003
    - type: nauc_ndcg_at_3_diff1
      value: 34.8248
    - type: nauc_ndcg_at_5_max
      value: 38.7175
    - type: nauc_ndcg_at_5_std
      value: 1.6251000000000002
    - type: nauc_ndcg_at_5_diff1
      value: 34.1513
    - type: nauc_ndcg_at_10_max
      value: 40.038000000000004
    - type: nauc_ndcg_at_10_std
      value: 2.8985
    - type: nauc_ndcg_at_10_diff1
      value: 33.4189
    - type: nauc_ndcg_at_20_max
      value: 41.722
    - type: nauc_ndcg_at_20_std
      value: 6.819100000000001
    - type: nauc_ndcg_at_20_diff1
      value: 33.5606
    - type: nauc_ndcg_at_100_max
      value: 42.2102
    - type: nauc_ndcg_at_100_std
      value: 8.309099999999999
    - type: nauc_ndcg_at_100_diff1
      value: 34.036899999999996
    - type: nauc_ndcg_at_1000_max
      value: 41.9273
    - type: nauc_ndcg_at_1000_std
      value: 8.3582
    - type: nauc_ndcg_at_1000_diff1
      value: 34.4614
    - type: nauc_map_at_1_max
      value: 20.202
    - type: nauc_map_at_1_std
      value: -8.095099999999999
    - type: nauc_map_at_1_diff1
      value: 42.2902
    - type: nauc_map_at_3_max
      value: 33.0956
    - type: nauc_map_at_3_std
      value: -3.7472
    - type: nauc_map_at_3_diff1
      value: 36.3181
    - type: nauc_map_at_5_max
      value: 34.3309
    - type: nauc_map_at_5_std
      value: -3.0949999999999998
    - type: nauc_map_at_5_diff1
      value: 35.441
    - type: nauc_map_at_10_max
      value: 35.924
    - type: nauc_map_at_10_std
      value: -1.3787
    - type: nauc_map_at_10_diff1
      value: 35.0315
    - type: nauc_map_at_20_max
      value: 36.7677
    - type: nauc_map_at_20_std
      value: 0.4997
    - type: nauc_map_at_20_diff1
      value: 35.037600000000005
    - type: nauc_map_at_100_max
      value: 36.8927
    - type: nauc_map_at_100_std
      value: 0.8881999999999999
    - type: nauc_map_at_100_diff1
      value: 35.0792
    - type: nauc_map_at_1000_max
      value: 36.897999999999996
    - type: nauc_map_at_1000_std
      value: 0.9301
    - type: nauc_map_at_1000_diff1
      value: 35.0961
    - type: nauc_recall_at_1_max
      value: 20.202
    - type: nauc_recall_at_1_std
      value: -8.095099999999999
    - type: nauc_recall_at_1_diff1
      value: 42.2902
    - type: nauc_recall_at_3_max
      value: 33.1749
    - type: nauc_recall_at_3_std
      value: -4.6383
    - type: nauc_recall_at_3_diff1
      value: 30.5276
    - type: nauc_recall_at_5_max
      value: 35.2372
    - type: nauc_recall_at_5_std
      value: -6.0825
    - type: nauc_recall_at_5_diff1
      value: 27.128200000000003
    - type: nauc_recall_at_10_max
      value: 37.465199999999996
    - type: nauc_recall_at_10_std
      value: -4.937600000000001
    - type: nauc_recall_at_10_diff1
      value: 21.6784
    - type: nauc_recall_at_20_max
      value: 45.9944
    - type: nauc_recall_at_20_std
      value: 10.5054
    - type: nauc_recall_at_20_diff1
      value: 19.4427
    - type: nauc_recall_at_100_max
      value: 60.7611
    - type: nauc_recall_at_100_std
      value: 35.4282
    - type: nauc_recall_at_100_diff1
      value: 14.2406
    - type: nauc_recall_at_1000_max
      value: 83.2149
    - type: nauc_recall_at_1000_std
      value: 87.3129
    - type: nauc_recall_at_1000_diff1
      value: 15.7695
    - type: nauc_precision_at_1_max
      value: 42.345
    - type: nauc_precision_at_1_std
      value: 12.6892
    - type: nauc_precision_at_1_diff1
      value: 42.4669
    - type: nauc_precision_at_3_max
      value: 38.0839
    - type: nauc_precision_at_3_std
      value: 22.0767
    - type: nauc_precision_at_3_diff1
      value: 1.4477
    - type: nauc_precision_at_5_max
      value: 31.290499999999998
    - type: nauc_precision_at_5_std
      value: 23.3095
    - type: nauc_precision_at_5_diff1
      value: -5.9094
    - type: nauc_precision_at_10_max
      value: 25.186199999999996
    - type: nauc_precision_at_10_std
      value: 27.7866
    - type: nauc_precision_at_10_diff1
      value: -12.773200000000001
    - type: nauc_precision_at_20_max
      value: 21.0353
    - type: nauc_precision_at_20_std
      value: 33.7266
    - type: nauc_precision_at_20_diff1
      value: -15.188699999999999
    - type: nauc_precision_at_100_max
      value: 16.1451
    - type: nauc_precision_at_100_std
      value: 35.4163
    - type: nauc_precision_at_100_diff1
      value: -17.631800000000002
    - type: nauc_precision_at_1000_max
      value: 12.2855
    - type: nauc_precision_at_1000_std
      value: 34.2766
    - type: nauc_precision_at_1000_diff1
      value: -17.664099999999998
    - type: nauc_mrr_at_1_max
      value: 42.345
    - type: nauc_mrr_at_1_std
      value: 12.6892
    - type: nauc_mrr_at_1_diff1
      value: 42.4669
    - type: nauc_mrr_at_3_max
      value: 47.5742
    - type: nauc_mrr_at_3_std
      value: 17.136499999999998
    - type: nauc_mrr_at_3_diff1
      value: 37.68
    - type: nauc_mrr_at_5_max
      value: 47.510799999999996
    - type: nauc_mrr_at_5_std
      value: 17.1225
    - type: nauc_mrr_at_5_diff1
      value: 37.485099999999996
    - type: nauc_mrr_at_10_max
      value: 47.2849
    - type: nauc_mrr_at_10_std
      value: 17.2096
    - type: nauc_mrr_at_10_diff1
      value: 37.2312
    - type: nauc_mrr_at_20_max
      value: 47.3962
    - type: nauc_mrr_at_20_std
      value: 17.2426
    - type: nauc_mrr_at_20_diff1
      value: 37.500499999999995
    - type: nauc_mrr_at_100_max
      value: 47.344
    - type: nauc_mrr_at_100_std
      value: 17.144499999999997
    - type: nauc_mrr_at_100_diff1
      value: 37.5291
    - type: nauc_mrr_at_1000_max
      value: 47.3332
    - type: nauc_mrr_at_1000_std
      value: 17.1381
    - type: nauc_mrr_at_1000_diff1
      value: 37.532199999999996
    - type: main_score
      value: 71.774
    task:
      type: Retrieval
  - dataset:
      config: yo
      name: MTEB MIRACLRetrieval (yo)
      revision: main
      split: dev
      type: miracl/mmteb-miracl
    metrics:
    - type: ndcg_at_1
      value: 46.217999999999996
    - type: ndcg_at_3
      value: 57.609
    - type: ndcg_at_5
      value: 62.021
    - type: ndcg_at_10
      value: 64.685
    - type: ndcg_at_20
      value: 65.548
    - type: ndcg_at_100
      value: 66.94099999999999
    - type: ndcg_at_1000
      value: 67.361
    - type: map_at_1
      value: 42.787
    - type: map_at_3
      value: 53.852
    - type: map_at_5
      value: 56.541
    - type: map_at_10
      value: 57.924
    - type: map_at_20
      value: 58.223
    - type: map_at_100
      value: 58.41499999999999
    - type: map_at_1000
      value: 58.43000000000001
    - type: recall_at_1
      value: 42.787
    - type: recall_at_3
      value: 65.40599999999999
    - type: recall_at_5
      value: 75.42
    - type: recall_at_10
      value: 82.913
    - type: recall_at_20
      value: 85.994
    - type: recall_at_100
      value: 93.277
    - type: recall_at_1000
      value: 96.499
    - type: precision_at_1
      value: 46.217999999999996
    - type: precision_at_3
      value: 24.37
    - type: precision_at_5
      value: 17.479
    - type: precision_at_10
      value: 9.748
    - type: precision_at_20
      value: 5.0840000000000005
    - type: precision_at_100
      value: 1.109
    - type: precision_at_1000
      value: 0.116
    - type: mrr_at_1
      value: 46.2185
    - type: mrr_at_3
      value: 56.582600000000006
    - type: mrr_at_5
      value: 58.977599999999995
    - type: mrr_at_10
      value: 59.890299999999996
    - type: mrr_at_20
      value: 60.077999999999996
    - type: mrr_at_100
      value: 60.2472
    - type: mrr_at_1000
      value: 60.2553
    - type: nauc_ndcg_at_1_max
      value: 15.3057
    - type: nauc_ndcg_at_1_std
      value: -20.3881
    - type: nauc_ndcg_at_1_diff1
      value: 51.7456
    - type: nauc_ndcg_at_3_max
      value: 17.750799999999998
    - type: nauc_ndcg_at_3_std
      value: -9.165
    - type: nauc_ndcg_at_3_diff1
      value: 53.4833
    - type: nauc_ndcg_at_5_max
      value: 18.6146
    - type: nauc_ndcg_at_5_std
      value: -3.832
    - type: nauc_ndcg_at_5_diff1
      value: 52.8833
    - type: nauc_ndcg_at_10_max
      value: 20.4881
    - type: nauc_ndcg_at_10_std
      value: -3.7813
    - type: nauc_ndcg_at_10_diff1
      value: 53.873099999999994
    - type: nauc_ndcg_at_20_max
      value: 22.234499999999997
    - type: nauc_ndcg_at_20_std
      value: -4.5588999999999995
    - type: nauc_ndcg_at_20_diff1
      value: 53.75149999999999
    - type: nauc_ndcg_at_100_max
      value: 22.5348
    - type: nauc_ndcg_at_100_std
      value: -5.6818
    - type: nauc_ndcg_at_100_diff1
      value: 54.996199999999995
    - type: nauc_ndcg_at_1000_max
      value: 21.8399
    - type: nauc_ndcg_at_1000_std
      value: -6.904000000000001
    - type: nauc_ndcg_at_1000_diff1
      value: 54.5607
    - type: nauc_map_at_1_max
      value: 11.5768
    - type: nauc_map_at_1_std
      value: -16.317400000000003
    - type: nauc_map_at_1_diff1
      value: 56.0748
    - type: nauc_map_at_3_max
      value: 14.5127
    - type: nauc_map_at_3_std
      value: -9.9466
    - type: nauc_map_at_3_diff1
      value: 54.4564
    - type: nauc_map_at_5_max
      value: 15.6777
    - type: nauc_map_at_5_std
      value: -7.3351
    - type: nauc_map_at_5_diff1
      value: 53.8739
    - type: nauc_map_at_10_max
      value: 17.380200000000002
    - type: nauc_map_at_10_std
      value: -7.8866000000000005
    - type: nauc_map_at_10_diff1
      value: 54.17380000000001
    - type: nauc_map_at_20_max
      value: 17.7812
    - type: nauc_map_at_20_std
      value: -8.1005
    - type: nauc_map_at_20_diff1
      value: 54.16029999999999
    - type: nauc_map_at_100_max
      value: 17.8472
    - type: nauc_map_at_100_std
      value: -8.197899999999999
    - type: nauc_map_at_100_diff1
      value: 54.3604
    - type: nauc_map_at_1000_max
      value: 17.838
    - type: nauc_map_at_1000_std
      value: -8.241800000000001
    - type: nauc_map_at_1000_diff1
      value: 54.3379
    - type: nauc_recall_at_1_max
      value: 11.5768
    - type: nauc_recall_at_1_std
      value: -16.317400000000003
    - type: nauc_recall_at_1_diff1
      value: 56.0748
    - type: nauc_recall_at_3_max
      value: 19.2218
    - type: nauc_recall_at_3_std
      value: -0.9331
    - type: nauc_recall_at_3_diff1
      value: 52.159299999999995
    - type: nauc_recall_at_5_max
      value: 23.1526
    - type: nauc_recall_at_5_std
      value: 18.569399999999998
    - type: nauc_recall_at_5_diff1
      value: 49.3007
    - type: nauc_recall_at_10_max
      value: 30.9861
    - type: nauc_recall_at_10_std
      value: 29.1945
    - type: nauc_recall_at_10_diff1
      value: 53.94520000000001
    - type: nauc_recall_at_20_max
      value: 45.5532
    - type: nauc_recall_at_20_std
      value: 30.500500000000002
    - type: nauc_recall_at_20_diff1
      value: 53.197799999999994
    - type: nauc_recall_at_100_max
      value: 69.0118
    - type: nauc_recall_at_100_std
      value: 42.4681
    - type: nauc_recall_at_100_diff1
      value: 73.61229999999999
    - type: nauc_recall_at_1000_max
      value: 73.9661
    - type: nauc_recall_at_1000_std
      value: 27.5085
    - type: nauc_recall_at_1000_diff1
      value: 75.1985
    - type: nauc_precision_at_1_max
      value: 15.3057
    - type: nauc_precision_at_1_std
      value: -20.3881
    - type: nauc_precision_at_1_diff1
      value: 51.7456
    - type: nauc_precision_at_3_max
      value: 24.9404
    - type: nauc_precision_at_3_std
      value: -5.6223
    - type: nauc_precision_at_3_diff1
      value: 33.2281
    - type: nauc_precision_at_5_max
      value: 23.1681
    - type: nauc_precision_at_5_std
      value: 3.7264
    - type: nauc_precision_at_5_diff1
      value: 13.463700000000001
    - type: nauc_precision_at_10_max
      value: 27.1828
    - type: nauc_precision_at_10_std
      value: 0.2287
    - type: nauc_precision_at_10_diff1
      value: 3.3236000000000003
    - type: nauc_precision_at_20_max
      value: 30.8431
    - type: nauc_precision_at_20_std
      value: -1.7745
    - type: nauc_precision_at_20_diff1
      value: -1.4821
    - type: nauc_precision_at_100_max
      value: 31.920399999999997
    - type: nauc_precision_at_100_std
      value: -9.9216
    - type: nauc_precision_at_100_diff1
      value: -12.0477
    - type: nauc_precision_at_1000_max
      value: 21.9173
    - type: nauc_precision_at_1000_std
      value: -20.7394
    - type: nauc_precision_at_1000_diff1
      value: -23.9441
    - type: nauc_mrr_at_1_max
      value: 15.3057
    - type: nauc_mrr_at_1_std
      value: -20.3881
    - type: nauc_mrr_at_1_diff1
      value: 51.7456
    - type: nauc_mrr_at_3_max
      value: 20.1871
    - type: nauc_mrr_at_3_std
      value: -15.1173
    - type: nauc_mrr_at_3_diff1
      value: 52.30089999999999
    - type: nauc_mrr_at_5_max
      value: 20.514599999999998
    - type: nauc_mrr_at_5_std
      value: -12.8977
    - type: nauc_mrr_at_5_diff1
      value: 52.350300000000004
    - type: nauc_mrr_at_10_max
      value: 20.4557
    - type: nauc_mrr_at_10_std
      value: -12.6083
    - type: nauc_mrr_at_10_diff1
      value: 52.766000000000005
    - type: nauc_mrr_at_20_max
      value: 20.7793
    - type: nauc_mrr_at_20_std
      value: -12.8431
    - type: nauc_mrr_at_20_diff1
      value: 52.6664
    - type: nauc_mrr_at_100_max
      value: 20.8067
    - type: nauc_mrr_at_100_std
      value: -12.9037
    - type: nauc_mrr_at_100_diff1
      value: 52.86729999999999
    - type: nauc_mrr_at_1000_max
      value: 20.793
    - type: nauc_mrr_at_1000_std
      value: -12.924900000000001
    - type: nauc_mrr_at_1000_diff1
      value: 52.8605
    - type: main_score
      value: 64.685
    task:
      type: Retrieval
  - dataset:
      config: zh
      name: MTEB MIRACLRetrieval (zh)
      revision: main
      split: dev
      type: miracl/mmteb-miracl
    metrics:
    - type: ndcg_at_1
      value: 41.985
    - type: ndcg_at_3
      value: 42.094
    - type: ndcg_at_5
      value: 44.273
    - type: ndcg_at_10
      value: 48.370000000000005
    - type: ndcg_at_20
      value: 51.595
    - type: ndcg_at_100
      value: 55.961000000000006
    - type: ndcg_at_1000
      value: 57.620000000000005
    - type: map_at_1
      value: 21.446
    - type: map_at_3
      value: 32.499
    - type: map_at_5
      value: 35.772
    - type: map_at_10
      value: 38.567
    - type: map_at_20
      value: 39.98
    - type: map_at_100
      value: 40.992
    - type: map_at_1000
      value: 41.119
    - type: recall_at_1
      value: 21.446
    - type: recall_at_3
      value: 40.377
    - type: recall_at_5
      value: 49.03
    - type: recall_at_10
      value: 59.695
    - type: recall_at_20
      value: 69.25200000000001
    - type: recall_at_100
      value: 87.388
    - type: recall_at_1000
      value: 96.833
    - type: precision_at_1
      value: 41.985
    - type: precision_at_3
      value: 29.008
    - type: precision_at_5
      value: 21.985
    - type: precision_at_10
      value: 14.097000000000001
    - type: precision_at_20
      value: 8.346
    - type: precision_at_100
      value: 2.155
    - type: precision_at_1000
      value: 0.243
    - type: mrr_at_1
      value: 41.984700000000004
    - type: mrr_at_3
      value: 52.078
    - type: mrr_at_5
      value: 53.5284
    - type: mrr_at_10
      value: 54.4979
    - type: mrr_at_20
      value: 54.9953
    - type: mrr_at_100
      value: 55.2428
    - type: mrr_at_1000
      value: 55.263
    - type: nauc_ndcg_at_1_max
      value: 41.7348
    - type: nauc_ndcg_at_1_std
      value: 23.8594
    - type: nauc_ndcg_at_1_diff1
      value: 31.156299999999998
    - type: nauc_ndcg_at_3_max
      value: 39.0525
    - type: nauc_ndcg_at_3_std
      value: 21.7916
    - type: nauc_ndcg_at_3_diff1
      value: 23.9925
    - type: nauc_ndcg_at_5_max
      value: 33.8643
    - type: nauc_ndcg_at_5_std
      value: 16.3399
    - type: nauc_ndcg_at_5_diff1
      value: 26.001
    - type: nauc_ndcg_at_10_max
      value: 35.3007
    - type: nauc_ndcg_at_10_std
      value: 19.127
    - type: nauc_ndcg_at_10_diff1
      value: 25.444899999999997
    - type: nauc_ndcg_at_20_max
      value: 37.6068
    - type: nauc_ndcg_at_20_std
      value: 23.0043
    - type: nauc_ndcg_at_20_diff1
      value: 23.7603
    - type: nauc_ndcg_at_100_max
      value: 40.4028
    - type: nauc_ndcg_at_100_std
      value: 25.0083
    - type: nauc_ndcg_at_100_diff1
      value: 23.491999999999997
    - type: nauc_ndcg_at_1000_max
      value: 39.8716
    - type: nauc_ndcg_at_1000_std
      value: 24.7264
    - type: nauc_ndcg_at_1000_diff1
      value: 24.6697
    - type: nauc_map_at_1_max
      value: 25.7275
    - type: nauc_map_at_1_std
      value: 7.7392
    - type: nauc_map_at_1_diff1
      value: 36.5897
    - type: nauc_map_at_3_max
      value: 32.2774
    - type: nauc_map_at_3_std
      value: 12.2275
    - type: nauc_map_at_3_diff1
      value: 28.8092
    - type: nauc_map_at_5_max
      value: 31.183899999999998
    - type: nauc_map_at_5_std
      value: 12.1811
    - type: nauc_map_at_5_diff1
      value: 28.532400000000003
    - type: nauc_map_at_10_max
      value: 33.4812
    - type: nauc_map_at_10_std
      value: 15.6339
    - type: nauc_map_at_10_diff1
      value: 27.695999999999998
    - type: nauc_map_at_20_max
      value: 34.855999999999995
    - type: nauc_map_at_20_std
      value: 17.8001
    - type: nauc_map_at_20_diff1
      value: 26.3975
    - type: nauc_map_at_100_max
      value: 35.8497
    - type: nauc_map_at_100_std
      value: 18.688
    - type: nauc_map_at_100_diff1
      value: 26.177899999999998
    - type: nauc_map_at_1000_max
      value: 35.8459
    - type: nauc_map_at_1000_std
      value: 18.7007
    - type: nauc_map_at_1000_diff1
      value: 26.257200000000005
    - type: nauc_recall_at_1_max
      value: 25.7275
    - type: nauc_recall_at_1_std
      value: 7.7392
    - type: nauc_recall_at_1_diff1
      value: 36.5897
    - type: nauc_recall_at_3_max
      value: 27.052100000000003
    - type: nauc_recall_at_3_std
      value: 9.632100000000001
    - type: nauc_recall_at_3_diff1
      value: 21.557399999999998
    - type: nauc_recall_at_5_max
      value: 21.0442
    - type: nauc_recall_at_5_std
      value: 5.7371
    - type: nauc_recall_at_5_diff1
      value: 20.653399999999998
    - type: nauc_recall_at_10_max
      value: 23.794
    - type: nauc_recall_at_10_std
      value: 12.2208
    - type: nauc_recall_at_10_diff1
      value: 17.305899999999998
    - type: nauc_recall_at_20_max
      value: 27.5932
    - type: nauc_recall_at_20_std
      value: 21.4346
    - type: nauc_recall_at_20_diff1
      value: 12.7064
    - type: nauc_recall_at_100_max
      value: 41.801300000000005
    - type: nauc_recall_at_100_std
      value: 36.4593
    - type: nauc_recall_at_100_diff1
      value: 5.7783
    - type: nauc_recall_at_1000_max
      value: 45.8507
    - type: nauc_recall_at_1000_std
      value: 66.6031
    - type: nauc_recall_at_1000_diff1
      value: 25.4961
    - type: nauc_precision_at_1_max
      value: 41.7348
    - type: nauc_precision_at_1_std
      value: 23.8594
    - type: nauc_precision_at_1_diff1
      value: 31.156299999999998
    - type: nauc_precision_at_3_max
      value: 43.336999999999996
    - type: nauc_precision_at_3_std
      value: 29.3989
    - type: nauc_precision_at_3_diff1
      value: 6.0378
    - type: nauc_precision_at_5_max
      value: 33.3518
    - type: nauc_precision_at_5_std
      value: 25.115199999999998
    - type: nauc_precision_at_5_diff1
      value: 3.9284
    - type: nauc_precision_at_10_max
      value: 33.466699999999996
    - type: nauc_precision_at_10_std
      value: 31.710300000000004
    - type: nauc_precision_at_10_diff1
      value: -2.0225
    - type: nauc_precision_at_20_max
      value: 33.651199999999996
    - type: nauc_precision_at_20_std
      value: 37.601600000000005
    - type: nauc_precision_at_20_diff1
      value: -9.591
    - type: nauc_precision_at_100_max
      value: 28.992
    - type: nauc_precision_at_100_std
      value: 33.631499999999996
    - type: nauc_precision_at_100_diff1
      value: -13.5546
    - type: nauc_precision_at_1000_max
      value: 20.091
    - type: nauc_precision_at_1000_std
      value: 26.9179
    - type: nauc_precision_at_1000_diff1
      value: -12.1766
    - type: nauc_mrr_at_1_max
      value: 41.7348
    - type: nauc_mrr_at_1_std
      value: 23.8594
    - type: nauc_mrr_at_1_diff1
      value: 31.156299999999998
    - type: nauc_mrr_at_3_max
      value: 43.2795
    - type: nauc_mrr_at_3_std
      value: 26.991500000000002
    - type: nauc_mrr_at_3_diff1
      value: 25.8376
    - type: nauc_mrr_at_5_max
      value: 42.1564
    - type: nauc_mrr_at_5_std
      value: 25.923299999999998
    - type: nauc_mrr_at_5_diff1
      value: 26.770500000000002
    - type: nauc_mrr_at_10_max
      value: 42.054
    - type: nauc_mrr_at_10_std
      value: 26.1554
    - type: nauc_mrr_at_10_diff1
      value: 26.4021
    - type: nauc_mrr_at_20_max
      value: 42.3932
    - type: nauc_mrr_at_20_std
      value: 26.5486
    - type: nauc_mrr_at_20_diff1
      value: 26.616400000000002
    - type: nauc_mrr_at_100_max
      value: 42.4887
    - type: nauc_mrr_at_100_std
      value: 26.4708
    - type: nauc_mrr_at_100_diff1
      value: 26.671899999999997
    - type: nauc_mrr_at_1000_max
      value: 42.478500000000004
    - type: nauc_mrr_at_1000_std
      value: 26.4606
    - type: nauc_mrr_at_1000_diff1
      value: 26.6946
    - type: main_score
      value: 48.370000000000005
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB MSMARCO (default)
      revision: c5a29a104738b98a9e76336939199e264163d4a0
      split: dev
      type: mteb/msmarco
    metrics:
    - type: ndcg_at_1
      value: 13.653
    - type: ndcg_at_3
      value: 21.836
    - type: ndcg_at_5
      value: 25.014999999999997
    - type: ndcg_at_10
      value: 28.319
    - type: ndcg_at_20
      value: 30.818
    - type: ndcg_at_100
      value: 34.527
    - type: ndcg_at_1000
      value: 36.702
    - type: map_at_1
      value: 13.313
    - type: map_at_3
      value: 19.615
    - type: map_at_5
      value: 21.389
    - type: map_at_10
      value: 22.768
    - type: map_at_20
      value: 23.465
    - type: map_at_100
      value: 23.976
    - type: map_at_1000
      value: 24.058
    - type: recall_at_1
      value: 13.313
    - type: recall_at_3
      value: 27.839999999999996
    - type: recall_at_5
      value: 35.481
    - type: recall_at_10
      value: 45.559
    - type: recall_at_20
      value: 55.301
    - type: recall_at_100
      value: 75.11
    - type: recall_at_1000
      value: 92.052
    - type: precision_at_1
      value: 13.653
    - type: precision_at_3
      value: 9.565
    - type: precision_at_5
      value: 7.338
    - type: precision_at_10
      value: 4.726
    - type: precision_at_20
      value: 2.8819999999999997
    - type: precision_at_100
      value: 0.79
    - type: precision_at_1000
      value: 0.098
    - type: mrr_at_1
      value: 13.653299999999998
    - type: mrr_at_3
      value: 20.0573
    - type: mrr_at_5
      value: 21.8295
    - type: mrr_at_10
      value: 23.1997
    - type: mrr_at_20
      value: 23.8785
    - type: mrr_at_100
      value: 24.3729
    - type: mrr_at_1000
      value: 24.448600000000003
    - type: nauc_ndcg_at_1_max
      value: 0.364
    - type: nauc_ndcg_at_1_std
      value: -12.840399999999999
    - type: nauc_ndcg_at_1_diff1
      value: 29.834699999999998
    - type: nauc_ndcg_at_3_max
      value: 1.9428
    - type: nauc_ndcg_at_3_std
      value: -13.696
    - type: nauc_ndcg_at_3_diff1
      value: 24.9774
    - type: nauc_ndcg_at_5_max
      value: 2.5951
    - type: nauc_ndcg_at_5_std
      value: -13.2667
    - type: nauc_ndcg_at_5_diff1
      value: 24.7581
    - type: nauc_ndcg_at_10_max
      value: 3.0274
    - type: nauc_ndcg_at_10_std
      value: -11.790799999999999
    - type: nauc_ndcg_at_10_diff1
      value: 23.9473
    - type: nauc_ndcg_at_20_max
      value: 3.5682
    - type: nauc_ndcg_at_20_std
      value: -10.132299999999999
    - type: nauc_ndcg_at_20_diff1
      value: 23.744100000000003
    - type: nauc_ndcg_at_100_max
      value: 5.1290000000000004
    - type: nauc_ndcg_at_100_std
      value: -6.8011
    - type: nauc_ndcg_at_100_diff1
      value: 23.6972
    - type: nauc_ndcg_at_1000_max
      value: 5.1967
    - type: nauc_ndcg_at_1000_std
      value: -7.396700000000001
    - type: nauc_ndcg_at_1000_diff1
      value: 24.1353
    - type: nauc_map_at_1_max
      value: 0.35200000000000004
    - type: nauc_map_at_1_std
      value: -12.8008
    - type: nauc_map_at_1_diff1
      value: 30.121199999999998
    - type: nauc_map_at_3_max
      value: 1.6415
    - type: nauc_map_at_3_std
      value: -13.5187
    - type: nauc_map_at_3_diff1
      value: 25.9894
    - type: nauc_map_at_5_max
      value: 2.0264
    - type: nauc_map_at_5_std
      value: -13.281
    - type: nauc_map_at_5_diff1
      value: 25.849
    - type: nauc_map_at_10_max
      value: 2.1982
    - type: nauc_map_at_10_std
      value: -12.6435
    - type: nauc_map_at_10_diff1
      value: 25.477100000000004
    - type: nauc_map_at_20_max
      value: 2.3562
    - type: nauc_map_at_20_std
      value: -12.1675
    - type: nauc_map_at_20_diff1
      value: 25.4162
    - type: nauc_map_at_100_max
      value: 2.5839999999999996
    - type: nauc_map_at_100_std
      value: -11.7018
    - type: nauc_map_at_100_diff1
      value: 25.4093
    - type: nauc_map_at_1000_max
      value: 2.5871999999999997
    - type: nauc_map_at_1000_std
      value: -11.7103
    - type: nauc_map_at_1000_diff1
      value: 25.424999999999997
    - type: nauc_recall_at_1_max
      value: 0.35200000000000004
    - type: nauc_recall_at_1_std
      value: -12.8008
    - type: nauc_recall_at_1_diff1
      value: 30.121199999999998
    - type: nauc_recall_at_3_max
      value: 2.6834000000000002
    - type: nauc_recall_at_3_std
      value: -14.0991
    - type: nauc_recall_at_3_diff1
      value: 22.6158
    - type: nauc_recall_at_5_max
      value: 3.9472
    - type: nauc_recall_at_5_std
      value: -13.167499999999999
    - type: nauc_recall_at_5_diff1
      value: 22.2686
    - type: nauc_recall_at_10_max
      value: 4.9908
    - type: nauc_recall_at_10_std
      value: -9.4435
    - type: nauc_recall_at_10_diff1
      value: 20.185200000000002
    - type: nauc_recall_at_20_max
      value: 6.880999999999999
    - type: nauc_recall_at_20_std
      value: -3.7041999999999997
    - type: nauc_recall_at_20_diff1
      value: 19.2889
    - type: nauc_recall_at_100_max
      value: 18.0012
    - type: nauc_recall_at_100_std
      value: 20.404600000000002
    - type: nauc_recall_at_100_diff1
      value: 17.1382
    - type: nauc_recall_at_1000_max
      value: 41.3456
    - type: nauc_recall_at_1000_std
      value: 50.3786
    - type: nauc_recall_at_1000_diff1
      value: 17.2713
    - type: nauc_precision_at_1_max
      value: 0.364
    - type: nauc_precision_at_1_std
      value: -12.840399999999999
    - type: nauc_precision_at_1_diff1
      value: 29.834699999999998
    - type: nauc_precision_at_3_max
      value: 2.7525
    - type: nauc_precision_at_3_std
      value: -13.992099999999999
    - type: nauc_precision_at_3_diff1
      value: 22.4985
    - type: nauc_precision_at_5_max
      value: 4.0076
    - type: nauc_precision_at_5_std
      value: -13.011800000000001
    - type: nauc_precision_at_5_diff1
      value: 21.9577
    - type: nauc_precision_at_10_max
      value: 5.3558
    - type: nauc_precision_at_10_std
      value: -8.8703
    - type: nauc_precision_at_10_diff1
      value: 19.5594
    - type: nauc_precision_at_20_max
      value: 7.764500000000001
    - type: nauc_precision_at_20_std
      value: -2.5067
    - type: nauc_precision_at_20_diff1
      value: 17.766199999999998
    - type: nauc_precision_at_100_max
      value: 17.8184
    - type: nauc_precision_at_100_std
      value: 20.153
    - type: nauc_precision_at_100_diff1
      value: 13.255500000000001
    - type: nauc_precision_at_1000_max
      value: 26.7508
    - type: nauc_precision_at_1000_std
      value: 31.494299999999996
    - type: nauc_precision_at_1000_diff1
      value: 5.8916
    - type: nauc_mrr_at_1_max
      value: 0.364
    - type: nauc_mrr_at_1_std
      value: -12.840399999999999
    - type: nauc_mrr_at_1_diff1
      value: 29.834699999999998
    - type: nauc_mrr_at_3_max
      value: 1.5876000000000001
    - type: nauc_mrr_at_3_std
      value: -13.4944
    - type: nauc_mrr_at_3_diff1
      value: 25.894099999999998
    - type: nauc_mrr_at_5_max
      value: 1.9839
    - type: nauc_mrr_at_5_std
      value: -13.1955
    - type: nauc_mrr_at_5_diff1
      value: 25.695899999999998
    - type: nauc_mrr_at_10_max
      value: 2.2034000000000002
    - type: nauc_mrr_at_10_std
      value: -12.504499999999998
    - type: nauc_mrr_at_10_diff1
      value: 25.3497
    - type: nauc_mrr_at_20_max
      value: 2.334
    - type: nauc_mrr_at_20_std
      value: -12.0259
    - type: nauc_mrr_at_20_diff1
      value: 25.3055
    - type: nauc_mrr_at_100_max
      value: 2.5492999999999997
    - type: nauc_mrr_at_100_std
      value: -11.6039
    - type: nauc_mrr_at_100_diff1
      value: 25.298
    - type: nauc_mrr_at_1000_max
      value: 2.5439
    - type: nauc_mrr_at_1000_std
      value: -11.6219
    - type: nauc_mrr_at_1000_diff1
      value: 25.312099999999997
    - type: main_score
      value: 28.319
    task:
      type: Retrieval
  - dataset:
      config: en
      name: MTEB MTOPDomainClassification (en)
      revision: d80d48c1eb48d3562165c59d59d0034df9fff0bf
      split: test
      type: mteb/mtop_domain
    metrics:
    - type: accuracy
      value: 88.9193
    - type: f1
      value: 88.6731
    - type: f1_weighted
      value: 88.8695
    - type: main_score
      value: 88.9193
    task:
      type: Classification
  - dataset:
      config: en
      name: MTEB MTOPIntentClassification (en)
      revision: ae001d0e6b1228650b7bd1c2c65fb50ad11a8aba
      split: test
      type: mteb/mtop_intent
    metrics:
    - type: accuracy
      value: 57.6448
    - type: f1
      value: 38.9997
    - type: f1_weighted
      value: 60.377
    - type: main_score
      value: 57.6448
    task:
      type: Classification
  - dataset:
      config: en
      name: MTEB MassiveIntentClassification (en)
      revision: 4672e20407010da34463acc759c162ca9734bca6
      split: test
      type: mteb/amazon_massive_intent
    metrics:
    - type: accuracy
      value: 62.518499999999996
    - type: f1
      value: 59.2963
    - type: f1_weighted
      value: 61.365700000000004
    - type: main_score
      value: 62.518499999999996
    task:
      type: Classification
  - dataset:
      config: en
      name: MTEB MassiveScenarioClassification (en)
      revision: fad2c6e8459f9e1c45d9315f4953d921437d70f8
      split: test
      type: mteb/amazon_massive_scenario
    metrics:
    - type: accuracy
      value: 69.36449999999999
    - type: f1
      value: 67.56259999999999
    - type: f1_weighted
      value: 68.9987
    - type: main_score
      value: 69.36449999999999
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB MedrxivClusteringP2P (default)
      revision: e7a26af6f3ae46b30dde8737f02c07b1505bcc73
      split: test
      type: mteb/medrxiv-clustering-p2p
    metrics:
    - type: v_measure
      value: 31.3521
    - type: v_measure_std
      value: 1.3192000000000002
    - type: main_score
      value: 31.3521
    task:
      type: Clustering
  - dataset:
      config: default
      name: MTEB MedrxivClusteringS2S (default)
      revision: 35191c8c0dca72d8ff3efcd72aa802307d469663
      split: test
      type: mteb/medrxiv-clustering-s2s
    metrics:
    - type: v_measure
      value: 28.020899999999997
    - type: v_measure_std
      value: 1.3569
    - type: main_score
      value: 28.020899999999997
    task:
      type: Clustering
  - dataset:
      config: default
      name: MTEB MindSmallReranking (default)
      revision: 59042f120c80e8afa9cdbb224f67076cec0fc9a7
      split: test
      type: mteb/mind_small
    metrics:
    - type: map
      value: 30.3048
    - type: mrr
      value: 31.326500000000003
    - type: nAUC_map_max
      value: -19.322300000000002
    - type: nAUC_map_std
      value: -4.424
    - type: nAUC_map_diff1
      value: 13.645299999999999
    - type: nAUC_mrr_max
      value: -13.5457
    - type: nAUC_mrr_std
      value: -2.0976000000000004
    - type: nAUC_mrr_diff1
      value: 12.965499999999999
    - type: main_score
      value: 30.3048
    task:
      type: Reranking
  - dataset:
      config: default
      name: MTEB NFCorpus (default)
      revision: ec0fa4fe99da2ff19ca1214b7966684033a58814
      split: test
      type: mteb/nfcorpus
    metrics:
    - type: ndcg_at_1
      value: 36.997
    - type: ndcg_at_3
      value: 32.279
    - type: ndcg_at_5
      value: 30.232
    - type: ndcg_at_10
      value: 26.991
    - type: ndcg_at_20
      value: 25.223000000000003
    - type: ndcg_at_100
      value: 24.953
    - type: ndcg_at_1000
      value: 33.881
    - type: map_at_1
      value: 4.2139999999999995
    - type: map_at_3
      value: 7.013999999999999
    - type: map_at_5
      value: 8.189
    - type: map_at_10
      value: 9.468
    - type: map_at_20
      value: 10.441
    - type: map_at_100
      value: 11.729000000000001
    - type: map_at_1000
      value: 12.920000000000002
    - type: recall_at_1
      value: 4.2139999999999995
    - type: recall_at_3
      value: 7.981000000000001
    - type: recall_at_5
      value: 10.306
    - type: recall_at_10
      value: 13.053999999999998
    - type: recall_at_20
      value: 16.499
    - type: recall_at_100
      value: 25.501
    - type: recall_at_1000
      value: 57.103
    - type: precision_at_1
      value: 38.39
    - type: precision_at_3
      value: 30.237000000000002
    - type: precision_at_5
      value: 26.006
    - type: precision_at_10
      value: 19.567
    - type: precision_at_20
      value: 14.613000000000001
    - type: precision_at_100
      value: 6.393
    - type: precision_at_1000
      value: 1.9
    - type: mrr_at_1
      value: 38.6997
    - type: mrr_at_3
      value: 45.0464
    - type: mrr_at_5
      value: 46.3622
    - type: mrr_at_10
      value: 46.9177
    - type: mrr_at_20
      value: 47.4995
    - type: mrr_at_100
      value: 47.7284
    - type: mrr_at_1000
      value: 47.7892
    - type: nauc_ndcg_at_1_max
      value: 30.8996
    - type: nauc_ndcg_at_1_std
      value: 18.2721
    - type: nauc_ndcg_at_1_diff1
      value: 34.836600000000004
    - type: nauc_ndcg_at_3_max
      value: 35.3352
    - type: nauc_ndcg_at_3_std
      value: 22.345699999999997
    - type: nauc_ndcg_at_3_diff1
      value: 29.5163
    - type: nauc_ndcg_at_5_max
      value: 36.8152
    - type: nauc_ndcg_at_5_std
      value: 25.799899999999997
    - type: nauc_ndcg_at_5_diff1
      value: 28.1756
    - type: nauc_ndcg_at_10_max
      value: 37.752599999999994
    - type: nauc_ndcg_at_10_std
      value: 28.2564
    - type: nauc_ndcg_at_10_diff1
      value: 25.9405
    - type: nauc_ndcg_at_20_max
      value: 36.0517
    - type: nauc_ndcg_at_20_std
      value: 29.4238
    - type: nauc_ndcg_at_20_diff1
      value: 23.8385
    - type: nauc_ndcg_at_100_max
      value: 39.027499999999996
    - type: nauc_ndcg_at_100_std
      value: 30.0156
    - type: nauc_ndcg_at_100_diff1
      value: 23.3814
    - type: nauc_ndcg_at_1000_max
      value: 43.9552
    - type: nauc_ndcg_at_1000_std
      value: 36.7709
    - type: nauc_ndcg_at_1000_diff1
      value: 23.2691
    - type: nauc_map_at_1_max
      value: 13.7444
    - type: nauc_map_at_1_std
      value: -3.6901
    - type: nauc_map_at_1_diff1
      value: 44.304700000000004
    - type: nauc_map_at_3_max
      value: 18.061
    - type: nauc_map_at_3_std
      value: -0.8826
    - type: nauc_map_at_3_diff1
      value: 34.1935
    - type: nauc_map_at_5_max
      value: 20.4082
    - type: nauc_map_at_5_std
      value: 1.6634
    - type: nauc_map_at_5_diff1
      value: 30.903999999999996
    - type: nauc_map_at_10_max
      value: 25.414900000000003
    - type: nauc_map_at_10_std
      value: 6.704899999999999
    - type: nauc_map_at_10_diff1
      value: 27.5783
    - type: nauc_map_at_20_max
      value: 27.746199999999998
    - type: nauc_map_at_20_std
      value: 10.5171
    - type: nauc_map_at_20_diff1
      value: 26.3814
    - type: nauc_map_at_100_max
      value: 29.7035
    - type: nauc_map_at_100_std
      value: 16.173000000000002
    - type: nauc_map_at_100_diff1
      value: 25.2415
    - type: nauc_map_at_1000_max
      value: 29.8974
    - type: nauc_map_at_1000_std
      value: 19.7694
    - type: nauc_map_at_1000_diff1
      value: 24.1468
    - type: nauc_recall_at_1_max
      value: 13.7444
    - type: nauc_recall_at_1_std
      value: -3.6901
    - type: nauc_recall_at_1_diff1
      value: 44.304700000000004
    - type: nauc_recall_at_3_max
      value: 18.4883
    - type: nauc_recall_at_3_std
      value: -0.9726999999999999
    - type: nauc_recall_at_3_diff1
      value: 29.502499999999998
    - type: nauc_recall_at_5_max
      value: 20.3422
    - type: nauc_recall_at_5_std
      value: 2.8535
    - type: nauc_recall_at_5_diff1
      value: 23.688100000000002
    - type: nauc_recall_at_10_max
      value: 26.8137
    - type: nauc_recall_at_10_std
      value: 6.3345
    - type: nauc_recall_at_10_diff1
      value: 19.5952
    - type: nauc_recall_at_20_max
      value: 25.4056
    - type: nauc_recall_at_20_std
      value: 8.8684
    - type: nauc_recall_at_20_diff1
      value: 16.9286
    - type: nauc_recall_at_100_max
      value: 29.1932
    - type: nauc_recall_at_100_std
      value: 19.6664
    - type: nauc_recall_at_100_diff1
      value: 14.8893
    - type: nauc_recall_at_1000_max
      value: 23.0622
    - type: nauc_recall_at_1000_std
      value: 25.8533
    - type: nauc_recall_at_1000_diff1
      value: 10.0844
    - type: nauc_precision_at_1_max
      value: 32.948699999999995
    - type: nauc_precision_at_1_std
      value: 19.2494
    - type: nauc_precision_at_1_diff1
      value: 33.955200000000005
    - type: nauc_precision_at_3_max
      value: 39.4863
    - type: nauc_precision_at_3_std
      value: 27.7083
    - type: nauc_precision_at_3_diff1
      value: 22.4854
    - type: nauc_precision_at_5_max
      value: 40.1376
    - type: nauc_precision_at_5_std
      value: 33.4658
    - type: nauc_precision_at_5_diff1
      value: 18.108
    - type: nauc_precision_at_10_max
      value: 39.333200000000005
    - type: nauc_precision_at_10_std
      value: 39.949600000000004
    - type: nauc_precision_at_10_diff1
      value: 11.7183
    - type: nauc_precision_at_20_max
      value: 32.0094
    - type: nauc_precision_at_20_std
      value: 45.1815
    - type: nauc_precision_at_20_diff1
      value: 7.2424
    - type: nauc_precision_at_100_max
      value: 18.073
    - type: nauc_precision_at_100_std
      value: 46.7008
    - type: nauc_precision_at_100_diff1
      value: -0.6927
    - type: nauc_precision_at_1000_max
      value: 2.9552
    - type: nauc_precision_at_1000_std
      value: 32.691199999999995
    - type: nauc_precision_at_1000_diff1
      value: -4.3427
    - type: nauc_mrr_at_1_max
      value: 32.7952
    - type: nauc_mrr_at_1_std
      value: 20.716
    - type: nauc_mrr_at_1_diff1
      value: 33.047
    - type: nauc_mrr_at_3_max
      value: 39.5698
    - type: nauc_mrr_at_3_std
      value: 25.674200000000003
    - type: nauc_mrr_at_3_diff1
      value: 31.7916
    - type: nauc_mrr_at_5_max
      value: 40.7711
    - type: nauc_mrr_at_5_std
      value: 27.2756
    - type: nauc_mrr_at_5_diff1
      value: 31.5432
    - type: nauc_mrr_at_10_max
      value: 41.033500000000004
    - type: nauc_mrr_at_10_std
      value: 27.364500000000003
    - type: nauc_mrr_at_10_diff1
      value: 31.394899999999996
    - type: nauc_mrr_at_20_max
      value: 40.9665
    - type: nauc_mrr_at_20_std
      value: 27.5866
    - type: nauc_mrr_at_20_diff1
      value: 31.6835
    - type: nauc_mrr_at_100_max
      value: 40.9471
    - type: nauc_mrr_at_100_std
      value: 27.643
    - type: nauc_mrr_at_100_diff1
      value: 31.553900000000002
    - type: nauc_mrr_at_1000_max
      value: 40.9207
    - type: nauc_mrr_at_1000_std
      value: 27.6206
    - type: nauc_mrr_at_1000_diff1
      value: 31.5596
    - type: main_score
      value: 26.991
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB NQ (default)
      revision: b774495ed302d8c44a3a7ea25c90dbce03968f31
      split: test
      type: mteb/nq
    metrics:
    - type: ndcg_at_1
      value: 32.937
    - type: ndcg_at_3
      value: 42.939
    - type: ndcg_at_5
      value: 47.044000000000004
    - type: ndcg_at_10
      value: 50.893
    - type: ndcg_at_20
      value: 53.093
    - type: ndcg_at_100
      value: 55.369
    - type: ndcg_at_1000
      value: 56.285
    - type: map_at_1
      value: 29.087000000000003
    - type: map_at_3
      value: 39.263
    - type: map_at_5
      value: 41.708
    - type: map_at_10
      value: 43.471
    - type: map_at_20
      value: 44.155
    - type: map_at_100
      value: 44.528
    - type: map_at_1000
      value: 44.568999999999996
    - type: recall_at_1
      value: 29.087000000000003
    - type: recall_at_3
      value: 50.451
    - type: recall_at_5
      value: 59.946
    - type: recall_at_10
      value: 71.109
    - type: recall_at_20
      value: 79.26299999999999
    - type: recall_at_100
      value: 90.51
    - type: recall_at_1000
      value: 97.277
    - type: precision_at_1
      value: 32.937
    - type: precision_at_3
      value: 19.602
    - type: precision_at_5
      value: 14.113999999999999
    - type: precision_at_10
      value: 8.462
    - type: precision_at_20
      value: 4.758
    - type: precision_at_100
      value: 1.0999999999999999
    - type: precision_at_1000
      value: 0.11800000000000001
    - type: mrr_at_1
      value: 32.9374
    - type: mrr_at_3
      value: 42.3957
    - type: mrr_at_5
      value: 44.5148
    - type: mrr_at_10
      value: 45.9459
    - type: mrr_at_20
      value: 46.4559
    - type: mrr_at_100
      value: 46.7367
    - type: mrr_at_1000
      value: 46.765
    - type: nauc_ndcg_at_1_max
      value: 24.0105
    - type: nauc_ndcg_at_1_std
      value: -1.5957
    - type: nauc_ndcg_at_1_diff1
      value: 33.1575
    - type: nauc_ndcg_at_3_max
      value: 26.388
    - type: nauc_ndcg_at_3_std
      value: -1.6223
    - type: nauc_ndcg_at_3_diff1
      value: 29.1908
    - type: nauc_ndcg_at_5_max
      value: 28.188800000000004
    - type: nauc_ndcg_at_5_std
      value: -0.3491
    - type: nauc_ndcg_at_5_diff1
      value: 28.287499999999998
    - type: nauc_ndcg_at_10_max
      value: 29.768800000000002
    - type: nauc_ndcg_at_10_std
      value: 2.093
    - type: nauc_ndcg_at_10_diff1
      value: 28.257700000000003
    - type: nauc_ndcg_at_20_max
      value: 30.8687
    - type: nauc_ndcg_at_20_std
      value: 3.4320000000000004
    - type: nauc_ndcg_at_20_diff1
      value: 28.220699999999997
    - type: nauc_ndcg_at_100_max
      value: 30.692199999999996
    - type: nauc_ndcg_at_100_std
      value: 4.0889
    - type: nauc_ndcg_at_100_diff1
      value: 28.468
    - type: nauc_ndcg_at_1000_max
      value: 29.9378
    - type: nauc_ndcg_at_1000_std
      value: 3.1003
    - type: nauc_ndcg_at_1000_diff1
      value: 28.8642
    - type: nauc_map_at_1_max
      value: 21.948999999999998
    - type: nauc_map_at_1_std
      value: -3.4299000000000004
    - type: nauc_map_at_1_diff1
      value: 33.5905
    - type: nauc_map_at_3_max
      value: 25.600299999999997
    - type: nauc_map_at_3_std
      value: -2.2762000000000002
    - type: nauc_map_at_3_diff1
      value: 30.235
    - type: nauc_map_at_5_max
      value: 26.6859
    - type: nauc_map_at_5_std
      value: -1.4717
    - type: nauc_map_at_5_diff1
      value: 29.6397
    - type: nauc_map_at_10_max
      value: 27.3731
    - type: nauc_map_at_10_std
      value: -0.4928
    - type: nauc_map_at_10_diff1
      value: 29.7079
    - type: nauc_map_at_20_max
      value: 27.668799999999997
    - type: nauc_map_at_20_std
      value: -0.0964
    - type: nauc_map_at_20_diff1
      value: 29.6945
    - type: nauc_map_at_100_max
      value: 27.675
    - type: nauc_map_at_100_std
      value: 0.0414
    - type: nauc_map_at_100_diff1
      value: 29.709000000000003
    - type: nauc_map_at_1000_max
      value: 27.647
    - type: nauc_map_at_1000_std
      value: 0.0063999999999999994
    - type: nauc_map_at_1000_diff1
      value: 29.724099999999996
    - type: nauc_recall_at_1_max
      value: 21.948999999999998
    - type: nauc_recall_at_1_std
      value: -3.4299000000000004
    - type: nauc_recall_at_1_diff1
      value: 33.5905
    - type: nauc_recall_at_3_max
      value: 27.2388
    - type: nauc_recall_at_3_std
      value: -1.4857
    - type: nauc_recall_at_3_diff1
      value: 25.991500000000002
    - type: nauc_recall_at_5_max
      value: 31.4282
    - type: nauc_recall_at_5_std
      value: 1.2066000000000001
    - type: nauc_recall_at_5_diff1
      value: 23.5681
    - type: nauc_recall_at_10_max
      value: 37.4517
    - type: nauc_recall_at_10_std
      value: 10.1238
    - type: nauc_recall_at_10_diff1
      value: 22.2133
    - type: nauc_recall_at_20_max
      value: 46.4783
    - type: nauc_recall_at_20_std
      value: 19.8515
    - type: nauc_recall_at_20_diff1
      value: 20.6028
    - type: nauc_recall_at_100_max
      value: 58.7011
    - type: nauc_recall_at_100_std
      value: 43.6264
    - type: nauc_recall_at_100_diff1
      value: 18.3446
    - type: nauc_recall_at_1000_max
      value: 74.3733
    - type: nauc_recall_at_1000_std
      value: 67.4933
    - type: nauc_recall_at_1000_diff1
      value: 25.375500000000002
    - type: nauc_precision_at_1_max
      value: 24.0105
    - type: nauc_precision_at_1_std
      value: -1.5957
    - type: nauc_precision_at_1_diff1
      value: 33.1575
    - type: nauc_precision_at_3_max
      value: 27.406399999999998
    - type: nauc_precision_at_3_std
      value: 0.9842
    - type: nauc_precision_at_3_diff1
      value: 21.793599999999998
    - type: nauc_precision_at_5_max
      value: 29.145
    - type: nauc_precision_at_5_std
      value: 4.6154
    - type: nauc_precision_at_5_diff1
      value: 16.8
    - type: nauc_precision_at_10_max
      value: 29.480600000000003
    - type: nauc_precision_at_10_std
      value: 12.286900000000001
    - type: nauc_precision_at_10_diff1
      value: 11.7686
    - type: nauc_precision_at_20_max
      value: 29.791
    - type: nauc_precision_at_20_std
      value: 18.0686
    - type: nauc_precision_at_20_diff1
      value: 7.2818
    - type: nauc_precision_at_100_max
      value: 22.605900000000002
    - type: nauc_precision_at_100_std
      value: 22.4834
    - type: nauc_precision_at_100_diff1
      value: -0.1403
    - type: nauc_precision_at_1000_max
      value: 11.637599999999999
    - type: nauc_precision_at_1000_std
      value: 16.299
    - type: nauc_precision_at_1000_diff1
      value: -4.3052
    - type: nauc_mrr_at_1_max
      value: 24.0105
    - type: nauc_mrr_at_1_std
      value: -1.5957
    - type: nauc_mrr_at_1_diff1
      value: 33.1575
    - type: nauc_mrr_at_3_max
      value: 26.375
    - type: nauc_mrr_at_3_std
      value: -0.2874
    - type: nauc_mrr_at_3_diff1
      value: 29.8333
    - type: nauc_mrr_at_5_max
      value: 27.2656
    - type: nauc_mrr_at_5_std
      value: 0.37
    - type: nauc_mrr_at_5_diff1
      value: 29.461900000000004
    - type: nauc_mrr_at_10_max
      value: 27.7811
    - type: nauc_mrr_at_10_std
      value: 1.2722
    - type: nauc_mrr_at_10_diff1
      value: 29.456
    - type: nauc_mrr_at_20_max
      value: 27.9525
    - type: nauc_mrr_at_20_std
      value: 1.4394
    - type: nauc_mrr_at_20_diff1
      value: 29.5184
    - type: nauc_mrr_at_100_max
      value: 27.887099999999997
    - type: nauc_mrr_at_100_std
      value: 1.4539
    - type: nauc_mrr_at_100_diff1
      value: 29.5789
    - type: nauc_mrr_at_1000_max
      value: 27.865499999999997
    - type: nauc_mrr_at_1000_std
      value: 1.4233
    - type: nauc_mrr_at_1000_diff1
      value: 29.5896
    - type: main_score
      value: 50.893
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB QuoraRetrieval (default)
      revision: e4e08e0b7dbe3c8700f0daef558ff32256715259
      split: test
      type: mteb/quora
    metrics:
    - type: ndcg_at_1
      value: 78.41
    - type: ndcg_at_3
      value: 82.614
    - type: ndcg_at_5
      value: 84.443
    - type: ndcg_at_10
      value: 85.845
    - type: ndcg_at_20
      value: 86.615
    - type: ndcg_at_100
      value: 87.313
    - type: ndcg_at_1000
      value: 87.492
    - type: map_at_1
      value: 68.092
    - type: map_at_3
      value: 78.604
    - type: map_at_5
      value: 80.527
    - type: map_at_10
      value: 81.639
    - type: map_at_20
      value: 82.07900000000001
    - type: map_at_100
      value: 82.314
    - type: map_at_1000
      value: 82.336
    - type: recall_at_1
      value: 68.092
    - type: recall_at_3
      value: 84.66900000000001
    - type: recall_at_5
      value: 89.751
    - type: recall_at_10
      value: 93.888
    - type: recall_at_20
      value: 96.389
    - type: recall_at_100
      value: 99.042
    - type: recall_at_1000
      value: 99.929
    - type: precision_at_1
      value: 78.41
    - type: precision_at_3
      value: 36.027
    - type: precision_at_5
      value: 23.844
    - type: precision_at_10
      value: 13.043
    - type: precision_at_20
      value: 6.946
    - type: precision_at_100
      value: 1.506
    - type: precision_at_1000
      value: 0.156
    - type: mrr_at_1
      value: 78.4
    - type: mrr_at_3
      value: 83.9867
    - type: mrr_at_5
      value: 84.7992
    - type: mrr_at_10
      value: 85.1577
    - type: mrr_at_20
      value: 85.2505
    - type: mrr_at_100
      value: 85.2855
    - type: mrr_at_1000
      value: 85.2877
    - type: nauc_ndcg_at_1_max
      value: 39.8081
    - type: nauc_ndcg_at_1_std
      value: -28.606399999999997
    - type: nauc_ndcg_at_1_diff1
      value: 75.9446
    - type: nauc_ndcg_at_3_max
      value: 37.7924
    - type: nauc_ndcg_at_3_std
      value: -33.5391
    - type: nauc_ndcg_at_3_diff1
      value: 73.3973
    - type: nauc_ndcg_at_5_max
      value: 38.047
    - type: nauc_ndcg_at_5_std
      value: -33.5943
    - type: nauc_ndcg_at_5_diff1
      value: 73.7645
    - type: nauc_ndcg_at_10_max
      value: 39.0948
    - type: nauc_ndcg_at_10_std
      value: -32.3805
    - type: nauc_ndcg_at_10_diff1
      value: 74.2689
    - type: nauc_ndcg_at_20_max
      value: 39.4193
    - type: nauc_ndcg_at_20_std
      value: -31.309900000000003
    - type: nauc_ndcg_at_20_diff1
      value: 74.2915
    - type: nauc_ndcg_at_100_max
      value: 39.6566
    - type: nauc_ndcg_at_100_std
      value: -30.3777
    - type: nauc_ndcg_at_100_diff1
      value: 74.2375
    - type: nauc_ndcg_at_1000_max
      value: 39.6656
    - type: nauc_ndcg_at_1000_std
      value: -30.2466
    - type: nauc_ndcg_at_1000_diff1
      value: 74.22609999999999
    - type: nauc_map_at_1_max
      value: 29.1625
    - type: nauc_map_at_1_std
      value: -31.4393
    - type: nauc_map_at_1_diff1
      value: 77.41
    - type: nauc_map_at_3_max
      value: 35.3371
    - type: nauc_map_at_3_std
      value: -35.2729
    - type: nauc_map_at_3_diff1
      value: 74.6367
    - type: nauc_map_at_5_max
      value: 36.600100000000005
    - type: nauc_map_at_5_std
      value: -34.9097
    - type: nauc_map_at_5_diff1
      value: 74.48479999999999
    - type: nauc_map_at_10_max
      value: 37.5994
    - type: nauc_map_at_10_std
      value: -33.702
    - type: nauc_map_at_10_diff1
      value: 74.4678
    - type: nauc_map_at_20_max
      value: 37.890299999999996
    - type: nauc_map_at_20_std
      value: -32.9179
    - type: nauc_map_at_20_diff1
      value: 74.3744
    - type: nauc_map_at_100_max
      value: 38.0205
    - type: nauc_map_at_100_std
      value: -32.4364
    - type: nauc_map_at_100_diff1
      value: 74.3232
    - type: nauc_map_at_1000_max
      value: 38.0296
    - type: nauc_map_at_1000_std
      value: -32.390600000000006
    - type: nauc_map_at_1000_diff1
      value: 74.323
    - type: nauc_recall_at_1_max
      value: 29.1625
    - type: nauc_recall_at_1_std
      value: -31.4393
    - type: nauc_recall_at_1_diff1
      value: 77.41
    - type: nauc_recall_at_3_max
      value: 32.2751
    - type: nauc_recall_at_3_std
      value: -39.215
    - type: nauc_recall_at_3_diff1
      value: 70.3264
    - type: nauc_recall_at_5_max
      value: 32.9445
    - type: nauc_recall_at_5_std
      value: -40.7042
    - type: nauc_recall_at_5_diff1
      value: 68.803
    - type: nauc_recall_at_10_max
      value: 36.6396
    - type: nauc_recall_at_10_std
      value: -37.5092
    - type: nauc_recall_at_10_diff1
      value: 68.8674
    - type: nauc_recall_at_20_max
      value: 38.8048
    - type: nauc_recall_at_20_std
      value: -31.1471
    - type: nauc_recall_at_20_diff1
      value: 69.5775
    - type: nauc_recall_at_100_max
      value: 42.9809
    - type: nauc_recall_at_100_std
      value: -18.932299999999998
    - type: nauc_recall_at_100_diff1
      value: 69.4688
    - type: nauc_recall_at_1000_max
      value: 67.836
    - type: nauc_recall_at_1000_std
      value: 38.124
    - type: nauc_recall_at_1000_diff1
      value: 71.4131
    - type: nauc_precision_at_1_max
      value: 39.8081
    - type: nauc_precision_at_1_std
      value: -28.606399999999997
    - type: nauc_precision_at_1_diff1
      value: 75.9446
    - type: nauc_precision_at_3_max
      value: 14.0877
    - type: nauc_precision_at_3_std
      value: 2.1809
    - type: nauc_precision_at_3_diff1
      value: -8.5037
    - type: nauc_precision_at_5_max
      value: 7.3131
    - type: nauc_precision_at_5_std
      value: 11.67
    - type: nauc_precision_at_5_diff1
      value: -23.663500000000003
    - type: nauc_precision_at_10_max
      value: 2.4924999999999997
    - type: nauc_precision_at_10_std
      value: 20.4298
    - type: nauc_precision_at_10_diff1
      value: -32.5249
    - type: nauc_precision_at_20_max
      value: -0.8340000000000001
    - type: nauc_precision_at_20_std
      value: 25.5814
    - type: nauc_precision_at_20_diff1
      value: -36.879
    - type: nauc_precision_at_100_max
      value: -4.2415
    - type: nauc_precision_at_100_std
      value: 30.588700000000003
    - type: nauc_precision_at_100_diff1
      value: -40.0441
    - type: nauc_precision_at_1000_max
      value: -5.7567
    - type: nauc_precision_at_1000_std
      value: 31.6137
    - type: nauc_precision_at_1000_diff1
      value: -40.8601
    - type: nauc_mrr_at_1_max
      value: 39.7059
    - type: nauc_mrr_at_1_std
      value: -28.6757
    - type: nauc_mrr_at_1_diff1
      value: 75.96730000000001
    - type: nauc_mrr_at_3_max
      value: 40.842
    - type: nauc_mrr_at_3_std
      value: -29.4321
    - type: nauc_mrr_at_3_diff1
      value: 74.588
    - type: nauc_mrr_at_5_max
      value: 40.8178
    - type: nauc_mrr_at_5_std
      value: -29.343700000000002
    - type: nauc_mrr_at_5_diff1
      value: 74.7965
    - type: nauc_mrr_at_10_max
      value: 40.9508
    - type: nauc_mrr_at_10_std
      value: -29.1159
    - type: nauc_mrr_at_10_diff1
      value: 74.9315
    - type: nauc_mrr_at_20_max
      value: 40.9157
    - type: nauc_mrr_at_20_std
      value: -29.040899999999997
    - type: nauc_mrr_at_20_diff1
      value: 74.9526
    - type: nauc_mrr_at_100_max
      value: 40.8672
    - type: nauc_mrr_at_100_std
      value: -29.0691
    - type: nauc_mrr_at_100_diff1
      value: 74.9558
    - type: nauc_mrr_at_1000_max
      value: 40.8655
    - type: nauc_mrr_at_1000_std
      value: -29.0682
    - type: nauc_mrr_at_1000_diff1
      value: 74.9558
    - type: main_score
      value: 85.845
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB RedditClustering (default)
      revision: 24640382cdbf8abc73003fb0fa6d111a705499eb
      split: test
      type: mteb/reddit-clustering
    metrics:
    - type: v_measure
      value: 43.7063
    - type: v_measure_std
      value: 4.7175
    - type: main_score
      value: 43.7063
    task:
      type: Clustering
  - dataset:
      config: default
      name: MTEB RedditClusteringP2P (default)
      revision: 385e3cb46b4cfa89021f56c4380204149d0efe33
      split: test
      type: mteb/reddit-clustering-p2p
    metrics:
    - type: v_measure
      value: 53.54
    - type: v_measure_std
      value: 11.809600000000001
    - type: main_score
      value: 53.54
    task:
      type: Clustering
  - dataset:
      config: default
      name: MTEB SCIDOCS (default)
      revision: f8c2fcf00f625baaa80f62ec5bd9e1fff3b8ae88
      split: test
      type: mteb/scidocs
    metrics:
    - type: ndcg_at_1
      value: 20.7
    - type: ndcg_at_3
      value: 16.518
    - type: ndcg_at_5
      value: 14.441
    - type: ndcg_at_10
      value: 17.380000000000003
    - type: ndcg_at_20
      value: 19.991
    - type: ndcg_at_100
      value: 24.747
    - type: ndcg_at_1000
      value: 30.296
    - type: map_at_1
      value: 4.208
    - type: map_at_3
      value: 7.335
    - type: map_at_5
      value: 8.712
    - type: map_at_10
      value: 10.135
    - type: map_at_20
      value: 11.068999999999999
    - type: map_at_100
      value: 11.951
    - type: map_at_1000
      value: 12.245000000000001
    - type: recall_at_1
      value: 4.208
    - type: recall_at_3
      value: 9.303
    - type: recall_at_5
      value: 12.797
    - type: recall_at_10
      value: 18.195
    - type: recall_at_20
      value: 24.318
    - type: recall_at_100
      value: 39.803
    - type: recall_at_1000
      value: 66.99000000000001
    - type: precision_at_1
      value: 20.7
    - type: precision_at_3
      value: 15.299999999999999
    - type: precision_at_5
      value: 12.6
    - type: precision_at_10
      value: 8.959999999999999
    - type: precision_at_20
      value: 5.985
    - type: precision_at_100
      value: 1.959
    - type: precision_at_1000
      value: 0.33
    - type: mrr_at_1
      value: 20.7
    - type: mrr_at_3
      value: 27.3833
    - type: mrr_at_5
      value: 29.168300000000002
    - type: mrr_at_10
      value: 30.598799999999997
    - type: mrr_at_20
      value: 31.217
    - type: mrr_at_100
      value: 31.688499999999998
    - type: mrr_at_1000
      value: 31.763599999999997
    - type: nauc_ndcg_at_1_max
      value: 21.5429
    - type: nauc_ndcg_at_1_std
      value: 4.718
    - type: nauc_ndcg_at_1_diff1
      value: 19.3827
    - type: nauc_ndcg_at_3_max
      value: 32.1126
    - type: nauc_ndcg_at_3_std
      value: 9.314400000000001
    - type: nauc_ndcg_at_3_diff1
      value: 20.0916
    - type: nauc_ndcg_at_5_max
      value: 31.849800000000002
    - type: nauc_ndcg_at_5_std
      value: 10.8725
    - type: nauc_ndcg_at_5_diff1
      value: 17.7008
    - type: nauc_ndcg_at_10_max
      value: 33.366600000000005
    - type: nauc_ndcg_at_10_std
      value: 13.625399999999999
    - type: nauc_ndcg_at_10_diff1
      value: 16.375
    - type: nauc_ndcg_at_20_max
      value: 34.6677
    - type: nauc_ndcg_at_20_std
      value: 15.3872
    - type: nauc_ndcg_at_20_diff1
      value: 16.8414
    - type: nauc_ndcg_at_100_max
      value: 37.2778
    - type: nauc_ndcg_at_100_std
      value: 20.4858
    - type: nauc_ndcg_at_100_diff1
      value: 16.7288
    - type: nauc_ndcg_at_1000_max
      value: 36.601
    - type: nauc_ndcg_at_1000_std
      value: 22.312199999999997
    - type: nauc_ndcg_at_1000_diff1
      value: 16.2465
    - type: nauc_map_at_1_max
      value: 21.2741
    - type: nauc_map_at_1_std
      value: 4.7143
    - type: nauc_map_at_1_diff1
      value: 18.8297
    - type: nauc_map_at_3_max
      value: 31.727800000000002
    - type: nauc_map_at_3_std
      value: 6.8229999999999995
    - type: nauc_map_at_3_diff1
      value: 20.4232
    - type: nauc_map_at_5_max
      value: 32.3588
    - type: nauc_map_at_5_std
      value: 8.565100000000001
    - type: nauc_map_at_5_diff1
      value: 18.9604
    - type: nauc_map_at_10_max
      value: 33.6113
    - type: nauc_map_at_10_std
      value: 10.743
    - type: nauc_map_at_10_diff1
      value: 17.6337
    - type: nauc_map_at_20_max
      value: 34.7121
    - type: nauc_map_at_20_std
      value: 11.9819
    - type: nauc_map_at_20_diff1
      value: 18.0342
    - type: nauc_map_at_100_max
      value: 35.6623
    - type: nauc_map_at_100_std
      value: 13.7498
    - type: nauc_map_at_100_diff1
      value: 17.985300000000002
    - type: nauc_map_at_1000_max
      value: 35.663
    - type: nauc_map_at_1000_std
      value: 14.050099999999999
    - type: nauc_map_at_1000_diff1
      value: 17.9269
    - type: nauc_recall_at_1_max
      value: 21.2741
    - type: nauc_recall_at_1_std
      value: 4.7143
    - type: nauc_recall_at_1_diff1
      value: 18.8297
    - type: nauc_recall_at_3_max
      value: 36.2097
    - type: nauc_recall_at_3_std
      value: 11.6014
    - type: nauc_recall_at_3_diff1
      value: 20.0114
    - type: nauc_recall_at_5_max
      value: 33.7826
    - type: nauc_recall_at_5_std
      value: 13.603000000000002
    - type: nauc_recall_at_5_diff1
      value: 15.4714
    - type: nauc_recall_at_10_max
      value: 34.105999999999995
    - type: nauc_recall_at_10_std
      value: 17.4216
    - type: nauc_recall_at_10_diff1
      value: 12.3734
    - type: nauc_recall_at_20_max
      value: 35.2885
    - type: nauc_recall_at_20_std
      value: 19.9833
    - type: nauc_recall_at_20_diff1
      value: 13.2726
    - type: nauc_recall_at_100_max
      value: 37.3523
    - type: nauc_recall_at_100_std
      value: 30.2207
    - type: nauc_recall_at_100_diff1
      value: 11.437700000000001
    - type: nauc_recall_at_1000_max
      value: 29.276000000000003
    - type: nauc_recall_at_1000_std
      value: 35.906
    - type: nauc_recall_at_1000_diff1
      value: 6.281499999999999
    - type: nauc_precision_at_1_max
      value: 21.5429
    - type: nauc_precision_at_1_std
      value: 4.718
    - type: nauc_precision_at_1_diff1
      value: 19.3827
    - type: nauc_precision_at_3_max
      value: 36.609
    - type: nauc_precision_at_3_std
      value: 11.863700000000001
    - type: nauc_precision_at_3_diff1
      value: 20.4735
    - type: nauc_precision_at_5_max
      value: 34.3364
    - type: nauc_precision_at_5_std
      value: 13.7951
    - type: nauc_precision_at_5_diff1
      value: 15.992700000000001
    - type: nauc_precision_at_10_max
      value: 34.6556
    - type: nauc_precision_at_10_std
      value: 17.4014
    - type: nauc_precision_at_10_diff1
      value: 12.981699999999998
    - type: nauc_precision_at_20_max
      value: 35.836
    - type: nauc_precision_at_20_std
      value: 20.1892
    - type: nauc_precision_at_20_diff1
      value: 13.6046
    - type: nauc_precision_at_100_max
      value: 37.9677
    - type: nauc_precision_at_100_std
      value: 30.3386
    - type: nauc_precision_at_100_diff1
      value: 11.8783
    - type: nauc_precision_at_1000_max
      value: 29.795700000000004
    - type: nauc_precision_at_1000_std
      value: 35.4107
    - type: nauc_precision_at_1000_diff1
      value: 6.6238
    - type: nauc_mrr_at_1_max
      value: 21.5429
    - type: nauc_mrr_at_1_std
      value: 4.718
    - type: nauc_mrr_at_1_diff1
      value: 19.3827
    - type: nauc_mrr_at_3_max
      value: 27.635900000000003
    - type: nauc_mrr_at_3_std
      value: 9.5593
    - type: nauc_mrr_at_3_diff1
      value: 18.4684
    - type: nauc_mrr_at_5_max
      value: 26.682499999999997
    - type: nauc_mrr_at_5_std
      value: 9.7369
    - type: nauc_mrr_at_5_diff1
      value: 17.4317
    - type: nauc_mrr_at_10_max
      value: 27.032400000000003
    - type: nauc_mrr_at_10_std
      value: 10.4662
    - type: nauc_mrr_at_10_diff1
      value: 17.3209
    - type: nauc_mrr_at_20_max
      value: 27.1752
    - type: nauc_mrr_at_20_std
      value: 10.5774
    - type: nauc_mrr_at_20_diff1
      value: 17.3725
    - type: nauc_mrr_at_100_max
      value: 27.228099999999998
    - type: nauc_mrr_at_100_std
      value: 10.710600000000001
    - type: nauc_mrr_at_100_diff1
      value: 17.4312
    - type: nauc_mrr_at_1000_max
      value: 27.172600000000003
    - type: nauc_mrr_at_1000_std
      value: 10.6434
    - type: nauc_mrr_at_1000_diff1
      value: 17.421400000000002
    - type: main_score
      value: 17.380000000000003
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB SICK-R (default)
      revision: 20a6d6f312dd54037fe07a32d58e5e168867909d
      split: test
      type: mteb/sickr-sts
    metrics:
    - type: pearson
      value: 75.385
    - type: spearman
      value: 68.46560000000001
    - type: cosine_pearson
      value: 75.385
    - type: cosine_spearman
      value: 68.46560000000001
    - type: manhattan_pearson
      value: 72.53309999999999
    - type: manhattan_spearman
      value: 68.79899999999999
    - type: euclidean_pearson
      value: 72.5239
    - type: euclidean_spearman
      value: 68.46560000000001
    - type: main_score
      value: 68.46560000000001
    task:
      type: STS
  - dataset:
      config: default
      name: MTEB STS12 (default)
      revision: a0d554a64d88156834ff5ae9920b964011b16384
      split: test
      type: mteb/sts12-sts
    metrics:
    - type: pearson
      value: 80.9088
    - type: spearman
      value: 74.7362
    - type: cosine_pearson
      value: 80.9088
    - type: cosine_spearman
      value: 74.7362
    - type: manhattan_pearson
      value: 77.3291
    - type: manhattan_spearman
      value: 75.0881
    - type: euclidean_pearson
      value: 77.5321
    - type: euclidean_spearman
      value: 74.7347
    - type: main_score
      value: 74.7362
    task:
      type: STS
  - dataset:
      config: default
      name: MTEB STS13 (default)
      revision: 7e90230a92c190f1bf69ae9002b8cea547a64cca
      split: test
      type: mteb/sts13-sts
    metrics:
    - type: pearson
      value: 74.6345
    - type: spearman
      value: 75.63990000000001
    - type: cosine_pearson
      value: 74.6345
    - type: cosine_spearman
      value: 75.63990000000001
    - type: manhattan_pearson
      value: 75.5227
    - type: manhattan_spearman
      value: 75.5136
    - type: euclidean_pearson
      value: 75.5744
    - type: euclidean_spearman
      value: 75.63990000000001
    - type: main_score
      value: 75.63990000000001
    task:
      type: STS
  - dataset:
      config: default
      name: MTEB STS14 (default)
      revision: 6031580fec1f6af667f0bd2da0a551cf4f0b2375
      split: test
      type: mteb/sts14-sts
    metrics:
    - type: pearson
      value: 76.66629999999999
    - type: spearman
      value: 73.1976
    - type: cosine_pearson
      value: 76.66629999999999
    - type: cosine_spearman
      value: 73.1976
    - type: manhattan_pearson
      value: 75.0827
    - type: manhattan_spearman
      value: 73.2472
    - type: euclidean_pearson
      value: 75.2873
    - type: euclidean_spearman
      value: 73.1976
    - type: main_score
      value: 73.1976
    task:
      type: STS
  - dataset:
      config: default
      name: MTEB STS15 (default)
      revision: ae752c7c21bf194d8b67fd573edf7ae58183cbe3
      split: test
      type: mteb/sts15-sts
    metrics:
    - type: pearson
      value: 84.33810000000001
    - type: spearman
      value: 85.0551
    - type: cosine_pearson
      value: 84.33810000000001
    - type: cosine_spearman
      value: 85.0551
    - type: manhattan_pearson
      value: 84.5984
    - type: manhattan_spearman
      value: 85.1619
    - type: euclidean_pearson
      value: 84.529
    - type: euclidean_spearman
      value: 85.0551
    - type: main_score
      value: 85.0551
    task:
      type: STS
  - dataset:
      config: default
      name: MTEB STS16 (default)
      revision: 4d8694f8f0e0100860b497b999b3dbed754a0513
      split: test
      type: mteb/sts16-sts
    metrics:
    - type: pearson
      value: 79.5933
    - type: spearman
      value: 81.11120000000001
    - type: cosine_pearson
      value: 79.5933
    - type: cosine_spearman
      value: 81.11120000000001
    - type: manhattan_pearson
      value: 80.136
    - type: manhattan_spearman
      value: 80.8767
    - type: euclidean_pearson
      value: 80.3305
    - type: euclidean_spearman
      value: 81.11120000000001
    - type: main_score
      value: 81.11120000000001
    task:
      type: STS
  - dataset:
      config: en-tr
      name: MTEB STS17 (en-tr)
      revision: faeb762787bd10488a50c8b5be4a3b82e411949c
      split: test
      type: mteb/sts17-crosslingual-sts
    metrics:
    - type: pearson
      value: 38.2331
    - type: spearman
      value: 33.7346
    - type: cosine_pearson
      value: 38.2331
    - type: cosine_spearman
      value: 33.7346
    - type: manhattan_pearson
      value: 40.986
    - type: manhattan_spearman
      value: 34.253099999999996
    - type: euclidean_pearson
      value: 40.2622
    - type: euclidean_spearman
      value: 33.7346
    - type: main_score
      value: 33.7346
    task:
      type: STS
  - dataset:
      config: fr-en
      name: MTEB STS17 (fr-en)
      revision: faeb762787bd10488a50c8b5be4a3b82e411949c
      split: test
      type: mteb/sts17-crosslingual-sts
    metrics:
    - type: pearson
      value: 73.5477
    - type: spearman
      value: 74.1745
    - type: cosine_pearson
      value: 73.5477
    - type: cosine_spearman
      value: 74.1745
    - type: manhattan_pearson
      value: 74.84920000000001
    - type: manhattan_spearman
      value: 74.49900000000001
    - type: euclidean_pearson
      value: 74.14
    - type: euclidean_spearman
      value: 74.1745
    - type: main_score
      value: 74.1745
    task:
      type: STS
  - dataset:
      config: it-en
      name: MTEB STS17 (it-en)
      revision: faeb762787bd10488a50c8b5be4a3b82e411949c
      split: test
      type: mteb/sts17-crosslingual-sts
    metrics:
    - type: pearson
      value: 66.7169
    - type: spearman
      value: 66.864
    - type: cosine_pearson
      value: 66.7169
    - type: cosine_spearman
      value: 66.864
    - type: manhattan_pearson
      value: 67.39359999999999
    - type: manhattan_spearman
      value: 67.0985
    - type: euclidean_pearson
      value: 66.9389
    - type: euclidean_spearman
      value: 66.864
    - type: main_score
      value: 66.864
    task:
      type: STS
  - dataset:
      config: es-en
      name: MTEB STS17 (es-en)
      revision: faeb762787bd10488a50c8b5be4a3b82e411949c
      split: test
      type: mteb/sts17-crosslingual-sts
    metrics:
    - type: pearson
      value: 70.5101
    - type: spearman
      value: 70.05930000000001
    - type: cosine_pearson
      value: 70.5101
    - type: cosine_spearman
      value: 70.05930000000001
    - type: manhattan_pearson
      value: 72.7524
    - type: manhattan_spearman
      value: 71.2907
    - type: euclidean_pearson
      value: 71.148
    - type: euclidean_spearman
      value: 70.05930000000001
    - type: main_score
      value: 70.05930000000001
    task:
      type: STS
  - dataset:
      config: nl-en
      name: MTEB STS17 (nl-en)
      revision: faeb762787bd10488a50c8b5be4a3b82e411949c
      split: test
      type: mteb/sts17-crosslingual-sts
    metrics:
    - type: pearson
      value: 68.3089
    - type: spearman
      value: 68.4899
    - type: cosine_pearson
      value: 68.3089
    - type: cosine_spearman
      value: 68.4899
    - type: manhattan_pearson
      value: 69.3956
    - type: manhattan_spearman
      value: 68.9486
    - type: euclidean_pearson
      value: 68.8059
    - type: euclidean_spearman
      value: 68.4899
    - type: main_score
      value: 68.4899
    task:
      type: STS
  - dataset:
      config: en-en
      name: MTEB STS17 (en-en)
      revision: faeb762787bd10488a50c8b5be4a3b82e411949c
      split: test
      type: mteb/sts17-crosslingual-sts
    metrics:
    - type: pearson
      value: 78.28739999999999
    - type: spearman
      value: 78.6966
    - type: cosine_pearson
      value: 78.28739999999999
    - type: cosine_spearman
      value: 78.6966
    - type: manhattan_pearson
      value: 78.97070000000001
    - type: manhattan_spearman
      value: 79.1907
    - type: euclidean_pearson
      value: 78.36070000000001
    - type: euclidean_spearman
      value: 78.6966
    - type: main_score
      value: 78.6966
    task:
      type: STS
  - dataset:
      config: en-ar
      name: MTEB STS17 (en-ar)
      revision: faeb762787bd10488a50c8b5be4a3b82e411949c
      split: test
      type: mteb/sts17-crosslingual-sts
    metrics:
    - type: pearson
      value: 59.611999999999995
    - type: spearman
      value: 59.9288
    - type: cosine_pearson
      value: 59.611999999999995
    - type: cosine_spearman
      value: 59.9288
    - type: manhattan_pearson
      value: 60.3549
    - type: manhattan_spearman
      value: 59.696099999999994
    - type: euclidean_pearson
      value: 60.4754
    - type: euclidean_spearman
      value: 59.9288
    - type: main_score
      value: 59.9288
    task:
      type: STS
  - dataset:
      config: en-de
      name: MTEB STS17 (en-de)
      revision: faeb762787bd10488a50c8b5be4a3b82e411949c
      split: test
      type: mteb/sts17-crosslingual-sts
    metrics:
    - type: pearson
      value: 70.6341
    - type: spearman
      value: 69.9775
    - type: cosine_pearson
      value: 70.6341
    - type: cosine_spearman
      value: 69.9775
    - type: manhattan_pearson
      value: 72.7788
    - type: manhattan_spearman
      value: 71.2033
    - type: euclidean_pearson
      value: 71.5822
    - type: euclidean_spearman
      value: 69.9775
    - type: main_score
      value: 69.9775
    task:
      type: STS
  - dataset:
      config: en
      name: MTEB STS22 (en)
      revision: de9d86b3b84231dc21f76c7b7af1f28e2f57f6e3
      split: test
      type: mteb/sts22-crosslingual-sts
    metrics:
    - type: pearson
      value: 67.2703
    - type: spearman
      value: 67.58229999999999
    - type: cosine_pearson
      value: 67.2703
    - type: cosine_spearman
      value: 67.58229999999999
    - type: manhattan_pearson
      value: 68.1768
    - type: manhattan_spearman
      value: 67.6479
    - type: euclidean_pearson
      value: 67.9708
    - type: euclidean_spearman
      value: 67.58229999999999
    - type: main_score
      value: 67.58229999999999
    task:
      type: STS
  - dataset:
      config: de-en
      name: MTEB STS22 (de-en)
      revision: de9d86b3b84231dc21f76c7b7af1f28e2f57f6e3
      split: test
      type: mteb/sts22-crosslingual-sts
    metrics:
    - type: pearson
      value: 62.2109
    - type: spearman
      value: 56.2314
    - type: cosine_pearson
      value: 62.2109
    - type: cosine_spearman
      value: 56.2314
    - type: manhattan_pearson
      value: 65.9455
    - type: manhattan_spearman
      value: 56.5496
    - type: euclidean_pearson
      value: 65.30550000000001
    - type: euclidean_spearman
      value: 56.2314
    - type: main_score
      value: 56.2314
    task:
      type: STS
  - dataset:
      config: pl-en
      name: MTEB STS22 (pl-en)
      revision: de9d86b3b84231dc21f76c7b7af1f28e2f57f6e3
      split: test
      type: mteb/sts22-crosslingual-sts
    metrics:
    - type: pearson
      value: 74.4185
    - type: spearman
      value: 72.82119999999999
    - type: cosine_pearson
      value: 74.4185
    - type: cosine_spearman
      value: 72.82119999999999
    - type: manhattan_pearson
      value: 75.6921
    - type: manhattan_spearman
      value: 72.3315
    - type: euclidean_pearson
      value: 75.1725
    - type: euclidean_spearman
      value: 72.82119999999999
    - type: main_score
      value: 72.82119999999999
    task:
      type: STS
  - dataset:
      config: es-en
      name: MTEB STS22 (es-en)
      revision: de9d86b3b84231dc21f76c7b7af1f28e2f57f6e3
      split: test
      type: mteb/sts22-crosslingual-sts
    metrics:
    - type: pearson
      value: 78.6974
    - type: spearman
      value: 79.5845
    - type: cosine_pearson
      value: 78.6974
    - type: cosine_spearman
      value: 79.5845
    - type: manhattan_pearson
      value: 79.6724
    - type: manhattan_spearman
      value: 79.668
    - type: euclidean_pearson
      value: 79.69380000000001
    - type: euclidean_spearman
      value: 79.5845
    - type: main_score
      value: 79.5845
    task:
      type: STS
  - dataset:
      config: zh-en
      name: MTEB STS22 (zh-en)
      revision: de9d86b3b84231dc21f76c7b7af1f28e2f57f6e3
      split: test
      type: mteb/sts22-crosslingual-sts
    metrics:
    - type: pearson
      value: 71.3237
    - type: spearman
      value: 71.5178
    - type: cosine_pearson
      value: 71.3237
    - type: cosine_spearman
      value: 71.5178
    - type: manhattan_pearson
      value: 73.3948
    - type: manhattan_spearman
      value: 71.5607
    - type: euclidean_pearson
      value: 73.1403
    - type: euclidean_spearman
      value: 71.5178
    - type: main_score
      value: 71.5178
    task:
      type: STS
  - dataset:
      config: default
      name: MTEB STSBenchmark (default)
      revision: b0fddb56ed78048fa8b90373c8a3cfc37b684831
      split: test
      type: mteb/stsbenchmark-sts
    metrics:
    - type: pearson
      value: 75.5279
    - type: spearman
      value: 76.9844
    - type: cosine_pearson
      value: 75.5279
    - type: cosine_spearman
      value: 76.9844
    - type: manhattan_pearson
      value: 77.5474
    - type: manhattan_spearman
      value: 77.4353
    - type: euclidean_pearson
      value: 77.1612
    - type: euclidean_spearman
      value: 76.9844
    - type: main_score
      value: 76.9844
    task:
      type: STS
  - dataset:
      config: default
      name: MTEB SciDocsRR (default)
      revision: d3c5e1fc0b855ab6097bf1cda04dd73947d7caab
      split: test
      type: mteb/scidocs-reranking
    metrics:
    - type: map
      value: 79.33109999999999
    - type: mrr
      value: 94.0725
    - type: nAUC_map_max
      value: 59.0089
    - type: nAUC_map_std
      value: 69.9131
    - type: nAUC_map_diff1
      value: 5.900600000000001
    - type: nAUC_mrr_max
      value: 84.5132
    - type: nAUC_mrr_std
      value: 77.767
    - type: nAUC_mrr_diff1
      value: 46.5557
    - type: main_score
      value: 79.33109999999999
    task:
      type: Reranking
  - dataset:
      config: default
      name: MTEB SciFact (default)
      revision: 0228b52cf27578f30900b9e5271d331663a030d7
      split: test
      type: mteb/scifact
    metrics:
    - type: ndcg_at_1
      value: 51.333
    - type: ndcg_at_3
      value: 57.781000000000006
    - type: ndcg_at_5
      value: 60.925
    - type: ndcg_at_10
      value: 63.254
    - type: ndcg_at_20
      value: 64.955
    - type: ndcg_at_100
      value: 66.155
    - type: ndcg_at_1000
      value: 67.193
    - type: map_at_1
      value: 48.428
    - type: map_at_3
      value: 55.145999999999994
    - type: map_at_5
      value: 57.055
    - type: map_at_10
      value: 58.17
    - type: map_at_20
      value: 58.723000000000006
    - type: map_at_100
      value: 58.901
    - type: map_at_1000
      value: 58.940000000000005
    - type: recall_at_1
      value: 48.428
    - type: recall_at_3
      value: 62.55
    - type: recall_at_5
      value: 70.367
    - type: recall_at_10
      value: 76.972
    - type: recall_at_20
      value: 83.317
    - type: recall_at_100
      value: 89.7
    - type: recall_at_1000
      value: 98.0
    - type: precision_at_1
      value: 51.333
    - type: precision_at_3
      value: 22.444
    - type: precision_at_5
      value: 15.4
    - type: precision_at_10
      value: 8.6
    - type: precision_at_20
      value: 4.717
    - type: precision_at_100
      value: 1.02
    - type: precision_at_1000
      value: 0.11100000000000002
    - type: mrr_at_1
      value: 51.3333
    - type: mrr_at_3
      value: 57.5556
    - type: mrr_at_5
      value: 59.255599999999994
    - type: mrr_at_10
      value: 60.104400000000005
    - type: mrr_at_20
      value: 60.4592
    - type: mrr_at_100
      value: 60.590999999999994
    - type: mrr_at_1000
      value: 60.622299999999996
    - type: nauc_ndcg_at_1_max
      value: 55.0684
    - type: nauc_ndcg_at_1_std
      value: 13.461200000000002
    - type: nauc_ndcg_at_1_diff1
      value: 67.4931
    - type: nauc_ndcg_at_3_max
      value: 54.1942
    - type: nauc_ndcg_at_3_std
      value: 11.029300000000001
    - type: nauc_ndcg_at_3_diff1
      value: 61.4423
    - type: nauc_ndcg_at_5_max
      value: 53.712199999999996
    - type: nauc_ndcg_at_5_std
      value: 11.0586
    - type: nauc_ndcg_at_5_diff1
      value: 59.3723
    - type: nauc_ndcg_at_10_max
      value: 55.2513
    - type: nauc_ndcg_at_10_std
      value: 13.413400000000001
    - type: nauc_ndcg_at_10_diff1
      value: 58.5176
    - type: nauc_ndcg_at_20_max
      value: 56.721900000000005
    - type: nauc_ndcg_at_20_std
      value: 14.9832
    - type: nauc_ndcg_at_20_diff1
      value: 59.1445
    - type: nauc_ndcg_at_100_max
      value: 56.5049
    - type: nauc_ndcg_at_100_std
      value: 15.021799999999999
    - type: nauc_ndcg_at_100_diff1
      value: 59.4117
    - type: nauc_ndcg_at_1000_max
      value: 56.0829
    - type: nauc_ndcg_at_1000_std
      value: 14.4429
    - type: nauc_ndcg_at_1000_diff1
      value: 60.45700000000001
    - type: nauc_map_at_1_max
      value: 50.901799999999994
    - type: nauc_map_at_1_std
      value: 6.0093
    - type: nauc_map_at_1_diff1
      value: 66.6214
    - type: nauc_map_at_3_max
      value: 52.684200000000004
    - type: nauc_map_at_3_std
      value: 7.9088
    - type: nauc_map_at_3_diff1
      value: 62.906600000000005
    - type: nauc_map_at_5_max
      value: 52.6187
    - type: nauc_map_at_5_std
      value: 8.2372
    - type: nauc_map_at_5_diff1
      value: 61.772000000000006
    - type: nauc_map_at_10_max
      value: 53.317899999999995
    - type: nauc_map_at_10_std
      value: 9.397
    - type: nauc_map_at_10_diff1
      value: 61.355599999999995
    - type: nauc_map_at_20_max
      value: 54.04259999999999
    - type: nauc_map_at_20_std
      value: 10.2201
    - type: nauc_map_at_20_diff1
      value: 61.684000000000005
    - type: nauc_map_at_100_max
      value: 54.0394
    - type: nauc_map_at_100_std
      value: 10.2894
    - type: nauc_map_at_100_diff1
      value: 61.7302
    - type: nauc_map_at_1000_max
      value: 54.024300000000004
    - type: nauc_map_at_1000_std
      value: 10.2881
    - type: nauc_map_at_1000_diff1
      value: 61.7661
    - type: nauc_recall_at_1_max
      value: 50.901799999999994
    - type: nauc_recall_at_1_std
      value: 6.0093
    - type: nauc_recall_at_1_diff1
      value: 66.6214
    - type: nauc_recall_at_3_max
      value: 52.8806
    - type: nauc_recall_at_3_std
      value: 10.7463
    - type: nauc_recall_at_3_diff1
      value: 55.5486
    - type: nauc_recall_at_5_max
      value: 52.277300000000004
    - type: nauc_recall_at_5_std
      value: 12.2395
    - type: nauc_recall_at_5_diff1
      value: 49.147800000000004
    - type: nauc_recall_at_10_max
      value: 57.403499999999994
    - type: nauc_recall_at_10_std
      value: 20.4581
    - type: nauc_recall_at_10_diff1
      value: 44.0595
    - type: nauc_recall_at_20_max
      value: 65.5378
    - type: nauc_recall_at_20_std
      value: 29.5288
    - type: nauc_recall_at_20_diff1
      value: 43.2217
    - type: nauc_recall_at_100_max
      value: 67.4941
    - type: nauc_recall_at_100_std
      value: 36.178399999999996
    - type: nauc_recall_at_100_diff1
      value: 39.3443
    - type: nauc_recall_at_1000_max
      value: 72.50229999999999
    - type: nauc_recall_at_1000_std
      value: 51.455
    - type: nauc_recall_at_1000_diff1
      value: 62.153800000000004
    - type: nauc_precision_at_1_max
      value: 55.0684
    - type: nauc_precision_at_1_std
      value: 13.461200000000002
    - type: nauc_precision_at_1_diff1
      value: 67.4931
    - type: nauc_precision_at_3_max
      value: 54.947599999999994
    - type: nauc_precision_at_3_std
      value: 23.1875
    - type: nauc_precision_at_3_diff1
      value: 51.166199999999996
    - type: nauc_precision_at_5_max
      value: 50.1483
    - type: nauc_precision_at_5_std
      value: 27.1119
    - type: nauc_precision_at_5_diff1
      value: 37.3846
    - type: nauc_precision_at_10_max
      value: 46.800799999999995
    - type: nauc_precision_at_10_std
      value: 37.737500000000004
    - type: nauc_precision_at_10_diff1
      value: 22.945999999999998
    - type: nauc_precision_at_20_max
      value: 43.980000000000004
    - type: nauc_precision_at_20_std
      value: 46.3352
    - type: nauc_precision_at_20_diff1
      value: 14.718300000000001
    - type: nauc_precision_at_100_max
      value: 34.8346
    - type: nauc_precision_at_100_std
      value: 49.0032
    - type: nauc_precision_at_100_diff1
      value: 4.7538
    - type: nauc_precision_at_1000_max
      value: 19.9994
    - type: nauc_precision_at_1000_std
      value: 51.132999999999996
    - type: nauc_precision_at_1000_diff1
      value: -6.5839
    - type: nauc_mrr_at_1_max
      value: 55.0684
    - type: nauc_mrr_at_1_std
      value: 13.461200000000002
    - type: nauc_mrr_at_1_diff1
      value: 67.4931
    - type: nauc_mrr_at_3_max
      value: 56.2153
    - type: nauc_mrr_at_3_std
      value: 15.4146
    - type: nauc_mrr_at_3_diff1
      value: 63.273199999999996
    - type: nauc_mrr_at_5_max
      value: 56.0011
    - type: nauc_mrr_at_5_std
      value: 15.7535
    - type: nauc_mrr_at_5_diff1
      value: 62.1466
    - type: nauc_mrr_at_10_max
      value: 56.643100000000004
    - type: nauc_mrr_at_10_std
      value: 16.354
    - type: nauc_mrr_at_10_diff1
      value: 62.0124
    - type: nauc_mrr_at_20_max
      value: 56.686800000000005
    - type: nauc_mrr_at_20_std
      value: 16.1984
    - type: nauc_mrr_at_20_diff1
      value: 62.095
    - type: nauc_mrr_at_100_max
      value: 56.6659
    - type: nauc_mrr_at_100_std
      value: 16.1601
    - type: nauc_mrr_at_100_diff1
      value: 62.157399999999996
    - type: nauc_mrr_at_1000_max
      value: 56.657599999999995
    - type: nauc_mrr_at_1000_std
      value: 16.1579
    - type: nauc_mrr_at_1000_diff1
      value: 62.195
    - type: main_score
      value: 63.254
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB SprintDuplicateQuestions (default)
      revision: d66bd1f72af766a5cc4b0ca5e00c162f89e8cc46
      split: test
      type: mteb/sprintduplicatequestions-pairclassification
    metrics:
    - type: similarity_accuracy
      value: 99.7465
    - type: similarity_accuracy_threshold
      value: 84.08489999999999
    - type: similarity_f1
      value: 86.9388
    - type: similarity_f1_threshold
      value: 84.08489999999999
    - type: similarity_precision
      value: 88.75
    - type: similarity_recall
      value: 85.2
    - type: similarity_ap
      value: 93.56139999999999
    - type: cosine_accuracy
      value: 99.7465
    - type: cosine_accuracy_threshold
      value: 84.08489999999999
    - type: cosine_f1
      value: 86.9388
    - type: cosine_f1_threshold
      value: 84.08489999999999
    - type: cosine_precision
      value: 88.75
    - type: cosine_recall
      value: 85.2
    - type: cosine_ap
      value: 93.56139999999999
    - type: manhattan_accuracy
      value: 99.7614
    - type: manhattan_accuracy_threshold
      value: 853.1299
    - type: manhattan_f1
      value: 87.7053
    - type: manhattan_f1_threshold
      value: 888.5799999999999
    - type: manhattan_precision
      value: 87.3142
    - type: manhattan_recall
      value: 88.1
    - type: manhattan_ap
      value: 94.0777
    - type: euclidean_accuracy
      value: 99.7465
    - type: euclidean_accuracy_threshold
      value: 56.4183
    - type: euclidean_f1
      value: 86.9388
    - type: euclidean_f1_threshold
      value: 56.4183
    - type: euclidean_precision
      value: 88.75
    - type: euclidean_recall
      value: 85.2
    - type: euclidean_ap
      value: 93.5613
    - type: dot_accuracy
      value: 99.7465
    - type: dot_accuracy_threshold
      value: 84.08489999999999
    - type: dot_f1
      value: 86.9388
    - type: dot_f1_threshold
      value: 84.08489999999999
    - type: dot_precision
      value: 88.75
    - type: dot_recall
      value: 85.2
    - type: dot_ap
      value: 93.56139999999999
    - type: max_accuracy
      value: 99.7614
    - type: max_f1
      value: 87.7053
    - type: max_precision
      value: 88.75
    - type: max_recall
      value: 88.1
    - type: max_ap
      value: 94.0777
    - type: main_score
      value: 94.0777
    task:
      type: PairClassification
  - dataset:
      config: default
      name: MTEB StackExchangeClustering (default)
      revision: 6cbc1f7b2bc0622f2e39d2c77fa502909748c259
      split: test
      type: mteb/stackexchange-clustering
    metrics:
    - type: v_measure
      value: 54.13980000000001
    - type: v_measure_std
      value: 5.5665
    - type: main_score
      value: 54.13980000000001
    task:
      type: Clustering
  - dataset:
      config: default
      name: MTEB StackExchangeClusteringP2P (default)
      revision: 815ca46b2622cec33ccafc3735d572c266efdb44
      split: test
      type: mteb/stackexchange-clustering-p2p
    metrics:
    - type: v_measure
      value: 32.6113
    - type: v_measure_std
      value: 1.6389999999999998
    - type: main_score
      value: 32.6113
    task:
      type: Clustering
  - dataset:
      config: default
      name: MTEB StackOverflowDupQuestions (default)
      revision: e185fbe320c72810689fc5848eb6114e1ef5ec69
      split: test
      type: mteb/stackoverflowdupquestions-reranking
    metrics:
    - type: map
      value: 50.813900000000004
    - type: mrr
      value: 51.702099999999994
    - type: nAUC_map_max
      value: 14.127600000000001
    - type: nAUC_map_std
      value: 8.6735
    - type: nAUC_map_diff1
      value: 36.4317
    - type: nAUC_mrr_max
      value: 15.504399999999999
    - type: nAUC_mrr_std
      value: 9.7053
    - type: nAUC_mrr_diff1
      value: 36.7021
    - type: main_score
      value: 50.813900000000004
    task:
      type: Reranking
  - dataset:
      config: default
      name: MTEB StackOverflowQA (default)
      revision: db8f169f3894c14a00251061f957b2063eef2bd5
      split: test
      type: CoIR-Retrieval/stackoverflow-qa
    metrics:
    - type: ndcg_at_1
      value: 54.26299999999999
    - type: ndcg_at_3
      value: 62.395
    - type: ndcg_at_5
      value: 64.603
    - type: ndcg_at_10
      value: 66.57600000000001
    - type: ndcg_at_20
      value: 68.089
    - type: ndcg_at_100
      value: 69.587
    - type: ndcg_at_1000
      value: 70.216
    - type: map_at_1
      value: 54.26299999999999
    - type: map_at_3
      value: 60.373
    - type: map_at_5
      value: 61.609
    - type: map_at_10
      value: 62.419999999999995
    - type: map_at_20
      value: 62.83800000000001
    - type: map_at_100
      value: 63.04
    - type: map_at_1000
      value: 63.063
    - type: recall_at_1
      value: 54.26299999999999
    - type: recall_at_3
      value: 68.255
    - type: recall_at_5
      value: 73.571
    - type: recall_at_10
      value: 79.689
    - type: recall_at_20
      value: 85.65700000000001
    - type: recall_at_100
      value: 93.781
    - type: recall_at_1000
      value: 98.79599999999999
    - type: precision_at_1
      value: 54.26299999999999
    - type: precision_at_3
      value: 22.752
    - type: precision_at_5
      value: 14.713999999999999
    - type: precision_at_10
      value: 7.968999999999999
    - type: precision_at_20
      value: 4.283
    - type: precision_at_100
      value: 0.938
    - type: precision_at_1000
      value: 0.099
    - type: mrr_at_1
      value: 54.2628
    - type: mrr_at_3
      value: 60.372800000000005
    - type: mrr_at_5
      value: 61.609
    - type: mrr_at_10
      value: 62.4202
    - type: mrr_at_20
      value: 62.83800000000001
    - type: mrr_at_100
      value: 63.0402
    - type: mrr_at_1000
      value: 63.06270000000001
    - type: nauc_ndcg_at_1_max
      value: 61.3558
    - type: nauc_ndcg_at_1_std
      value: -7.5783000000000005
    - type: nauc_ndcg_at_1_diff1
      value: 72.637
    - type: nauc_ndcg_at_3_max
      value: 59.621900000000004
    - type: nauc_ndcg_at_3_std
      value: -7.8752
    - type: nauc_ndcg_at_3_diff1
      value: 67.341
    - type: nauc_ndcg_at_5_max
      value: 59.32150000000001
    - type: nauc_ndcg_at_5_std
      value: -6.783500000000001
    - type: nauc_ndcg_at_5_diff1
      value: 66.3908
    - type: nauc_ndcg_at_10_max
      value: 58.8665
    - type: nauc_ndcg_at_10_std
      value: -6.8839999999999995
    - type: nauc_ndcg_at_10_diff1
      value: 65.5914
    - type: nauc_ndcg_at_20_max
      value: 59.071
    - type: nauc_ndcg_at_20_std
      value: -6.7216
    - type: nauc_ndcg_at_20_diff1
      value: 66.0076
    - type: nauc_ndcg_at_100_max
      value: 59.2928
    - type: nauc_ndcg_at_100_std
      value: -6.0869
    - type: nauc_ndcg_at_100_diff1
      value: 66.5509
    - type: nauc_ndcg_at_1000_max
      value: 59.551
    - type: nauc_ndcg_at_1000_std
      value: -6.3229
    - type: nauc_ndcg_at_1000_diff1
      value: 67.0501
    - type: nauc_map_at_1_max
      value: 61.3558
    - type: nauc_map_at_1_std
      value: -7.5783000000000005
    - type: nauc_map_at_1_diff1
      value: 72.637
    - type: nauc_map_at_3_max
      value: 60.0638
    - type: nauc_map_at_3_std
      value: -7.824599999999999
    - type: nauc_map_at_3_diff1
      value: 68.7255
    - type: nauc_map_at_5_max
      value: 59.9035
    - type: nauc_map_at_5_std
      value: -7.236199999999999
    - type: nauc_map_at_5_diff1
      value: 68.2474
    - type: nauc_map_at_10_max
      value: 59.73159999999999
    - type: nauc_map_at_10_std
      value: -7.3129
    - type: nauc_map_at_10_diff1
      value: 67.9742
    - type: nauc_map_at_20_max
      value: 59.799800000000005
    - type: nauc_map_at_20_std
      value: -7.2599
    - type: nauc_map_at_20_diff1
      value: 68.1128
    - type: nauc_map_at_100_max
      value: 59.8324
    - type: nauc_map_at_100_std
      value: -7.1589
    - type: nauc_map_at_100_diff1
      value: 68.1784
    - type: nauc_map_at_1000_max
      value: 59.845099999999995
    - type: nauc_map_at_1000_std
      value: -7.1592
    - type: nauc_map_at_1000_diff1
      value: 68.19770000000001
    - type: nauc_recall_at_1_max
      value: 61.3558
    - type: nauc_recall_at_1_std
      value: -7.5783000000000005
    - type: nauc_recall_at_1_diff1
      value: 72.637
    - type: nauc_recall_at_3_max
      value: 58.1732
    - type: nauc_recall_at_3_std
      value: -8.028599999999999
    - type: nauc_recall_at_3_diff1
      value: 62.7847
    - type: nauc_recall_at_5_max
      value: 57.1488
    - type: nauc_recall_at_5_std
      value: -4.9189
    - type: nauc_recall_at_5_diff1
      value: 59.392599999999995
    - type: nauc_recall_at_10_max
      value: 54.7384
    - type: nauc_recall_at_10_std
      value: -4.683
    - type: nauc_recall_at_10_diff1
      value: 54.317499999999995
    - type: nauc_recall_at_20_max
      value: 54.5659
    - type: nauc_recall_at_20_std
      value: -2.9657
    - type: nauc_recall_at_20_diff1
      value: 53.039899999999996
    - type: nauc_recall_at_100_max
      value: 53.5805
    - type: nauc_recall_at_100_std
      value: 12.822
    - type: nauc_recall_at_100_diff1
      value: 49.3168
    - type: nauc_recall_at_1000_max
      value: 64.52839999999999
    - type: nauc_recall_at_1000_std
      value: 44.954699999999995
    - type: nauc_recall_at_1000_diff1
      value: 51.3607
    - type: nauc_precision_at_1_max
      value: 61.3558
    - type: nauc_precision_at_1_std
      value: -7.5783000000000005
    - type: nauc_precision_at_1_diff1
      value: 72.637
    - type: nauc_precision_at_3_max
      value: 58.1732
    - type: nauc_precision_at_3_std
      value: -8.028599999999999
    - type: nauc_precision_at_3_diff1
      value: 62.7847
    - type: nauc_precision_at_5_max
      value: 57.1488
    - type: nauc_precision_at_5_std
      value: -4.9189
    - type: nauc_precision_at_5_diff1
      value: 59.392599999999995
    - type: nauc_precision_at_10_max
      value: 54.7384
    - type: nauc_precision_at_10_std
      value: -4.683
    - type: nauc_precision_at_10_diff1
      value: 54.317499999999995
    - type: nauc_precision_at_20_max
      value: 54.5659
    - type: nauc_precision_at_20_std
      value: -2.9657
    - type: nauc_precision_at_20_diff1
      value: 53.039899999999996
    - type: nauc_precision_at_100_max
      value: 53.5805
    - type: nauc_precision_at_100_std
      value: 12.822
    - type: nauc_precision_at_100_diff1
      value: 49.3168
    - type: nauc_precision_at_1000_max
      value: 64.52839999999999
    - type: nauc_precision_at_1000_std
      value: 44.954699999999995
    - type: nauc_precision_at_1000_diff1
      value: 51.3607
    - type: nauc_mrr_at_1_max
      value: 61.3558
    - type: nauc_mrr_at_1_std
      value: -7.5783000000000005
    - type: nauc_mrr_at_1_diff1
      value: 72.637
    - type: nauc_mrr_at_3_max
      value: 60.0638
    - type: nauc_mrr_at_3_std
      value: -7.824599999999999
    - type: nauc_mrr_at_3_diff1
      value: 68.7255
    - type: nauc_mrr_at_5_max
      value: 59.9035
    - type: nauc_mrr_at_5_std
      value: -7.236199999999999
    - type: nauc_mrr_at_5_diff1
      value: 68.2474
    - type: nauc_mrr_at_10_max
      value: 59.73159999999999
    - type: nauc_mrr_at_10_std
      value: -7.3129
    - type: nauc_mrr_at_10_diff1
      value: 67.9742
    - type: nauc_mrr_at_20_max
      value: 59.799800000000005
    - type: nauc_mrr_at_20_std
      value: -7.2599
    - type: nauc_mrr_at_20_diff1
      value: 68.1128
    - type: nauc_mrr_at_100_max
      value: 59.8324
    - type: nauc_mrr_at_100_std
      value: -7.1589
    - type: nauc_mrr_at_100_diff1
      value: 68.1784
    - type: nauc_mrr_at_1000_max
      value: 59.845099999999995
    - type: nauc_mrr_at_1000_std
      value: -7.1592
    - type: nauc_mrr_at_1000_diff1
      value: 68.19770000000001
    - type: main_score
      value: 66.57600000000001
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB SummEval (default)
      revision: cda12ad7615edc362dbf25a00fdd61d3b1eaf93c
      split: test
      type: mteb/summeval
    metrics:
    - type: pearson
      value: 31.255699999999997
    - type: spearman
      value: 31.121
    - type: cosine_spearman
      value: 31.121
    - type: cosine_pearson
      value: 31.255699999999997
    - type: dot_spearman
      value: 31.121
    - type: dot_pearson
      value: 31.255699999999997
    - type: main_score
      value: 31.121
    task:
      type: Summarization
  - dataset:
      config: default
      name: MTEB SyntheticText2SQL (default)
      revision: 686b87296c3a0191b5d9415a00526c62db9fce09
      split: test
      type: CoIR-Retrieval/synthetic-text2sql
    metrics:
    - type: ndcg_at_1
      value: 2.752
    - type: ndcg_at_3
      value: 32.669
    - type: ndcg_at_5
      value: 36.313
    - type: ndcg_at_10
      value: 39.341
    - type: ndcg_at_20
      value: 41.22
    - type: ndcg_at_100
      value: 43.682
    - type: ndcg_at_1000
      value: 44.679
    - type: map_at_1
      value: 2.752
    - type: map_at_3
      value: 25.918999999999997
    - type: map_at_5
      value: 27.939000000000004
    - type: map_at_10
      value: 29.195999999999998
    - type: map_at_20
      value: 29.711
    - type: map_at_100
      value: 30.057000000000002
    - type: map_at_1000
      value: 30.092999999999996
    - type: recall_at_1
      value: 2.752
    - type: recall_at_3
      value: 51.957
    - type: recall_at_5
      value: 60.809999999999995
    - type: recall_at_10
      value: 70.14200000000001
    - type: recall_at_20
      value: 77.576
    - type: recall_at_100
      value: 90.771
    - type: recall_at_1000
      value: 98.667
    - type: precision_at_1
      value: 2.752
    - type: precision_at_3
      value: 17.319000000000003
    - type: precision_at_5
      value: 12.162
    - type: precision_at_10
      value: 7.013999999999999
    - type: precision_at_20
      value: 3.879
    - type: precision_at_100
      value: 0.9079999999999999
    - type: precision_at_1000
      value: 0.099
    - type: mrr_at_1
      value: 23.534399999999998
    - type: mrr_at_3
      value: 37.8739
    - type: mrr_at_5
      value: 39.6078
    - type: mrr_at_10
      value: 40.7592
    - type: mrr_at_20
      value: 41.2449
    - type: mrr_at_100
      value: 41.5832
    - type: mrr_at_1000
      value: 41.6198
    - type: nauc_ndcg_at_1_max
      value: 13.625200000000001
    - type: nauc_ndcg_at_1_std
      value: -17.2342
    - type: nauc_ndcg_at_1_diff1
      value: 72.20830000000001
    - type: nauc_ndcg_at_3_max
      value: 33.5059
    - type: nauc_ndcg_at_3_std
      value: -15.198400000000001
    - type: nauc_ndcg_at_3_diff1
      value: -55.0763
    - type: nauc_ndcg_at_5_max
      value: 31.461699999999997
    - type: nauc_ndcg_at_5_std
      value: -15.857899999999999
    - type: nauc_ndcg_at_5_diff1
      value: -51.2902
    - type: nauc_ndcg_at_10_max
      value: 30.206699999999998
    - type: nauc_ndcg_at_10_std
      value: -15.9071
    - type: nauc_ndcg_at_10_diff1
      value: -48.7532
    - type: nauc_ndcg_at_20_max
      value: 29.5645
    - type: nauc_ndcg_at_20_std
      value: -15.509400000000001
    - type: nauc_ndcg_at_20_diff1
      value: -47.8463
    - type: nauc_ndcg_at_100_max
      value: 29.8902
    - type: nauc_ndcg_at_100_std
      value: -14.0898
    - type: nauc_ndcg_at_100_diff1
      value: -46.7294
    - type: nauc_ndcg_at_1000_max
      value: 30.285800000000002
    - type: nauc_ndcg_at_1000_std
      value: -14.7898
    - type: nauc_ndcg_at_1000_diff1
      value: -47.0235
    - type: nauc_map_at_1_max
      value: 13.625200000000001
    - type: nauc_map_at_1_std
      value: -17.2342
    - type: nauc_map_at_1_diff1
      value: 72.20830000000001
    - type: nauc_map_at_3_max
      value: 32.7681
    - type: nauc_map_at_3_std
      value: -15.386700000000001
    - type: nauc_map_at_3_diff1
      value: -49.9214
    - type: nauc_map_at_5_max
      value: 31.436799999999998
    - type: nauc_map_at_5_std
      value: -15.8028
    - type: nauc_map_at_5_diff1
      value: -47.2353
    - type: nauc_map_at_10_max
      value: 30.857200000000002
    - type: nauc_map_at_10_std
      value: -15.878200000000001
    - type: nauc_map_at_10_diff1
      value: -45.9157
    - type: nauc_map_at_20_max
      value: 30.660300000000003
    - type: nauc_map_at_20_std
      value: -15.7674
    - type: nauc_map_at_20_diff1
      value: -45.5729
    - type: nauc_map_at_100_max
      value: 30.7164
    - type: nauc_map_at_100_std
      value: -15.579200000000002
    - type: nauc_map_at_100_diff1
      value: -45.3606
    - type: nauc_map_at_1000_max
      value: 30.728
    - type: nauc_map_at_1000_std
      value: -15.598600000000001
    - type: nauc_map_at_1000_diff1
      value: -45.367200000000004
    - type: nauc_recall_at_1_max
      value: 13.625200000000001
    - type: nauc_recall_at_1_std
      value: -17.2342
    - type: nauc_recall_at_1_diff1
      value: 72.20830000000001
    - type: nauc_recall_at_3_max
      value: 34.6344
    - type: nauc_recall_at_3_std
      value: -14.868200000000002
    - type: nauc_recall_at_3_diff1
      value: -63.1221
    - type: nauc_recall_at_5_max
      value: 31.1334
    - type: nauc_recall_at_5_std
      value: -16.0306
    - type: nauc_recall_at_5_diff1
      value: -57.4562
    - type: nauc_recall_at_10_max
      value: 27.9709
    - type: nauc_recall_at_10_std
      value: -15.9834
    - type: nauc_recall_at_10_diff1
      value: -52.4094
    - type: nauc_recall_at_20_max
      value: 25.136599999999998
    - type: nauc_recall_at_20_std
      value: -14.491000000000001
    - type: nauc_recall_at_20_diff1
      value: -50.1152
    - type: nauc_recall_at_100_max
      value: 23.1454
    - type: nauc_recall_at_100_std
      value: 1.0654000000000001
    - type: nauc_recall_at_100_diff1
      value: -42.3044
    - type: nauc_recall_at_1000_max
      value: 23.3796
    - type: nauc_recall_at_1000_std
      value: 18.206
    - type: nauc_recall_at_1000_diff1
      value: -44.292300000000004
    - type: nauc_precision_at_1_max
      value: 13.625200000000001
    - type: nauc_precision_at_1_std
      value: -17.2342
    - type: nauc_precision_at_1_diff1
      value: 72.20830000000001
    - type: nauc_precision_at_3_max
      value: 34.6344
    - type: nauc_precision_at_3_std
      value: -14.868200000000002
    - type: nauc_precision_at_3_diff1
      value: -63.1221
    - type: nauc_precision_at_5_max
      value: 31.1334
    - type: nauc_precision_at_5_std
      value: -16.0306
    - type: nauc_precision_at_5_diff1
      value: -57.4562
    - type: nauc_precision_at_10_max
      value: 27.9709
    - type: nauc_precision_at_10_std
      value: -15.9834
    - type: nauc_precision_at_10_diff1
      value: -52.4094
    - type: nauc_precision_at_20_max
      value: 25.136599999999998
    - type: nauc_precision_at_20_std
      value: -14.491000000000001
    - type: nauc_precision_at_20_diff1
      value: -50.1152
    - type: nauc_precision_at_100_max
      value: 23.1454
    - type: nauc_precision_at_100_std
      value: 1.0654000000000001
    - type: nauc_precision_at_100_diff1
      value: -42.3044
    - type: nauc_precision_at_1000_max
      value: 23.3796
    - type: nauc_precision_at_1000_std
      value: 18.206
    - type: nauc_precision_at_1000_diff1
      value: -44.292300000000004
    - type: nauc_mrr_at_1_max
      value: 21.4193
    - type: nauc_mrr_at_1_std
      value: -10.3504
    - type: nauc_mrr_at_1_diff1
      value: -39.323
    - type: nauc_mrr_at_3_max
      value: 28.0993
    - type: nauc_mrr_at_3_std
      value: -12.9194
    - type: nauc_mrr_at_3_diff1
      value: -52.07580000000001
    - type: nauc_mrr_at_5_max
      value: 27.378999999999998
    - type: nauc_mrr_at_5_std
      value: -13.184299999999999
    - type: nauc_mrr_at_5_diff1
      value: -51.0092
    - type: nauc_mrr_at_10_max
      value: 26.9761
    - type: nauc_mrr_at_10_std
      value: -13.0161
    - type: nauc_mrr_at_10_diff1
      value: -50.266200000000005
    - type: nauc_mrr_at_20_max
      value: 26.8175
    - type: nauc_mrr_at_20_std
      value: -12.9521
    - type: nauc_mrr_at_20_diff1
      value: -50.137699999999995
    - type: nauc_mrr_at_100_max
      value: 26.8202
    - type: nauc_mrr_at_100_std
      value: -12.809000000000001
    - type: nauc_mrr_at_100_diff1
      value: -50.0703
    - type: nauc_mrr_at_1000_max
      value: 26.8223
    - type: nauc_mrr_at_1000_std
      value: -12.8169
    - type: nauc_mrr_at_1000_diff1
      value: -50.0798
    - type: main_score
      value: 39.341
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB TRECCOVID (default)
      revision: bb9466bac8153a0349341eb1b22e06409e78ef4e
      split: test
      type: mteb/trec-covid
    metrics:
    - type: ndcg_at_1
      value: 59.0
    - type: ndcg_at_3
      value: 61.173
    - type: ndcg_at_5
      value: 61.927
    - type: ndcg_at_10
      value: 62.815
    - type: ndcg_at_20
      value: 60.716
    - type: ndcg_at_100
      value: 50.699000000000005
    - type: ndcg_at_1000
      value: 46.711999999999996
    - type: map_at_1
      value: 0.186
    - type: map_at_3
      value: 0.47200000000000003
    - type: map_at_5
      value: 0.749
    - type: map_at_10
      value: 1.43
    - type: map_at_20
      value: 2.608
    - type: map_at_100
      value: 8.876000000000001
    - type: map_at_1000
      value: 22.055
    - type: recall_at_1
      value: 0.186
    - type: recall_at_3
      value: 0.519
    - type: recall_at_5
      value: 0.8699999999999999
    - type: recall_at_10
      value: 1.773
    - type: recall_at_20
      value: 3.338
    - type: recall_at_100
      value: 12.516
    - type: recall_at_1000
      value: 44.699
    - type: precision_at_1
      value: 66.0
    - type: precision_at_3
      value: 67.333
    - type: precision_at_5
      value: 67.60000000000001
    - type: precision_at_10
      value: 68.4
    - type: precision_at_20
      value: 65.7
    - type: precision_at_100
      value: 52.78
    - type: precision_at_1000
      value: 21.048000000000002
    - type: mrr_at_1
      value: 66.0
    - type: mrr_at_3
      value: 77.33330000000001
    - type: mrr_at_5
      value: 78.3333
    - type: mrr_at_10
      value: 79.3333
    - type: mrr_at_20
      value: 79.3333
    - type: mrr_at_100
      value: 79.3333
    - type: mrr_at_1000
      value: 79.3333
    - type: nauc_ndcg_at_1_max
      value: 17.5939
    - type: nauc_ndcg_at_1_std
      value: 18.9798
    - type: nauc_ndcg_at_1_diff1
      value: 7.1539
    - type: nauc_ndcg_at_3_max
      value: 29.7636
    - type: nauc_ndcg_at_3_std
      value: 31.7841
    - type: nauc_ndcg_at_3_diff1
      value: 7.1419
    - type: nauc_ndcg_at_5_max
      value: 29.316
    - type: nauc_ndcg_at_5_std
      value: 46.3408
    - type: nauc_ndcg_at_5_diff1
      value: -0.4602
    - type: nauc_ndcg_at_10_max
      value: 27.446900000000003
    - type: nauc_ndcg_at_10_std
      value: 53.37
    - type: nauc_ndcg_at_10_diff1
      value: -4.2545
    - type: nauc_ndcg_at_20_max
      value: 30.0264
    - type: nauc_ndcg_at_20_std
      value: 58.7602
    - type: nauc_ndcg_at_20_diff1
      value: -9.146899999999999
    - type: nauc_ndcg_at_100_max
      value: 37.939299999999996
    - type: nauc_ndcg_at_100_std
      value: 75.0271
    - type: nauc_ndcg_at_100_diff1
      value: -16.2298
    - type: nauc_ndcg_at_1000_max
      value: 40.1712
    - type: nauc_ndcg_at_1000_std
      value: 80.865
    - type: nauc_ndcg_at_1000_diff1
      value: -20.5847
    - type: nauc_map_at_1_max
      value: 16.9528
    - type: nauc_map_at_1_std
      value: -0.49119999999999997
    - type: nauc_map_at_1_diff1
      value: 14.029
    - type: nauc_map_at_3_max
      value: 22.714000000000002
    - type: nauc_map_at_3_std
      value: 4.587
    - type: nauc_map_at_3_diff1
      value: 18.4359
    - type: nauc_map_at_5_max
      value: 26.631700000000002
    - type: nauc_map_at_5_std
      value: 16.3506
    - type: nauc_map_at_5_diff1
      value: 15.8387
    - type: nauc_map_at_10_max
      value: 26.4635
    - type: nauc_map_at_10_std
      value: 22.819300000000002
    - type: nauc_map_at_10_diff1
      value: 9.7916
    - type: nauc_map_at_20_max
      value: 29.7699
    - type: nauc_map_at_20_std
      value: 34.153099999999995
    - type: nauc_map_at_20_diff1
      value: 1.4186
    - type: nauc_map_at_100_max
      value: 41.5138
    - type: nauc_map_at_100_std
      value: 68.24799999999999
    - type: nauc_map_at_100_diff1
      value: -12.2417
    - type: nauc_map_at_1000_max
      value: 45.9887
    - type: nauc_map_at_1000_std
      value: 82.8023
    - type: nauc_map_at_1000_diff1
      value: -20.608999999999998
    - type: nauc_recall_at_1_max
      value: 16.9528
    - type: nauc_recall_at_1_std
      value: -0.49119999999999997
    - type: nauc_recall_at_1_diff1
      value: 14.029
    - type: nauc_recall_at_3_max
      value: 22.601
    - type: nauc_recall_at_3_std
      value: 5.037
    - type: nauc_recall_at_3_diff1
      value: 20.4189
    - type: nauc_recall_at_5_max
      value: 23.8002
    - type: nauc_recall_at_5_std
      value: 17.2469
    - type: nauc_recall_at_5_diff1
      value: 15.3806
    - type: nauc_recall_at_10_max
      value: 20.0149
    - type: nauc_recall_at_10_std
      value: 17.2152
    - type: nauc_recall_at_10_diff1
      value: 8.289
    - type: nauc_recall_at_20_max
      value: 23.2578
    - type: nauc_recall_at_20_std
      value: 25.9678
    - type: nauc_recall_at_20_diff1
      value: 1.6708
    - type: nauc_recall_at_100_max
      value: 34.7341
    - type: nauc_recall_at_100_std
      value: 59.1777
    - type: nauc_recall_at_100_diff1
      value: -10.6132
    - type: nauc_recall_at_1000_max
      value: 36.492599999999996
    - type: nauc_recall_at_1000_std
      value: 74.2008
    - type: nauc_recall_at_1000_diff1
      value: -21.9119
    - type: nauc_precision_at_1_max
      value: 25.7227
    - type: nauc_precision_at_1_std
      value: 14.152500000000002
    - type: nauc_precision_at_1_diff1
      value: 11.1952
    - type: nauc_precision_at_3_max
      value: 35.1261
    - type: nauc_precision_at_3_std
      value: 31.342399999999998
    - type: nauc_precision_at_3_diff1
      value: 3.0915999999999997
    - type: nauc_precision_at_5_max
      value: 33.8418
    - type: nauc_precision_at_5_std
      value: 52.1046
    - type: nauc_precision_at_5_diff1
      value: -5.7694
    - type: nauc_precision_at_10_max
      value: 29.5701
    - type: nauc_precision_at_10_std
      value: 56.474999999999994
    - type: nauc_precision_at_10_diff1
      value: -11.305800000000001
    - type: nauc_precision_at_20_max
      value: 37.1605
    - type: nauc_precision_at_20_std
      value: 62.65690000000001
    - type: nauc_precision_at_20_diff1
      value: -16.114600000000003
    - type: nauc_precision_at_100_max
      value: 42.5736
    - type: nauc_precision_at_100_std
      value: 77.8946
    - type: nauc_precision_at_100_diff1
      value: -18.5221
    - type: nauc_precision_at_1000_max
      value: 31.0108
    - type: nauc_precision_at_1000_std
      value: 54.306200000000004
    - type: nauc_precision_at_1000_diff1
      value: -20.7365
    - type: nauc_mrr_at_1_max
      value: 25.7227
    - type: nauc_mrr_at_1_std
      value: 14.152500000000002
    - type: nauc_mrr_at_1_diff1
      value: 11.1952
    - type: nauc_mrr_at_3_max
      value: 37.1749
    - type: nauc_mrr_at_3_std
      value: 32.7833
    - type: nauc_mrr_at_3_diff1
      value: 5.9276
    - type: nauc_mrr_at_5_max
      value: 34.5503
    - type: nauc_mrr_at_5_std
      value: 31.1188
    - type: nauc_mrr_at_5_diff1
      value: 2.9541
    - type: nauc_mrr_at_10_max
      value: 32.3008
    - type: nauc_mrr_at_10_std
      value: 27.4621
    - type: nauc_mrr_at_10_diff1
      value: 5.944599999999999
    - type: nauc_mrr_at_20_max
      value: 32.3008
    - type: nauc_mrr_at_20_std
      value: 27.4621
    - type: nauc_mrr_at_20_diff1
      value: 5.944599999999999
    - type: nauc_mrr_at_100_max
      value: 32.3008
    - type: nauc_mrr_at_100_std
      value: 27.4621
    - type: nauc_mrr_at_100_diff1
      value: 5.944599999999999
    - type: nauc_mrr_at_1000_max
      value: 32.3008
    - type: nauc_mrr_at_1000_std
      value: 27.4621
    - type: nauc_mrr_at_1000_diff1
      value: 5.944599999999999
    - type: main_score
      value: 62.815
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB Touche2020 (default)
      revision: a34f9a33db75fa0cbb21bb5cfc3dae8dc8bec93f
      split: test
      type: mteb/touche2020
    metrics:
    - type: ndcg_at_1
      value: 34.694
    - type: ndcg_at_3
      value: 27.976
    - type: ndcg_at_5
      value: 27.029999999999998
    - type: ndcg_at_10
      value: 24.853
    - type: ndcg_at_20
      value: 26.188
    - type: ndcg_at_100
      value: 36.225
    - type: ndcg_at_1000
      value: 47.583999999999996
    - type: map_at_1
      value: 2.987
    - type: map_at_3
      value: 4.9799999999999995
    - type: map_at_5
      value: 7.170999999999999
    - type: map_at_10
      value: 9.788
    - type: map_at_20
      value: 12.379
    - type: map_at_100
      value: 15.692
    - type: map_at_1000
      value: 17.27
    - type: recall_at_1
      value: 2.987
    - type: recall_at_3
      value: 6.084
    - type: recall_at_5
      value: 9.609
    - type: recall_at_10
      value: 15.512
    - type: recall_at_20
      value: 24.248
    - type: recall_at_100
      value: 46.916999999999994
    - type: recall_at_1000
      value: 80.447
    - type: precision_at_1
      value: 36.735
    - type: precision_at_3
      value: 27.891
    - type: precision_at_5
      value: 26.531
    - type: precision_at_10
      value: 22.041
    - type: precision_at_20
      value: 17.347
    - type: precision_at_100
      value: 7.550999999999999
    - type: precision_at_1000
      value: 1.492
    - type: mrr_at_1
      value: 36.7347
    - type: mrr_at_3
      value: 46.258500000000005
    - type: mrr_at_5
      value: 47.585
    - type: mrr_at_10
      value: 49.4266
    - type: mrr_at_20
      value: 50.4374
    - type: mrr_at_100
      value: 50.6221
    - type: mrr_at_1000
      value: 50.6221
    - type: nauc_ndcg_at_1_max
      value: -30.5017
    - type: nauc_ndcg_at_1_std
      value: 20.9115
    - type: nauc_ndcg_at_1_diff1
      value: 14.0996
    - type: nauc_ndcg_at_3_max
      value: -32.4852
    - type: nauc_ndcg_at_3_std
      value: 7.378500000000001
    - type: nauc_ndcg_at_3_diff1
      value: 6.1796
    - type: nauc_ndcg_at_5_max
      value: -31.3343
    - type: nauc_ndcg_at_5_std
      value: -1.8091
    - type: nauc_ndcg_at_5_diff1
      value: 2.7997
    - type: nauc_ndcg_at_10_max
      value: -28.2383
    - type: nauc_ndcg_at_10_std
      value: -3.1220999999999997
    - type: nauc_ndcg_at_10_diff1
      value: 10.0107
    - type: nauc_ndcg_at_20_max
      value: -33.4679
    - type: nauc_ndcg_at_20_std
      value: -8.3618
    - type: nauc_ndcg_at_20_diff1
      value: 7.3284
    - type: nauc_ndcg_at_100_max
      value: -33.0007
    - type: nauc_ndcg_at_100_std
      value: 18.1058
    - type: nauc_ndcg_at_100_diff1
      value: 7.5906
    - type: nauc_ndcg_at_1000_max
      value: -30.4942
    - type: nauc_ndcg_at_1000_std
      value: 29.7125
    - type: nauc_ndcg_at_1000_diff1
      value: 4.3626
    - type: nauc_map_at_1_max
      value: -27.8899
    - type: nauc_map_at_1_std
      value: -2.694
    - type: nauc_map_at_1_diff1
      value: 15.2888
    - type: nauc_map_at_3_max
      value: -28.008499999999998
    - type: nauc_map_at_3_std
      value: -8.2292
    - type: nauc_map_at_3_diff1
      value: 11.0099
    - type: nauc_map_at_5_max
      value: -25.1626
    - type: nauc_map_at_5_std
      value: -14.2187
    - type: nauc_map_at_5_diff1
      value: 4.6605
    - type: nauc_map_at_10_max
      value: -21.1923
    - type: nauc_map_at_10_std
      value: -16.653299999999998
    - type: nauc_map_at_10_diff1
      value: 6.869599999999999
    - type: nauc_map_at_20_max
      value: -24.2959
    - type: nauc_map_at_20_std
      value: -17.707
    - type: nauc_map_at_20_diff1
      value: 6.6531
    - type: nauc_map_at_100_max
      value: -24.9706
    - type: nauc_map_at_100_std
      value: -6.2074
    - type: nauc_map_at_100_diff1
      value: 7.940300000000001
    - type: nauc_map_at_1000_max
      value: -24.5016
    - type: nauc_map_at_1000_std
      value: -1.7534
    - type: nauc_map_at_1000_diff1
      value: 7.0978
    - type: nauc_recall_at_1_max
      value: -27.8899
    - type: nauc_recall_at_1_std
      value: -2.694
    - type: nauc_recall_at_1_diff1
      value: 15.2888
    - type: nauc_recall_at_3_max
      value: -33.166000000000004
    - type: nauc_recall_at_3_std
      value: -13.9572
    - type: nauc_recall_at_3_diff1
      value: 6.8492999999999995
    - type: nauc_recall_at_5_max
      value: -26.5866
    - type: nauc_recall_at_5_std
      value: -18.4333
    - type: nauc_recall_at_5_diff1
      value: 0.9511999999999999
    - type: nauc_recall_at_10_max
      value: -23.4865
    - type: nauc_recall_at_10_std
      value: -17.3336
    - type: nauc_recall_at_10_diff1
      value: 9.8763
    - type: nauc_recall_at_20_max
      value: -34.451
    - type: nauc_recall_at_20_std
      value: -18.5261
    - type: nauc_recall_at_20_diff1
      value: 8.4592
    - type: nauc_recall_at_100_max
      value: -31.3903
    - type: nauc_recall_at_100_std
      value: 30.2519
    - type: nauc_recall_at_100_diff1
      value: 9.4903
    - type: nauc_recall_at_1000_max
      value: -20.7349
    - type: nauc_recall_at_1000_std
      value: 72.50229999999999
    - type: nauc_recall_at_1000_diff1
      value: -0.7664
    - type: nauc_precision_at_1_max
      value: -27.048
    - type: nauc_precision_at_1_std
      value: 18.2883
    - type: nauc_precision_at_1_diff1
      value: 18.5083
    - type: nauc_precision_at_3_max
      value: -31.4006
    - type: nauc_precision_at_3_std
      value: -1.9464
    - type: nauc_precision_at_3_diff1
      value: 5.7819
    - type: nauc_precision_at_5_max
      value: -25.740800000000004
    - type: nauc_precision_at_5_std
      value: -11.5328
    - type: nauc_precision_at_5_diff1
      value: 0.4881
    - type: nauc_precision_at_10_max
      value: -20.8035
    - type: nauc_precision_at_10_std
      value: -9.3623
    - type: nauc_precision_at_10_diff1
      value: 13.7272
    - type: nauc_precision_at_20_max
      value: -27.124399999999998
    - type: nauc_precision_at_20_std
      value: -4.7749
    - type: nauc_precision_at_20_diff1
      value: 6.5773
    - type: nauc_precision_at_100_max
      value: -7.2334
    - type: nauc_precision_at_100_std
      value: 60.89639999999999
    - type: nauc_precision_at_100_diff1
      value: 3.9092000000000002
    - type: nauc_precision_at_1000_max
      value: 33.7911
    - type: nauc_precision_at_1000_std
      value: 44.2182
    - type: nauc_precision_at_1000_diff1
      value: -11.840399999999999
    - type: nauc_mrr_at_1_max
      value: -27.048
    - type: nauc_mrr_at_1_std
      value: 18.2883
    - type: nauc_mrr_at_1_diff1
      value: 18.5083
    - type: nauc_mrr_at_3_max
      value: -35.0702
    - type: nauc_mrr_at_3_std
      value: 11.0891
    - type: nauc_mrr_at_3_diff1
      value: 11.4635
    - type: nauc_mrr_at_5_max
      value: -35.9339
    - type: nauc_mrr_at_5_std
      value: 11.4561
    - type: nauc_mrr_at_5_diff1
      value: 11.792900000000001
    - type: nauc_mrr_at_10_max
      value: -35.5993
    - type: nauc_mrr_at_10_std
      value: 13.369800000000001
    - type: nauc_mrr_at_10_diff1
      value: 14.168
    - type: nauc_mrr_at_20_max
      value: -35.587
    - type: nauc_mrr_at_20_std
      value: 12.8052
    - type: nauc_mrr_at_20_diff1
      value: 13.6937
    - type: nauc_mrr_at_100_max
      value: -35.424
    - type: nauc_mrr_at_100_std
      value: 13.0847
    - type: nauc_mrr_at_100_diff1
      value: 13.5063
    - type: nauc_mrr_at_1000_max
      value: -35.424
    - type: nauc_mrr_at_1000_std
      value: 13.0847
    - type: nauc_mrr_at_1000_diff1
      value: 13.5063
    - type: main_score
      value: 24.853
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB ToxicConversationsClassification (default)
      revision: edfaf9da55d3dd50d43143d90c1ac476895ae6de
      split: test
      type: mteb/toxic_conversations_50k
    metrics:
    - type: accuracy
      value: 60.380900000000004
    - type: f1
      value: 46.8295
    - type: f1_weighted
      value: 69.05930000000001
    - type: ap
      value: 10.5988
    - type: ap_weighted
      value: 10.5988
    - type: main_score
      value: 60.380900000000004
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB TweetSentimentExtractionClassification (default)
      revision: d604517c81ca91fe16a244d1248fc021f9ecee7a
      split: test
      type: mteb/tweet_sentiment_extraction
    metrics:
    - type: accuracy
      value: 58.537099999999995
    - type: f1
      value: 58.7006
    - type: f1_weighted
      value: 58.013400000000004
    - type: main_score
      value: 58.537099999999995
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB TwentyNewsgroupsClustering (default)
      revision: 6125ec4e24fa026cec8a478383ee943acfbd5449
      split: test
      type: mteb/twentynewsgroups-clustering
    metrics:
    - type: v_measure
      value: 36.6842
    - type: v_measure_std
      value: 1.9854
    - type: main_score
      value: 36.6842
    task:
      type: Clustering
  - dataset:
      config: default
      name: MTEB TwitterSemEval2015 (default)
      revision: 70970daeab8776df92f5ea462b6173c0b46fd2d1
      split: test
      type: mteb/twittersemeval2015-pairclassification
    metrics:
    - type: similarity_accuracy
      value: 82.3866
    - type: similarity_accuracy_threshold
      value: 87.0467
    - type: similarity_f1
      value: 58.4102
    - type: similarity_f1_threshold
      value: 82.61540000000001
    - type: similarity_precision
      value: 52.937400000000004
    - type: similarity_recall
      value: 65.1451
    - type: similarity_ap
      value: 61.6413
    - type: cosine_accuracy
      value: 82.3866
    - type: cosine_accuracy_threshold
      value: 87.0467
    - type: cosine_f1
      value: 58.4102
    - type: cosine_f1_threshold
      value: 82.61540000000001
    - type: cosine_precision
      value: 52.937400000000004
    - type: cosine_recall
      value: 65.1451
    - type: cosine_ap
      value: 61.6413
    - type: manhattan_accuracy
      value: 82.12429999999999
    - type: manhattan_accuracy_threshold
      value: 786.2048
    - type: manhattan_f1
      value: 57.862899999999996
    - type: manhattan_f1_threshold
      value: 911.9348
    - type: manhattan_precision
      value: 50.2725
    - type: manhattan_recall
      value: 68.15299999999999
    - type: manhattan_ap
      value: 60.6893
    - type: euclidean_accuracy
      value: 82.3866
    - type: euclidean_accuracy_threshold
      value: 50.8985
    - type: euclidean_f1
      value: 58.4102
    - type: euclidean_f1_threshold
      value: 58.9654
    - type: euclidean_precision
      value: 52.937400000000004
    - type: euclidean_recall
      value: 65.1451
    - type: euclidean_ap
      value: 61.6413
    - type: dot_accuracy
      value: 82.3866
    - type: dot_accuracy_threshold
      value: 87.0467
    - type: dot_f1
      value: 58.4102
    - type: dot_f1_threshold
      value: 82.61540000000001
    - type: dot_precision
      value: 52.937400000000004
    - type: dot_recall
      value: 65.1451
    - type: dot_ap
      value: 61.6413
    - type: max_accuracy
      value: 82.3866
    - type: max_f1
      value: 58.4102
    - type: max_precision
      value: 52.937400000000004
    - type: max_recall
      value: 68.15299999999999
    - type: max_ap
      value: 61.6413
    - type: main_score
      value: 61.6413
    task:
      type: PairClassification
  - dataset:
      config: default
      name: MTEB TwitterURLCorpus (default)
      revision: 8b6510b0b1fa4e4c4f879467980e9be563ec1cdf
      split: test
      type: mteb/twitterurlcorpus-pairclassification
    metrics:
    - type: similarity_accuracy
      value: 88.77629999999999
    - type: similarity_accuracy_threshold
      value: 82.2251
    - type: similarity_f1
      value: 77.3613
    - type: similarity_f1_threshold
      value: 80.3174
    - type: similarity_precision
      value: 75.0906
    - type: similarity_recall
      value: 79.7736
    - type: similarity_ap
      value: 85.6694
    - type: cosine_accuracy
      value: 88.77629999999999
    - type: cosine_accuracy_threshold
      value: 82.2251
    - type: cosine_f1
      value: 77.3613
    - type: cosine_f1_threshold
      value: 80.3174
    - type: cosine_precision
      value: 75.0906
    - type: cosine_recall
      value: 79.7736
    - type: cosine_ap
      value: 85.6694
    - type: manhattan_accuracy
      value: 88.7317
    - type: manhattan_accuracy_threshold
      value: 914.4955
    - type: manhattan_f1
      value: 77.1707
    - type: manhattan_f1_threshold
      value: 946.5603
    - type: manhattan_precision
      value: 76.2825
    - type: manhattan_recall
      value: 78.0798
    - type: manhattan_ap
      value: 85.5718
    - type: euclidean_accuracy
      value: 88.77629999999999
    - type: euclidean_accuracy_threshold
      value: 59.6237
    - type: euclidean_f1
      value: 77.3613
    - type: euclidean_f1_threshold
      value: 62.7417
    - type: euclidean_precision
      value: 75.0906
    - type: euclidean_recall
      value: 79.7736
    - type: euclidean_ap
      value: 85.6694
    - type: dot_accuracy
      value: 88.77629999999999
    - type: dot_accuracy_threshold
      value: 82.2251
    - type: dot_f1
      value: 77.3613
    - type: dot_f1_threshold
      value: 80.3174
    - type: dot_precision
      value: 75.0906
    - type: dot_recall
      value: 79.7736
    - type: dot_ap
      value: 85.6694
    - type: max_accuracy
      value: 88.77629999999999
    - type: max_f1
      value: 77.3613
    - type: max_precision
      value: 76.2825
    - type: max_recall
      value: 79.7736
    - type: max_ap
      value: 85.6694
    - type: main_score
      value: 85.6694
    task:
      type: PairClassification
pipeline_tag: sentence-similarity
---
# Granite-Embedding-107m-multilingual

**Model Summary:**
Granite-Embedding-107M-Multilingual is a 107M parameter dense biencoder embedding model from the Granite Embeddings suite that can be used to generate high quality text embeddings. This model produces embedding vectors of size 384 and is trained using a combination of open source relevance-pair datasets with permissive, enterprise-friendly license, and IBM collected and generated datasets. This model is developed using contrastive finetuning, knowledge distillation and model merging for improved performance.

- **Developers:** Granite Embedding Team, IBM
- **GitHub Repository:** [ibm-granite/granite-embedding-models](https://github.com/ibm-granite/granite-embedding-models)
- **Website**: [Granite Docs](https://www.ibm.com/granite/docs/)
- **Paper:** Coming Soon
- **Release Date**: December 18th, 2024
- **License:** [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0)

**Supported Languages:** 
English, German, Spanish, French, Japanese, Portuguese, Arabic, Czech, Italian, Korean, Dutch, and Chinese. Users may finetune Granite-Embedding-107M-Multilingual for languages beyond these 12 languages.

**Intended use:** 
The model is designed to produce fixed length vector representations for a given text, which can be used for text similarity, retrieval, and search applications.

**Usage with Sentence Transformers:** 
The model is compatible with SentenceTransformer library and is very easy to use:

First, install the sentence transformers library
```shell
pip install sentence_transformers
```

The model can then be used to encode pairs of text and find the similarity between their representations

```python
from sentence_transformers import SentenceTransformer, util

model_path = "ibm-granite/granite-embedding-107m-multilingual"
# Load the Sentence Transformer model
model = SentenceTransformer(model_path)

input_queries = [
    ' Who made the song My achy breaky heart? ',
    'summit define'
    ]

input_passages = [
    "Achy Breaky Heart is a country song written by Don Von Tress. Originally titled Don't Tell My Heart and performed by The Marcy Brothers in 1991. ",
    "Definition of summit for English Language Learners. : 1 the highest point of a mountain : the top of a mountain. : 2 the highest level. : 3 a meeting or series of meetings between the leaders of two or more governments."
    ]

# encode queries and passages
query_embeddings = model.encode(input_queries)
passage_embeddings = model.encode(input_passages)

# calculate cosine similarity
print(util.cos_sim(query_embeddings, passage_embeddings))
```

**Usage with Huggingface Transformers:** 
This is a simple example of how to use the Granite-Embedding-107m-Multilingual model with the Transformers library and PyTorch.

First, install the required libraries
```shell
pip install transformers torch
```

The model can then be used to encode pairs of text

```python
import torch
from transformers import AutoModel, AutoTokenizer

model_path = "ibm-granite/granite-embedding-107m-multilingual"

# Load the model and tokenizer
model = AutoModel.from_pretrained(model_path)
tokenizer = AutoTokenizer.from_pretrained(model_path)
model.eval()

input_queries = [
    ' Who made the song My achy breaky heart? ',
    'summit define'
    ]

# tokenize inputs
tokenized_queries = tokenizer(input_queries, padding=True, truncation=True, return_tensors='pt')

# encode queries
with torch.no_grad():
    # Queries
    model_output = model(**tokenized_queries)
    # Perform pooling. granite-embedding-107m-multilingual uses CLS Pooling
    query_embeddings = model_output[0][:, 0]

# normalize the embeddings
query_embeddings = torch.nn.functional.normalize(query_embeddings, dim=1)

```

**Evaluation:**
The average performance of the Granite-Embedding-107M-Multilingual on Multilingual Miracl (across 18 langauges), Mintaka Retrieval (across 8 languages) and MTEB Retrieval for English (across 15 tasks), German (across 4 tasks), Spanish (across 2 tasks), Frenc (across 5 tasks), Japanese (across 2 tasks), Arabic (1 task), Korean (1 task) and Chinese (across 8 tasks) is reported below. Granite-Embedding-107M-Multilingual is twice as fast as other models with similar embedding dimensions.

| Model                              | Paramters (M)| Embedding Dimension | Miracl (18)   |  Mintaka Retrieval (8) | MTEB English (15) | MTEB German (4) |MTEB Spanish (2) | MTEB French (5) | MTEB Japanese (2) |  MTEB Arabic (1) | MTEB Korean (1) | MTEB Chinese (8) | 
|------------------------------------|:------------:|:-------------------:|:-------------:| :---------------------:|:-----------------:|:---------------:|:---------------:|:---------------:|:----------------:|:----------------:|----------------:|-----------------:|
|granite-embedding-107m-multilingual | 107 | 384 | 55.9 | 22.6 | 45.3 | 70.3 | 48.7 | 51.1 | 59.0 | 63.2 | 70.5 | 40.8 | 

**Model Architecture:**
Granite-Embedding-107m-Multilingual is based on an encoder-only XLM-RoBERTa like transformer architecture, trained internally at IBM Research.

| Model                     | granite-embedding-30m-english | granite-embedding-125m-english    | granite-embedding-107m-multilingual | granite-embedding-278m-multilingual |
| :---------                | :-------:| :--------:   | :---------:| :-----:|
| Embedding size            | 384      | 768          | **384**    | 768    |
| Number of layers          | 6        | 12           | **6**      | 12     |
| Number of attention heads | 12       | 12           | **12**     | 12     |
| Intermediate size         | 1536     | 3072         | **1536**   | 3072   |
| Activation Function       | GeLU     | GeLU         | **GeLU**   | GeLU   |
| Vocabulary Size           | 50265    | 50265        | **250002** | 250002 |
| Max. Sequence Length      | 512      | 512          | **512**    | 512    |
| # Parameters              | 30M      | 125M         | **107M**   | 278M   |


**Training Data:**
Overall, the training data consists of four key sources: (1) unsupervised title-body paired data scraped from the web, (2) publicly available paired with permissive, enterprise-friendly license, (3) IBM-internal paired data targetting specific technical domains, and (4) IBM-generated synthetic data. The data is listed below:

| **Dataset**                                                               | **Num. Pairs** | 
|:--------------------------------------------------------------------------|:--------------:|
| Multilingual MC4                                                          | 52,823,484     |
| Multilingual Webhose                                                      | 12,369,322     | 
| English Wikipedia                                                         | 20,745,403     | 
| Multilingual Wikimedia                                                    | 2,911,090      |
| Miracl Corpus (Title-Body)                                                | 10,120,398     |
| Stack Exchange Duplicate questions (titles)                               | 304,525        | 
| Stack Exchange Duplicate questions (titles)                               | 304,525        | 
| Stack Exchange Duplicate questions (bodies)                               | 250,519        | 
| Machine Translations of Stack Exchange Duplicate questions (titles)       | 187,195        | 
| Stack Exchange (Title, Answer) pairs                                      | 4,067,139      | 
| Stack Exchange (Title, Body) pairs                                        | 23,978,013     | 
| Stack Exchange (Title, Body) pairs                                        | 23,978,013     | 
| Machine Translations of Stack Exchange (Title+Body, Answer) pairs         | 1,827,15       | 
| SearchQA                                                                  | 582,261        | 
| S2ORC (Title, Abstract)                                                   | 41,769,185     | 
| WikiAnswers Duplicate question pairs                                      | 77,427,422     | 
| CCNews                                                                    | 614,664        |
| XSum                                                                      | 226,711        |
| SimpleWiki                                                                | 102,225        |
| Machine Translated Cross Lingual Parallel Corpora                         | 28,376,115     |
| SPECTER citation triplets                                                 | 684,100        | 
| Machine Translations of SPECTER citation triplets                         | 4,104,600      | 
| Natural Questions (NQ)                                                    | 100,231        | 
| SQuAD2.0                                                                  | 87,599         | 
| HotpotQA                                                                  | 85,000         | 
| Fever                                                                     | 109,810        | 
| PubMed                                                                    | 20,000,000     | 
| Multilingual Miracl Triples                                               | 81,409         | 
| Multilingual MrTydi Triples                                               | 48,715         | 
| Sadeeem Question Asnwering                                                | 4,037          | 
| DBPedia Title-Body Pairs                                                  | 4,635,922      | 
| Synthetic: English Query-Wikipedia Passage                                | 1,879,093      | 
| Synthetic: English Fact Verification                                      | 9,888          | 
| Synthetic: Multilingual Query-Wikipedia Passage                           | 300,266        |
| Synthetic: Multilingual News Summaries                                    | 37,489         |
| IBM Internal Triples                                                      | 40,290         | 
| IBM Internal Title-Body Pairs                                             | 1,524,586      |

Notably, we do not use the popular MS-MARCO retrieval dataset in our training corpus due to its non-commercial license, while other open-source models train on this dataset due to its high quality.

**Infrastructure:**
We train Granite Embedding Models using IBM's computing cluster, Cognitive Compute Cluster, which is outfitted with NVIDIA A100 80gb GPUs. This cluster provides a scalable and efficient infrastructure for training our models over multiple GPUs.

**Ethical Considerations and Limitations:** 
The data used to train the base language model was filtered to remove text containing hate, abuse, and profanity. Granite-Embedding-107m-Multilingual is finetuned on 12 languages, and has a context length of 512 tokens (longer texts will be truncated to this size).

**Resources**
- ⭐️ Learn about the latest updates with Granite: https://www.ibm.com/granite
- 📄 Get started with tutorials, best practices, and prompt engineering advice: https://www.ibm.com/granite/docs/
- 💡 Learn about the latest Granite learning resources: https://ibm.biz/granite-learning-resources

<!-- ## Citation
```
@misc{granite-embedding-models,
  author = {author 1, author2, ...},
  title = {},
  journal = {},
  volume = {},
  year = {2024},
  url = {https://arxiv.org/abs/0000.00000},
}
``` -->