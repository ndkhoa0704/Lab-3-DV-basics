"""
Created on Tue Jan 27 02:33:19 2015

@author: nymph
"""
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib.dates as mdates


############################## Your code for loading and preprocess the data ##


############################ Complete the following 4 functions ###############
def plot1(ax=None):
    ax.hist(
        df["Global_active_power"],
        color="r",
        bins=np.arange(0, 7, 0.5),
        edgecolor="k",
        align="left",
    )
    ax.set_xticks(np.arange(0, 7, 2))
    ax.set_yticks(np.arange(0, 1400, 200))
    ax.spines[["top", "right"]].set_visible(False)
    ax.spines["left"].set_position(("outward", 2))
    ax.spines["bottom"].set_position(("axes", -0.05))
    ax.spines["left"].set_bounds(0, 1200)
    ax.spines["bottom"].set_bounds(0, 6)
    ax.set_xlabel("Global Active Power (kilowatts)", size=20)
    ax.set_ylabel("Frequency", size=20)
    ax.set_title("Global Active Power", fontweight="bold", size=20)
    return ax


def plot2(col="Global_active_power", ax=None):
    ax.plot(df["datetime"], df[col], color="k")
    if col == "Global_active_power":
        ax.set_yticks(np.arange(0, 7, 2))
        ax.set_ylabel("Global Active Power (kilowatts)", size=20)
    else:
        ax.set_ylabel(col, size=20)
        ax.set_xlabel("datetime", size=20)
    ax.xaxis.set_major_locator(mdates.DayLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%a"))
    return ax


def plot3(ax=None):
    ax.plot(df["datetime"], df["Sub_metering_1"], color="k")
    ax.plot(df["datetime"], df["Sub_metering_2"], color="r")
    ax.plot(df["datetime"], df["Sub_metering_3"], color="b")
    ax.set_yticks(np.arange(0, 40, 10))
    ax.set_ylabel("Energy sub metering", size=20)
    ax.xaxis.set_major_locator(mdates.DayLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%a"))
    ax.legend(["Sub_metering_1", "Sub_metering_2", "Sub_metering_3"])
    return ax


def plot4():
    fig, ax = plt.subplots(2, 2, figsize=(18, 7))
    plot2(ax=ax[0, 0])
    plot2(col="Voltage", ax=ax[0, 1])
    plot3(ax=ax[1, 0])
    plot2(col="Global_reactive_power", ax=ax[1, 1])
    fig.savefig("plot4.png")


if __name__ == "__main__":
    # Preprocessing
    df = pd.read_csv("household_power_consumption.txt", sep=";")

    # Set datetime
    df["Date"] = pd.to_datetime(df["Date"], format="%d/%m/%Y")
    df = df[(df.Date >= "2007-02-01") & (df.Date <= "2007-02-02")]
    df["datetime"] = df["Date"].astype("str") + " " + df["Time"]
    df["datetime"] = pd.to_datetime(df["datetime"])

    # Convert numeric columns to its true type
    numeric_cols = [
        col for col in df.columns if col not in ["Date", "Time", "datetime"]
    ]
    df[numeric_cols] = df[numeric_cols].astype("float")

    # Plot and save image to file
    fig, ax = plt.subplots(1, 1, figsize=(15, 7))
    # Plot 1
    plot1(ax=ax)
    fig.savefig("plot1.png")
    # Plot 2
    fig, ax = plt.subplots(1, 1, figsize=(15, 7))
    plot2(ax=ax)
    fig.savefig("plot2.png")
    # Plot 3
    fig, ax = plt.subplots(1, 1, figsize=(15, 7))
    plot3(ax=ax)
    fig.savefig("plot3.png")
    # Plot 4
    plot4()

