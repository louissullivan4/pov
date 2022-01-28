import { View, Text } from 'react-native';
import React from 'react';
import styles from "./styles";
import ResultsWheel from '../../components/results/resultWheel';


export default function ResultsScreen() {
  return (
    <View style={styles.container}>
      <View style={styles.rowContainer}>
        <View style={{flex:1,justifyContent:'space-around', height:'100%', padding:10}}>
          <Text>Result:</Text>
          <ResultsWheel/>
        </View>
        <View style={{flex:1, justifyContent:'space-around', height:'100%',padding:10 }}>
          <Text>No. Comments:</Text>
          <Text>Positive:</Text>
          <Text>Negative:</Text>
        </View>
      </View>
      <View style={styles.rowContainer}>

      </View>
      <View style={styles.rowContainer}>

      </View>

      </View>
    
  );
}
