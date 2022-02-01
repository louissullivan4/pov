import { View, Text } from 'react-native';
import React from 'react';
import { StyleSheet } from "react-native";
import { useFonts, BebasNeue_400Regular } from '@expo-google-fonts/bebas-neue';

export default function AppText(props) {
    let [fontsLoaded] = useFonts({
        BebasNeue_400Regular,
    });
  return (
    <View style={styles.container}>
      <Text style={[styles.text, {fontFamily: fontsLoaded ? 'BebasNeue_400Regular': 'sans-serif-thin'}]}>{props.children}</Text>
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


