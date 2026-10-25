// UI/UX Ultra v3.5 — SwiftUI Multi-Platform Theme
// Family: travel-bharat-nomad | Category: travel
import SwiftUI

public struct AppTheme {
  public struct Light {
    public static let canvas = Color(hex: "#FDFBF7")
    public static let surface = Color(hex: "#F4EFE6")
    public static let elevated = Color(hex: "#FFFFFF")
    public static let textPrimary = Color(hex: "#241914")
    public static let textMuted = Color(hex: "#6E5A4F")
    public static let accent = Color(hex: "#C85A32")
    public static let secondary = Color(hex: "#0F766E")
    public static let border = Color(hex: "#E6DEC8")
  }

  public struct Dark {
    public static let canvas = Color(hex: "#0E0A08")
    public static let surface = Color(hex: "#18120E")
    public static let elevated = Color(hex: "#241B15")
    public static let textPrimary = Color(hex: "#FAF5EE")
    public static let textMuted = Color(hex: "#A68E80")
    public static let accent = Color(hex: "#E07A5F")
    public static let secondary = Color(hex: "#14B8A6")
    public static let border = Color(hex: "#362820")
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
