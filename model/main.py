# ML Pipeline

import argparse
import train_model
import compute_scores
import os


def go(args):
    """
    Execute Piepeline
    """

    if args.pipeline_steps == "train":
        train_model.train()

    elif args.pipeline_steps == "check_performance":
        compute_scores.check_performance_on_slices()
    else:
        raise ValueError("pipeline_stes should be train_test_model or check_performance")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Training model pipeline"
    )

    parser.add_argument(
        "--pipeline_steps",
        help="Pipeline step to be executed: train or check_performance",
        type=str,
        required=False,
        default="train" 
    )
    args = parser.parse_args()
    go(args)