import { View, Text } from 'react-native';
import React from 'react';
import { StyleSheet } from "react-native";
import { useFonts, BebasNeue_400Regular } from '@expo-google-fonts/bebas-neue';

export default function AppText(props) {
    let fontOS = Platform.OS === "android" ? "sans-serif-thin" : "Arial"
    let [fontsLoaded] = useFonts({
        BebasNeue_400Regular,
    });
  return (
    <View>
      <Text style={[styles.text, {fontFamily: fontsLoaded ? 'BebasNeue_400Regular': fontOS}]}>{props.children}</Text>
    </View>
  );

}

const styles = StyleSheet.create({
    container: {
        justifyContent: 'center',
      },
      text: {
        fontSize: 22,
        color: '#6e867f',
      },
});


