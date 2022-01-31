import { View, Text } from 'react-native';
import React from 'react';
import { StyleSheet } from "react-native";
import { useFonts, JuliusSansOne_400Regular } from '@expo-google-fonts/julius-sans-one';

export default function AppTitle() {
    let [fontsLoaded] = useFonts({
        JuliusSansOne_400Regular,
    });
  return (
    <View style={styles.container}>
      <Text style={[styles.text, {fontFamily: fontsLoaded ? 'JuliusSansOne_400Regular': 'sans-serif-thin'}]}>POV</Text>
    </View>
  );

}

const styles = StyleSheet.create({
    container: {
        justifyContent: 'center',

      },
      text: {
        fontSize: 34,
      },
});





