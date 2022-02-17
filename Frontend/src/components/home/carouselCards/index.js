import { View, Text, Dimensions} from 'react-native';
import React from 'react';

import Carousel from 'react-native-snap-carousel'
import CarouselCardItem from '../carouselCardItem';
import data from '../../../../data'

import styles from "./styles";

const SLIDER_WIDTH = Dimensions.get('window').width + 80;
const ITEM_WIDTH = Math.round(SLIDER_WIDTH * 0.7);

export default function CarouselCards(props) {
  const isCarousel = React.useRef(null)

  const renderItem = ({ item, index }) => (
    <CarouselCardItem
    item = {item}
    index = {index}
    onPress={
      (searchTerm, category) => 
      props.navigation.push('Results', {
      searchTerm: searchTerm, 
      searchCategory: category,

    })}
    />
  )

  
  return (
    <View style={styles.container}>
      <Carousel
        layout="default"
        ref={isCarousel}
        data={data}
        renderItem={renderItem}
        sliderWidth={SLIDER_WIDTH}
        itemWidth={ITEM_WIDTH}
        inactiveSlideShift={1}
      />
    </View>
  );
}
