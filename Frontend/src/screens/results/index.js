import React, { useState } from 'react';
import { View, Text, ScrollView, Image, Button } from 'react-native';
import { IconButton } from 'react-native-paper';

import styles from "./styles";

import ResultsWheel from '../../components/results/resultWheel';
import AppTitle from '../../components/general/appTitle';
import AppText from '../../components/general/appText';
import SearchBar from '../../components/home/seachBar';

export default function ResultsScreen({ navigation }) {
  const [clicked, setClicked] = useState(false);
  const [searchPhrase, setSearchPhrase] = useState("");
  return (
    <View style={styles.container}>
      <View style={{margin:10,}}>
        <AppTitle/>
      </View>
      <SearchBar
        searchPhrase = {searchPhrase}
        setSearchPhrase = {setSearchPhrase}
        clicked = {clicked}
        setClicked = {setClicked}
      />
      <View style={{position: "absolute", top: 0, right: 30}}>
        <IconButton
            icon="home"
            size={30}
            onPress={() => navigation.pop()}
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
