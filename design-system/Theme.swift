// UI/UX Ultra v3.5 — SwiftUI Multi-Platform Theme
// Family: saas-linear-indigo | Category: saas
import SwiftUI

public struct AppTheme {
  public struct Light {
    public static let canvas = Color(hex: "#F8FAFC")
    public static let surface = Color(hex: "#FFFFFF")
    public static let elevated = Color(hex: "#F1F5F9")
    public static let textPrimary = Color(hex: "#0B0F19")
    public static let textMuted = Color(hex: "#475569")
    public static let accent = Color(hex: "#4F46E5")
    public static let secondary = Color(hex: "#0D9488")
    public static let border = Color(hex: "#E2E8F0")
  }

  public struct Dark {
    public static let canvas = Color(hex: "#08090C")
    public static let surface = Color(hex: "#11131A")
    public static let elevated = Color(hex: "#1A1D27")
    public static let textPrimary = Color(hex: "#F3F4F6")
    public static let textMuted = Color(hex: "#8A94A6")
    public static let accent = Color(hex: "#6366F1")
    public static let secondary = Color(hex: "#14B8A6")
    public static let border = Color(hex: "#222634")
  }

  // iOS Human Interface Guidelines (HIG) Touch & Spring Constants
  public static let minTouchTarget: CGFloat = 44.0 // Fitts's Law
  public static let cornerRadiusCard: CGFloat = 14.0
  public static let snappySpring = Animation.spring(response: 0.35, dampingFraction: 0.8)
  public static let bounceSpring = Animation.spring(response: 0.45, dampingFraction: 0.65)
}

public extension Color {
  init(hex: String) {
    let cleanHex = hex.trimmingCharacters(in: CharacterSet.alphanumerics.inverted)
    var int: UInt64 = 0
    Scanner(string: cleanHex).scanHexInt64(&int)
    let a, r, g, b: UInt64
    switch cleanHex.count {
    case 6:
      (a, r, g, b) = (255, int >> 16, int >> 8 & 0xFF, int & 0xFF)
    case 8:
      (a, r, g, b) = (int >> 24, int >> 16 & 0xFF, int >> 8 & 0xFF, int & 0xFF)
    default:
      (a, r, g, b) = (255, 0, 0, 0)
    }
    self.init(
      .sRGB,
      red: Double(r) / 255,
      green: Double(g) / 255,
      blue:  Double(b) / 255,
      opacity: Double(a) / 255
    )
  }
}
