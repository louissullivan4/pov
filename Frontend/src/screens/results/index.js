import React, { useState, useEffect } from 'react';
import { View, Text, ScrollView, ActivityIndicator, Linking  } from 'react-native';
import { IconButton } from 'react-native-paper';
import Cloud from 'react-native-word-cloud';

import styles from "./styles";

import ResultsWheel from '../../components/results/resultWheel';
import AppTitle from '../../components/general/appTitle';
import AppText from '../../components/general/appText';

import ErrorScreen from '../error';

function product(voteCount) {
  return (
    <View>
      <View style={{justifyContent:'flex-start', padding:10}}>
        <AppText>Stats:</AppText>
        <Text style={styles.textlist}>{'>'} {voteCount} number of reviews counted</Text>
        <Text style={styles.textlist}>
          <Text>{'>'} Data gathered at </Text>
          <Text style={styles.urltext} onPress={() => Linking.openURL('https://www.amazon.com/')}>Amazon</Text>
        </Text>
      </View>
    </View>
  )
}

function movie(voteCount, rank) {
  return (
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
    </View> 
  )
}

function reddit(voteCount, wordCloud) {
  return (
    <View style={{width:'100%', height: 1000}}>
      <View style={{justifyContent:'flex-start', padding:10}}>
        <AppText>Stats:</AppText>
        <Text style={styles.textlist}>{'>'} {voteCount} number of reviews counted</Text>
        <Text style={styles.textlist}>
          <Text>{'>'} Data gathered at </Text>
          <Text style={styles.urltext} onPress={() => Linking.openURL('https://www.reddit.com/')}>Reddit</Text>
        </Text>
      </View>

    
    <Cloud keywords={wordCloud} scale={250} largestAtCenter={true} drawContainerCircle={true} containerCircleColor={'#345678'} /> 

    </View> 
  )
}

function twitter(voteCount, wordCloud) {
  <View>
    <View style={{justifyContent:'flex-start', padding:10}}>
      <AppText>Stats:</AppText>
      <Text style={styles.textlist}>{'>'} {voteCount} number of reviews counted</Text>
      <Text style={styles.textlist}>
        <Text>{'>'} Data gathered at </Text>
        <Text style={styles.urltext} onPress={() => Linking.openURL('https://www.twitter.com/')}>Twitter</Text>
      </Text>
    </View>

    <Cloud keywords={wordCloud} scale={250} largestAtCenter={true} drawContainerCircle={true} containerCircleColor={'#345678'} /> 

  </View>
}
export default function ResultsScreen({ navigation, route }) {
  const [isLoading, setLoading] = useState(true);
  const [rating, setRating] = useState(0);
  const [popularComment, setPopularComment] = useState("null");
  const [recentComment, setRecentComment] = useState("null")
  const [voteCount, setVoteCount] = useState(0);
  const [rank, setRank] = useState(0)
  const [isError, setIsError] = useState(false)  
  const [wordCloud, setWordCloud] = useState([])

  const { searchTerm, searchCategory } = route.params;
  let searchspace = searchTerm.split(' ').join('+');

  const reddit_list = ['game', 'music', 'sport', 'travel']
  const twitter_list = ['celebrities', 'politics']

  const apiURL = "http://team15.pythonanywhere.com/pov/results/"+searchspace+"/"+searchCategory+"";
  console.log(apiURL)
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
          else if (reddit_list.includes(searchCategory)){
            let popluarJson = json.reviews[0].charAt(0).toUpperCase() + json.reviews[0].slice(1);
            let recentJson = json.reviews[3].charAt(0).toUpperCase() + json.reviews[3].slice(1);
            let totalJson = json.total_reviews;

            let wordCountJson = json.word_bubble;
            for (let i of wordCountJson) {
              console.log(i)
              setWordCloud([...wordCloud, {
                keyword: i[0],
                frequency: i[1],
                color: "#fff",
              }])
            }

            setRating(parseFloat(json.rating))
            setPopularComment(popluarJson)
            setRecentComment(recentJson)
            setVoteCount(parseInt(totalJson))
          }
          else {
            let popluarJson = json.reviews[0].charAt(0).toUpperCase() + json.reviews[0].slice(1);
            let recentJson = json.reviews[3].charAt(0).toUpperCase() + json.reviews[3].slice(1);
            let totalJson = json.total_reviews;

            let wordCountJson = json.word_bubble;
            for (let i of wordCountJson) {
              console.log(i)
              setWordCloud([...wordCloud, {
                keyword: i[0],
                frequency: i[1],
                color: "#fff",
              }])
            }

            setRating(parseFloat(json.rating))
            setPopularComment(popluarJson)
            setRecentComment(recentJson)
            setVoteCount(parseInt(totalJson))
          }
        }
        else {
          setIsError(true)
        }
      })
      .catch((error) => setIsError(true))
      // .catch((error) => alert(error))
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
        <View style={{alignSelf:'flex-start', marginLeft:'5%', marginTop:10}}>
          <AppText >Results for: {searchTerm}</AppText>
        </View>
        <View style={{margin:10,}}>
          <ResultsWheel rating={rating}
          />
        </View>
        <Text style={{fontSize:12, marginTop: 5}}>Positivity rating</Text>   
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
              {(searchCategory == "product") ? product(voteCount) : <View/> }
              {(searchCategory == "movie") ?  movie(voteCount, rank) : <View/> }
              {(reddit_list.includes(searchCategory)) ? reddit(voteCount, wordCloud) : <View/> }
              {(twitter_list.includes(searchCategory)) ? twitter(voteCount, wordCloud) : <View/>}
          </View>
        </View>
      </ScrollView> 
    );
  }
}
