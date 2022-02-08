import React, { useState, useEffect } from 'react';
import { View, Text, ScrollView, Image, Button, ActivityIndicator } from 'react-native';
import { IconButton } from 'react-native-paper';

import styles from "./styles";

import ResultsWheel from '../../components/results/resultWheel';
import AppTitle from '../../components/general/appTitle';
import AppText from '../../components/general/appText';
import SearchBar from '../../components/home/seachBar';
import LineGraph from '../../components/results/LineGraph';

export default function ResultsScreen({ navigation }) {
  const [clicked, setClicked] = useState(false);
  const [searchPhrase, setSearchPhrase] = useState("");
  const [isLoading, setLoading] = useState(true);
  const [rating, setRating] = useState(0);
  const [popularComment, setPopularComment] = useState("Insane! Already own 12 but I might buy another");
  const [recentComment, setRecentComment] = useState("This isn't what was advertised, it's better")

  const cate = false;
  const apiURL = "http://team15.pythonanywhere.com/pov/results/playstation5/product";
  
  useEffect(() => {
    fetch(apiURL)
      .then((response) => response.json())
      .then((json) => {
          var popluarJson = json.reviews[0].charAt(0).toUpperCase() + json.reviews[0].slice(1);
          var recentJson = json.reviews[3].charAt(0).toUpperCase() + json.reviews[3].slice(1);
          setRating(parseFloat(json.rating))
          setPopularComment(popluarJson)
          setRecentComment(recentJson)
      })
      .catch((error) => alert(error))
      .finally(() => setLoading(false));
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
        <ResultsWheel rating={rating}
        />
      </View>
      <View style={styles.rowContainer}>
        <View style={{justifyContent:'flex-start', padding:10}}>
          <AppText>Most popular comments:</AppText>
          <Text style={styles.text}>"{popularComment}"</Text>
        </View>
      </View>
      <View style={styles.rowContainer}>
        <View style={{justifyContent:'flex-start', padding:10}}>
          <AppText>Most recent comments:</AppText>
          <Text style={styles.text}>"{recentComment}"</Text>
        </View>
      </View>
      <View styles={{margin:10,}}>
          
          {cate ? <LineGraph/> : <View></View>}
      </View>

   
      </View>
    );
  }
}
