import React from 'react';
import { View, Text, ScrollView, Image, Button } from 'react-native';
import { IconButton } from 'react-native-paper';

import styles from "./styles";

import ResultsWheel from '../../components/results/resultWheel';
import AppTitle from '../../components/general/appTitle';
import AppText from '../../components/general/appText';


export default function ResultsScreen({ navigation }) {
  return (
    <View style={styles.container}>
      <View style={{margin:10,}}>
        <AppTitle/>
      </View>
      <View style={{position: "absolute", alignSelf: "left", margintop: 5}}>
        <IconButton
            icon="home"
            size={30}
            onPress={() => navigation.push("Home")}
        />
      </View>
      <View style={{margin:10,}}>
        <ResultsWheel/>
      </View>
      <View style={styles.rowContainer}>
        <View style={{justifyContent:'flex-start', padding:10}}>
          <AppText>Most popular comments:</AppText>
        </View>
      </View>
      <View style={styles.rowContainer}>
        <View style={{justifyContent:'flex-start', padding:10}}>
          <AppText>Most recent comments:</AppText>
        </View>
      </View>
      <View style={styles.rowContainer}>
        <View style={{justifyContent:'flex-start', padding:10}}>
          <AppText>Graph:</AppText>
        </View>
      </View>
      </View>
    
  );
}
