import { View, Text } from 'react-native';
import React from 'react';
import { StyleSheet } from "react-native";
import { useFonts, JuliusSansOne_400Regular } from '@expo-google-fonts/julius-sans-one';

export default function AppTitle() {
    let fontOS = Platform.OS === "android" ? "sans-serif-thin" : "Arial"
    let [fontsLoaded] = useFonts({
        JuliusSansOne_400Regular,
    });
  return (
    <View style={styles.container}>
      <Text style={[styles.text, {fontFamily: fontsLoaded ? 'JuliusSansOne_400Regular': fontOS}]}>POV</Text>
    </View>
  );

}

const styles = StyleSheet.create({
    container: {
        justifyContent: 'center',
      },
      text: {
        fontSize: 40
        ,
        color: '#6e867f',
        letterSpacing: 12,
      },
});





