# ML Pipeline

import argparse
import train_model
import compute_scores
import os


if "DYNO" in os.environ and os.path.isdir(".dvc"):
    os.system("dvc config core.no_scm true")
    if os.system("dvc pull") != 0:
        exit("dvc pull failed")
    os.system("rm -r .dvc .apt/usr/lib/dvc")


def go(args):
    """
    Execute Piepeline
    """

    if argparse.pipeline_steps == "train_test_model":
        train_model.train()

    if args.pipeline_steps == "check_performance":
        compute_scores.check_performance_on_slices()

    if args.pipeline_steps == "all":
        train_model.train()
        compute_scores.check_performance_on_slices()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Training model pipeline"
    )

    parser.add_argument(
        "--pipeline_steps",
        help="Pipeline step to be executed: train_test_model or check_performance or all",
        type=str,
        required=False,
        default="all" 
    )
    args = parser.parse_args()
    go(args)