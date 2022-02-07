import { View, Text } from 'react-native';
import React from 'react';
import {LineChart} from "react-native-chart-kit"
import chartConfig from './config';
import { Dimensions } from "react-native";

const screenWidth = Dimensions.get("window").width;
const data = {
    labels: ["January", "February", "March", "April", "May", "June"],
    datasets: [
        {
        data: [20, 45, 28, 80, 99, 43],
        strokeWidth: 2 // optional
        }
    ],
    legend: ["Rainy Days"] // optional
    };

export default function LineGraph() {
  return (
    <LineChart
  data={data}
  width={screenWidth*0.9}
  height={150}
  chartConfig={chartConfig}
  style={{borderRadius:20}}
/>
  );
}
