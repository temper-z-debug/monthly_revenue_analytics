import matplotlib as mpl


def apply_portfolio_theme(font_family: str = "Segoe UI"):
    """
    Apply a consistent, portfolio-grade Matplotlib theme across all figures.
    Works well on Windows; if Segoe UI is unavailable, switch to 'DejaVu Sans' or 'Arial'.
    """

    mpl.rcParams.update({
        # ---- Font ----
        "font.family": font_family,
        "font.size": 10,
        "axes.titlesize": 14,
        "axes.titleweight": "bold",
        "axes.labelsize": 11,

        # ---- Figure ----
        "figure.dpi": 110,
        "savefig.dpi": 180,
        "savefig.bbox": "tight",
        "savefig.pad_inches": 0.15,

        # ---- Axes ----
        "axes.grid": True,
        "grid.linestyle": "--",
        "grid.alpha": 0.28,
        "axes.spines.top": True,
        "axes.spines.right": True,

        # ---- Ticks ----
        "xtick.labelsize": 10,
        "ytick.labelsize": 10,

        # ---- Legend ----
        "legend.frameon": True,
        "legend.framealpha": 0.95,
        "legend.fontsize": 10,
        "legend.title_fontsize": 10,

        # ---- Misc ----
        "axes.unicode_minus": False,
    })
