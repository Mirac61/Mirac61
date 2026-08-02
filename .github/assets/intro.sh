#!/usr/bin/env bash

ART=(
'                        '
'   ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄   '
'  ▀▀▀▀█▀▀▀▀▀▀▀▀▀▀█▀▀▀▀  '
'      █          █      '
'  ▄▄▄▄█▄▄▄▄▄▄▄▄▄▄█▄▄▄▄  '
'      █          █      '
'      █          █      '
'      █          █      '
'      █          █      '
'     ▄█▄        ▄█▄     '
'                        '
)

ART_COLOR='\033[38;2;196;116;110m'
LABEL='\033[38;2;149;127;184m'
VALUE='\033[38;2;220;215;186m'
DIM='\033[38;2;114;113;105m'
ACCENT='\033[38;2;126;156;216m'
OFF='\033[0m'

_row() {
  local art="$1" label="$2" value="$3"
  printf '  %b%s%b   ' "$ART_COLOR" "$art" "$OFF"
  if [ -n "$label" ]; then
    printf '%b%-9s%b%b%s%b' "$LABEL" "$label" "$OFF" "$VALUE" "$value" "$OFF"
  else
    printf '%b' "$value"
  fi
  printf '\n'
  sleep 0.11
}

_palette() {
  local colors=('84;84;109' '195;64;67' '152;187;108' '230;195;132' '126;156;216' '149;127;184' '122;168;159' '220;215;186')
  local index
  printf '  %b%s%b   ' "$ART_COLOR" "${ART[10]}" "$OFF"
  for ((index = 0; index < 8; index++)); do
    printf '\033[38;2;%bm███%b' "${colors[index]}" "$OFF"
    sleep 0.05
  done
  printf '\n'
}

_typewrite() {
  local text="$1" index
  printf '%28s' ''
  for ((index = 0; index < ${#text}; index++)); do
    printf '\033[38;2;230;195;132m%s\033[0m' "${text:index:1}"
    sleep 0.028
  done
  printf '\n'
}

about() {
  clear
  printf '\n'

  _row "${ART[0]}"  '' "$(printf '%bmirac%b%b@%b%bfedora%b' "$ACCENT" "$OFF" "$DIM" "$OFF" "$LABEL" "$OFF")"
  _row "${ART[1]}"  '' "$(printf '%b─────────────────────────────────────────────%b' "$DIM" "$OFF")"
  _row "${ART[2]}"  'os'     'Fedora · macOS'
  _row "${ART[3]}"  'wm'     'Hyprland · AeroSpace'
  _row "${ART[4]}"  'editor' 'Neovim · Zed'
  _row "${ART[5]}"  '' ''
  _row "${ART[6]}"  'study'  'Software Engineering · HS Esslingen · 4th sem'
  _row "${ART[7]}"  'langs'  'Go · Java · Kotlin · TypeScript · C++'
  _row "${ART[8]}"  'stack'  'Spring Boot · Gin · PostgreSQL · Docker'
  _row "${ART[9]}"  'now'    'VentoryGo — invoice backend in Go'

  _palette
  printf '\n'
  sleep 0.25
  _typewrite '» open for working student roles from WS26'
  printf '\n'
}
