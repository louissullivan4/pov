import { View, Text, Dimensions} from 'react-native';
import React from 'react';

import Carousel from 'react-native-snap-carousel'
import styles from "./styles";
import CarouselCardItem from '../carouselCardItem';
import data from '../../../../data'

const SLIDER_WIDTH = Dimensions.get('window').width + 80;
const ITEM_WIDTH = Math.round(SLIDER_WIDTH * 0.7);

export default function CarouselCards() {
  const isCarousel = React.useRef(null)

  return (
    <View style={styles.container}>
      <Carousel
        layout="default"
        ref={isCarousel}
        data={data}
        renderItem={CarouselCardItem}
        sliderWidth={SLIDER_WIDTH}
        itemWidth={ITEM_WIDTH}
        inactiveSlideShift={0}
      />
    </View>
  );
}
