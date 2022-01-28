import { View, Text } from 'react-native';
import React from 'react';
import AnimatedProgressWheel from 'react-native-progress-wheel';
import styles from './styles';

export default function ResultsWheel() {
  return (
        <View style={{position: 'relative', }}>
          <AnimatedProgressWheel 
              width={100}
              size={160}
              animateFromValue={0}
              progress={70}
              backgroundColor={'#c8e8df'}
              duration={2000}
              color={'#8fcdba'}
          />
          <Text style={{position: 'absolute', alignSelf:'center', bottom:50, fontSize: 55}}>9.6</Text>
        </View>

  );
}
