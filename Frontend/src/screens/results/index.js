import React, { useState, useEffect } from 'react';
import { View, Text, ScrollView, Image, Button, ActivityIndicator } from 'react-native';
import { IconButton } from 'react-native-paper';

import styles from "./styles";

import ResultsWheel from '../../components/results/resultWheel';
import AppTitle from '../../components/general/appTitle';
import AppText from '../../components/general/appText';
import SearchBar from '../../components/home/seachBar';
import LineGraph from '../../components/results/LineGraph';

export default function ResultsScreen({ navigation, route }) {
  const [isLoading, setLoading] = useState(true);
  const [rating, setRating] = useState(0);
  const [popularComment, setPopularComment] = useState("This movie was lack luster... ");
  const [recentComment, setRecentComment] = useState("I think people are harsh on this movie, give it a go!")

  const { searchTerm, searchCategory } = route.params;

  const category_list = ['celebrities', 'game', 'music', 'politics', 'sport']
  const cate = false;
  
  const apiURL = "http://team15.pythonanywhere.com/pov/results/"+searchTerm+"/"+searchCategory+"";
  
  useEffect(() => {
    fetch(apiURL)
      .then((response) => response.json())
      .then((json) => {
        if (json.status == "200"){
          if (searchCategory == "product"){
            let popluarJson = json.reviews[0].charAt(0).toUpperCase() + json.reviews[0].slice(1);
            let recentJson = json.reviews[3].charAt(0).toUpperCase() + json.reviews[3].slice(1);
            setRating(parseFloat(json.rating))
            setPopularComment(popluarJson)
            setRecentComment(recentJson)
          }
          else if (searchCategory == "movie"){
            let popluarJson = json.rating_count;
            let recentJson = json.peak_rank;
            setRating(parseFloat(json.rating))
            // setPopularComment(parseInt(popluarJson))
            // setRecentComment(parseInt(recentJson))
          }
          else if (category_list.includes(searchCategory)){
            cate = true;
            console.log("other apis")
          }
          else {
            navigation.push('Error')
          }
        }
        else {
          navigation.push('Error')
        }
      })
      // .catch((error) => navigation.push('Error'))
      .catch((error) => alert(error))
      .finally(() => setLoading(false));
  })
  if (isLoading) {
    return (<ActivityIndicator/>);
  } else {
  return (

    <ScrollView showsVerticalScrollIndicator={false} contentContainerStyle={{flexGrow:1}} >

    <View style={styles.container}>
      <View style={{margin:10,}}>
        <AppTitle/>
      </View>
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

      <View style={styles.rowContainer}>
        <View style={{justifyContent:'flex-start', padding:10}}>
        {/* <AppText>"{textbox2}"</AppText> */}
        <AppText>Most recent comments:</AppText>
          <Text style={styles.text}>"{recentComment}"</Text>
        </View>
      </View>
      <View style={styles.rowContainer}>
        <View style={{justifyContent:'flex-start', padding:10}}>
        {/* <AppText>"{textbox2}"</AppText> */}
        <AppText>Most recent comments:</AppText>
          <Text style={styles.text}>"{recentComment}"</Text>
        </View>
      </View>
      <View style={styles.rowContainer}>
        <View style={{justifyContent:'flex-start', padding:10}}>
        {/* <AppText>"{textbox2}"</AppText> */}

        <AppText>Most recent comments:</AppText>
          <Text style={styles.text}>"{recentComment}"</Text>
        </View>
      </View>
      <View style={styles.rowContainer}>
        <View style={{justifyContent:'flex-start', padding:10}}>

        {/* <AppText>"{textbox2}"</AppText> */}
        <AppText>Most recent comments:</AppText>
          <Text style={styles.text}>"{recentComment}"</Text>
        </View>
      </View>
      <View style={styles.rowContainer}>
        <View style={{justifyContent:'flex-start', padding:10}}>
        {/* <AppText>"{textbox2}"</AppText> */}
        <AppText>Most recent comments:</AppText>
          <Text style={styles.text}>"{recentComment}"</Text>
        </View>
      </View>
     

      <View styles={{margin:10,}}>
          {cate ? <LineGraph/> : <View style={styles.rowContainer}></View>}
      </View>
      </View>
      </ScrollView>
    );
  }
}
