# config.py
from pathlib import Path

# ---------- Paths ----------
ROOT = Path("/content/drive/MyDrive/ENGG 680 - Group 2")   
DATA_DIR = ROOT / "Project Dataset/PAD-UFES-20"
META_CSV = DATA_DIR / "metadata.csv"
FOLDS_CSV = DATA_DIR / "folds.csv"
PRED_DIR = ROOT / "preds"
RESULTS_DIR = ROOT / "results"

DRIVE_IMG_DIR = DATA_DIR / "images"      # slow to read from
IMG_DIR = Path("/content/images")        # local copy; copy images here each session

# ---------- Reproducibility ----------
SEEDS = [0, 1, 2]
N_FOLDS = 5
FOLD_SEED = 42

# ---------- Columns ----------
ID_COL = "patient_id"
LABEL_COL = "diagnostic"
IMG_COL = "img_id"
CANCER_CODES = ["BCC", "SCC", "MEL"]     # positive class; everything else = 0

# ---------- Metadata groups ----------
GROUPS = {
    "demographics": ["age", "gender", "fitspatrick"],
    "lifestyle":    ["smoke", "drink", "pesticide",
                     "has_piped_water", "has_sewage_system"],
    "history":      ["skin_cancer_history", "cancer_history",
                     "background_father", "background_mother"],
    "symptoms":     ["itch", "grew", "hurt", "changed", "bleed"],
    "morphology":   ["diameter_1", "diameter_2", "elevation", "region"],
}
NUMERIC_COLS = ["age", "diameter_1", "diameter_2"]

# ---------- Experiment configs ----------
ALL = list(GROUPS)
CONFIGS = {
    "image_only": [],
    "meta_only": ALL,
    "img+all": ALL,
    **{f"img+{g}": [g] for g in ALL},
    **{f"img+all_minus_{g}": [x for x in ALL if x != g] for g in ALL},
    "img+shuffled": ALL,
}

# ---------- Model / training ----------
BACKBONE = "resnet18"
IMG_SIZE = 224
BATCH_SIZE = 32
EPOCHS = 20
LR = 1e-4
WEIGHT_DECAY = 1e-2
PATIENCE = 5
META_HIDDEN = 64
DROPOUT = 0.3
