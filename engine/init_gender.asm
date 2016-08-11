InitCrystalData: ; 48000
	ld a, $1
	ld [wd474], a
	xor a
	ld [wd473], a
	ld [PlayerGender], a
	ld [wd475], a
	ld [wd476], a
	ld [wd477], a
	ld [wd478], a
	ld [wd002], a
	ld [wd003], a
	; could have done "ld a, [wd479] \ and %11111100", saved four operations
	ld a, [wd479]
	res 0, a
	ld [wd479], a
	ld a, [wd479]
	res 1, a
	ld [wd479], a
	ret
; 4802f

INCLUDE "misc/mobile_12.asm"

InitGender: ; 48dcb (12:4dcb)
	call InitGenderScreen
	call LoadGenderScreenPal
	call LoadGenderScreenLightBlueTile
	call WaitBGMap2
	call SetPalettes
	ld hl, TextJump_AreYouABoyOrAreYouAGirl
	call PrintText
	ld hl, .MenuDataHeader
	call LoadMenuDataHeader
	call WaitBGMap2
	call VerticalMenu
	call CloseWindow
	ld a, [wMenuCursorY]
	dec a
	ld [PlayerGender], a
	ld c, 10
	call DelayFrames
	ret
; 48dfc (12:4dfc)

.MenuDataHeader: ; 0x48dfc
	db $40 ; flags
	db 04, 06 ; start coords
	db 09, 13 ; end coords
	dw .MenuData2
	db 1 ; default option
; 0x48e04

.MenuData2: ; 0x48e04
	db $a1 ; flags
	db 2 ; items
	db "Left@"
	db "Right@"
; 0x48e0f

TextJump_AreYouABoyOrAreYouAGirl: ; 0x48e0f
	; Are you a boy? Or are you a girl?
	text_jump Text_AreYouABoyOrAreYouAGirl
	db "@"
; 0x48e14

InitGenderScreen: ; 48e14 (12:4e14)
	ld a, $10
	ld [MusicFade], a
	ld a, MUSIC_NONE
	ld [MusicFadeIDLo], a
	ld a, $0
	ld [MusicFadeIDHi], a
	ld c, 8
	call DelayFrames
	call ClearBGPalettes
	call InitCrystalData
	call LoadFontsExtra
	hlcoord 0, 0
	ld bc, SCREEN_HEIGHT * SCREEN_WIDTH
	ld a, $0
	call ByteFill

	hlcoord 0, 0, AttrMap
	ld bc, SCREEN_HEIGHT * SCREEN_WIDTH
	ld a, 1
	call ByteFill

  hlcoord 0, 3, AttrMap
	ld bc, 7
	xor a
	call ByteFill
  hlcoord 0, 4, AttrMap
	ld bc, 7
	xor a
	call ByteFill
  hlcoord 0, 5, AttrMap
	ld bc, 7
	xor a
	call ByteFill
  hlcoord 0, 6, AttrMap
	ld bc, 7
	xor a
	call ByteFill
  hlcoord 0, 7, AttrMap
	ld bc, 7
	xor a
	call ByteFill
  hlcoord 0, 8, AttrMap
	ld bc, 7
	xor a
	call ByteFill
  hlcoord 0, 9, AttrMap
	ld bc, 7
	xor a
	call ByteFill

; hackerdehack
	ld a, 0
	ld [hGraphicStartTile], a
	hlcoord 0, 3
	lb bc, 7, 7
	predef PlaceGraphic

	ld a, 49
	ld [hGraphicStartTile], a
	hlcoord 13, 3
	lb bc, 7, 7
	predef PlaceGraphic

	ret

LoadGenderScreenPal: ; 48e47 (12:4e47)
	ld hl, .Palette
	ld de, UnknBGPals
	ld bc, 2 palettes
	ld a, $5
	call FarCopyWRAM
	callba ApplyPals
	ret
; 48e5c (12:4e5c)

.Palette: ; 48e5c
	RGB $1f, $1f, $1f
	RGB $19, $12, $0c
	RGB $16, $09, $05
	RGB $00, $00, $00

	RGB $1f, $1f, $1f
	RGB $1b, $11, $0e
	RGB $07, $05, $1f
	RGB $00, $00, $00
; 48e64

LoadGenderScreenLightBlueTile: ; 48e64 (12:4e64)
	ld de, .LightBlueTile
	ld hl, VTiles2 tile $00
	lb bc, BANK(.LightBlueTile), 1
	call Get2bpp
; hackety hack
	ld de, ChrisPic
	ld hl, VTiles2 tile 0
	ld b, BANK(ChrisPic) ; BANK(KrisPic)
	ld c, 7 * 7 ; dimensions
	call Get2bpp

	ld de, KrisPic
	ld hl, VTiles2 tile 49
	ld b, BANK(KrisPic) ; BANK(KrisPic)
	ld c, 7 * 7 ; dimensions
	call Get2bpp

	ret
; 48e71 (12:4e71)

.LightBlueTile: ; 48e71
INCBIN "gfx/intro/gender_screen.2bpp"
