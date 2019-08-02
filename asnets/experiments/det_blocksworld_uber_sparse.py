"""For more-challenging experiments on deterministic blocksworld; aim is to
provide strong empirical evidence that our method CAN solve BW perfectly (or
alternatively to show that it can't yet do so)."""

PDDL_DIR = '../problems/mine/det-bw-challenge/pddl/'
COMMON_PDDLS = ['domain.pddl']
TRAIN_PDDLS = [
    'train/prob-blocks-blocks-nblk5-seed896255376-seq0.pddl',
    'train/prob-blocks-blocks-nblk5-seed896255376-seq1.pddl',
    'train/prob-blocks-blocks-nblk5-seed896255376-seq2.pddl',
    # Sam: added -seq{5,3,9} because the other sparse net failed at them (rest of
    # seq{0..9} are fine)
    'train/prob-blocks-blocks-nblk5-seed896255376-seq3.pddl',
    'train/prob-blocks-blocks-nblk5-seed896255376-seq5.pddl',
    'train/prob-blocks-blocks-nblk5-seed896255376-seq9.pddl',
    'train/prob-blocks-blocks-nblk8-ntow1-seed270765476-seq0.pddl',
    # old net also failed at nblk8-ntow1-…-seq1, despite it being in the
    # training set
    'train/prob-blocks-blocks-nblk8-ntow1-seed270765476-seq1.pddl',
    # for whatever reason, nblk8-…-seq{0..4,6,8,9}.pddl all work fine
    # (surprises me given number of failures on nblk5 instances). Ones that
    # don't work include -seq{5,7}.
    # I'll replace -seq0 with -seq7
    'train/prob-blocks-blocks-nblk8-seed236108287-seq0.pddl',
    'train/prob-blocks-blocks-nblk8-seed236108287-seq1.pddl',
    'train/prob-blocks-blocks-nblk8-seed236108287-seq2.pddl',
    # replacing seq3 with seq5 to get some harder probs
    'train/prob-blocks-blocks-nblk8-seed236108287-seq3.pddl',
    'train/prob-blocks-blocks-nblk8-seed236108287-seq5.pddl',
    'train/prob-blocks-blocks-nblk8-seed236108287-seq7.pddl',
    'train/prob-blocks-blocks-nblk8-seed236108287-seq8.pddl',
    'train/prob-blocks-blocks-nblk8-seed236108287-seq9.pddl',
]  # yapf: disable
TRAIN_NAMES = None
_TEST_RUNS = [
    'prob-blocks-blocks-nblk25-seed1428122178-seq25.pddl',
    'prob-blocks-blocks-nblk35-seed2107726020-seq57.pddl',
    'prob-blocks-blocks-nblk50-seed1184714140-seq84.pddl',
    'prob-blocks-blocks-nblk35-seed2107726020-seq84.pddl',
    'prob-blocks-blocks-nblk35-seed2107726020-seq16.pddl',
    'prob-blocks-blocks-nblk50-seed1184714140-seq47.pddl',
    'prob-blocks-blocks-nblk35-seed2107726020-seq92.pddl',
    'prob-blocks-blocks-nblk50-seed1184714140-seq43.pddl',
    'prob-blocks-blocks-nblk50-seed1184714140-seq93.pddl',
    'prob-blocks-blocks-nblk35-seed2107726020-seq66.pddl',
    'prob-blocks-blocks-nblk50-seed1184714140-seq18.pddl',
    'prob-blocks-blocks-nblk25-seed1428122178-seq58.pddl',
    'prob-blocks-blocks-nblk50-seed1184714140-seq40.pddl',
    'prob-blocks-blocks-nblk35-seed2107726020-seq65.pddl',
    'prob-blocks-blocks-nblk50-seed1184714140-seq7.pddl',
    'prob-blocks-blocks-nblk50-seed1184714140-seq94.pddl',
    'prob-blocks-blocks-nblk25-seed1428122178-seq60.pddl',
    'prob-blocks-blocks-nblk50-seed1184714140-seq3.pddl',
    'prob-blocks-blocks-nblk50-seed1184714140-seq37.pddl',
    'prob-blocks-blocks-nblk25-seed1428122178-seq57.pddl',
    'prob-blocks-blocks-nblk35-seed2107726020-seq68.pddl',
    'prob-blocks-blocks-nblk50-seed1184714140-seq0.pddl',
    'prob-blocks-blocks-nblk35-seed2107726020-seq28.pddl',
    'prob-blocks-blocks-nblk50-seed1184714140-seq61.pddl',
    'prob-blocks-blocks-nblk50-seed1184714140-seq71.pddl',
    'prob-blocks-blocks-nblk35-seed2107726020-seq73.pddl',
    'prob-blocks-blocks-nblk25-seed1428122178-seq7.pddl',
    'prob-blocks-blocks-nblk35-seed2107726020-seq9.pddl',
    'prob-blocks-blocks-nblk25-seed1428122178-seq93.pddl',
    'prob-blocks-blocks-nblk35-seed2107726020-seq41.pddl',
    'prob-blocks-blocks-nblk35-seed2107726020-seq85.pddl',
    'prob-blocks-blocks-nblk25-seed1428122178-seq76.pddl',
    'prob-blocks-blocks-nblk50-seed1184714140-seq73.pddl',
    'prob-blocks-blocks-nblk50-seed1184714140-seq2.pddl',
    'prob-blocks-blocks-nblk50-seed1184714140-seq36.pddl',
    'prob-blocks-blocks-nblk50-seed1184714140-seq53.pddl',
    'prob-blocks-blocks-nblk50-seed1184714140-seq15.pddl',
    'prob-blocks-blocks-nblk25-seed1428122178-seq46.pddl',
    'prob-blocks-blocks-nblk50-seed1184714140-seq89.pddl',
    'prob-blocks-blocks-nblk35-seed2107726020-seq50.pddl',
    'prob-blocks-blocks-nblk25-seed1428122178-seq84.pddl',
    'prob-blocks-blocks-nblk50-seed1184714140-seq1.pddl',
    'prob-blocks-blocks-nblk50-seed1184714140-seq90.pddl',
    'prob-blocks-blocks-nblk35-seed2107726020-seq38.pddl',
    'prob-blocks-blocks-nblk35-seed2107726020-seq29.pddl',
    'prob-blocks-blocks-nblk50-seed1184714140-seq20.pddl',
    'prob-blocks-blocks-nblk50-seed1184714140-seq21.pddl',
    'prob-blocks-blocks-nblk35-seed2107726020-seq13.pddl',
    'prob-blocks-blocks-nblk50-seed1184714140-seq19.pddl',
    'prob-blocks-blocks-nblk50-seed1184714140-seq46.pddl',
    'prob-blocks-blocks-nblk35-seed2107726020-seq14.pddl',
    'prob-blocks-blocks-nblk35-seed2107726020-seq11.pddl',
    'prob-blocks-blocks-nblk25-seed1428122178-seq40.pddl',
    'prob-blocks-blocks-nblk35-seed2107726020-seq0.pddl',
    'prob-blocks-blocks-nblk50-seed1184714140-seq4.pddl',
    'prob-blocks-blocks-nblk25-seed1428122178-seq36.pddl',
    'prob-blocks-blocks-nblk35-seed2107726020-seq12.pddl',
    'prob-blocks-blocks-nblk25-seed1428122178-seq56.pddl',
    'prob-blocks-blocks-nblk35-seed2107726020-seq51.pddl',
    'prob-blocks-blocks-nblk25-seed1428122178-seq88.pddl',
    'prob-blocks-blocks-nblk50-seed1184714140-seq33.pddl',
    'prob-blocks-blocks-nblk35-seed2107726020-seq37.pddl',
    'prob-blocks-blocks-nblk50-seed1184714140-seq26.pddl',
    'prob-blocks-blocks-nblk35-seed2107726020-seq62.pddl',
    'prob-blocks-blocks-nblk25-seed1428122178-seq71.pddl',
    'prob-blocks-blocks-nblk35-seed2107726020-seq1.pddl',
    'prob-blocks-blocks-nblk25-seed1428122178-seq42.pddl',
    'prob-blocks-blocks-nblk50-seed1184714140-seq35.pddl',
    'prob-blocks-blocks-nblk25-seed1428122178-seq20.pddl',
    'prob-blocks-blocks-nblk50-seed1184714140-seq23.pddl',
    'prob-blocks-blocks-nblk50-seed1184714140-seq91.pddl',
    'prob-blocks-blocks-nblk25-seed1428122178-seq17.pddl',
    'prob-blocks-blocks-nblk25-seed1428122178-seq97.pddl',
    'prob-blocks-blocks-nblk50-seed1184714140-seq87.pddl',
    'prob-blocks-blocks-nblk35-seed2107726020-seq53.pddl',
    'prob-blocks-blocks-nblk35-seed2107726020-seq2.pddl',
    'prob-blocks-blocks-nblk35-seed2107726020-seq20.pddl',
    'prob-blocks-blocks-nblk25-seed1428122178-seq78.pddl',
    'prob-blocks-blocks-nblk25-seed1428122178-seq81.pddl',
    'prob-blocks-blocks-nblk35-seed2107726020-seq93.pddl',
    'prob-blocks-blocks-nblk25-seed1428122178-seq55.pddl',
    'prob-blocks-blocks-nblk50-seed1184714140-seq95.pddl',
    'prob-blocks-blocks-nblk25-seed1428122178-seq18.pddl',
    'prob-blocks-blocks-nblk50-seed1184714140-seq10.pddl',
    'prob-blocks-blocks-nblk35-seed2107726020-seq54.pddl',
    'prob-blocks-blocks-nblk25-seed1428122178-seq98.pddl',
    'prob-blocks-blocks-nblk25-seed1428122178-seq75.pddl',
    'prob-blocks-blocks-nblk25-seed1428122178-seq66.pddl',
    'prob-blocks-blocks-nblk25-seed1428122178-seq80.pddl',
    'prob-blocks-blocks-nblk35-seed2107726020-seq27.pddl',
    'prob-blocks-blocks-nblk50-seed1184714140-seq80.pddl',
    'prob-blocks-blocks-nblk50-seed1184714140-seq68.pddl',
    'prob-blocks-blocks-nblk25-seed1428122178-seq8.pddl',
    'prob-blocks-blocks-nblk50-seed1184714140-seq65.pddl',
    'prob-blocks-blocks-nblk25-seed1428122178-seq23.pddl',
    'prob-blocks-blocks-nblk35-seed2107726020-seq90.pddl',
    'prob-blocks-blocks-nblk35-seed2107726020-seq5.pddl',
    'prob-blocks-blocks-nblk50-seed1184714140-seq28.pddl',
    'prob-blocks-blocks-nblk50-seed1184714140-seq52.pddl',
    'prob-blocks-blocks-nblk35-seed2107726020-seq71.pddl',
    'prob-blocks-blocks-nblk25-seed1428122178-seq33.pddl',
    'prob-blocks-blocks-nblk25-seed1428122178-seq49.pddl',
    'prob-blocks-blocks-nblk50-seed1184714140-seq81.pddl',
    'prob-blocks-blocks-nblk35-seed2107726020-seq22.pddl',
    'prob-blocks-blocks-nblk35-seed2107726020-seq15.pddl',
    'prob-blocks-blocks-nblk25-seed1428122178-seq64.pddl',
    'prob-blocks-blocks-nblk25-seed1428122178-seq45.pddl',
    'prob-blocks-blocks-nblk50-seed1184714140-seq78.pddl',
    'prob-blocks-blocks-nblk50-seed1184714140-seq67.pddl',
    'prob-blocks-blocks-nblk50-seed1184714140-seq70.pddl',
    'prob-blocks-blocks-nblk35-seed2107726020-seq76.pddl',
    'prob-blocks-blocks-nblk35-seed2107726020-seq88.pddl',
    'prob-blocks-blocks-nblk35-seed2107726020-seq70.pddl',
    'prob-blocks-blocks-nblk35-seed2107726020-seq24.pddl',
    'prob-blocks-blocks-nblk35-seed2107726020-seq81.pddl',
    'prob-blocks-blocks-nblk35-seed2107726020-seq18.pddl',
    'prob-blocks-blocks-nblk25-seed1428122178-seq24.pddl',
    'prob-blocks-blocks-nblk50-seed1184714140-seq24.pddl',
    'prob-blocks-blocks-nblk50-seed1184714140-seq42.pddl',
    'prob-blocks-blocks-nblk35-seed2107726020-seq72.pddl',
    'prob-blocks-blocks-nblk35-seed2107726020-seq17.pddl',
    'prob-blocks-blocks-nblk35-seed2107726020-seq86.pddl',
    'prob-blocks-blocks-nblk25-seed1428122178-seq43.pddl',
    'prob-blocks-blocks-nblk35-seed2107726020-seq4.pddl',
    'prob-blocks-blocks-nblk50-seed1184714140-seq25.pddl',
    'prob-blocks-blocks-nblk50-seed1184714140-seq50.pddl',
    'prob-blocks-blocks-nblk25-seed1428122178-seq19.pddl',
    'prob-blocks-blocks-nblk35-seed2107726020-seq55.pddl',
    'prob-blocks-blocks-nblk35-seed2107726020-seq45.pddl',
    'prob-blocks-blocks-nblk50-seed1184714140-seq57.pddl',
    'prob-blocks-blocks-nblk35-seed2107726020-seq43.pddl',
    'prob-blocks-blocks-nblk35-seed2107726020-seq64.pddl',
    'prob-blocks-blocks-nblk35-seed2107726020-seq34.pddl',
    'prob-blocks-blocks-nblk50-seed1184714140-seq49.pddl',
    'prob-blocks-blocks-nblk25-seed1428122178-seq27.pddl',
    'prob-blocks-blocks-nblk35-seed2107726020-seq77.pddl',
    'prob-blocks-blocks-nblk50-seed1184714140-seq55.pddl',
    'prob-blocks-blocks-nblk50-seed1184714140-seq39.pddl',
    'prob-blocks-blocks-nblk50-seed1184714140-seq14.pddl',
    'prob-blocks-blocks-nblk25-seed1428122178-seq39.pddl',
    'prob-blocks-blocks-nblk50-seed1184714140-seq30.pddl',
    'prob-blocks-blocks-nblk35-seed2107726020-seq44.pddl',
    'prob-blocks-blocks-nblk25-seed1428122178-seq92.pddl',
    'prob-blocks-blocks-nblk35-seed2107726020-seq67.pddl',
    'prob-blocks-blocks-nblk25-seed1428122178-seq16.pddl',
    'prob-blocks-blocks-nblk25-seed1428122178-seq4.pddl',
    'prob-blocks-blocks-nblk35-seed2107726020-seq61.pddl',
    'prob-blocks-blocks-nblk50-seed1184714140-seq98.pddl',
    'prob-blocks-blocks-nblk50-seed1184714140-seq82.pddl',
    'prob-blocks-blocks-nblk50-seed1184714140-seq75.pddl',
    'prob-blocks-blocks-nblk50-seed1184714140-seq83.pddl',
    'prob-blocks-blocks-nblk35-seed2107726020-seq32.pddl',
    'prob-blocks-blocks-nblk25-seed1428122178-seq85.pddl',
    'prob-blocks-blocks-nblk25-seed1428122178-seq61.pddl',
    'prob-blocks-blocks-nblk50-seed1184714140-seq59.pddl',
    'prob-blocks-blocks-nblk35-seed2107726020-seq89.pddl',
    'prob-blocks-blocks-nblk25-seed1428122178-seq53.pddl',
    'prob-blocks-blocks-nblk25-seed1428122178-seq0.pddl',
    'prob-blocks-blocks-nblk25-seed1428122178-seq6.pddl',
    'prob-blocks-blocks-nblk25-seed1428122178-seq90.pddl',
    'prob-blocks-blocks-nblk25-seed1428122178-seq28.pddl',
    'prob-blocks-blocks-nblk50-seed1184714140-seq76.pddl',
    'prob-blocks-blocks-nblk50-seed1184714140-seq99.pddl',
    'prob-blocks-blocks-nblk50-seed1184714140-seq66.pddl',
    'prob-blocks-blocks-nblk50-seed1184714140-seq29.pddl',
    'prob-blocks-blocks-nblk35-seed2107726020-seq7.pddl',
    'prob-blocks-blocks-nblk50-seed1184714140-seq54.pddl',
    'prob-blocks-blocks-nblk35-seed2107726020-seq48.pddl',
    'prob-blocks-blocks-nblk50-seed1184714140-seq79.pddl',
    'prob-blocks-blocks-nblk25-seed1428122178-seq96.pddl',
    'prob-blocks-blocks-nblk25-seed1428122178-seq3.pddl',
    'prob-blocks-blocks-nblk35-seed2107726020-seq99.pddl',
    'prob-blocks-blocks-nblk50-seed1184714140-seq13.pddl',
    'prob-blocks-blocks-nblk25-seed1428122178-seq74.pddl',
    'prob-blocks-blocks-nblk35-seed2107726020-seq96.pddl',
    'prob-blocks-blocks-nblk35-seed2107726020-seq31.pddl',
    'prob-blocks-blocks-nblk35-seed2107726020-seq97.pddl',
    'prob-blocks-blocks-nblk50-seed1184714140-seq9.pddl',
    'prob-blocks-blocks-nblk35-seed2107726020-seq59.pddl',
    'prob-blocks-blocks-nblk35-seed2107726020-seq75.pddl',
    'prob-blocks-blocks-nblk25-seed1428122178-seq89.pddl',
    'prob-blocks-blocks-nblk25-seed1428122178-seq95.pddl',
    'prob-blocks-blocks-nblk25-seed1428122178-seq14.pddl',
    'prob-blocks-blocks-nblk25-seed1428122178-seq5.pddl',
    'prob-blocks-blocks-nblk25-seed1428122178-seq32.pddl',
    'prob-blocks-blocks-nblk25-seed1428122178-seq87.pddl',
    'prob-blocks-blocks-nblk35-seed2107726020-seq6.pddl',
    'prob-blocks-blocks-nblk50-seed1184714140-seq97.pddl',
    'prob-blocks-blocks-nblk50-seed1184714140-seq22.pddl',
    'prob-blocks-blocks-nblk50-seed1184714140-seq27.pddl',
    'prob-blocks-blocks-nblk25-seed1428122178-seq13.pddl',
    'prob-blocks-blocks-nblk25-seed1428122178-seq65.pddl',
    'prob-blocks-blocks-nblk50-seed1184714140-seq86.pddl',
    'prob-blocks-blocks-nblk35-seed2107726020-seq8.pddl',
    'prob-blocks-blocks-nblk35-seed2107726020-seq60.pddl',
    'prob-blocks-blocks-nblk50-seed1184714140-seq38.pddl',
    'prob-blocks-blocks-nblk25-seed1428122178-seq41.pddl',
    'prob-blocks-blocks-nblk35-seed2107726020-seq46.pddl',
    'prob-blocks-blocks-nblk50-seed1184714140-seq31.pddl',
    'prob-blocks-blocks-nblk35-seed2107726020-seq69.pddl',
    'prob-blocks-blocks-nblk35-seed2107726020-seq39.pddl',
    'prob-blocks-blocks-nblk25-seed1428122178-seq83.pddl',
    'prob-blocks-blocks-nblk35-seed2107726020-seq58.pddl',
    'prob-blocks-blocks-nblk50-seed1184714140-seq32.pddl',
    'prob-blocks-blocks-nblk25-seed1428122178-seq30.pddl',
    'prob-blocks-blocks-nblk35-seed2107726020-seq49.pddl',
    'prob-blocks-blocks-nblk35-seed2107726020-seq36.pddl',
    'prob-blocks-blocks-nblk35-seed2107726020-seq95.pddl',
    'prob-blocks-blocks-nblk35-seed2107726020-seq19.pddl',
    'prob-blocks-blocks-nblk50-seed1184714140-seq34.pddl',
    'prob-blocks-blocks-nblk35-seed2107726020-seq63.pddl',
    'prob-blocks-blocks-nblk35-seed2107726020-seq25.pddl',
    'prob-blocks-blocks-nblk25-seed1428122178-seq82.pddl',
    'prob-blocks-blocks-nblk50-seed1184714140-seq51.pddl',
    'prob-blocks-blocks-nblk35-seed2107726020-seq80.pddl',
    'prob-blocks-blocks-nblk35-seed2107726020-seq47.pddl',
    'prob-blocks-blocks-nblk50-seed1184714140-seq58.pddl',
    'prob-blocks-blocks-nblk25-seed1428122178-seq94.pddl',
    'prob-blocks-blocks-nblk25-seed1428122178-seq52.pddl',
    'prob-blocks-blocks-nblk25-seed1428122178-seq69.pddl',
    'prob-blocks-blocks-nblk50-seed1184714140-seq77.pddl',
    'prob-blocks-blocks-nblk25-seed1428122178-seq68.pddl',
    'prob-blocks-blocks-nblk35-seed2107726020-seq21.pddl',
    'prob-blocks-blocks-nblk35-seed2107726020-seq35.pddl',
    'prob-blocks-blocks-nblk50-seed1184714140-seq88.pddl',
    'prob-blocks-blocks-nblk50-seed1184714140-seq85.pddl',
    'prob-blocks-blocks-nblk50-seed1184714140-seq72.pddl',
    'prob-blocks-blocks-nblk35-seed2107726020-seq33.pddl',
    'prob-blocks-blocks-nblk25-seed1428122178-seq2.pddl',
    'prob-blocks-blocks-nblk35-seed2107726020-seq52.pddl',
    'prob-blocks-blocks-nblk50-seed1184714140-seq60.pddl',
    'prob-blocks-blocks-nblk35-seed2107726020-seq83.pddl',
    'prob-blocks-blocks-nblk35-seed2107726020-seq56.pddl',
    'prob-blocks-blocks-nblk25-seed1428122178-seq51.pddl',
    'prob-blocks-blocks-nblk25-seed1428122178-seq48.pddl',
    'prob-blocks-blocks-nblk50-seed1184714140-seq96.pddl',
    'prob-blocks-blocks-nblk25-seed1428122178-seq70.pddl',
    'prob-blocks-blocks-nblk50-seed1184714140-seq11.pddl',
    'prob-blocks-blocks-nblk25-seed1428122178-seq11.pddl',
    'prob-blocks-blocks-nblk50-seed1184714140-seq16.pddl',
    'prob-blocks-blocks-nblk25-seed1428122178-seq1.pddl',
    'prob-blocks-blocks-nblk35-seed2107726020-seq82.pddl',
    'prob-blocks-blocks-nblk25-seed1428122178-seq15.pddl',
    'prob-blocks-blocks-nblk50-seed1184714140-seq45.pddl',
    'prob-blocks-blocks-nblk35-seed2107726020-seq30.pddl',
    'prob-blocks-blocks-nblk50-seed1184714140-seq48.pddl',
    'prob-blocks-blocks-nblk35-seed2107726020-seq26.pddl',
    'prob-blocks-blocks-nblk25-seed1428122178-seq12.pddl',
    'prob-blocks-blocks-nblk50-seed1184714140-seq62.pddl',
    'prob-blocks-blocks-nblk50-seed1184714140-seq17.pddl',
    'prob-blocks-blocks-nblk25-seed1428122178-seq10.pddl',
    'prob-blocks-blocks-nblk25-seed1428122178-seq29.pddl',
    'prob-blocks-blocks-nblk25-seed1428122178-seq67.pddl',
    'prob-blocks-blocks-nblk35-seed2107726020-seq3.pddl',
    'prob-blocks-blocks-nblk25-seed1428122178-seq31.pddl',
    'prob-blocks-blocks-nblk25-seed1428122178-seq79.pddl',
    'prob-blocks-blocks-nblk50-seed1184714140-seq63.pddl',
    'prob-blocks-blocks-nblk35-seed2107726020-seq40.pddl',
    'prob-blocks-blocks-nblk50-seed1184714140-seq64.pddl',
    'prob-blocks-blocks-nblk25-seed1428122178-seq54.pddl',
    'prob-blocks-blocks-nblk35-seed2107726020-seq42.pddl',
    'prob-blocks-blocks-nblk25-seed1428122178-seq37.pddl',
    'prob-blocks-blocks-nblk25-seed1428122178-seq99.pddl',
    'prob-blocks-blocks-nblk25-seed1428122178-seq22.pddl',
    'prob-blocks-blocks-nblk35-seed2107726020-seq94.pddl',
    'prob-blocks-blocks-nblk50-seed1184714140-seq56.pddl',
    'prob-blocks-blocks-nblk50-seed1184714140-seq92.pddl',
    'prob-blocks-blocks-nblk50-seed1184714140-seq44.pddl',
    'prob-blocks-blocks-nblk25-seed1428122178-seq21.pddl',
    'prob-blocks-blocks-nblk25-seed1428122178-seq73.pddl',
    'prob-blocks-blocks-nblk25-seed1428122178-seq50.pddl',
    'prob-blocks-blocks-nblk50-seed1184714140-seq5.pddl',
    'prob-blocks-blocks-nblk50-seed1184714140-seq41.pddl',
    'prob-blocks-blocks-nblk35-seed2107726020-seq10.pddl',
    'prob-blocks-blocks-nblk25-seed1428122178-seq9.pddl',
    'prob-blocks-blocks-nblk25-seed1428122178-seq86.pddl',
    'prob-blocks-blocks-nblk50-seed1184714140-seq69.pddl',
    'prob-blocks-blocks-nblk35-seed2107726020-seq74.pddl',
    'prob-blocks-blocks-nblk35-seed2107726020-seq91.pddl',
    'prob-blocks-blocks-nblk25-seed1428122178-seq26.pddl',
    'prob-blocks-blocks-nblk25-seed1428122178-seq77.pddl',
    'prob-blocks-blocks-nblk25-seed1428122178-seq35.pddl',
    'prob-blocks-blocks-nblk35-seed2107726020-seq87.pddl',
    'prob-blocks-blocks-nblk50-seed1184714140-seq8.pddl',
    'prob-blocks-blocks-nblk50-seed1184714140-seq6.pddl',
    'prob-blocks-blocks-nblk25-seed1428122178-seq91.pddl',
    'prob-blocks-blocks-nblk25-seed1428122178-seq63.pddl',
    'prob-blocks-blocks-nblk50-seed1184714140-seq74.pddl',
    'prob-blocks-blocks-nblk25-seed1428122178-seq34.pddl',
    'prob-blocks-blocks-nblk35-seed2107726020-seq79.pddl',
    'prob-blocks-blocks-nblk35-seed2107726020-seq23.pddl',
    'prob-blocks-blocks-nblk50-seed1184714140-seq12.pddl',
    'prob-blocks-blocks-nblk25-seed1428122178-seq44.pddl',
    'prob-blocks-blocks-nblk25-seed1428122178-seq47.pddl',
    'prob-blocks-blocks-nblk25-seed1428122178-seq72.pddl',
    'prob-blocks-blocks-nblk25-seed1428122178-seq62.pddl',
    'prob-blocks-blocks-nblk35-seed2107726020-seq78.pddl',
    'prob-blocks-blocks-nblk25-seed1428122178-seq59.pddl',
    'prob-blocks-blocks-nblk35-seed2107726020-seq98.pddl',
    'prob-blocks-blocks-nblk25-seed1428122178-seq38.pddl',
]  # yapf: disable
TEST_RUNS = [([fname], None) for fname in _TEST_RUNS]