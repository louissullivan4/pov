import React, { useState, useEffect } from 'react';
import { View, Text, ScrollView, ActivityIndicator, Linking  } from 'react-native';
import { IconButton } from 'react-native-paper';

import styles from "./styles";

import ResultsWheel from '../../components/results/resultWheel';
import AppTitle from '../../components/general/appTitle';
import AppText from '../../components/general/appText';

import ErrorScreen from '../error';

export default function ResultsScreen({ navigation, route }) {
  const [isLoading, setLoading] = useState(true);
  const [rating, setRating] = useState(0);
  const [popularComment, setPopularComment] = useState("null");
  const [recentComment, setRecentComment] = useState("null")
  const [voteCount, setVoteCount] = useState(0);
  const [rank, setRank] = useState(0)
  const [isError, setIsError] = useState(false)  

  const { searchTerm, searchCategory } = route.params;

  const category_list = ['celebrities', 'game', 'music', 'politics', 'sport']
  
  const apiURL = "http://team15.pythonanywhere.com/pov/results/"+searchTerm+"/"+searchCategory+"";
  
  useEffect(() => {
    fetch(apiURL)
      .then((response) => response.json())
      .then((json) => {
        if (json.status == "200"){
          if (searchCategory == "product"){
            let popluarJson = json.reviews[0].charAt(0).toUpperCase() + json.reviews[0].slice(1);
            let recentJson = json.reviews[3].charAt(0).toUpperCase() + json.reviews[3].slice(1);
            let totalJson = json.total_reviews;
            setRating(parseFloat(json.rating))
            setPopularComment(popluarJson)
            setRecentComment(recentJson)
            setVoteCount(parseInt(totalJson))
          }
          else if (searchCategory == "movie"){
            let popluarJson = json.reviews[0].charAt(0).toUpperCase() + json.reviews[0].slice(1);
            let recentJson = json.reviews[3].charAt(0).toUpperCase() + json.reviews[3].slice(1);
            let ratingCountJson = json.rating_count;
            let rankJson = json.peak_rank;

            setRating(parseFloat(json.rating))
            setPopularComment(popluarJson)
            setRecentComment(recentJson)
            setVoteCount(parseInt(ratingCountJson))
            setRank(parseInt(rankJson))
          }
          else if (category_list.includes(searchCategory)){
            setIsError(true)
          }
          else {
            setIsError(true)

          }
        }
        else {
          setIsError(true)

        }
      })
      // .catch((error) => setIsError(true))
      .catch((error) => alert(error))
      .finally(() => setLoading(false));
  })
  if (isLoading) {
    return (<ActivityIndicator/>);
  } else if (isError) {
    return (<ErrorScreen navigation={navigation}/>);
  }else {
      return (
      <ScrollView style={{backgroundColor: '#FFF'}} showsVerticalScrollIndicator={false} contentContainerStyle={{flexGrow:1}} >
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
          <AppText>User's most popular comment:</AppText>
            <Text style={styles.text}>"{popularComment}"</Text>
          </View>
        </View>
        <View style={styles.rowContainer}>
          <View style={{justifyContent:'flex-start', padding:10}}>
          <AppText>User's most recent comment:</AppText>
            <Text style={styles.text}>"{recentComment}"</Text>
          </View>
        </View>
        <View style={styles.rowContainer}> 
            {(searchCategory == "product") ? 
            <View>
               <View style={{justifyContent:'flex-start', padding:10}}>
                  <AppText>Stats:</AppText>
                  <Text style={styles.textlist}>{'>'} {voteCount} number of reviews counted</Text>
                  <Text style={styles.textlist}>
                    <Text>{'>'} Data gathered at </Text>
                    <Text style={styles.urltext} onPress={() => Linking.openURL('https://www.amazon.com/')}>Amazon</Text>
                  </Text>
               </View>
             </View> : 
            (searchCategory == "movie") ?  
            <View>
               <View style={{justifyContent:'flex-start', padding:10}}>
                  <AppText>Stats:</AppText>
                  <Text style={styles.textlist}>{'>'} {voteCount} number of votes counted</Text>
                  <Text style={styles.textlist}>{'>'} {rank} was this movie's peak rank</Text>
                  <Text style={styles.textlist}>
                    <Text>{'>'} Data gathered at </Text>
                    <Text style={styles.urltext} onPress={() => Linking.openURL('https://www.imdb.com/')}>IMDB</Text>
                  </Text>
               </View>
             </View> : 
             <View>
              <View style={{justifyContent:'flex-start', padding:10}}>
                <AppText>Word Bubble</AppText>
              </View>
             </View>}
          </View>
        </View>
      </ScrollView> 
    );
  }
}
