const chartConfig = {
    backgroundGradientFrom: "#6e867f",
    backgroundGradientFromOpacity: 1,
    backgroundGradientTo: "#6e867f",
    backgroundGradientToOpacity: 1,
    color: (opacity = 1) => `rgba(26, 255, 146, ${opacity})`,
    strokeWidth: 2, // optional, default 3
    barPercentage: 0.5,
    useShadowColorFromDataset: false // optional
  };

  export default chartConfig;