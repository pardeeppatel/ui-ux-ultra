// UI/UX Ultra v3.5 — Flutter Material 3 & Cupertino Theme
// Family: saas-linear-indigo | Category: saas
import 'package:flutter/material.dart';

class AppTheme {
  // ─── Light ColorScheme ──────────────────────────────────────────
  static final ColorScheme lightColorScheme = ColorScheme(
    brightness: Brightness.light,
    primary: const Color(0xFF4F46E5),
    onPrimary: const Color(0xFFFFFFFF),
    secondary: const Color(0xFF0D9488),
    onSecondary: const Color(0xFFFFFFFF),
    surface: const Color(0xFFFFFFFF),
    onSurface: const Color(0xFF0B0F19),
    surfaceVariant: const Color(0xFFF1F5F9),
    onSurfaceVariant: const Color(0xFF475569),
    background: const Color(0xFFF8FAFC),
    onBackground: const Color(0xFF0B0F19),
    error: const Color(0xFFDC2626),
    onError: const Color(0xFFFFFFFF),
    outline: const Color(0xFFE2E8F0),
  );

  // ─── Dark ColorScheme ───────────────────────────────────────────
  static final ColorScheme darkColorScheme = ColorScheme(
    brightness: Brightness.dark,
    primary: const Color(0xFF6366F1),
    onPrimary: const Color(0xFFFFFFFF),
    secondary: const Color(0xFF14B8A6),
    onSecondary: const Color(0xFFFFFFFF),
    surface: const Color(0xFF11131A),
    onSurface: const Color(0xFFF3F4F6),
    surfaceVariant: const Color(0xFF1A1D27),
    onSurfaceVariant: const Color(0xFF8A94A6),
    background: const Color(0xFF08090C),
    onBackground: const Color(0xFFF3F4F6),
    error: const Color(0xFFEF4444),
    onError: const Color(0xFFFFFFFF),
    outline: const Color(0xFF222634),
  );

  // ─── ThemeData Builders ─────────────────────────────────────────
  static ThemeData get lightTheme => ThemeData(
    useMaterial3: true,
    colorScheme: lightColorScheme,
    scaffoldBackgroundColor: const Color(0xFFF8FAFC),
    cardTheme: CardTheme(
      color: const Color(0xFFFFFFFF),
      elevation: 0,
      shape: RoundedRectangleBorder(
        borderRadius: BorderRadius.circular(14),
        side: const BorderSide(color: Color(0xFFE2E8F0)),
      ),
    ),
    elevatedButtonTheme: ElevatedButtonThemeData(
      style: ElevatedButton.styleFrom(
        backgroundColor: const Color(0xFF4F46E5),
        foregroundColor: const Color(0xFFFFFFFF),
        minimumSize: const Size(88, 44), // Fitts's Law 44pt touch target
        shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(10)),
      ),
    ),
  );

  static ThemeData get darkTheme => ThemeData(
    useMaterial3: true,
    colorScheme: darkColorScheme,
    scaffoldBackgroundColor: const Color(0xFF08090C),
    cardTheme: CardTheme(
      color: const Color(0xFF11131A),
      elevation: 0,
      shape: RoundedRectangleBorder(
        borderRadius: BorderRadius.circular(14),
        side: const BorderSide(color: Color(0xFF222634)),
      ),
    ),
    elevatedButtonTheme: ElevatedButtonThemeData(
      style: ElevatedButton.styleFrom(
        backgroundColor: const Color(0xFF6366F1),
        foregroundColor: const Color(0xFFFFFFFF),
        minimumSize: const Size(88, 44), // Fitts's Law 44pt touch target
        shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(10)),
      ),
    ),
  );
}
