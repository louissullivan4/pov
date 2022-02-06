import { View, Text, Image, TouchableHighlight } from 'react-native';
import React from 'react';

import styles from './styles';

export default function CarouselCardItem({index, item}) {
  return (
    <View style={styles.container} key={index}>

          <Image
            source={item.imgUrl}
            style={styles.image}
          />
          <Text style={styles.header}>{item.title}</Text>
    </View>
  );
}

