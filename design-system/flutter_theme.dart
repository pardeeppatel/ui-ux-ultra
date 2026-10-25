// UI/UX Ultra v3.5 — Flutter Material 3 & Cupertino Theme
// Family: travel-bharat-nomad | Category: travel
import 'package:flutter/material.dart';

class AppTheme {
  // ─── Light ColorScheme ──────────────────────────────────────────
  static final ColorScheme lightColorScheme = ColorScheme(
    brightness: Brightness.light,
    primary: const Color(0xFFC85A32),
    onPrimary: const Color(0xFF0B0F19),
    secondary: const Color(0xFF0F766E),
    onSecondary: const Color(0xFFFFFFFF),
    surface: const Color(0xFFF4EFE6),
    onSurface: const Color(0xFF241914),
    surfaceVariant: const Color(0xFFFFFFFF),
    onSurfaceVariant: const Color(0xFF6E5A4F),
    background: const Color(0xFFFDFBF7),
    onBackground: const Color(0xFF241914),
    error: const Color(0xFFDC2626),
    onError: const Color(0xFFFFFFFF),
    outline: const Color(0xFFE6DEC8),
  );

  // ─── Dark ColorScheme ───────────────────────────────────────────
  static final ColorScheme darkColorScheme = ColorScheme(
    brightness: Brightness.dark,
    primary: const Color(0xFFE07A5F),
    onPrimary: const Color(0xFF08090C),
    secondary: const Color(0xFF14B8A6),
    onSecondary: const Color(0xFFFFFFFF),
    surface: const Color(0xFF18120E),
    onSurface: const Color(0xFFFAF5EE),
    surfaceVariant: const Color(0xFF241B15),
    onSurfaceVariant: const Color(0xFFA68E80),
    background: const Color(0xFF0E0A08),
    onBackground: const Color(0xFFFAF5EE),
    error: const Color(0xFFEF4444),
    onError: const Color(0xFFFFFFFF),
    outline: const Color(0xFF362820),
  );

  // ─── ThemeData Builders ─────────────────────────────────────────
  static ThemeData get lightTheme => ThemeData(
    useMaterial3: true,
    colorScheme: lightColorScheme,
    scaffoldBackgroundColor: const Color(0xFFFDFBF7),
    cardTheme: CardTheme(
      color: const Color(0xFFF4EFE6),
      elevation: 0,
      shape: RoundedRectangleBorder(
        borderRadius: BorderRadius.circular(14),
        side: const BorderSide(color: Color(0xFFE6DEC8)),
      ),
    ),
    elevatedButtonTheme: ElevatedButtonThemeData(
      style: ElevatedButton.styleFrom(
        backgroundColor: const Color(0xFFC85A32),
        foregroundColor: const Color(0xFF0B0F19),
        minimumSize: const Size(88, 44), // Fitts's Law 44pt touch target
        shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(10)),
      ),
    ),
  );

  static ThemeData get darkTheme => ThemeData(
    useMaterial3: true,
    colorScheme: darkColorScheme,
    scaffoldBackgroundColor: const Color(0xFF0E0A08),
    cardTheme: CardTheme(
      color: const Color(0xFF18120E),
      elevation: 0,
      shape: RoundedRectangleBorder(
        borderRadius: BorderRadius.circular(14),
        side: const BorderSide(color: Color(0xFF362820)),
      ),
    ),
    elevatedButtonTheme: ElevatedButtonThemeData(
      style: ElevatedButton.styleFrom(
        backgroundColor: const Color(0xFFE07A5F),
        foregroundColor: const Color(0xFF08090C),
        minimumSize: const Size(88, 44), // Fitts's Law 44pt touch target
        shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(10)),
      ),
    ),
  );
}
