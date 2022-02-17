import { View, Text, Image, TouchableHighlight, Pressable } from 'react-native';
import React from 'react';
import { useNavigation } from'@react-navigation/native';
import styles from './styles';


export default function CarouselCardItem(props) {
  let nav = useNavigation();
  return (
      <View style={styles.container} key={props.index}>
          <Pressable
            onPress={()=> {
              props.onPress(props.item.title, props.item.category)
            }}
          >
            <Image
              source={props.item.imgUrl}
              style={styles.image}
            />
            <Text style={styles.header}>"{props.item.title}"</Text>
          </Pressable>
      </View>

  );
}

