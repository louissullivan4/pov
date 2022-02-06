
import React, { useState, useEffect } from 'react';
import { View, Text, ScrollView, Image, Button, ActivityIndicator } from 'react-native';
import { IconButton } from 'react-native-paper';

import styles from "./styles";

import ResultsWheel from '../../components/results/resultWheel';
import AppTitle from '../../components/general/appTitle';
import AppText from '../../components/general/appText';
import SearchBar from '../../components/home/seachBar';

export default function ResultsScreen({ navigation }) {
  const [clicked, setClicked] = useState(false);
  const [searchPhrase, setSearchPhrase] = useState("");
  const [isLoading, setLoading] = useState(true);
  const [rating, setRating] = useState(0);

  const apiURL = "https://louissullivcs.pythonanywhere.com/imdb/rating/tt1160419";
  
  useEffect(() => {
    fetch(apiURL)
      .then((response) => response.json())
      .then((json) => {
        setRating(parseFloat(json.rating))
      
      })
      .catch((error) => alert(error))
      .finally(setLoading(false));
  })
  if (isLoading) {
    return (<ActivityIndicator/>);
  } else {
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
        <View style={{margin:10,}}>
          <ResultsWheel rating={rating} />
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


      </View>
      <View style={styles.rowContainer}>
        <View style={{justifyContent:'flex-start', padding:10}}>
          <AppText>Graph:</AppText>


        </View>
      </View>
    );}
  }
}
