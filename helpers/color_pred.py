def color_pred(val, treshold):
  color = 'olive' if val > treshold else 'orangered'
  return f'background-color: {color}'